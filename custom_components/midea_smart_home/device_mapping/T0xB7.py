from homeassistant.const import (
    Platform,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass

DEVICE_MAPPING = {
    "default": {
        "rationale": ["off", "on"],
        "centralized": [
            "version",
            "error_type",
            "error_eq",
            "error_code",
            "lock",
            "dry_fire_protection",
            "light_lampblack_mode",
            "gas_leakage_code",
            "gas_leakage_alarm",
            "is_error",
            "is_error_flag",
            "left_status",
            "left_power",
            "left_cookmode",
            "left_gear",
            "left_work_time",
            "left_target_time",
            "left_rest_time",
            "left_current_temperature",
            "left_target_temperature",
            "left_lock",
            "left_dry_fire_protection",
            "right_status",
            "right_power",
            "right_cookmode",
            "right_gear",
            "right_work_time",
            "right_target_time",
            "right_rest_time",
            "right_current_temperature",
            "right_target_temperature",
            "right_lock",
            "right_dry_fire_protection",
        ],
        "calculate": {
            "get": [
                {"lvalue": "[gas_leakage_alarm]", "rvalue": "\"on\" if [gas_leakage_code] in (1, \"1\", \"on\", True) else \"off\""},
                {"lvalue": "[is_error_flag]", "rvalue": "\"on\" if [is_error] in (1, \"1\", \"on\", True) else \"off\""},
            ]
        },
        "entities": {
            Platform.SELECT: {
                "lock_control": {
                    "options": {
                        "unlock": {"eq": "total", "lock": "off"},
                        "lock": {"eq": "total", "lock": "on"},
                    },
                },
                "dry_fire_protection_control": {
                    "options": {
                        "off": {"eq": "total", "dry_fire_protection": "off"},
                        "on": {"eq": "total", "dry_fire_protection": "on"},
                    },
                },
                "left_burner_command": {
                    "options": {
                        "none": {},
                        "off": {"eq": "left", "power": "off"},
                    },
                },
                "right_burner_command": {
                    "options": {
                        "none": {},
                        "off": {"eq": "right", "power": "off"},
                    },
                },
            },
            Platform.BINARY_SENSOR: {
                "lock": {
                    "device_class": BinarySensorDeviceClass.LOCK,
                    "translation_key": "lock",
                },
                "dry_fire_protection": {
                    "device_class": BinarySensorDeviceClass.SAFETY,
                    "translation_key": "dry_fire_protection",
                },
                "gas_leakage_alarm": {
                    "device_class": BinarySensorDeviceClass.GAS,
                    "translation_key": "gas_leakage_alarm",
                },
                "is_error_flag": {
                    "device_class": BinarySensorDeviceClass.PROBLEM,
                    "translation_key": "is_error_flag",
                },
                "left_power": {
                    "device_class": BinarySensorDeviceClass.POWER,
                    "translation_key": "left_power",
                },
                "left_lock": {
                    "device_class": BinarySensorDeviceClass.LOCK,
                    "translation_key": "left_lock",
                },
                "left_dry_fire_protection": {
                    "device_class": BinarySensorDeviceClass.SAFETY,
                    "translation_key": "left_dry_fire_protection",
                },
                "right_power": {
                    "device_class": BinarySensorDeviceClass.POWER,
                    "translation_key": "right_power",
                },
                "right_lock": {
                    "device_class": BinarySensorDeviceClass.LOCK,
                    "translation_key": "right_lock",
                },
                "right_dry_fire_protection": {
                    "device_class": BinarySensorDeviceClass.SAFETY,
                    "translation_key": "right_dry_fire_protection",
                },
            },
            Platform.SENSOR: {
                "version": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "version",
                },
                "error_type": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "error_type",
                },
                "error_eq": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "error_eq",
                },
                "error_code": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "error_code",
                },
                "light_lampblack_mode": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "light_lampblack_mode",
                },
                "gas_leakage_code": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "gas_leakage_code",
                },
                "is_error": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "is_error",
                },
                "left_status": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "left_status",
                },
                "left_cookmode": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "left_cookmode",
                },
                "left_gear": {
                    "icon": "mdi:fire",
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "left_gear",
                },
                "left_work_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.SECONDS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "left_work_time",
                },
                "left_target_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.SECONDS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "left_target_time",
                },
                "left_rest_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.SECONDS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "left_rest_time",
                },
                "left_current_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "left_current_temperature",
                },
                "left_target_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "left_target_temperature",
                },
                "right_status": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "right_status",
                },
                "right_cookmode": {
                    "device_class": SensorDeviceClass.ENUM,
                    "translation_key": "right_cookmode",
                },
                "right_gear": {
                    "icon": "mdi:fire",
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "right_gear",
                },
                "right_work_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.SECONDS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "right_work_time",
                },
                "right_target_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.SECONDS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "right_target_time",
                },
                "right_rest_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.SECONDS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "right_rest_time",
                },
                "right_current_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "right_current_temperature",
                },
                "right_target_temperature": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "translation_key": "right_target_temperature",
                },
            },
        },
    }
}
