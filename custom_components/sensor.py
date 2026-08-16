"""Sensors exposed by Localtonet."""
from __future__ import annotations
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.const import PERCENTAGE
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([LocaltonetSensor(coordinator, entry, "status", "Status"), LocaltonetSensor(coordinator, entry, "public_url", "Public URL"), LocaltonetSensor(coordinator, entry, "connected", "Connected")])

class LocaltonetSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, entry, key, label):
        super().__init__(coordinator)
        self._key, self._attr_name = key, f"Localtonet {label}"
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_device_info = {"identifiers": {(DOMAIN, entry.entry_id)}, "name": "Localtonet", "manufacturer": "dug.ovh"}
        # These are deliberately plain state sensors: URL/boolean values do not have numeric units.
    @property
    def native_value(self):
        value = self.coordinator.client.value(self.coordinator.data or {}, self._key)
        if self._key == "connected" and isinstance(value, bool):
            return "Connected" if value else "Disconnected"
        return value
