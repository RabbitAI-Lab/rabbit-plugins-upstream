"""
Input release guard — prevents stuck keys/mouse buttons.

When keyboard_down or mouse_down are called without a matching _up,
this module's watchdog thread automatically releases the stuck input
after a configurable timeout (default 5 seconds).

Design:
  - A background daemon thread runs every second.
  - If an input was pressed > AUTO_RELEASE_SECONDS ago without release,
    the guard sends the corresponding UP event and logs a warning.
  - Thread-safe: uses a dict protected by a threading.Lock.
"""
import logging
import threading
import time

logger = logging.getLogger(__name__)

AUTO_RELEASE_SECONDS = 5
_POLL_INTERVAL = 1.0

# State: {resource_name: {"button": str/"key": str, "ts": float}}
_pressed = {}
_lock = threading.Lock()
_watchdog = None
_watchdog_running = threading.Event()


def _resource_key(resource_type, identifier):
    """Generate a unique key for a pressed resource.

    resource_type: "mouse" or "keyboard"
    identifier: button name or vk code
    """
    return f"{resource_type}:{identifier}"


# ── Track pressed inputs ──────────────────────────────────────────────────

def press(resource_type: str, identifier):
    """Record that an input has been pressed."""
    key = _resource_key(resource_type, identifier)
    with _lock:
        # If already pressed, update timestamp
        _pressed[key] = {"type": resource_type, "id": identifier, "ts": time.monotonic()}
        _ensure_watchdog()


def release(resource_type: str, identifier):
    """Record that an input has been released."""
    key = _resource_key(resource_type, identifier)
    with _lock:
        _pressed.pop(key, None)


def is_pressed(resource_type: str, identifier) -> bool:
    """Check if an input is currently held."""
    key = _resource_key(resource_type, identifier)
    with _lock:
        return key in _pressed


def is_any_pressed() -> bool:
    """Check if any inputs are held."""
    with _lock:
        return len(_pressed) > 0


# ── Watchdog ──────────────────────────────────────────────────────────────

_RELEASE_ACTIONS = {
    ("mouse", "left"):   lambda: __import__("daemon.utils.sendinput", fromlist=["mouse_up"]).mouse_up("left"),
    ("mouse", "right"):  lambda: __import__("daemon.utils.sendinput", fromlist=["mouse_up"]).mouse_up("right"),
    ("mouse", "middle"): lambda: __import__("daemon.utils.sendinput", fromlist=["mouse_up"]).mouse_up("middle"),
    ("keyboard",):       lambda id: __import__("daemon.utils.sendinput", fromlist=["keyboard_up"]).keyboard_up(id),
}


def _auto_release(key, state):
    """Send the 'up' event for a timed-out input."""
    rtype = state["type"]
    rid = state["id"]
    try:
        if rtype == "mouse":
            from daemon.utils.sendinput import mouse_up
            mouse_up(rid)
        elif rtype == "keyboard":
            from daemon.utils.sendinput import keyboard_up
            keyboard_up(rid)
        logger.warning(
            f"[AUTO-RELEASE] {rtype}.{rid} stuck for >{AUTO_RELEASE_SECONDS}s → released"
        )
    except Exception as e:
        logger.error(
            f"[AUTO-RELEASE FAILED] {rtype}.{rid}: {e}"
        )


def _watchdog_loop():
    """Watchdog thread main loop."""
    while _watchdog_running.is_set():
        time.sleep(_POLL_INTERVAL)
        now = time.monotonic()
        expired = []
        with _lock:
            for key, state in _pressed.items():
                if now - state["ts"] >= AUTO_RELEASE_SECONDS:
                    expired.append((key, state))
            for key, _ in expired:
                _pressed.pop(key, None)

        for key, state in expired:
            _auto_release(key, state)


def _ensure_watchdog():
    """Start watchdog thread if not running."""
    global _watchdog
    if _watchdog is None or not _watchdog.is_alive():
        _watchdog_running.set()
        _watchdog = threading.Thread(target=_watchdog_loop, daemon=True)
        _watchdog.start()


def shutdown():
    """Stop the watchdog and release all inputs."""
    _watchdog_running.clear()
    with _lock:
        expired = list(_pressed.items())
        _pressed.clear()
    for key, state in expired:
        _auto_release(key, state)
