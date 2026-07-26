"""
Active window awareness handlers.

Provides:
  - get_active_window:  foreground window + process info
  - window_get_context: UIA control tree (max 2 levels deep) for a window
"""
import ctypes
import ctypes.wintypes as w
import os
import time

import win32gui
import win32process
import psutil


def _get_process_info(pid):
    """Return dict with pid, name, path for a given PID."""
    try:
        proc = psutil.Process(pid)
        return {
            "pid": pid,
            "name": proc.name(),
            "path": proc.exe(),
        }
    except (psutil.NoSuchProcess, psutil.AccessDenied, OSError):
        return {"pid": pid, "name": "unknown", "path": ""}


def handle_get_active_window(params):
    """Return detailed info about the current foreground window.

    Returns:
        {
            "hwnd": 123456,
            "title": "...",
            "class": "...",
            "process": {"pid": ..., "name": "...", "path": "..."},
            "rect": {"left": ..., "top": ..., "width": ..., "height": ...}
        }
    """
    hwnd = win32gui.GetForegroundWindow()
    if not hwnd:
        raise RuntimeError("No foreground window detected")

    title = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = _get_process_info(pid)
    rect = win32gui.GetWindowRect(hwnd)

    return {
        "hwnd": hwnd,
        "title": title,
        "class": class_name,
        "process": process,
        "rect": {
            "left": rect[0], "top": rect[1],
            "width": rect[2] - rect[0],
            "height": rect[3] - rect[1],
        },
    }


# --- UIA context (2-level tree scan) ---

def _try_uia():
    """Lazy import pywinauto. Returns None if not available."""
    try:
        import pywinauto
        return pywinauto
    except ImportError:
        return None


def _scan_uia_children(control, depth=0, max_depth=2):
    """Recursively scan UIA control tree up to max_depth.

    Returns a list of simplified control descriptors.
    """
    if depth > max_depth:
        return []

    elements = []
    try:
        # If this is the Desktop root, get all top-level windows
        if depth == 0:
            children = control.children()
        else:
            children = [c for c in control.children()]
    except Exception:
        return []

    for child in children:
        try:
            rect = child.rectangle()
            elem = {
                "control_type": child.element_info.control_type,
                "name": child.element_info.name,
                "automation_id": child.element_info.automation_id,
                "rect": {
                    "left": int(rect.left),
                    "top": int(rect.top),
                    "width": int(rect.width()),
                    "height": int(rect.height()),
                } if rect else None,
                "children": _scan_uia_children(child, depth + 1, max_depth),
            }
        except Exception:
            continue
        elements.append(elem)

    return elements


def handle_window_get_context(params):
    """Return a simplified UIA control tree for the given window
    (or the active window if no hwnd given).

    Traversal is limited to 2 levels deep and 1 second timeout
    to avoid freezing on complex UIs.

    Params:
        hwnd:      optional window handle (defaults to active window)
        max_depth: optional recursion depth (default 2)

    Returns:
        {"hwnd": ..., "elements": [...]}
    """
    import concurrent.futures

    hwnd = params.get("hwnd")
    if not hwnd:
        hwnd = win32gui.GetForegroundWindow()
        if not hwnd:
            raise RuntimeError("No foreground window detected")

    if not win32gui.IsWindow(hwnd):
        raise ValueError(f"Invalid or destroyed hwnd: {hwnd}")

    pywinauto = _try_uia()
    if pywinauto is None:
        raise RuntimeError(
            "pywinauto is not installed (required for UIA context). "
            "Run: pip install pywinauto"
        )

    title = win32gui.GetWindowText(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = _get_process_info(pid)

    def _scan():
        desktop = pywinauto.Desktop(backend="uia")
        window_obj = desktop.window(handle=hwnd)
        return _scan_uia_children(window_obj, depth=0,
                                  max_depth=params.get("max_depth", 2))

    # Run scan with a 1-second timeout
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(_scan)
        try:
            elements = future.result(timeout=1.0)
        except concurrent.futures.TimeoutError:
            # Return partial results if available; otherwise empty
            elements = []

    return {
        "hwnd": hwnd,
        "title": title,
        "process": process,
        "elements": elements,
        "note": "UIA scan timed out at 1 second" if not elements else None,
    }
