"""
SendInput wrapper via ctypes — pure Python, no extra deps.
Provides mouse and keyboard input using user32.dll SendInput.

v1.1.3 additions:
  - mouse_move_relative: relative movement
  - mouse_down / mouse_up: split click into press + release
  - mouse_move_smooth: bezier curve interpolation (human-like movement)
  - keyboard_down / keyboard_up: split press into down + release
  - keyboard_type_delayed: per-character delay
  - clipboard_get / clipboard_set: explicit clipboard operations
  - key name resolution with _resolve_vk helper
"""
import ctypes
import ctypes.wintypes as w
import math
import random
import time
from ctypes import Structure, c_uint, c_ulong, c_int, c_long, c_ushort, c_byte, c_void_p, POINTER

# --- Win32 constants ---

# Mouse flags
MOUSEEVENTF_MOVE       = 0x0001
MOUSEEVENTF_LEFTDOWN   = 0x0002
MOUSEEVENTF_LEFTUP     = 0x0004
MOUSEEVENTF_RIGHTDOWN  = 0x0008
MOUSEEVENTF_RIGHTUP    = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP   = 0x0040
MOUSEEVENTF_ABSOLUTE   = 0x8000
MOUSEEVENTF_WHEEL      = 0x0800

# Mouse button map
BUTTON_FLAGS = {
    "left":   (MOUSEEVENTF_LEFTDOWN,   MOUSEEVENTF_LEFTUP),
    "right":  (MOUSEEVENTF_RIGHTDOWN,  MOUSEEVENTF_RIGHTUP),
    "middle": (MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP),
}
BUTTON_DOWN_FLAGS = {
    "left": MOUSEEVENTF_LEFTDOWN,
    "right": MOUSEEVENTF_RIGHTDOWN,
    "middle": MOUSEEVENTF_MIDDLEDOWN,
}
BUTTON_UP_FLAGS = {
    "left": MOUSEEVENTF_LEFTUP,
    "right": MOUSEEVENTF_RIGHTUP,
    "middle": MOUSEEVENTF_MIDDLEUP,
}

# Keyboard flags
KEYEVENTF_KEYDOWN     = 0x0000
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1

# --- Structures ---

class MOUSEINPUT(Structure):
    _fields_ = [
        ("dx",          c_long),
        ("dy",          c_long),
        ("mouseData",   c_ulong),
        ("dwFlags",     c_ulong),
        ("time",        c_ulong),
        ("dwExtraInfo", POINTER(c_ulong)),
    ]

class KEYBDINPUT(Structure):
    _fields_ = [
        ("wVk",         c_ushort),
        ("wScan",       c_ushort),
        ("dwFlags",     c_ulong),
        ("time",        c_ulong),
        ("dwExtraInfo", POINTER(c_ulong)),
    ]

class HARDWAREINPUT(Structure):
    _fields_ = [
        ("uMsg",    c_ulong),
        ("wParamL", c_ushort),
        ("wParamH", c_ushort),
    ]

class _INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("mi",   MOUSEINPUT),
        ("ki",   KEYBDINPUT),
        ("hi",   HARDWAREINPUT),
    ]

class INPUT(Structure):
    _fields_ = [
        ("type", c_ulong),
        ("u",    _INPUT_UNION),
    ]


# --- DPI awareness ---

def enable_dpi_awareness():
    """Set PerMonitorV2 DPI awareness — call once at daemon start."""
    try:
        shcore = ctypes.windll.shcore
        shcore.SetProcessDpiAwareness(2)
    except AttributeError:
        pass
    except OSError:
        pass


# =========================================================================
# Mouse — absolute movement
# =========================================================================

def _normalize_coords(x, y):
    """Convert pixel coords to 0..65535 absolute coords for SendInput."""
    sw = ctypes.windll.user32.GetSystemMetrics(78)
    sh = ctypes.windll.user32.GetSystemMetrics(79)
    sx = ctypes.windll.user32.GetSystemMetrics(76)
    sy = ctypes.windll.user32.GetSystemMetrics(77)
    nx = int((x - sx) * 65535 / max(sw - 1, 1))
    ny = int((y - sy) * 65535 / max(sh - 1, 1))
    return nx, ny


def mouse_move(x, y):
    """Move mouse to absolute pixel coordinates (virtual screen)."""
    nx, ny = _normalize_coords(x, y)
    _send_mouse_move(nx, ny)


