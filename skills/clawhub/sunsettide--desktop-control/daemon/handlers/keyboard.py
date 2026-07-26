"""
Keyboard operation handlers.

v1.1.3 additions:
  - keyboard_down / keyboard_up: split press
  - keyboard_type: delay + ime_safe (clipboard fallback for CJK)
  - clipboard_get / clipboard_set: explicit clipboard operations
  - resolve_key: helper for key name resolution
"""
import re
import time

from daemon.utils import sendinput as si
from daemon.utils import release_guard
from daemon.utils.human_engine import get_engine
from daemon.utils.humanize import apply_human_params


def _inject_human(params, op_type):
    """Enrich params with human-like settings based on context."""
    level = get_engine().get_level(
        operation_type=op_type,
        user_override=params.get("human"),
    )
    return apply_human_params(params, level)


# ── Smart space (CJK ↔ Latin) ────────────────────────────────────────────

def _insert_smart_spaces(text):
    """Insert a space between CJK and Latin characters."""
    text = re.sub(r'([\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff])([a-zA-Z0-9])', r'\1 \2', text)
    text = re.sub(r'([a-zA-Z0-9])([\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff])', r'\1 \2', text)
    return text


# ── IME-safe clipboard paste ──────────────────────────────────────────────

def _paste_via_clipboard(text):
    """Paste text via clipboard (for CJK input / long text compatibility).

    Saves and restores original clipboard content.
    """
    try:
        import pyperclip
        old = pyperclip.paste()
        pyperclip.copy(text)
        si.keyboard_hotkey(17, 86)  # Ctrl+V
        time.sleep(0.05)
        if old:
            pyperclip.copy(old)
        return True
    except Exception:
        return False


def _has_cjk(text):
    """Check if text contains any CJK characters."""
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf':
            return True
    return False


def _type_with_pressure(text, delay_range, pressure):
    """Type text with randomized delay and pressure simulation.

    delay_range: None (no delay), [min, max] (randomized per-char delay).
    pressure: 0.0-1.0, affects down/up interval (higher = shorter = "faster").
    """
    from daemon.utils.human_profile import random_delay
    from daemon.utils.sendinput import (INPUT, INPUT_KEYBOARD, _INPUT_UNION, KEYBDINPUT,
                                         KEYEVENTF_UNICODE, KEYEVENTF_KEYDOWN, KEYEVENTF_KEYUP)
    import ctypes

    if delay_range is None:
        # No delay randomization, just type
        si.keyboard_type(text)
        return

    # Per-character randomized typing
    for ch in text:
        delay = random_delay(delay_range)
        code = ord(ch)
        flags_down = KEYEVENTF_KEYDOWN  # 0x0000
        flags_up = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP  # 0x0004 | 0x0002 = 0x0006

        # Key down
        inp = INPUT(type=INPUT_KEYBOARD)
        inp.u.ki = KEYBDINPUT(0, code, flags_down, 0, None)
        ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

        # Variable hold time based on pressure
        hold = 0.01 + (1.0 - pressure) * 0.03  # 0.01 (heavy) to 0.04 (light)
        time.sleep(hold)

        # Key up
        inp = INPUT(type=INPUT_KEYBOARD)
        inp.u.ki = KEYBDINPUT(0, code, flags_up, 0, None)
        ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

        # Random delay between chars
        if delay > 0:
            time.sleep(delay)


# ── Handlers ──────────────────────────────────────────────────────────────

def handle_type(params):
    """Type text with smart options.

    Params:
        text:          Required. Text to type.
        delay:         Per-character delay in seconds (0 = instant; 0.05 = 20 chars/s).
                       Also accepts [min, max] list for randomized delay.
        smart_space:   Auto-insert spaces between CJK and Latin (default: false).
        ime_safe:      Auto-switch to clipboard for CJK text (default: true).
        input_method:  "auto"|"unicode"|"clipboard" (default: "auto").
        pressure:      Key hold pressure 0.0-1.0 (higher = shorter = "heavier").
        human:         "off"|"light"|"heavy" — override automatic humanization.
    """
    params = _inject_human(params, "type")
    text = params.get("text")
    if text is None:
        raise ValueError("Missing required parameter 'text' for keyboard_type.")

    smart_space = params.get("smart_space", False)
    ime_safe = params.get("ime_safe", True)
    input_method = params.get("input_method", "auto")

    # Resolve human-like typing parameters
    from daemon.utils.human_profile import resolve_delay_range, resolve_pressure, random_delay
    delay_range = resolve_delay_range(params.get("delay"))
    pressure = resolve_pressure(params.get("pressure"))

    if smart_space:
        text = _insert_smart_spaces(text)

    # Decide input method
    should_paste = False
    if input_method == "clipboard":
        should_paste = True
    elif input_method == "unicode":
        should_paste = False
    elif ime_safe and _has_cjk(text):
        should_paste = True

    if should_paste:
        if not _paste_via_clipboard(text):
            # Fallback: type with randomized delay
            _type_with_pressure(text, delay_range, pressure)
    else:
        _type_with_pressure(text, delay_range, pressure)

    return {"action": "keyboard_type", "chars": len(text),
            "smart_space": smart_space, "ime_safe": ime_safe,
            "method": "clipboard" if should_paste else "unicode",
            "delay_range": delay_range, "pressure": round(pressure, 2)}


def handle_press(params):
    params = _inject_human(params, "press")
    key = params.get("key", "")
    code = si.resolve_key(key)
    times = params.get("times", 1)
    for _ in range(times):
        si.keyboard_press(code)
    return {"action": "keyboard_press", "key": key, "times": times}


def handle_down(params):
    params = _inject_human(params, "down")
    key = params.get("key", "")
    code = si.resolve_key(key)
    si.keyboard_down(code)
    release_guard.press("keyboard", code)
    return {"action": "keyboard_down", "key": key, "vk": code}


def handle_up(params):
    params = _inject_human(params, "up")
    key = params.get("key", "")
    code = si.resolve_key(key)
    si.keyboard_up(code)
    release_guard.release("keyboard", code)
    return {"action": "keyboard_up", "key": key, "vk": code}


def handle_hotkey(params):
    params = _inject_human(params, "hotkey")
    keys = params.get("keys", [])
    codes = [si.resolve_key(k) for k in keys]

    from daemon.utils.human_profile import resolve_hold_range, random_delay
    hold_range = resolve_hold_range(params.get("hold_duration"))

    if hold_range:
        # Custom hold: press in order, wait randomized hold, release in reverse
        for k in codes:
            si.keyboard_down(k)
        hold = random_delay(hold_range)
        time.sleep(hold)
        for k in reversed(codes):
            si.keyboard_up(k)
    else:
        si.keyboard_hotkey(*codes)

    return {"action": "keyboard_hotkey", "keys": keys,
            "hold_range": hold_range}


# ── Clipboard ─────────────────────────────────────────────────────────────

def handle_clipboard_get(params):
    text = si.clipboard_get()
    return {"text": text or ""}


def handle_clipboard_set(params):
    text = params.get("text", "")
    si.clipboard_set(text)
    return {"success": True, "chars": len(text)}
