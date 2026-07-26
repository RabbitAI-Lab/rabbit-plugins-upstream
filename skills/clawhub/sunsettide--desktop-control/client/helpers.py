"""
Client-side helper functions for polling-based waits.

These run *on the client side* by repeatedly calling existing daemon APIs.
They do NOT change the daemon architecture (still short-lived request-response).
"""
import re
import time

from .client import send_request


def wait_for_pixel(x, y, expected_color, timeout=5, interval=0.3, tolerance=5, monitor=0):
    """Poll pixel_color until the target pixel matches expected_color.

    Args:
        x, y:         pixel coordinates (absolute or monitor-relative)
        expected_color: str like "#RRGGBB" or dict like {"r": r, "g": g, "b": b}
        timeout:      max seconds to wait (default 5)
        interval:     seconds between polls (default 0.3)
        tolerance:    max per-channel difference for a match (default 5;
                      set to 0 for exact match)
        monitor:      monitor index (0=virtual desktop absolute, 1=primary, …)

    Returns:
        True if colour matched within timeout (within tolerance).
        False if timed out.

    Example:
        from client.helpers import wait_for_pixel
        wait_for_pixel(500, 300, "#FF0000", timeout=10, tolerance=8)
    """
    # Normalise expected_color to (r, g, b)
    if isinstance(expected_color, dict):
        ex_r = expected_color.get("r", 0)
        ex_g = expected_color.get("g", 0)
        ex_b = expected_color.get("b", 0)
    else:
        h = str(expected_color).lstrip("#").upper()
        if len(h) == 6:
            ex_r = int(h[0:2], 16)
            ex_g = int(h[2:4], 16)
            ex_b = int(h[4:6], 16)
        else:
            ex_r, ex_g, ex_b = 0, 0, 0

    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = send_request("pixel_color", {
            "x": x, "y": y, "monitor": monitor,
        })
        if resp.get("result", {}).get("success"):
            ac = resp["result"]["data"]
            dr = abs(ac["r"] - ex_r)
            dg = abs(ac["g"] - ex_g)
            db = abs(ac["b"] - ex_b)
            if dr <= tolerance and dg <= tolerance and db <= tolerance:
                return True
        time.sleep(interval)
    return False


def wait_for_window(title_regex, timeout=5, interval=0.5):
    """Poll window_list until a window matching title_regex appears.

    Args:
        title_regex: string pattern (passed to re.search, case-insensitive)
        timeout:     max seconds to wait (default 5)
        interval:    seconds between polls (default 0.5)

    Returns:
        dict with window info {"hwnd": ..., "title": ..., ...} or None if timed out.
    """
    pattern = re.compile(title_regex, re.IGNORECASE)
    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = send_request("window_list", {})
        if resp.get("result", {}).get("success"):
            windows = resp["result"]["data"].get("windows", [])
            for w in windows:
                if pattern.search(w.get("title", "")):
                    return w
        time.sleep(interval)
    return None


def wait_for_window_gone(title_regex, timeout=5, interval=0.5):
    """Poll window_list until a window matching title_regex is *gone*.

    Useful for waiting for a dialog to close.

    Returns:
        True if window disappeared within timeout.
        False if timed out.
    """
    pattern = re.compile(title_regex, re.IGNORECASE)
    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = send_request("window_list", {})
        found = False
        if resp.get("result", {}).get("success"):
            windows = resp["result"]["data"].get("windows", [])
            for w in windows:
                if pattern.search(w.get("title", "")):
                    found = True
                    break
        if not found:
            return True
        time.sleep(interval)
    return False
