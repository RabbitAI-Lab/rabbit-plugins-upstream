"""
Central humanization parameter injection.

Takes a level ("robotic"|"light"|"heavy") and enriches handler params
with the corresponding human-like settings.

This is designed to be called once per handler invocation:
    level = get_engine().get_level("click", process_name, params.get("human"))
    params = apply_human_params(params, level)
"""
from daemon.utils.human_profile import (
    _DEFAULT_PROFILE, _PRESETS, get_current, set_from_dict
)


def apply_human_params(params: dict, level: str) -> dict:
    """Merge human-like parameters into a handler's params dict.

    Priority: caller's explicit param > level profile > default.

    Args:
        params: Handler parameter dict (may already have tremor/drift/delay etc).
        level: "robotic", "light", or "heavy".

    Returns:
        Enriched params dict. Original dict is NOT modified (a copy is returned).
    """
    if level == "robotic":
        # No humanization — params stay as-is
        return dict(params)

    # Map level to preset key (add "human_" prefix if needed)
    preset_key = f"human_{level}" if not level.startswith("human_") else level
    preset = _PRESETS.get(preset_key)
    if not preset:
        return dict(params)

    profile = preset.get("profile", {})

    enriched = dict(params)

    # Apply mouse parameters (only if not already explicitly set by caller)
    for key, pkey in [
        ("tremor", "mouse_tremor"),
        ("tremor_freq", "mouse_tremor_freq"),
        ("pre_move", "mouse_pre_move"),
        ("pre_move_distance", "mouse_pre_move_distance"),
        ("drift", "mouse_drift"),
        ("drift_radius", "mouse_drift_radius"),
        ("random_variance", "mouse_scroll_variance"),
    ]:
        if key not in enriched:
            enriched[key] = profile.get(pkey)

    # Apply keyboard parameters
    for key, pkey in [
        ("delay", "key_delay_range"),
        ("pressure", "key_pressure"),
        ("hold_duration", "hotkey_hold_range"),
    ]:
        if key not in enriched:
            val = profile.get(pkey)
            if val is not None:
                enriched[key] = val

    # Clean up None values (don't send null defaults to handlers)
    return {k: v for k, v in enriched.items() if v is not None}
