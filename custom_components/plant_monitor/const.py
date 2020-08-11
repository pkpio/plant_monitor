"""Constants for Plant monitor."""
# Base component constants
NAME = "Plant monitor"
DOMAIN = "plant_monitor"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ISSUE_URL = "https://github.com/praveendath92/plant_monitor/issues"

# Icons
ICON = "mdi:leaf"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
