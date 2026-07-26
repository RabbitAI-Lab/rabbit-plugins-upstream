"""
Context-aware humanization engine.

Automatically detects when to apply human-like behavior (mouse tremor, click drift,
randomized typing speed, etc.) based on:
  - Active window process name (browsers → more human-like)
  - Operation frequency (rapid clicks → more human-like)
  - Main window class name (covers Chromium variants not in process-name whitelist)
  - User override via 'human' parameter in any handler call

Architecture:
  - HumanEngine is a singleton, holds state (active window, op counter, timer).
  - mouse.py / keyboard.py handlers call human_engine.get_level() at the start.
  - The engine returns "robotic" | "light" | "heavy".
  - Handlers then apply the corresponding profile parameters.

No manual profile switching needed. Fully automatic.
"""
import threading
import time
from typing import Optional

# ── Browser detection ─────────────────────────────────────────────────────

# 1. Process-name whitelist (comprehensive)
BROWSER_PROCESSES = {
    "chrome.exe", "msedge.exe", "firefox.exe", "opera.exe", "brave.exe",
    "360chrome.exe", "360se.exe", "sogouexplorer.exe", "liebao.exe",
    "maxthon.exe", "safari.exe", "vivaldi.exe", "yandexbrowser.exe",
    "centbrowser.exe", "coccocbrowser.exe", "tor.exe", "waterfox.exe",
    "palemoon.exe", "seamonkey.exe", "k-meleon.exe", "netsurf.exe",
    "iridium.exe", "dissenterbrowser.exe",
}

# 2. Window-class prefixes (catches Chromium forks not in process-name list)
BROWSER_CLASS_PREFIXES = {
    "Chrome_WidgetWin",       # Chrome/Edge/Chromium
    "MozillaWindowClass",     # Firefox
    "MozillaUIWindowClass",   # Firefox sub-windows
    "IEFrame",                # Internet Explorer / Edge Legacy
    "ApplicationFrameWindow", # UWP apps including Edge
}


def _detect_browser_from_class() -> bool:
    """Check if the foreground window class suggests a browser.

    This catches browsers whose executable name isn't in BROWSER_PROCESSES
    (e.g., obscure Chromium forks, custom builds).
    """
    try:
        import win32gui
        hwnd = win32gui.GetForegroundWindow()
        class_name = win32gui.GetClassName(hwnd)
        for prefix in BROWSER_CLASS_PREFIXES:
            if class_name.startswith(prefix):
                return True
        # Also check top-level owner window for IEFrame pattern
        parent = win32gui.GetParent(hwnd)
        if parent:
            parent_class = win32gui.GetClassName(parent)
            if parent_class.startswith("IEFrame"):
                return True
    except Exception:
        pass
    return False


# ── Thresholds ────────────────────────────────────────────────────────────

LIGHT_OP_THRESHOLD = 5      # ops in same window → human_light
HEAVY_OP_THRESHOLD = 10     # ops in same window → human_heavy
RAPID_INTERVAL = 0.1        # seconds between ops to count as "rapid"
ESCALATION_DELAY = 10.0     # seconds of sustained activity → human_heavy
DECAY_TIMEOUT = 3.0         # seconds idle → back to robotic (non-browser)
BROWSER_DECAY_TIMEOUT = 5.0 # browser idle timeout (longer to avoid flickering)
UIA_ABSENCE_HEAVY = True    # no UIA controls → human_heavy


# ── Engine ────────────────────────────────────────────────────────────────

