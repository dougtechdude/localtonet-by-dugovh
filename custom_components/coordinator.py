"""Data coordinator."""
from __future__ import annotations
from datetime import timedelta
import aiohttp
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .api import LocaltonetClient, LocaltonetApiError
from .const import CONF_API_KEY, CONF_BASE_URL, DOMAIN

class LocaltonetCoordinator(DataUpdateCoordinator[dict]):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.client = LocaltonetClient(async_get_clientsession(hass), entry.data[CONF_BASE_URL], entry.data[CONF_API_KEY])
        super().__init__(hass, logger=__import__("logging").getLogger(DOMAIN), name=DOMAIN, update_interval=timedelta(minutes=1))

    async def _async_update_data(self) -> dict:
        try:
            return await self.client.async_get_status()
        except LocaltonetApiError as err:
            raise UpdateFailed(str(err)) from err
