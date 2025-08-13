import requests
from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from .const import API_URL

class SncfTrainsSensor(SensorEntity):
    def __init__(self, api_key, station_name, max_trains, active_start, active_end):
        self.station_name = station_name
        self._name = f"trains_{station_name.lower().replace(' ', '_')}"
        self._state = None
        self._attributes = {}
        self.api_key = api_key
        self.max_trains = max_trains
        self.active_start = active_start
        self.active_end = active_end

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{API_URL}{self.station_name}/departures"
        try:
            r = requests.get(url, headers=headers, timeout=10)
            r.raise_for_status()
            data = r.json()
            trains = []

            for departure in data.get("departures", []):
                dep_hour = datetime.fromisoformat(departure["stop_date_time"]["departure_date_time"]).hour
                if not (self.active_start <= dep_hour <= self.active_end):
                    continue
                trains.append({
                    "destination": departure["display_informations"]["direction"],
                    "time": departure["stop_date_time"]["departure_date_time"],
                    "train_number": departure["display_informations"]["headsign"]
                })
                if len(trains) >= self.max_trains:
                    break

            self._state = f"{len(trains)} trains à venir"
            self._attributes = {"trains": trains}
        except Exception as e:
            self._state = "Erreur"
            self._attributes = {"error": str(e)}

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([SncfTrainsSensor(
        api_key=entry.data["api_key"],
        station_name=entry.data["station_name"],
        max_trains=entry.data["max_trains"],
        active_start=entry.data["active_start"],
        active_end=entry.data["active_end"]
    )])
