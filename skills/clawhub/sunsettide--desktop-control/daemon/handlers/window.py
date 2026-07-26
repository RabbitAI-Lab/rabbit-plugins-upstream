"""Window management handlers using win32gui."""
import ctypes
import ctypes.wintypes as w

import win32gui
import win32con

from daemon.utils import lifecycle

# --- Helpers ---

HWND_TOP = 0
HWND_TOPMOST = -1
SW_SHOWNORMAL = 1
SW_SHOWMINIMIZED = 2
SW_SHOWMAXIMIZED = 3
SW_RESTORE = 9
SW_FORCEMINIMIZE = 11


def _enum_windows():
    """Return list of all visible windows with basic info."""
    windows = []

    def callback(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return True
        title = win32gui.GetWindowText(hwnd)
        if not title.strip():
            return True
        rect = win32gui.GetWindowRect(hwnd)
        cls = win32gui.GetClassName(hwnd)
        windows.append({
            "hwnd": hwnd,
            "title": title,
            "class_name": cls,
            "rect": {"left": rect[0], "top": rect[1],
                     "right": rect[2], "bottom": rect[3]},
        })
        return True

    win32gui.EnumWindows(callback, None)
    return windows


def _find_window(title=None, hwnd=None, class_name=None, process_name=None):
    """Find a window by various criteria. Returns single result or raises."""
    # If an explicit hwnd is provided, validate it first before scanning
    if hwnd is not None and not win32gui.IsWindow(hwnd):
        raise LookupError(f"Invalid or destroyed hwnd: {hwnd}")
    windows = _enum_windows()
    for w in windows:
        if hwnd is not None and w["hwnd"] == hwnd:
            return w
        if title and title.lower() in w["title"].lower():
            return w
        if class_name and class_name.lower() in w["class_name"].lower():
            return w
    raise LookupError(f"Window not found: title='{title}' hwnd={hwnd}")


def _force_foreground(hwnd):
    """Bypass foreground lock using AttachThreadInput trick."""
    fore_thread = ctypes.windll.user32.GetWindowThreadProcessId(
        ctypes.windll.user32.GetForegroundWindow(), None)
    target_thread = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, None)
    ctypes.windll.user32.AttachThreadInput(fore_thread, target_thread, True)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    ctypes.windll.user32.AttachThreadInput(fore_thread, target_thread, False)


# --- Handlers ---

def handle_list(params):
    windows = _enum_windows()
    return {"windows": windows, "count": len(windows)}


def handle_focus(params):
    if "hwnd" not in params and "title" not in params and "class_name" not in params:
        raise ValueError(
            "Missing search criteria for window_focus. "
            "Provide at least one of: hwnd, title, or class_name. "
            "Example: {\"title\": \"Notepad\"}"
        )
    w = _find_window(
        title=params.get("title"),
        hwnd=params.get("hwnd"),
        class_name=params.get("class_name"),
    )
    _force_foreground(w["hwnd"])
    return {"action": "window_focus", "hwnd": w["hwnd"], "title": w["title"]}


def handle_info(params):
    w = _find_window(
        title=params.get("title"),
        hwnd=params.get("hwnd"),
    )
    return w


def handle_minimize(params):
    w = _find_window(title=params.get("title"), hwnd=params.get("hwnd"))
    win32gui.ShowWindow(w["hwnd"], SW_SHOWMINIMIZED)
    return {"action": "window_minimize", "hwnd": w["hwnd"]}


def handle_maximize(params):
    w = _find_window(title=params.get("title"), hwnd=params.get("hwnd"))
    win32gui.ShowWindow(w["hwnd"], SW_SHOWMAXIMIZED)
    return {"action": "window_maximize", "hwnd": w["hwnd"]}


def handle_close(params):
    w = _find_window(title=params.get("title"), hwnd=params.get("hwnd"))
    win32gui.PostMessage(w["hwnd"], win32con.WM_CLOSE, 0, 0)
    return {"action": "window_close", "hwnd": w["hwnd"]}


def handle_move(params):
    w = _find_window(title=params.get("title"), hwnd=params.get("hwnd"))
    x = int(params["x"])
    y = int(params["y"])
    win32gui.SetWindowPos(w["hwnd"], HWND_TOP, x, y, 0, 0,
                           win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)
    return {"action": "window_move", "hwnd": w["hwnd"], "x": x, "y": y}


def handle_resize(params):
    w = _find_window(title=params.get("title"), hwnd=params.get("hwnd"))
    width = int(params["width"])
    height = int(params["height"])
    win32gui.SetWindowPos(w["hwnd"], HWND_TOP, 0, 0, width, height,
                           win32con.SWP_NOMOVE | win32con.SWP_NOZORDER)
    return {"action": "window_resize", "hwnd": w["hwnd"], "width": width, "height": height}


def handle_set_topmost(params):
    """Set or unset a window's topmost (always-on-top) style.

    Params:
        hwnd:    window handle (required)
        topmost: bool, True=HWND_TOPMOST, False=HWND_NOTOPMOST (default: True)
    """
    w = _find_window(hwnd=params.get("hwnd"), title=params.get("title"))
    topmost = params.get("topmost", True)
    flags = win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
    if topmost:
        win32gui.SetWindowPos(w["hwnd"], win32con.HWND_TOPMOST, 0, 0, 0, 0, flags)
    else:
        win32gui.SetWindowPos(w["hwnd"], win32con.HWND_NOTOPMOST, 0, 0, 0, 0, flags)
    return {"action": "window_set_topmost", "hwnd": w["hwnd"], "topmost": topmost}
