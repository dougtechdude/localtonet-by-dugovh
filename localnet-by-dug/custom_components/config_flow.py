"""Config flow for Localtonet by dug.ovh."""
from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.selector import TextSelector, TextSelectorConfig, TextSelectorType
from .api import LocaltonetApiError, LocaltonetClient
from .const import CONF_BASE_URL, DEFAULT_API_URL, DOMAIN

async def _validate(hass: HomeAssistant, base_url: str, api_key: str) -> None:
    await LocaltonetClient(async_get_clientsession(hass), base_url, api_key).async_get_status()

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            try:
                await _validate(self.hass, user_input[CONF_BASE_URL], user_input[CONF_API_KEY])
            except LocaltonetApiError:
                errors["base"] = "cannot_connect"
            else:
                await self.async_set_unique_id(user_input[CONF_BASE_URL].rstrip("/"))
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title="Localtonet", data=user_input)
        schema = vol.Schema({vol.Required(CONF_BASE_URL, default=DEFAULT_API_URL): str, vol.Required(CONF_API_KEY): str})
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
