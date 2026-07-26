"""
Mouse operation handlers.

v1.1.3 additions:
  - mouse_move_relative: relative movement
  - mouse_down / mouse_up: split click
  - mouse_move duration/curve: bezier smooth movement
  - mouse_click text: smart routing (text param → click_text)
  - mouse_get_position: enhanced alias with monitor detection
  - Safety bounds checking on all movement
"""
import math
import random as _random
import time

from daemon.utils import sendinput as si
from daemon.utils.monitors import resolve_coords, get_monitors, _build_virtual_bounds
from daemon.utils import release_guard
from daemon.utils.human_engine import get_engine
from daemon.utils.humanize import apply_human_params
import random as _random


# ── Safety bounds ─────────────────────────────────────────────────────────

_SAFETY_BOUNDS_ENABLED = True


def _check_safety_bounds(x, y):
    """Validate (x, y) is within the combined virtual desktop bounds."""
    if not _SAFETY_BOUNDS_ENABLED:
        return

    monitors = get_monitors()
    if len(monitors) < 2:
        return
    left, top, right, bottom = _build_virtual_bounds(monitors)
    if left == right or top == bottom:
        return

    margin = 10  # small tolerance
    if x < left - margin or y < top - margin or x > right + margin or y > bottom + margin:
        raise ValueError(
            f"Mouse coordinates ({x}, {y}) are outside the virtual screen bounds "
            f"[{left}, {top}] - [{right}, {bottom}]. "
            f"Check your monitor configuration or disable safety bounds."
        )


# ── Handlers ──────────────────────────────────────────────────────────────

def _inject_human(params, op_type):
    """Enrich params with human-like settings based on context."""
    level = get_engine().get_level(
        operation_type=op_type,
        user_override=params.get("human"),
    )
    return apply_human_params(params, level)


def handle_move(params):
    params = _inject_human(params, "move")
    x = params.get("x")
    y = params.get("y")
    duration = params.get("duration", 0)
    curve = params.get("curve", "linear")

    if x is None or y is None:
        raise ValueError(
            "Missing required parameters 'x' and 'y' for mouse_move. "
            "Example: {\"x\": 500, \"y\": 300}"
        )

    monitor = params.get("monitor", 0)
    abs_x, abs_y = resolve_coords(monitor, int(x), int(y))
    _check_safety_bounds(abs_x, abs_y)

    # Resolve human-like parameters from profile/call
    from daemon.utils.human_profile import resolve_tremor, resolve_delay_range, random_delay
    tremor_amp, tremor_freq = resolve_tremor(params.get("tremor"))

    if duration and duration > 0 and curve == "bezier":
        si.mouse_move_smooth(abs_x, abs_y, duration=float(duration),
                              tremor_amp=tremor_amp, tremor_freq=tremor_freq)
    elif duration and duration > 0:
        # Linear smooth with optional tremor
        cx, cy = si.mouse_position()
        steps = max(int(duration / 0.05), 5)
        for i in range(steps):
            t = (i + 1) / steps
            px = cx + (abs_x - cx) * t
            py = cy + (abs_y - cy) * t
            if tremor_amp > 0:
                elapsed = t * duration
                angle = _random.uniform(0, 2 * math.pi)
                px += math.cos(angle) * math.sin(elapsed * tremor_freq * 2 * math.pi) * tremor_amp
                py += math.sin(angle) * math.sin(elapsed * tremor_freq * 2 * math.pi) * tremor_amp
            si.mouse_move(int(px), int(py))
            time.sleep(duration / steps)
    else:
        si.mouse_move(abs_x, abs_y)

    return {"action": "mouse_move", "x": params["x"], "y": params["y"],
            "monitor": monitor, "resolved": {"x": abs_x, "y": abs_y},
            "duration": duration, "curve": curve,
            "tremor_amp": tremor_amp}


def handle_move_relative(params):
    params = _inject_human(params, "move_relative")
    dx = params.get("dx")
    dy = params.get("dy")
    if dx is None or dy is None:
        raise ValueError(
            "Missing required parameters 'dx' and 'dy' for mouse_move_relative. "
            "Example: {\"dx\": 100, \"dy\": -50}"
        )
    from_x, from_y = si.mouse_position()
    si.mouse_move_relative(int(dx), int(dy))
    to_x, to_y = si.mouse_position()
    return {"success": True, "from": {"x": from_x, "y": from_y},
            "to": {"x": to_x, "y": to_y}}


