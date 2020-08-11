"""Sensor platform for plant monitor."""
from custom_components.plant_monitor.const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from custom_components.plant_monitor.entity import PlantEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([PlantSensor(coordinator, entry)])


class PlantSensor(PlantEntity):
    """Plant sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("static")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON
