""" The commons const for all tests """
from homeassistant.components.climate.const import (  # pylint: disable=unused-import
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
    PRESET_NONE,
    PRESET_ACTIVITY,
)

from custom_components.versatile_thermostat.const import *  # pylint: disable=wildcard-import, unused-wildcard-import

MOCK_TH_OVER_SWITCH_USER_CONFIG = {
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_SWITCH,
}

MOCK_TH_OVER_SWITCH_MAIN_CONFIG = {
    CONF_NAME: "TheOverSwitchMockName",
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_CYCLE_MIN: 5,
    CONF_DEVICE_POWER: 1,
    CONF_USE_WINDOW_FEATURE: True,
    CONF_USE_MOTION_FEATURE: True,
    CONF_USE_POWER_FEATURE: True,
    CONF_USE_PRESENCE_FEATURE: True,
    CONF_USE_MAIN_CENTRAL_CONFIG: True,
}

MOCK_TH_OVER_4SWITCH_USER_CONFIG = {
    CONF_NAME: "TheOver4SwitchMockName",
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_SWITCH,
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_CYCLE_MIN: 8,
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    CONF_DEVICE_POWER: 1,
    CONF_USE_WINDOW_FEATURE: True,
    CONF_USE_MOTION_FEATURE: True,
    CONF_USE_POWER_FEATURE: True,
    CONF_USE_PRESENCE_FEATURE: True,
}

MOCK_TH_OVER_CLIMATE_USER_CONFIG = {
    CONF_THERMOSTAT_TYPE: CONF_THERMOSTAT_CLIMATE,
}


MOCK_TH_OVER_CLIMATE_MAIN_CONFIG = {
    CONF_NAME: "TheOverClimateMockName",
    CONF_TEMP_SENSOR: "sensor.mock_temp_sensor",
    CONF_CYCLE_MIN: 5,
    CONF_DEVICE_POWER: 1,
    CONF_USE_MAIN_CENTRAL_CONFIG: False,
    CONF_USE_CENTRAL_MODE: True
    # Keep default values which are False
}

MOCK_TH_OVER_CLIMATE_CENTRAL_MAIN_CONFIG = {
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    # Keep default values which are False
}

MOCK_TH_OVER_SWITCH_CENTRAL_MAIN_CONFIG = {
    CONF_EXTERNAL_TEMP_SENSOR: "sensor.mock_ext_temp_sensor",
    CONF_TEMP_MIN: 15,
    CONF_TEMP_MAX: 30,
    # Keep default values which are False
}

MOCK_TH_OVER_SWITCH_TYPE_CONFIG = {
    CONF_HEATER: "switch.mock_switch",
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
    CONF_AC_MODE: False,
    CONF_INVERSE_SWITCH: False,
}

MOCK_TH_OVER_SWITCH_AC_TYPE_CONFIG = {
    CONF_HEATER: "switch.mock_air_conditioner",
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
    CONF_AC_MODE: True,
    CONF_INVERSE_SWITCH: False,
}

MOCK_TH_OVER_4SWITCH_TYPE_CONFIG = {
    CONF_HEATER: "switch.mock_4switch0",
    CONF_HEATER_2: "switch.mock_4switch1",
    CONF_HEATER_3: "switch.mock_4switch2",
    CONF_HEATER_4: "switch.mock_4switch3",
    CONF_PROP_FUNCTION: PROPORTIONAL_FUNCTION_TPI,
    CONF_AC_MODE: False,
    CONF_INVERSE_SWITCH: False,
}

MOCK_TH_OVER_SWITCH_TPI_CONFIG = {
    CONF_TPI_COEF_INT: 0.3,
    CONF_TPI_COEF_EXT: 0.1,
}

MOCK_TH_OVER_CLIMATE_TYPE_CONFIG = {
    CONF_CLIMATE: "climate.mock_climate",
    CONF_AC_MODE: False,
    CONF_AUTO_REGULATION_MODE: CONF_AUTO_REGULATION_STRONG,
    CONF_AUTO_REGULATION_DTEMP: 0.5,
    CONF_AUTO_REGULATION_PERIOD_MIN: 2,
    CONF_AUTO_FAN_MODE: CONF_AUTO_FAN_HIGH,
}

MOCK_TH_OVER_CLIMATE_TYPE_NOT_REGULATED_CONFIG = {
    CONF_CLIMATE: "climate.mock_climate",
    CONF_AC_MODE: False,
    CONF_AUTO_REGULATION_MODE: CONF_AUTO_REGULATION_NONE,
}

MOCK_TH_OVER_CLIMATE_TYPE_AC_CONFIG = {
    CONF_CLIMATE: "climate.mock_climate",
    CONF_AC_MODE: True,
    CONF_AUTO_REGULATION_MODE: CONF_AUTO_REGULATION_STRONG,
    CONF_AUTO_REGULATION_DTEMP: 0.5,
    CONF_AUTO_REGULATION_PERIOD_MIN: 1,
}

MOCK_PRESETS_CONFIG = {
    PRESET_FROST_PROTECTION + "_temp": 7,
    PRESET_ECO + "_temp": 16,
    PRESET_COMFORT + "_temp": 17,
    PRESET_BOOST + "_temp": 18,
}

MOCK_PRESETS_AC_CONFIG = {
    PRESET_FROST_PROTECTION + "_temp": 7,
    PRESET_ECO + "_temp": 17,
    PRESET_COMFORT + "_temp": 19,
    PRESET_BOOST + "_temp": 20,
    PRESET_ECO + "_ac_temp": 25,
    PRESET_COMFORT + "_ac_temp": 23,
    PRESET_BOOST + "_ac_temp": 21,
}

MOCK_WINDOW_CONFIG = {
    CONF_WINDOW_SENSOR: "binary_sensor.window_sensor",
    # Not used normally only for tests to avoid rewrite all tests
    CONF_WINDOW_DELAY: 10,
}

MOCK_WINDOW_DELAY_CONFIG = {
    CONF_WINDOW_DELAY: 10,
}

MOCK_WINDOW_AUTO_CONFIG = {
    CONF_WINDOW_AUTO_OPEN_THRESHOLD: 1.0,
    CONF_WINDOW_AUTO_CLOSE_THRESHOLD: 0.0,
    CONF_WINDOW_AUTO_MAX_DURATION: 5.0,
    CONF_WINDOW_ACTION: CONF_WINDOW_FAN_ONLY,
}

MOCK_MOTION_CONFIG = {
    CONF_MOTION_SENSOR: "input_boolean.motion_sensor",
    CONF_MOTION_DELAY: 10,
    CONF_MOTION_OFF_DELAY: 30,
    CONF_MOTION_PRESET: PRESET_COMFORT,
    CONF_NO_MOTION_PRESET: PRESET_ECO,
}

MOCK_POWER_CONFIG = {
    CONF_POWER_SENSOR: "sensor.power_sensor",
    CONF_MAX_POWER_SENSOR: "sensor.power_max_sensor",
    CONF_PRESET_POWER: 10,
}

MOCK_PRESENCE_CONFIG = {
    CONF_PRESENCE_SENSOR: "person.presence_sensor",
    PRESET_ECO + PRESET_AWAY_SUFFIX + "_temp": 16,
    PRESET_COMFORT + PRESET_AWAY_SUFFIX + "_temp": 17,
    PRESET_BOOST + PRESET_AWAY_SUFFIX + "_temp": 18,
}

MOCK_PRESENCE_AC_CONFIG = {
    CONF_PRESENCE_SENSOR: "person.presence_sensor",
    PRESET_FROST_PROTECTION + PRESET_AWAY_SUFFIX + "_temp": 7,
    PRESET_ECO + PRESET_AWAY_SUFFIX + "_temp": 16,
    PRESET_COMFORT + PRESET_AWAY_SUFFIX + "_temp": 17,
    PRESET_BOOST + PRESET_AWAY_SUFFIX + "_temp": 18,
    PRESET_ECO + "_ac" + PRESET_AWAY_SUFFIX + "_temp": 27,
    PRESET_COMFORT + "_ac" + PRESET_AWAY_SUFFIX + "_temp": 26,
    PRESET_BOOST + "_ac" + PRESET_AWAY_SUFFIX + "_temp": 25,
}

MOCK_ADVANCED_CONFIG = {
    CONF_MINIMAL_ACTIVATION_DELAY: 10,
    CONF_SECURITY_DELAY_MIN: 5,
    CONF_SECURITY_MIN_ON_PERCENT: 0.4,
    CONF_SECURITY_DEFAULT_ON_PERCENT: 0.3,
}

MOCK_DEFAULT_FEATURE_CONFIG = {
    CONF_USE_WINDOW_FEATURE: False,
    CONF_USE_MOTION_FEATURE: False,
    CONF_USE_POWER_FEATURE: False,
    CONF_USE_PRESENCE_FEATURE: False,
}

MOCK_DEFAULT_CENTRAL_CONFIG = {
    CONF_USE_MAIN_CENTRAL_CONFIG: False,
    CONF_USE_TPI_CENTRAL_CONFIG: False,
    CONF_USE_PRESETS_CENTRAL_CONFIG: False,
    CONF_USE_WINDOW_CENTRAL_CONFIG: False,
    CONF_USE_MOTION_CENTRAL_CONFIG: False,
    CONF_USE_POWER_CENTRAL_CONFIG: False,
    CONF_USE_PRESENCE_CENTRAL_CONFIG: False,
    CONF_USE_ADVANCED_CENTRAL_CONFIG: False,
}
