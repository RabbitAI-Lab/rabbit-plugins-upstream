"""
desktop-control client package.

Exposes IPC client and optional polling helpers.
"""
from .client import send_request, _ensure_daemon
from .helpers import wait_for_pixel, wait_for_window, wait_for_window_gone

__all__ = [
    "send_request",
    "_ensure_daemon",
    "wait_for_pixel",
    "wait_for_window",
    "wait_for_window_gone",
]
