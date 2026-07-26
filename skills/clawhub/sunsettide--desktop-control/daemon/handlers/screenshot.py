"""Screenshot handlers using mss + optional file save.

New in v1.2.0:
  - pixel_color: get colour at a single pixel
  - monitor parameter on screenshot/screenshot_save for multi-display coordinate anchoring
"""
import base64
import io
import os
import tempfile
import time

import mss
from PIL import Image

from daemon.utils.monitors import resolve_coords, resolve_region


def _grab_pil(region=None):
    """Return a PIL Image of the full virtual screen, or a region.

    Args:
        region: optional dict with keys {left, top, width, height}.
                When provided, only that area is captured.
    """
    with mss.mss() as sct:
        if region:
            mon = {
                "left": int(region["left"]),
                "top": int(region["top"]),
                "width": int(region["width"]),
                "height": int(region["height"]),
            }
        else:
            mon = sct.monitors[0]  # full virtual screen
        raw = sct.grab(mon)
        img = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")
        return img


def _pixel(x, y):
    """Return (r, g, b) at a single pixel. Uses 1x1 mss grab for speed."""
    with mss.mss() as sct:
        raw = sct.grab({"left": x, "top": y, "width": 1, "height": 1})
        # bgra pixel at mss pixel 0,0
        r, g, b = raw.pixel(0, 0)
        return r, g, b


def handle_pixel_color(params):
    """Get the colour of a single pixel.

    Params:
        x, y:    integer coordinates
        monitor: optional monitor index (1=primary, 2=…);
                 when given, x/y are relative to that monitor
                 when omitted (or 0), x/y are absolute virtual-screen coords
    Returns:
        {"r": r, "g": g, "b": b, "hex": "#RRGGBB"}
    """
    if "x" not in params or "y" not in params:
        raise ValueError(
            "Missing required parameters 'x' and 'y' for pixel_color. "
            "Example: {\"x\": 100, \"y\": 200}"
        )
    x = int(params["x"])
    y = int(params["y"])
    monitor = params.get("monitor", 0)
    abs_x, abs_y = resolve_coords(monitor, x, y)

    r, g, b = _pixel(abs_x, abs_y)
    return {
        "r": r, "g": g, "b": b,
        "hex": f"#{r:02X}{g:02X}{b:02X}",
        "resolved": {"x": abs_x, "y": abs_y},
    }


def handle_screenshot(params):
    """Take screenshot (full-screen or region), return base64 PNG data.

    Params:
        format: "b64" (default) or "file"
        region: optional dict {left, top, width, height}
                (monitor-relative when monitor is given)
        monitor: optional int — anchor region or full-screen to this monitor
        path:   optional file path (used when format="file")
    """
    monitor = params.get("monitor", 0)
    region = params.get("region")
    if region is not None:
        region = resolve_region(monitor, region)

    fmt = params.get("format", "b64")
    img = _grab_pil(region)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")

    if fmt == "b64":
        return {"format": "b64", "data": b64, "size_bytes": len(buf.getvalue()), "monitor": monitor}
    else:
        out_path = params.get("path") or os.path.join(
            tempfile.gettempdir(),
            f"oc_screenshot_{int(time.time())}.png",
        )
        img.save(out_path)
        return {"format": "file", "path": out_path, "size_bytes": len(buf.getvalue()), "monitor": monitor}


def handle_screenshot_save(params):
    """Take screenshot and save to a specific path.

    Params:
        path:   optional output file path
        region: optional dict {left, top, width, height}
        monitor: optional int — anchor region to this monitor
    """
    monitor = params.get("monitor", 0)
    region = params.get("region")
    if region is not None:
        region = resolve_region(monitor, region)

    out_path = params.get("path", os.path.join(tempfile.gettempdir(),
                                                f"oc_screenshot_{int(time.time())}.png"))
    img = _grab_pil(region)
    img.save(out_path)
    return {"path": out_path, "size_bytes": os.path.getsize(out_path), "monitor": monitor}
