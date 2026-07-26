"""
Screen template matching handler.

Finds a given template image within a screen region using OpenCV's
TM_CCOEFF_NORMED.  This is a SOFT dependency — opencv-python is NOT
in requirements.txt.

Typical use case: locate an icon or button that has no UIA access,
then click on it via mouse_move + mouse_click.
"""
import base64
import io
import os

import numpy as np
from PIL import Image

from daemon.utils.monitors import resolve_region
from .screenshot import _grab_pil

# Optional OpenCV import
_cv2 = None
_cv2_import_error = None
try:
    import cv2 as _cv
    _cv2 = _cv
except Exception as e:
    _cv2_import_error = str(e)


def handle_image_find(params):
    """Find a template image on screen.

    Params:
        template:   Base64-encoded PNG string of the template image (required)
        region:     optional search area {left, top, width, height}
                    (monitor-relative when monitor is given)
        monitor:    optional monitor index (default 0 = virtual desktop)
        confidence: min matching confidence 0.0-1.0 (default 0.8)
        limit:      max results to return (default 1, -1 = all)

    Returns:
        {"matches": [{"x": int, "y": int, "width": int, "height": int,
                       "confidence": float}, ...]}

    Raises:
        ValueError: cv2 not installed, invalid template, no matches found.
    """
    if _cv2 is None:
        msg = _cv2_import_error or "opencv-python is not installed"
        raise ValueError(
            f"Image matching unavailable: {msg}. "
            f"Install: pip install opencv-python numpy"
        )

    # Parse template
    template_b64 = params.get("template")
    if not template_b64:
        raise ValueError(
            "Missing required parameter 'template' (base64 PNG). "
            "Example: {\"template\": \"iVBOR...\", \"confidence\": 0.8}"
        )

    try:
        template_bytes = base64.b64decode(template_b64)
        np_arr = np.frombuffer(template_bytes, dtype=np.uint8)
        template_img = _cv2.imdecode(np_arr, _cv2.IMREAD_COLOR)
        if template_img is None:
            raise ValueError("Template image could not be decoded. Ensure it's a valid PNG/JPEG.")
    except Exception as e:
        if "Base64" in type(e).__name__:
            raise ValueError(f"Invalid base64 template: {e}")
        raise ValueError(f"Failed to decode template image: {e}")

    t_h, t_w = template_img.shape[:2]

    # Resolve region
    monitor = params.get("monitor", 0)
    region = params.get("region")
    if region is not None:
        region = resolve_region(monitor, region)

    # Grab screen image
    screen = _grab_pil(region)
    # PIL -> OpenCV (RGB -> BGR)
    screen_np = np.array(screen)
    screen_np = _cv2.cvtColor(screen_np, _cv2.COLOR_RGB2BGR)

    # Match
    confidence = float(params.get("confidence", 0.8))
    result = _cv2.matchTemplate(screen_np, template_img, _cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= confidence)

    return_center = params.get("return_center", True)
    limit = int(params.get("limit", 1))
    matches = []
    for pt in zip(*locations[::-1]):  # Switch to (x, y) format
        top_left_x = int(pt[0])
        top_left_y = int(pt[1])
        match = {
            "x": top_left_x,
            "y": top_left_y,
            "width": t_w,
            "height": t_h,
            "confidence": float(result[pt[1], pt[0]]),
        }
        if return_center:
            match["center_x"] = top_left_x + t_w // 2
            match["center_y"] = top_left_y + t_h // 2
        matches.append(match)
        if limit > 0 and len(matches) >= limit:
            break

    if not matches:
        return {"matches": [], "note": f"No matches found above confidence {confidence}"}

    return {"matches": matches}
