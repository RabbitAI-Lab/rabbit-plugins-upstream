"""Whitelist of actively-tracked Apple Watch metrics, grouped by category.

Anything not listed here (nutrition, weight, height, mindful_minutes,
swimming/underwater, etc.) is intentionally dropped during ingestion —
those series stopped being tracked and are excluded from all reports.
"""

# Metrics whose raw records look like {"date", "qty", "source"}.
QTY_METRICS = {
    "activity": {
        "step_count",
        "walking_running_distance",
        "cycling_distance",
        "flights_climbed",
        "active_energy",
        "basal_energy_burned",
        "apple_exercise_time",
        "apple_stand_time",
        "apple_stand_hour",
    },
    "vitals": {
        "resting_heart_rate",
        "walking_heart_rate_average",
        "heart_rate_variability",
        "respiratory_rate",
        "blood_oxygen_saturation",
        "apple_sleeping_wrist_temperature",
        "vo2_max",
        "cardio_recovery",
    },
    "other": {
        "walking_speed",
        "walking_step_length",
        "walking_asymmetry_percentage",
        "walking_double_support_percentage",
        "stair_speed_up",
        "stair_speed_down",
        "six_minute_walking_test_distance",
        "environmental_audio_exposure",
        "headphone_audio_exposure",
        "time_in_daylight",
        "physical_effort",
        "running_power",
        "running_speed",
        "running_stride_length",
        "running_vertical_oscillation",
        "running_ground_contact_time",
    },
}

# Metrics whose raw records look like {"date", "Min", "Avg", "Max", "source"}.
HR_METRICS = {
    "vitals": {"heart_rate"},
}

# Metrics whose raw records are full sleep-stage sessions.
SLEEP_METRICS = {
    "sleep": {"sleep_analysis"},
}


def _flatten(groups):
    return {name for names in groups.values() for name in names}


ALL_QTY = _flatten(QTY_METRICS)
ALL_HR = _flatten(HR_METRICS)
ALL_SLEEP = _flatten(SLEEP_METRICS)

# name -> category, across all three shapes
CATEGORY_OF = {}
for groups in (QTY_METRICS, HR_METRICS, SLEEP_METRICS):
    for category, names in groups.items():
        for name in names:
            CATEGORY_OF[name] = category

# Cumulative metrics: sum across a period is meaningful.
# Everything else in QTY/HR is a rate/point-in-time metric: avg/min/max is meaningful, sum is not.
CUMULATIVE_METRICS = {
    "step_count",
    "walking_running_distance",
    "cycling_distance",
    "flights_climbed",
    "active_energy",
    "basal_energy_burned",
    "apple_exercise_time",
    "apple_stand_time",
    "apple_stand_hour",
    "time_in_daylight",
}
