# Localtonet by dug.ovh — Home Assistant custom integration

Install by copying `custom_components/localtonet_by_dugovh` into Home Assistant's `custom_components` directory, restart Home Assistant, then add **Localtonet** from Settings → Devices & services.

## Before use

1. Replace `YOUR_GITHUB_USERNAME` in `manifest.json` and publish this folder under that GitHub account (if using HACS).
2. Confirm or change `DEFAULT_API_URL` in `const.py`. The endpoint entered in the config flow is used for all requests.
3. Confirm `STATUS_PATH`, `API_KEY_HEADER`, and `RESPONSE_MAPPINGS` against the deployed API. No API key is bundled.

The included sensors intentionally use plain states for status, URL, and connection state; no potentially invalid unit/device-class combinations are declared.
