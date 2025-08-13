from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up the SNCF Trains integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    # Charger le platform sensor correctement
    await async_load_platform(hass, "sensor", DOMAIN, {}, entry)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload the integration."""
    # Ici on pourrait supprimer les sensors si nécessaire
    return True
