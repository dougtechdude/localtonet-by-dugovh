"""Small async API client for Localtonet."""
from __future__ import annotations
import aiohttp
from .const import API_KEY_HEADER, REQUEST_TIMEOUT, RESPONSE_MAPPINGS, STATUS_PATH

class LocaltonetApiError(Exception):
    """Raised when the Localtonet API cannot be used."""

class LocaltonetClient:
    def __init__(self, session: aiohttp.ClientSession, base_url: str, api_key: str) -> None:
        self._session, self._base_url, self._api_key = session, base_url.rstrip("/"), api_key

    async def async_get_status(self) -> dict:
        url = f"{self._base_url}{STATUS_PATH}"
        headers = {API_KEY_HEADER: self._api_key, "Accept": "application/json"}
        try:
            async with self._session.get(url, headers=headers, timeout=REQUEST_TIMEOUT) as response:
                if response.status >= 400:
                    raise LocaltonetApiError(f"HTTP {response.status}")
                data = await response.json(content_type=None)
        except (aiohttp.ClientError, TimeoutError, ValueError) as err:
            raise LocaltonetApiError(str(err)) from err
        if not isinstance(data, dict):
            raise LocaltonetApiError("API response is not a JSON object")
        return data

    @staticmethod
    def value(data: dict, name: str):
        for key in RESPONSE_MAPPINGS.get(name, (name,)):
            current = data
            for part in key.split("."):
                if not isinstance(current, dict) or part not in current:
                    break
                current = current[part]
            else:
                return current
        return None