def handle_click(params):
    params = _inject_human(params, "click")
    # Smart routing: if 'text' param is present, delegate to click_text
    text = params.get("text")
    if text:
        from daemon.handlers.vision_click import handle_click_text
        return handle_click_text(params)

    x = params.get("x")
    y = params.get("y")
    monitor = params.get("monitor", 0)
    button = params.get("button", "left")
    clicks = params.get("clicks", 1)

    if button not in ("left", "right", "middle"):
        raise ValueError(
            f"Invalid button '{button}'. Supported: 'left', 'right', 'middle'."
        )

    final_x, final_y = x, y
    monitor = params.get("monitor", 0)

    if x is not None and y is not None:
        abs_x, abs_y = resolve_coords(monitor, int(x), int(y))
        _check_safety_bounds(abs_x, abs_y)

        # Pre-move: aim near target first, then micro-adjust
        from daemon.utils.human_profile import resolve_pre_move, resolve_drift
        pre_move_enabled, pre_move_dist = resolve_pre_move(params.get("pre_move"))
        drift_enabled, drift_radius = resolve_drift(params.get("drift"))

        if pre_move_enabled:
            # Move to a random spot near the target
            aim_x = abs_x + _random.randint(-pre_move_dist, pre_move_dist)
            aim_y = abs_y + _random.randint(-pre_move_dist, pre_move_dist)
            si.mouse_move(aim_x, aim_y)
            time.sleep(_random.uniform(0.05, 0.15))  # Human aiming pause
            # Final micro-adjust to target
            si.mouse_move(abs_x, abs_y)
            time.sleep(_random.uniform(0.02, 0.05))

        # Click drift: add random offset
        if drift_enabled:
            abs_x += _random.randint(-drift_radius, drift_radius)
            abs_y += _random.randint(-drift_radius, drift_radius)
            final_x, final_y = abs_x, abs_y

        si.mouse_click(abs_x, abs_y, button, clicks)
    else:
        si.mouse_click(None, None, button, clicks)

    return {"action": "mouse_click", "button": button, "clicks": clicks,
            "input_injected": True, "monitor": monitor,
            "clicked_at": {"x": final_x, "y": final_y} if final_x is not None else None}


def handle_down(params):
    params = _inject_human(params, "down")
    button = params.get("button", "left")
    if button not in ("left", "right", "middle"):
        raise ValueError(f"Invalid button: {button}")
    si.mouse_down(button)
    release_guard.press("mouse", button)
    return {"action": "mouse_down", "button": button}


def handle_up(params):
    params = _inject_human(params, "up")
    button = params.get("button", "left")
    if button not in ("left", "right", "middle"):
        raise ValueError(f"Invalid button: {button}")
    si.mouse_up(button)
    release_guard.release("mouse", button)
    return {"action": "mouse_up", "button": button}


def handle_drag(params):
    params = _inject_human(params, "drag")
    missing = [k for k in ("start_x", "start_y", "end_x", "end_y") if k not in params]
    if missing:
        raise ValueError(f"Missing parameter(s) {missing} for mouse_drag.")
    monitor = params.get("monitor", 0)
    sx, sy = resolve_coords(monitor, int(params["start_x"]), int(params["start_y"]))
    ex, ey = resolve_coords(monitor, int(params["end_x"]), int(params["end_y"]))
    _check_safety_bounds(sx, sy)
    _check_safety_bounds(ex, ey)
    si.mouse_drag(sx, sy, ex, ey, params.get("button", "left"))
    return {"action": "mouse_drag", "start": (sx, sy), "end": (ex, ey), "monitor": monitor}


def handle_scroll(params):
    params = _inject_human(params, "scroll")
    delta = params.get("delta", params.get("clicks", 1))
    direction = params.get("direction", "vertical")
    from daemon.utils.human_profile import resolve_scroll_variance
    variance = resolve_scroll_variance(params.get("random_variance"))
    si.mouse_scroll(int(delta), direction, variance=variance)
    base = int(delta)
    actual = int(delta * (1.0 + _random.uniform(-variance/2, variance/2))) if variance > 0 else base
    return {"action": "mouse_scroll", "delta": base, "actual": actual,
            "direction": direction, "variance": variance}


def handle_position(params):
    x, y = si.mouse_position()
    return {"x": x, "y": y}


def handle_get_position(params):
    """Enhanced position query with monitor detection."""
    x, y = si.mouse_position()

    # Find which monitor the cursor is on
    monitor_idx = 0
    monitors = get_monitors()
    for i in range(1, len(monitors)):
        m = monitors[i]
        if m["left"] <= x < m["left"] + m["width"] and m["top"] <= y < m["top"] + m["height"]:
            monitor_idx = i
            break

    return {"x": x, "y": y, "monitor": monitor_idx}


# ── Safety toggle ─────────────────────────────────────────────────────────

def handle_set_safety_bounds(params):
    """Enable or disable safety bounds checking.

    Params: {"enabled": true|false}
    """
    global _SAFETY_BOUNDS_ENABLED
    _SAFETY_BOUNDS_ENABLED = params.get("enabled", True)
    return {"safety_bounds_enabled": _SAFETY_BOUNDS_ENABLED}
