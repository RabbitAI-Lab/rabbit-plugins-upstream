"""
UIA (pywinauto) handlers — element finding, clicking, and text reading.

All methods run on the dedicated STA thread pool and return plain Python dicts.
"""
import time
from typing import Optional

import pywinauto

from daemon.utils.uia_threadpool import UIAThreadPool

# Global STA thread pool — shared across all UIA requests
_uia_pool = UIAThreadPool(max_workers=2)


# --- Internal helpers (run inside STA threads) ---

def _find_window(window_title: str):
    """Find a top-level window matching (case-insensitive substring). Returns None."""
    desktop = pywinauto.Desktop(backend="uia")
    for w in desktop.windows():
        txt = w.window_text()
        if window_title.lower() in txt.lower() and txt.strip():
            return w
    return None


def _find_element(window_title: str = None,
                  name: str = None,
                  control_type: str = None,
                  automation_id: str = None,
                  timeout: float = 10.0) -> tuple:
    """Find a UIA element and return (element_dict, None) or (None, error)."""
    try:
        if window_title:
            top = _find_window(window_title)
            if top is None:
                return None, f"No window matching '{window_title}'"
        else:
            desktop = pywinauto.Desktop(backend="uia")
            top = None
            for w in desktop.windows():
                if w.window_text().strip():
                    top = w
                    break
            if top is None:
                return None, "No visible windows found"

        # Find element by criteria
        criteria = {}
        if name:
            criteria["name"] = name
        if control_type:
            criteria["control_type"] = control_type
        if automation_id:
            criteria["automation_id"] = automation_id

        if criteria:
            elem = top.child_window(**criteria).wait("visible", timeout=timeout)
        else:
            elem = top

        rect = elem.rectangle()
        return {
            "name": elem.window_text(),
            "control_type": elem.element_info.control_type if hasattr(elem, 'element_info') else None,
            "automation_id": elem.element_info.automation_id if hasattr(elem, 'element_info') else None,
            "rect": {
                "left": rect.left, "top": rect.top,
                "right": rect.right, "bottom": rect.bottom,
                "width": rect.width(), "height": rect.height(),
            },
            "center": {"x": rect.mid_point().x, "y": rect.mid_point().y},
            "is_enabled": elem.is_enabled() if hasattr(elem, 'is_enabled') else True,
        }, None
    except Exception as e:
        return None, f"Element error: {e}"


def _uia_click(window_title: str = None,
               name: str = None,
               control_type: str = None,
               automation_id: str = None,
               timeout: float = 10.0) -> dict:
    """Find and click a UIA element."""
    elem, err = _find_element(window_title, name, control_type, automation_id, timeout)
    if err:
        return {"success": False, "error": err}

    try:
        # Try to invoke via the pywinauto wrapper
        top = _find_window(window_title) if window_title else None
        desktop = pywinauto.Desktop(backend="uia")
        if top is None:
            for w in desktop.windows():
                if w.window_text().strip():
                    top = w
                    break
        if top:
            criteria = {}
            if name:
                criteria["name"] = name
            if control_type:
                criteria["control_type"] = control_type
            if automation_id:
                criteria["automation_id"] = automation_id
            if criteria:
                target = top.child_window(**criteria).wait("visible", timeout=timeout)
                try:
                    target.invoke()
                    return {"success": True, "method": "invoke", "element": elem}
                except Exception:
                    pass  # fall to coordinate click

        # Coordinate click fallback
        cx, cy = elem["center"]["x"], elem["center"]["y"]
        from daemon.utils import sendinput as si
        si.mouse_click(cx, cy)
        return {"success": True, "method": "coordinate", "element": elem,
                "clicked_at": {"x": cx, "y": cy}}
    except Exception as ex:
        return {"success": False, "error": str(ex)}


def _read_text(window_title: str = None,
               name: str = None,
               control_type: str = None,
               timeout: float = 10.0) -> dict:
    """Read text from a window or specific element."""
    try:
        desktop = pywinauto.Desktop(backend="uia")
        if window_title:
            win = None
            for w in desktop.windows():
                if window_title.lower() in w.window_text().lower():
                    win = w
                    break
            if win is None:
                return {"success": False, "error": f"Window '{window_title}' not found"}
        else:
            win = None
            for w in desktop.windows():
                if w.window_text().strip():
                    win = w
                    break
            if win is None:
                return {"success": False, "error": "No visible windows"}

        if name or control_type:
            criteria = {}
            if name:
                criteria["name"] = name
            if control_type:
                criteria["control_type"] = control_type
            elem = win.child_window(**criteria).wait("visible", timeout=timeout)
            return {"success": True, "text": elem.window_text(), "element_name": name}

        # Read full window text
        texts = []
        for ctrl in win.descendants():
            txt = ctrl.window_text()
            if txt.strip():
                texts.append(txt.strip())
        return {"success": True, "text": "\n".join(texts), "element_count": len(texts)}
    except Exception as e:
        return {"success": False, "error": str(e)}


# --- Handlers (called from server.py dispatcher, return plain dicts) ---

def handle_find(params: dict) -> dict:
    future = _uia_pool.submit(
        _find_element,
        window_title=params.get("window_title"),
        name=params.get("name"),
        control_type=params.get("control_type"),
        automation_id=params.get("automation_id"),
        timeout=params.get("timeout", 10.0),
    )
    element, error = future.result()
    if error:
        return {"success": False, "error": error, "method": "uia_find"}
    return {"success": True, "element": element, "method": "uia_find"}


def handle_click(params: dict) -> dict:
    future = _uia_pool.submit(
        _uia_click,
        window_title=params.get("window_title"),
        name=params.get("name"),
        control_type=params.get("control_type"),
        automation_id=params.get("automation_id"),
        timeout=params.get("timeout", 10.0),
    )
    result = future.result()
    result["method"] = "uia_click"
    return result


def handle_get_text(params: dict) -> dict:
    future = _uia_pool.submit(
        _read_text,
        window_title=params.get("window_title"),
        name=params.get("name"),
        control_type=params.get("control_type"),
        timeout=params.get("timeout", 10.0),
    )
    return future.result()
