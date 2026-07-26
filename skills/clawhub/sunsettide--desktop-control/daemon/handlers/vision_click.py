"""
Vision-driven mouse and keyboard handlers.

Provides:
  - find_text:       OCR-based text search → coordinates
  - click_text:      find text then click
  - type_to_text:    find text then type near it
  - mouse_smart_action: multi-step action chain driven by text targets

All functions depend on pytesseract (soft dependency).
"""
import io
import os
import time
import threading

from PIL import Image

from daemon.utils.monitors import resolve_region, resolve_coords
from daemon.utils import sendinput as si

# --- pytesseract import (soft dep) ---

_pytesseract = None
_tesseract_import_error = None

def _resolve_tesseract_cmd():
    """Determine the tesseract executable path.
    Priority: TESSERACT_PATH env > registry > default install path."""
    tess_path = os.environ.get("TESSERACT_PATH", "")
    if tess_path and os.path.isfile(tess_path):
        return tess_path
    # Check registry
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
        tess_path, _ = winreg.QueryValueEx(key, "TESSERACT_PATH")
        if os.path.isfile(tess_path):
            return tess_path
    except Exception:
        pass
    # Default install paths
    for p in [r"C:\Program Files\Tesseract-OCR\tesseract.exe",
              r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"]:
        if os.path.isfile(p):
            return p
    return ""

try:
    import pytesseract as _pt
    _pytesseract = _pt
    tess_path = _resolve_tesseract_cmd()
    if tess_path:
        _pytesseract.pytesseract.tesseract_cmd = tess_path
except Exception as e:
    _tesseract_import_error = str(e)


def _check_pytesseract():
    if _pytesseract is None:
        msg = _tesseract_import_error or "pytesseract is not installed"
        raise ValueError(
            f"Vision-click unavailable: {msg}. "
            f"Install: pip install pytesseract, and download Tesseract OCR from "
            f"https://github.com/UB-Mannheim/tesseract/wiki"
        )
    # Re-check TESSERACT_PATH at runtime (in case daemon didn't inherit env)
    tess_path = os.environ.get("TESSERACT_PATH", "")
    if tess_path:
        _pytesseract.pytesseract.tesseract_cmd = tess_path
    # Also check tesseract binary is actually usable
    try:
        _pytesseract.get_tesseract_version()
    except Exception:
        raise ValueError(
            "Tesseract OCR engine is installed but tesseract binary was not found. "
            "Download from https://github.com/UB-Mannheim/tesseract/wiki "
            "and ensure it's in your PATH, or set TESSERACT_PATH env var."
        )


# --- Screenshot cache (500ms dedup) ---

_SCREENSHOT_CACHE = {}
_SCREENSHOT_CACHE_LOCK = threading.Lock()
_CACHE_TTL_MS = 500


def _grab_region_cached(region=None, monitor=0, lang="chi_sim+eng"):
    """Grab screenshot of region, with 500ms cache dedup.

    Cache key includes region + monitor + lang so that different screens
    or OCR language configs don't share a stale snapshot.
    """
    region_part = str(region) if region else "__full__"
    cache_key = f"{region_part}|mon{monitor}|{lang}"
    now = time.perf_counter()
    with _SCREENSHOT_CACHE_LOCK:
        cached = _SCREENSHOT_CACHE.get(cache_key)
        if cached and (now - cached["ts"]) * 1000 < _CACHE_TTL_MS:
            return cached["image"]

    # Grab from screenshot handler
    from .screenshot import _grab_pil
    img = _grab_pil(region)

    with _SCREENSHOT_CACHE_LOCK:
        _SCREENSHOT_CACHE[cache_key] = {"image": img, "ts": now}
    return img


# ============================================================================
# 1. find_text: OCR-based text search → coordinates
# ============================================================================

def _extract_text_regions(img, lang, exact_match, search_text, limit):
    """Run tesseract OCR and find bounding boxes matching search_text.

    Uses image_to_data() which returns per-word confidence and bounding boxes.

    Returns:
        list of dicts: {"text": str, "x": int, "y": int,
                        "bbox": {"left", "top", "width", "height"},
                        "confidence": float}
    """
    _check_pytesseract()
    data = _pytesseract.image_to_data(img, lang=lang, output_type=_pytesseract.Output.DICT)

    matches = []
    n = len(data.get("text", []))

    for i in range(n):
        word = data["text"][i].strip()
        if not word:
            continue
        conf = data.get("conf", [0])[i]
        try:
            conf = float(conf)
        except (ValueError, TypeError):
            conf = 0

        if exact_match:
            if word.lower() != search_text.lower():
                continue
        else:
            if search_text.lower() not in word.lower():
                continue

        left = int(data.get("left", [0])[i])
        top = int(data.get("top", [0])[i])
        width = int(data.get("width", [0])[i])
        height = int(data.get("height", [0])[i])

        matches.append({
            "text": data["text"][i].strip(),
            "x": left + width // 2,
            "y": top + height // 2,
            "bbox": {"left": left, "top": top, "width": width, "height": height},
            "confidence": round(conf, 1),
        })

    # Sort by confidence descending, then limit
    matches.sort(key=lambda m: m["confidence"], reverse=True)

    if limit and limit > 0:
        matches = matches[:limit]

    return matches


def handle_find_text(params):
    """Search for text on screen and return coordinates.

    Params:
        text:         Required. Text to search for.
        region:       Optional dict {left, top, width, height}.
        monitor:      Optional int — anchor region to this monitor.
        lang:         Tesseract language string (default: chi_sim+eng).
        exact_match:  Exact match or substring match (default: true).
        limit:        Max results (default: 10).

    Returns:
        {"matches": [...]}
    """
    search_text = params.get("text")
    if not search_text:
        raise ValueError(
            "Missing required parameter 'text' for find_text. "
            "Example: {\"text\": \"确定\"}"
        )

    region = params.get("region")
    monitor = params.get("monitor", 0)
    if region is not None:
        region = resolve_region(monitor, region)
    lang = params.get("lang", "chi_sim+eng")
    exact_match = params.get("exact_match", True)
    limit = params.get("limit", 10)

    img = _grab_region_cached(region, monitor=monitor, lang=lang)
    matches = _extract_text_regions(img, lang, exact_match, search_text, limit)

    return {"matches": matches, "count": len(matches)}


# ============================================================================
# 2. click_text: find text then click
# ============================================================================

def _pick_best_match(matches, prefer_center=True, screen_w=1920, screen_h=1080):
    """Pick the best match from a list of matches.

    Strategies:
      - prefer_center: pick the match closest to screen center
      - fallback: pick the highest confidence match
    """
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0]

    if prefer_center:
        cx, cy = screen_w / 2, screen_h / 2
        def _dist(m):
            return (m["x"] - cx) ** 2 + (m["y"] - cy) ** 2
        return min(matches, key=_dist)

    return matches[0]


