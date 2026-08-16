"""Constants for Localtonet by dug.ovh."""
from __future__ import annotations

DOMAIN = "localtonet_by_dugovh"
NAME = "Localtonet by dug.ovh"
CONF_API_KEY = "api_key"
CONF_BASE_URL = "base_url"
DEFAULT_API_URL = "https://api.localtonet.com"
# Both the client and config flow use this same relative validation path.
STATUS_PATH = "/api/status"
API_KEY_HEADER = "X-API-Key"
REQUEST_TIMEOUT = 15

# Adjust these mappings if the deployed API uses different JSON keys.
RESPONSE_MAPPINGS = {
    "status": ("status",),
    "public_url": ("public_url", "url", "tunnel_url"),
    "connected": ("connected", "online"),
    "bytes_in": ("bytes_in", "traffic.in", "traffic_in"),
    "bytes_out": ("bytes_out", "traffic.out", "traffic_out"),
}