def _send_mouse_move(nx, ny):
    """Internal: send a single mouse-move INPUT with absolute-normalized coords."""
    inp = INPUT(type=INPUT_MOUSE)
    inp.u.mi = MOUSEINPUT(nx, ny, 0, MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE | 0x4000, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def mouse_move_relative(dx, dy):
    """Move mouse relative to current position."""
    inp = INPUT(type=INPUT_MOUSE)
    inp.u.mi = MOUSEINPUT(dx, dy, 0, MOUSEEVENTF_MOVE, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


# =========================================================================
# Mouse — bezier smooth movement
# =========================================================================

def _bezier_point(t, p0, p1, p2, p3):
    """Compute a point on a cubic bezier curve at parameter t (0..1)."""
    u = 1 - t
    x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
    y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
    return (x, y)


def mouse_move_smooth(x, y, duration=0.3, steps=30, tremor_amp=0.0, tremor_freq=15.0):
    """Move mouse with bezier interpolation (human-like trajectory).

    Args:
        x, y: Target absolute coordinates.
        duration: Total movement time in seconds.
        steps: Number of interpolation steps (default 30).
        tremor_amp: Tremor amplitude in pixels (0 = off).
        tremor_freq: Tremor frequency in Hz (default 15).
    """
    cx, cy = mouse_position()

    # Generate random control points for bezier curve
    dx = x - cx
    dy = y - cy
    dist = math.sqrt(dx*dx + dy*dy)
    offset = max(dist * 0.3, 30.0)

    # Randomize control point placement
    if random.random() > 0.5:
        cp1 = (cx + dx * 0.3 + random.uniform(-offset, offset),
               cy + dy * 0.3 + random.uniform(-offset, offset))
        cp2 = (cx + dx * 0.6 + random.uniform(-offset*0.5, offset*0.5),
               cy + dy * 0.6 + random.uniform(-offset*0.5, offset*0.5))
    else:
        cp1 = (cx + dx * 0.2 + random.uniform(-offset*0.5, offset*0.5),
               cy + dy * 0.2 + random.uniform(-offset*0.5, offset*0.5))
        cp2 = (cx + dx * 0.7 + random.uniform(-offset, offset),
               cy + dy * 0.7 + random.uniform(-offset, offset))

    start = (cx, cy)
    end = (x, y)
    interval = duration / max(steps, 1)
    tremor_enabled = tremor_amp > 0.0

    for i in range(steps):
        t = (i + 1) / steps
        px, py = _bezier_point(t, start, cp1, cp2, end)

        # Add physiological tremor (sinusoidal oscillation)
        if tremor_enabled:
            elapsed = t * duration
            # Randomize tremor direction per step
            angle = random.uniform(0, 2 * math.pi)
            offset_x = math.cos(angle) * math.sin(elapsed * tremor_freq * 2 * math.pi) * tremor_amp
            offset_y = math.sin(angle) * math.sin(elapsed * tremor_freq * 2 * math.pi) * tremor_amp
            px += offset_x
            py += offset_y

        nx, ny = _normalize_coords(int(px), int(py))
        _send_mouse_move(nx, ny)
        time.sleep(interval)


# =========================================================================
# Mouse — down / up (split click)
# =========================================================================

def mouse_down(button="left"):
    """Press mouse button down (without releasing)."""
    flag = BUTTON_DOWN_FLAGS.get(button)
    if not flag:
        raise ValueError(f"Invalid button: {button}")
    inp = INPUT(type=INPUT_MOUSE)
    inp.u.mi = MOUSEINPUT(0, 0, 0, flag, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def mouse_up(button="left"):
    """Release mouse button."""
    flag = BUTTON_UP_FLAGS.get(button)
    if not flag:
        raise ValueError(f"Invalid button: {button}")
    inp = INPUT(type=INPUT_MOUSE)
    inp.u.mi = MOUSEINPUT(0, 0, 0, flag, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


# =========================================================================
# Mouse — click, drag, scroll, position
# =========================================================================

def mouse_click(x=None, y=None, button="left", clicks=1):
    """Click at (x,y) or current position. Supports left/right/middle, single/double."""
    if x is not None and y is not None:
        mouse_move(x, y)
    for _ in range(clicks):
        inp = (INPUT * 2)()
        inp[0].type = INPUT_MOUSE
        inp[0].u.mi = MOUSEINPUT(0, 0, 0, BUTTON_DOWN_FLAGS.get(button, MOUSEEVENTF_LEFTDOWN), 0, None)
        inp[1].type = INPUT_MOUSE
        inp[1].u.mi = MOUSEINPUT(0, 0, 0, BUTTON_UP_FLAGS.get(button, MOUSEEVENTF_LEFTUP), 0, None)
        ctypes.windll.user32.SendInput(2, inp, ctypes.sizeof(INPUT))


def mouse_drag(start_x, start_y, end_x, end_y, button="left"):
    """Drag from start to end."""
    down_flag = BUTTON_DOWN_FLAGS.get(button, MOUSEEVENTF_LEFTDOWN)
    up_flag = BUTTON_UP_FLAGS.get(button, MOUSEEVENTF_LEFTUP)

    mouse_move(start_x, start_y)
    inp_d = INPUT(type=INPUT_MOUSE)
    inp_d.u.mi = MOUSEINPUT(0, 0, 0, down_flag, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp_d), ctypes.sizeof(INPUT))

    mouse_move(end_x, end_y)

    inp_u = INPUT(type=INPUT_MOUSE)
    inp_u.u.mi = MOUSEINPUT(0, 0, 0, up_flag, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp_u), ctypes.sizeof(INPUT))


def mouse_scroll(clicks, direction="vertical", variance=0.0):
    """Scroll wheel. Positive=up/left, negative=down/right.

    Args:
        clicks: Base scroll amount.
        direction: "vertical" (default).
        variance: Randomization factor 0.0-1.0. Actual scroll = clicks * (1 +/- variance/2).
    """
    if variance > 0:
        factor = 1.0 + random.uniform(-variance/2, variance/2)
        clicks = int(clicks * factor)
    amount = clicks * 120
    inp = INPUT(type=INPUT_MOUSE)
    inp.u.mi = MOUSEINPUT(0, 0, amount, MOUSEEVENTF_WHEEL, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def mouse_position():
    """Return (x, y) of current cursor position."""
    class POINT(Structure):
        _fields_ = [("x", c_long), ("y", c_long)]
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return (pt.x, pt.y)


DEFAULT_DELAY = 0


# =========================================================================
# Keyboard
# =========================================================================

def keyboard_type(text, delay=DEFAULT_DELAY):
    """Type Unicode text using KEYEVENTF_UNICODE. No clipboard pollution.

    Args:
        text: String to type.
        delay: Per-character delay in seconds (0 = instant). 50ms = ~20 chars/s.
    """
    inputs = []
    for ch in text:
        code = ord(ch)
        inputs.append(INPUT(
            type=INPUT_KEYBOARD,
            u=_INPUT_UNION(ki=KEYBDINPUT(0, code, KEYEVENTF_UNICODE, 0, None)),
        ))
        inputs.append(INPUT(
            type=INPUT_KEYBOARD,
            u=_INPUT_UNION(ki=KEYBDINPUT(0, code, KEYEVENTF_UNICODE | KEYEVENTF_KEYUP, 0, None)),
        ))
        if delay > 0:
            # Flush current batch, sleep, then continue
            if inputs:
                n = len(inputs)
                arr = (INPUT * n)()
                for i, inp in enumerate(inputs):
                    arr[i] = inp
                ctypes.windll.user32.SendInput(n, arr, ctypes.sizeof(INPUT))
                inputs = []
            time.sleep(delay)

    if inputs:
        n = len(inputs)
        arr = (INPUT * n)()
        for i, inp in enumerate(inputs):
            arr[i] = inp
        ctypes.windll.user32.SendInput(n, arr, ctypes.sizeof(INPUT))


def keyboard_press(key_code):
    """Press and release a single virtual key by code."""
    inp = (INPUT * 2)()
    inp[0].type = INPUT_KEYBOARD
    inp[0].u.ki = KEYBDINPUT(key_code, 0, KEYEVENTF_KEYDOWN, 0, None)
    inp[1].type = INPUT_KEYBOARD
    inp[1].u.ki = KEYBDINPUT(key_code, 0, KEYEVENTF_KEYUP, 0, None)
    ctypes.windll.user32.SendInput(2, inp, ctypes.sizeof(INPUT))


def keyboard_down(key_code):
    """Press a key without releasing (for combos like Shift + click)."""
    inp = INPUT(type=INPUT_KEYBOARD)
    inp.u.ki = KEYBDINPUT(key_code, 0, KEYEVENTF_KEYDOWN, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def keyboard_up(key_code):
    """Release a held key."""
    inp = INPUT(type=INPUT_KEYBOARD)
    inp.u.ki = KEYBDINPUT(key_code, 0, KEYEVENTF_KEYUP, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


def keyboard_hotkey(*keys):
    """Press a combo. Keys: virtual-key codes in order (press), then reversed (release)."""
    for k in keys:
        inp = INPUT(type=INPUT_KEYBOARD)
        inp.u.ki = KEYBDINPUT(k, 0, KEYEVENTF_KEYDOWN, 0, None)
        ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))
    for k in reversed(keys):
        inp = INPUT(type=INPUT_KEYBOARD)
        inp.u.ki = KEYBDINPUT(k, 0, KEYEVENTF_KEYUP, 0, None)
        ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))


# =========================================================================
# Clipboard operations
# =========================================================================

def clipboard_get():
    """Get text from clipboard. Returns None if no text available."""
    try:
        import pyperclip
        return pyperclip.paste()
    except Exception:
        # Fallback: use Win32 CF_UNICODETEXT
        try:
            u32 = ctypes.windll.user32
            k32 = ctypes.windll.kernel32
            u32.OpenClipboard(0)
            handle = u32.GetClipboardData(13)  # CF_UNICODETEXT
            if handle:
                ptr = k32.GlobalLock(handle)
                if ptr:
                    text = ctypes.wstring_at(ptr)
                    k32.GlobalUnlock(handle)
                    u32.CloseClipboard()
                    return text
            u32.CloseClipboard()
        except Exception:
            pass
        return None


def clipboard_set(text):
    """Set clipboard text. Returns None."""
    try:
        import pyperclip
        pyperclip.copy(text)
        return
    except Exception:
        pass
    # Fallback: use Win32
    try:
        u32 = ctypes.windll.user32
        k32 = ctypes.windll.kernel32
        u32.OpenClipboard(0)
        u32.EmptyClipboard()
        h = k32.GlobalAlloc(0x42, (len(text) + 1) * 2)
        ptr = k32.GlobalLock(h)
        ctypes.memmove(ptr, text.encode("utf-16-le"), (len(text) + 1) * 2)
        k32.GlobalUnlock(h)
        u32.SetClipboardData(13, h)
        u32.CloseClipboard()
    except Exception:
        pass


# =========================================================================
# Key name resolution
# =========================================================================

# Common virtual-key codes (subset)
VK = {
    "enter": 13, "return": 13, "tab": 9, "escape": 27, "esc": 27,
    "backspace": 8, "bksp": 8,
    "delete": 46, "del": 46, "insert": 45, "ins": 45,
    "home": 36, "end": 35,
    "pageup": 33, "pagedown": 34, "pgup": 33, "pgdn": 34,
    "space": 32, "spc": 32,
    "up": 38, "down": 40, "left": 37, "right": 39,
    "ctrl": 17, "control": 17,
    "alt": 18, "menu": 18,
    "shift": 16,
    "win": 91, "lwin": 91, "rwin": 92,
    "f1": 112, "f2": 113, "f3": 114, "f4": 115,
    "f5": 116, "f6": 117, "f7": 118, "f8": 119,
    "f9": 120, "f10": 121, "f11": 122, "f12": 123,
    "capslock": 20, "numlock": 144, "scrolllock": 145,
    "printscreen": 44, "prtsc": 44,
    "pause": 19, "break": 19,
}


def resolve_key(key_name: str) -> int:
    """Resolve a key name to a virtual-key code.

    Supports VK dict names, aliases, and single characters (letters, digits).

    Returns: vk code int.

    Raises: ValueError if the key cannot be resolved.
    """
    k = key_name.lower().strip().replace("_", "").replace("-", "")
    code = VK.get(k)
    if code is not None:
        return code

    # Single character
    if len(k) == 1:
        if k.isalpha():
            return ord(k.upper())
        if k.isdigit():
            return ord(k)
        # Punctuation — map to VK
        punct_map = {
            ".": 190, ",": 188, "/": 191, "\\": 220,
            ";": 186, "'": 222, "[": 219, "]": 221,
            "-": 189, "=": 187, "`": 192,
        }
        vk = punct_map.get(k)
        if vk:
            return vk

    raise ValueError(f"Unknown key: '{key_name}'. Supported keys: {sorted(VK.keys())}")