def handle_click_text(params):
    """Find text on screen and click at its center.

    Params:
        text:         Required. Text to find and click.
        region:       Optional search region.
        monitor:      Optional monitor index.
        lang:         OCR language (default: chi_sim+eng).
        exact_match:  Exact or substring match (default: true).
        button:       Mouse button: left|right|middle (default: left).
        click_type:   single|double (default: single).
        offset:       dict {x, y} offset from text center (default: {0,0}).
        wait:         Seconds to wait before clicking (default: 0).
        prefer_center: Pick match closest to screen center (default: true).
    """
    search_text = params.get("text")
    if not search_text:
        raise ValueError(
            "Missing required parameter 'text' for click_text."
        )

    # First find the text
    find_params = {
        "text": search_text,
        "region": params.get("region"),
        "monitor": params.get("monitor", 0),
        "lang": params.get("lang", "chi_sim+eng"),
        "exact_match": params.get("exact_match", True),
        "limit": 10,
    }
    found = handle_find_text(find_params)
    matches = found.get("matches", [])

    if not matches:
        return {"success": False, "error": f"Text not found: '{search_text}'"}

    # Pick best match
    screen_w = 1920
    screen_h = 1080
    try:
        import ctypes
        screen_w = ctypes.windll.user32.GetSystemMetrics(0)
        screen_h = ctypes.windll.user32.GetSystemMetrics(1)
    except Exception:
        pass

    best = _pick_best_match(matches, params.get("prefer_center", True), screen_w, screen_h)

    # Apply offset
    offset = params.get("offset", {})
    click_x = best["x"] + offset.get("x", 0)
    click_y = best["y"] + offset.get("y", 0)

    # Optional wait
    wait = float(params.get("wait", 0))
    if wait > 0:
        time.sleep(wait)

    # Execute click
    button = params.get("button", "left")
    click_type = params.get("click_type", "single")
    clicks = 2 if click_type == "double" else 1

    # Resolve monitor coords if monitor is specified
    monitor = params.get("monitor", 0)
    abs_x, abs_y = resolve_coords(monitor, click_x, click_y)

    si.mouse_click(abs_x, abs_y, button, clicks)

    return {
        "success": True,
        "text": best["text"],
        "clicked_at": {"x": click_x, "y": click_y},
        "match_count": len(matches),
        "confidence": best["confidence"],
    }


# ============================================================================
# 3. type_to_text: find text then type near it
# ============================================================================

