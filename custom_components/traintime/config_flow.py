import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class SncfTrainsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=user_input["station_name"], data=user_input)

        schema = vol.Schema({
            vol.Required("api_key"): str,
            vol.Required("station_name"): str,
            vol.Required("update_interval", default=5): vol.All(int, vol.Range(min=5, max=10)),
            vol.Required("active_start", default=6): vol.All(int, vol.Range(min=0, max=23)),
            vol.Required("active_end", default=22): vol.All(int, vol.Range(min=0, max=23)),
            vol.Required("max_trains", default=3): vol.All(int, vol.Range(min=3, max=5))
        })
        return self.async_show_form(step_id="user", data_schema=schema)
