"""
Human-like behavior profile — configures mouse/keyboard "natural" parameters.

Provides:
  - Built-in presets: robotic (default), human_light, human_heavy
  - human_profile_set / human_profile_get handlers
  - Per-parameter helpers for use in sendinput/handler functions

Parameter resolution priority:
  1. Per-call function argument (highest)
  2. Current profile value
  3. Default value (all disabled = robotic)
"""
import threading
import random
import math
import time


# ── Profile schema with defaults ──────────────────────────────────────────

_DEFAULT_PROFILE = {
    # Mouse tremor
    "mouse_tremor": 0.0,         # 0 = off, >0 = amplitude (px)
    "mouse_tremor_freq": 15.0,   # Hz
    # Mouse pre-move
    "mouse_pre_move": False,
    "mouse_pre_move_distance": 15,
    # Mouse drift
    "mouse_drift": False,
    "mouse_drift_radius": 3,
    # Mouse scroll
    "mouse_scroll_variance": 0.0,
    # Keyboard
    "key_delay_range": None,     # [min, max] or None (use single value)
    "key_pressure": 1.0,         # 0.0-1.0, affects down/up interval
    "hotkey_hold_range": None,   # [min, max] or None
}


_PRESETS = {
    "robotic": {
        "description": "All human-like features off — precise, repeatable, deterministic.",
        "profile": {
            "mouse_tremor": 0.0,
            "mouse_pre_move": False,
            "mouse_drift": False,
            "mouse_scroll_variance": 0.0,
            "key_delay_range": None,
            "key_pressure": 1.0,
            "hotkey_hold_range": None,
        },
    },
    "human_light": {
        "description": "Subtle humanization — good for everyday automation without affecting accuracy.",
        "profile": {
            "mouse_tremor": 1.0,
            "mouse_tremor_freq": 15.0,
            "mouse_pre_move": False,
            "mouse_drift": True,
            "mouse_drift_radius": 2,
            "mouse_scroll_variance": 0.1,
            "key_delay_range": [0.02, 0.05],
            "key_pressure": 0.8,
            "hotkey_hold_range": None,
        },
    },
    "human_heavy": {
        "description": "Heavy humanization — for anti-detection scenarios. Slower but very natural.",
        "profile": {
            "mouse_tremor": 2.5,
            "mouse_tremor_freq": 15.0,
            "mouse_pre_move": True,
            "mouse_pre_move_distance": 20,
            "mouse_drift": True,
            "mouse_drift_radius": 4,
            "mouse_scroll_variance": 0.5,
            "key_delay_range": [0.04, 0.12],
            "key_pressure": 0.6,
            "hotkey_hold_range": [0.05, 0.2],
        },
    },
}


# ── Active profile (thread-safe) ──────────────────────────────────────────

_current_profile = dict(_DEFAULT_PROFILE)
_profile_lock = threading.Lock()


def get_current() -> dict:
    """Return a copy of the current profile dict."""
    with _profile_lock:
        return dict(_current_profile)


def set_from_dict(profile: dict):
    """Merge a profile dict into the current profile.

    Only known keys are applied; unknown keys are ignored.
    """
    with _profile_lock:
        for key in _DEFAULT_PROFILE:
            if key in profile:
                _current_profile[key] = profile[key]


def set_preset(name: str):
    """Apply a named preset."""
    name = name.lower().strip()
    if name not in _PRESETS:
        raise ValueError(
            f"Unknown preset '{name}'. Available: {sorted(_PRESETS.keys())}"
        )
    set_from_dict(_PRESETS[name]["profile"])


def list_presets() -> list:
    """Return list of preset names with descriptions."""
    return [
        {"name": k, "description": v["description"]}
        for k, v in _PRESETS.items()
    ]


def reset():
    """Reset to robotic (default)."""
    with _profile_lock:
        _current_profile.clear()
        _current_profile.update(_DEFAULT_PROFILE)


# ── Parameter resolution helpers ──────────────────────────────────────────
# These implement the priority: call-arg > profile > default

def resolve_tremor(call_arg=None):
    """Return (amplitude, frequency) for tremor effect."""
    p = get_current()
    amp = call_arg if call_arg is not None else p.get("mouse_tremor", 0)
    freq = p.get("mouse_tremor_freq", 15.0)
    return (amp, freq)


def resolve_pre_move(call_arg=None):
    """Return (enabled, distance) for pre-move aiming."""
    p = get_current()
    enabled = call_arg if call_arg is not None else p.get("mouse_pre_move", False)
    dist = p.get("mouse_pre_move_distance", 15)
    return (enabled, dist)


def resolve_drift(call_arg=None):
    """Return (enabled, radius) for click drift."""
    p = get_current()
    enabled = call_arg if call_arg is not None else p.get("mouse_drift", False)
    radius = p.get("mouse_drift_radius", 3)
    return (enabled, radius)


def resolve_scroll_variance(call_arg=None):
    """Return variance factor for scroll randomness."""
    p = get_current()
    return call_arg if call_arg is not None else p.get("mouse_scroll_variance", 0.0)


def resolve_delay_range(call_arg=None):
    """Return [min, max] delay range, or None for no delay randomization.

    If call_arg is a number, returns [call_arg, call_arg] (fixed).
    If call_arg is a list [min, max], returns as-is.
    Otherwise falls to profile.
    """
    if call_arg is not None:
        if isinstance(call_arg, (list, tuple)) and len(call_arg) == 2:
            return [float(call_arg[0]), float(call_arg[1])]
        if isinstance(call_arg, (int, float)):
            return [float(call_arg), float(call_arg)]
    p = get_current()
    rng = p.get("key_delay_range")
    if rng and len(rng) == 2:
        return [float(rng[0]), float(rng[1])]
    return None


def resolve_pressure(call_arg=None):
    """Return pressure value (0.0-1.0)."""
    p = get_current()
    return float(call_arg if call_arg is not None else p.get("key_pressure", 1.0))


def resolve_hold_range(call_arg=None):
    """Return [min, max] hold duration for hotkey modifiers, or None."""
    if call_arg is not None:
        if isinstance(call_arg, (list, tuple)) and len(call_arg) == 2:
            return [float(call_arg[0]), float(call_arg[1])]
    p = get_current()
    rng = p.get("hotkey_hold_range")
    if rng and len(rng) == 2:
        return [float(rng[0]), float(rng[1])]
    return None


def random_delay(delay_range):
    """Get a random delay from a [min, max] range.

    If delay_range is None, returns 0.
    If delay_range has min == max, returns that fixed value.
    """
    if delay_range is None:
        return 0.0
    return random.uniform(delay_range[0], delay_range[1])


# ── IPC handlers ──────────────────────────────────────────────────────────

def handle_human_profile_set(params):
    """Set the current human-like profile.

    Params:
        profile: dict of profile parameters (partial update supported).
        preset:  string, apply a named preset (overrides profile if both given).

    Returns:
        {"profile": {...}, "presets": [...]}
    """
    preset_name = params.get("preset")
    if preset_name:
        set_preset(preset_name)

    profile = params.get("profile")
    if profile:
        set_from_dict(profile)

    return {"profile": get_current(), "presets": list_presets()}


def handle_human_profile_get(params):
    """Get the current human-like profile and available presets.

    Returns:
        {"profile": {...}, "presets": [...]}
    """
    return {"profile": get_current(), "presets": list_presets()}
