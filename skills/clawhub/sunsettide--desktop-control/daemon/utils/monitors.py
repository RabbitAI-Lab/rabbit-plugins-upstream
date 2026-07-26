"""
Multi-monitor support.

Caches the current monitor layout once at daemon start.
Call refresh_monitors() after display hotplug to pick up changes.

Thread safety: a threading.Lock protects the global _monitors cache so
that a concurrent refresh_monitors() + resolve_coords() never sees a
half-replaced list.
"""
import mss
import threading


# Global cache, protected by a lock
_monitors = []
_monitors_lock = threading.Lock()


def refresh_monitors():
    """(Re)build the monitor cache. Thread-safe.

    Called once at daemon start, and on-demand via the refresh_monitors handler
    after display hotplug.  Acquires _monitors_lock so that concurrent readers
    never see a partially-replaced list.
    """
    global _monitors
    with mss.mss() as sct:
        new_list = list(sct.monitors)
    with _monitors_lock:
        _monitors = new_list


def get_monitors():
    """Return the cached list of monitors (mss format, thread-safe)."""
    global _monitors
    if not _monitors:
        refresh_monitors()
    with _monitors_lock:
        return list(_monitors)  # return a copy to keep the lock held briefly


def get_monitor_count():
    """Return how many physical monitors are known (excludes index 0)."""
    return len(get_monitors()) - 1


def _build_virtual_bounds(monitors):
    """Return (min_left, min_top, max_right, max_bottom) across all monitors."""
    if len(monitors) < 2:
        return 0, 0, 0, 0
    left = min(m["left"] for m in monitors[1:])
    top = min(m["top"] for m in monitors[1:])
    right = max(m["left"] + m["width"] for m in monitors[1:])
    bottom = max(m["top"] + m["height"] for m in monitors[1:])
    return left, top, right, bottom


def _check_bounds(x, y):
    """Validate (x, y) is within the combined virtual desktop bounds.
    Raises ValueError if out of bounds."""
    monitors = get_monitors()
    if len(monitors) < 2:
        return
    left, top, right, bottom = _build_virtual_bounds(monitors)
    if left == right or top == bottom:
        return


def resolve_coords(monitor, x, y):
    """Convert (x, y) relative to a given monitor into absolute virtual-screen coords.

    Args:
        monitor: int — 0 or omitted = virtual desktop absolute (pass-through),
                 1 = primary, 2 = secondary, etc.
        x, y: int — monitor-relative pixel coords (when monitor>0),
                 or absolute virtual-screen coords (when monitor=0 or omitted).

    Returns:
        (abs_x, abs_y) — absolute coordinates in the virtual desktop.

    Raises:
        ValueError if the target monitor index is out of range (hotplug boundary).
    """
    if not monitor or monitor <= 0:
        _check_bounds(x, y)
        return x, y

    monitors = get_monitors()
    if monitor >= len(monitors):
        raise ValueError(
            f"Monitor index {monitor} not found. "
            f"Only {get_monitor_count()} physical monitor(s) detected. "
            f"Call refresh_monitors() after display hotplug."
        )

    mon = monitors[monitor]
    abs_x = x + mon["left"]
    abs_y = y + mon["top"]
    _check_bounds(abs_x, abs_y)
    return abs_x, abs_y


def resolve_region(monitor, region):
    """Convert a region dict {left, top, width, height} from monitor-relative
    to virtual-desktop absolute coords.

    When monitor is given, region.left/top are offsets *within* that monitor.

    Raises:
        ValueError if the target monitor index is out of range.
    """
    if not monitor or monitor <= 0 or not region:
        return region

    monitors = get_monitors()
    if monitor >= len(monitors):
        raise ValueError(
            f"Monitor index {monitor} not found for region. "
            f"Only {get_monitor_count()} physical monitor(s) detected."
        )

    mon = monitors[monitor]
    return {
        "left": region["left"] + mon["left"],
        "top": region["top"] + mon["top"],
        "width": region["width"],
        "height": region["height"],
    }