_ANCHOR_OFFSETS = {
    "above": {"x": 0, "y": -30},
    "below": {"x": 0, "y": 30},
    "left":  {"x": -60, "y": 0},
    "right": {"x": 60, "y": 0},
}


def handle_type_to_text(params):
    """Find text on screen, click near it (based on anchor direction), then type.

    Params:
        text:         Required. Anchor text to find.
        input:        Required. Text to type.
        region:       Optional search region.
        monitor:      Optional monitor index.
        lang:         OCR language (default: chi_sim+eng).
        anchor:       Direction relative to text: above|below|left|right (default: below).
        offset:       Extra offset as {x, y} (added to anchor offset).
        clear_first:  Select all then delete before typing (default: true).
        press_enter:  Press Enter after typing (default: false).
        use_uia:      Try UIA edit field detection (default: true).
    """
    search_text = params.get("text")
    input_text = params.get("input")
    if not search_text:
        raise ValueError("Missing required parameter 'text' for type_to_text.")
    if input_text is None:
        raise ValueError("Missing required parameter 'input' for type_to_text.")

    anchor = params.get("anchor", "below")
    extra_offset = params.get("offset", {})
    clear_first = params.get("clear_first", True)
    press_enter = params.get("press_enter", False)
    use_uia = params.get("use_uia", True)
    monitor = params.get("monitor", 0)

    # Find the anchor text
    find_params = {
        "text": search_text,
        "region": params.get("region"),
        "monitor": monitor,
        "lang": params.get("lang", "chi_sim+eng"),
        "exact_match": True,
        "limit": 5,
    }
    found = handle_find_text(find_params)
    matches = found.get("matches", [])

    if not matches:
        return {"success": False, "error": f"Anchor text not found: '{search_text}'"}

    best = matches[0]

    # Try UIA-based edit field detection first
    uia_used = False
    if use_uia:
        try:
            from daemon.handlers.uia import handle_find
            # Search for editable fields near the anchor
            uia_params = {
                "control_type": "Edit",
                "title": "",
                "region": {
                    "left": best["bbox"]["left"],
                    "top": best["bbox"]["top"] - 80,
                    "width": best["bbox"]["width"] + 200,
                    "height": best["bbox"]["height"] + 160,
                },
            }
            uia_result = handle_find(uia_params)
            uia_fields = uia_result.get("controls", [])
            if uia_fields:
                # Use the first UIA edit field
                uia_target = uia_fields[0]
                uia_x = uia_target.get("x", 0) + uia_target.get("width", 100) // 2
                uia_y = uia_target.get("y", 0) + uia_target.get("height", 20) // 2
                si.mouse_click(uia_x, uia_y, "left", 1)
                time.sleep(0.1)
                uia_used = True
        except Exception:
            pass

    if not uia_used:
        # Calculate click position based on anchor, with DPI scaling
        # Get DPI scaling factor so offset values work at any resolution
        dpi_scale = 1.0
        try:
            import ctypes
            hdc = ctypes.windll.user32.GetDC(0)
            dpi_x = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # LOGPIXELSX
            ctypes.windll.user32.ReleaseDC(0, hdc)
            dpi_scale = max(1.0, dpi_x / 96.0)
        except Exception:
            pass

        anchor_off = _ANCHOR_OFFSETS.get(anchor, _ANCHOR_OFFSETS["below"])
        click_x = best["x"] + int(anchor_off["x"] * dpi_scale) + extra_offset.get("x", 0)
        click_y = best["y"] + int(anchor_off["y"] * dpi_scale) + extra_offset.get("y", 0)

        abs_x, abs_y = resolve_coords(monitor, click_x, click_y)
        si.mouse_click(abs_x, abs_y, "left", 1)
        time.sleep(0.1)

    # Clear existing text if requested
    if clear_first:
        si.keyboard_hotkey(17, 65)  # Ctrl+A
        time.sleep(0.05)
        si.keyboard_press(8)  # Backspace (VK_BACK = 8)
        time.sleep(0.05)

    # Type the input text
    si.keyboard_type(input_text)
    time.sleep(0.1)

    # Press Enter if requested
    if press_enter:
        si.keyboard_press(13)  # VK_RETURN

    return {
        "success": True,
        "anchor_text": search_text,
        "anchor_bbox": best["bbox"],
        "input_position": {"x": best["x"], "y": best["y"]},
        "input_length": len(input_text),
    }


# ============================================================================
# 4. mouse_smart_action: multi-step action chain driven by text
# ============================================================================

