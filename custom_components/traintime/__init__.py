from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up TrainTime from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.async_create_task(
        async_load_platform(hass, "sensor", DOMAIN, entry.data, entry)
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload the integration."""
    return True