class HumanEngine:
    """Thread-safe context-aware humanization engine."""

    def __init__(self):
        self._lock = threading.Lock()
        self._state = "robotic"          # current humanization level
        self._last_active_time = 0.0     # monotonic timestamp
        self._op_counter = 0             # operations since last window switch
        self._current_window_pid = 0     # pid of the last active window
        self._level_activated_at = 0.0   # when current level was activated
        self._process_name_cache = ""    # cached to avoid repeated syscalls

    def get_level(self, operation_type: str = "",
                  process_name: Optional[str] = None,
                  user_override: Optional[str] = None) -> str:
        """Determine the humanization level for the next operation.

        Args:
            operation_type: Optional description (e.g. "click", "type", "move").
            process_name: Active window process name (e.g. "chrome.exe").
                          None = auto-detect from foreground window.
                          Explicit empty string = "no browser context".
            user_override: Explicit human param from the caller.
                           "off" → robotic, "light" → light, "heavy" → heavy.
                           None → fully automatic.

        Returns:
            "robotic", "light", or "heavy".
        """
        with self._lock:
            return self._compute_level(operation_type, process_name, user_override)

    def _compute_level(self, op_type, process_name, user_override):
        """Internal logic, must be called with _lock held."""
        now = time.monotonic()

        # 1. User override wins everything
        if user_override:
            override_lower = user_override.lower().strip()
            if override_lower in ("off", "false", "0"):
                self._state = "robotic"
                return "robotic"
            if override_lower in ("light", "1"):
                self._state = "light"
                self._level_activated_at = now
                return "light"
            if override_lower in ("heavy", "2"):
                self._state = "heavy"
                self._level_activated_at = now
                return "heavy"
            # Unknown override value → ignore, use automatic

        # 2. Auto-detect process name if not provided
        if process_name is None:
            process_name = self._detect_active_process()
        if not process_name:
            process_name = ""

        # 3. Track window changes → operations are PER-WINDOW
        pid = self._detect_active_pid()
        if pid != self._current_window_pid:
            # Window changed → reset counter; state will decay naturally
            self._op_counter = 0
            self._current_window_pid = pid
            self._process_name_cache = process_name

        # 4. Update operation timing (sliding window — every call refreshes)
        time_since_last = now - self._last_active_time
        self._last_active_time = now

        if time_since_last < RAPID_INTERVAL:
            self._op_counter += 1
        else:
            # Cooldown between ops: decays counter
            if time_since_last > DECAY_TIMEOUT:
                self._op_counter = 0
            else:
                self._op_counter = max(1, self._op_counter)

        # 5. Determine browser context
        #    Check process-name whitelist first.
        #    Only fall back to window-class detection when no explicit
        #    process_name was provided by the caller (i.e. auto-detected).
        if process_name in BROWSER_PROCESSES:
            is_browser = True
        elif process_name:
            # Caller provided a non-browser name → trust it
            is_browser = False
        else:
            # process_name is empty or auto-detected → use window-class fallback
            is_browser = _detect_browser_from_class()
        effective_decay = BROWSER_DECAY_TIMEOUT if is_browser else DECAY_TIMEOUT

        # Idle for too long → back to robotic
        # (Fixed: browser idle uses longer timeout to avoid churn)
        idle_too_long = time_since_last > effective_decay and self._op_counter <= 1
        if idle_too_long and not is_browser:
            self._state = "robotic"
            return "robotic"

        # Browser always gets at least human_light
        if is_browser:
            if self._state == "robotic":
                self._state = "light"
                self._level_activated_at = now
            # Escalate after sustained heavy activity
            if self._state == "light" and (now - self._level_activated_at) >= ESCALATION_DELAY:
                self._state = "heavy"
                self._level_activated_at = now
            return self._state

        # Op counter → heavy
        if self._op_counter >= HEAVY_OP_THRESHOLD:
            self._state = "heavy"
            self._level_activated_at = now
            return "heavy"

        # Op counter → light
        if self._op_counter >= LIGHT_OP_THRESHOLD:
            if self._state != "light":
                self._state = "light"
                self._level_activated_at = now
            return "light"

        # Default
        self._state = "robotic"
        return "robotic"

    def _detect_active_pid(self) -> int:
        """Get foreground window PID."""
        try:
            import win32gui, win32process
            hwnd = win32gui.GetForegroundWindow()
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            return pid
        except Exception:
            return 0

    def _detect_active_process(self) -> str:
        """Get foreground window process name."""
        try:
            import win32gui, win32process, psutil
            hwnd = win32gui.GetForegroundWindow()
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                return psutil.Process(pid).name()
            except Exception:
                pass
        except Exception:
            pass
        return ""


# ── Global singleton ──────────────────────────────────────────────────────

_engine = None
_engine_lock = threading.Lock()


def get_engine() -> HumanEngine:
    global _engine, _engine_lock
    with _engine_lock:
        if _engine is None:
            _engine = HumanEngine()
        return _engine


def reset_engine():
    global _engine, _engine_lock
    with _engine_lock:
        _engine = HumanEngine()