def handle_mouse_smart_action(params):
    """Execute a chain of mouse actions driven by text targets.

    Params:
        text:     Initial text target to find.
        actions:  List of action dicts:
                  {"type": "hover|click|move_to|drag|wait", ...}
        monitor:  Optional monitor index.

    Returns:
        {"success": True, "steps_completed": N, "results": [...]}
    """
    initial_text = params.get("text")
    actions = params.get("actions", [])
    monitor = params.get("monitor", 0)
    lang = params.get("lang", "chi_sim+eng")
    region = params.get("region")

    if not actions:
        raise ValueError("Missing required parameter 'actions' for mouse_smart_action.")

    # Find initial target
    current_position = None
    results = []

    def _find_text_target(text):
        fp = handle_find_text({
            "text": text,
            "region": region,
            "monitor": monitor,
            "lang": lang,
            "exact_match": True,
            "limit": 5,
        })
        matches = fp.get("matches", [])
        if not matches:
            return None
        return matches[0]

    def _move_to_xy(x, y):
        abs_x, abs_y = resolve_coords(monitor, x, y)
        si.mouse_move(abs_x, abs_y)
        time.sleep(0.05)
        return {"x": x, "y": y}

    def _click(button, click_type):
        clicks = 2 if click_type == "double" else 1
        si.mouse_click(None, None, button, clicks)

    for i, action in enumerate(actions):
        atype = action.get("type", "")
        step_result = {"step": i, "type": atype}

        try:
            if atype == "hover":
                target_text = action.get("text", initial_text)
                target = _find_text_target(target_text)
                if not target:
                    step_result["error"] = f"Text not found: '{target_text}'"
                    step_result["success"] = False
                else:
                    _move_to_xy(target["x"], target["y"])
                    duration = float(action.get("duration", 0.5))
                    time.sleep(duration)
                    current_position = (target["x"], target["y"])
                    step_result["success"] = True
                    step_result["position"] = {"x": target["x"], "y": target["y"]}

            elif atype == "click":
                button = action.get("button", "left")
                click_type = action.get("click_type", "single")
                if current_position:
                    abs_x, abs_y = resolve_coords(monitor, current_position[0], current_position[1])
                    si.mouse_click(abs_x, abs_y, button, 2 if click_type == "double" else 1)
                else:
                    _click(button, click_type)
                step_result["success"] = True
                step_result["button"] = button

            elif atype == "move_to":
                target_text = action.get("text", "")
                if not target_text:
                    step_result["error"] = "Missing 'text' in move_to action"
                    step_result["success"] = False
                else:
                    target = _find_text_target(target_text)
                    if not target:
                        step_result["error"] = f"Text not found: '{target_text}'"
                        step_result["success"] = False
                    else:
                        _move_to_xy(target["x"], target["y"])
                        current_position = (target["x"], target["y"])
                        step_result["success"] = True
                        step_result["position"] = {"x": target["x"], "y": target["y"]}
                wait = float(action.get("wait", 0))
                if wait > 0:
                    time.sleep(wait)
                    step_result["waited"] = wait

            elif atype == "drag":
                from_text = action.get("from_text", initial_text)
                to_text = action.get("to_text", "")
                if not to_text:
                    step_result["error"] = "Missing 'to_text' in drag action"
                    step_result["success"] = False
                else:
                    from_target = _find_text_target(from_text)
                    to_target = _find_text_target(to_text)
                    if not from_target or not to_target:
                        step_result["error"] = f"Text not found: missing {not from_target and from_text or to_text}"
                        step_result["success"] = False
                    else:
                        abs_sx, abs_sy = resolve_coords(monitor, from_target["x"], from_target["y"])
                        abs_ex, abs_ey = resolve_coords(monitor, to_target["x"], to_target["y"])
                        si.mouse_drag(abs_sx, abs_sy, abs_ex, abs_ey,
                                      action.get("button", "left"))
                        current_position = (to_target["x"], to_target["y"])
                        step_result["success"] = True
                        step_result["from"] = {"x": from_target["x"], "y": from_target["y"]}
                        step_result["to"] = {"x": to_target["x"], "y": to_target["y"]}

            elif atype == "wait":
                duration = float(action.get("duration", action.get("wait", 1)))
                time.sleep(duration)
                step_result["success"] = True
                step_result["duration"] = duration

            else:
                step_result["error"] = f"Unknown action type: '{atype}'"
                step_result["success"] = False

        except Exception as e:
            step_result["error"] = str(e)
            step_result["success"] = False

        results.append(step_result)

        if not step_result.get("success"):
            break

    all_success = all(r.get("success") for r in results)
    # Find the first failed step index, if any
    failed_at = None
    for r in results:
        if not r.get("success"):
            failed_at = r.get("step")
            break

    resp = {
        "success": all_success,
        "steps_completed": len(results),
        "results": results,
    }
    if failed_at is not None:
        resp["failed_at"] = failed_at
    return resp
