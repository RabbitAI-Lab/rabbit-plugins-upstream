"""
Lifecycle utilities: mutex, PID file, process check, daemon status.
"""
import json
import os
import sys
import time
import threading

import win32event
import win32api
import win32security
import win32con
import win32api
import pywintypes
import psutil  # note: add to requirements.txt


_shutdown_hook = None
_start_time = time.time()


def get_user_sid() -> str:
    """Return current user's SID string (for pipe naming)."""
    token = win32security.OpenProcessToken(
        win32api.GetCurrentProcess(),
        win32con.TOKEN_QUERY,
    )
    sid = win32security.GetTokenInformation(token, win32security.TokenUser)[0]
    return win32security.ConvertSidToStringSid(sid)


def get_session_id() -> str:
    """Return terminal session id (for multi-session isolation)."""
    try:
        import win32ts
        return str(win32ts.WTSGetActiveConsoleSessionId())
    except (ImportError, AttributeError):
        # Fallback: use process session id
        return str(win32api.GetCurrentProcessId())


PID_FILE = os.path.join(os.environ.get("TEMP", os.path.expanduser("~")),
                         "oc_desktop_daemon.pid")
# Structured audit log directory
LOG_DIR = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
                        "DesktopControl", "Logs")
LOG_FILE = os.path.join(LOG_DIR, "daemon.log")


def get_mutex_name() -> str:
    sid = get_user_sid()
    return f"Global\\oc-desktop-daemon-{sid}"


def acquire_mutex() -> bool:
    """Try to create the named mutex. Returns True if caller got it (first instance)."""
    try:
        win32event.CreateMutex(None, False, get_mutex_name())
        last_err = win32api.GetLastError()
        if last_err == 183:  # ERROR_ALREADY_EXISTS
            return False
        return True
    except pywintypes.error:
        return False


def write_pid_file():
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))


def read_pid_file() -> int | None:
    if not os.path.exists(PID_FILE):
        return None
    try:
        with open(PID_FILE) as f:
            return int(f.read().strip())
    except (ValueError, IOError):
        return None


def pid_is_running(pid: int) -> bool:
    try:
        return psutil.pid_exists(pid)
    except Exception:
        return False


def clean_pid_file():
    if os.path.exists(PID_FILE):
        try:
            os.remove(PID_FILE)
        except OSError:
            pass


def try_acquire_or_exit():
    """Call at daemon startup. If another instance is running, exit silently."""
    if not acquire_mutex():
        sys.exit(0)
    # Check PID file
    existing_pid = read_pid_file()
    if existing_pid and pid_is_running(existing_pid) and existing_pid != os.getpid():
        sys.exit(0)
    write_pid_file()


def register_shutdown_hook(hook):
    global _shutdown_hook
    _shutdown_hook = hook


# --- Audit logging ---

def _ensure_log_dir():
    """Create log directory if it doesn't exist."""
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
    except Exception:
        pass


def log_action(pid, method, params, success):
    """Write a structured audit log entry (no sensitive data).

    Records: timestamp, PID, method name, sanitised params (text length only),
    success status.  Written as one JSON line per entry.
    """
    try:
        _ensure_log_dir()
        import datetime
        safe_params = {}
        for k, v in params.items():
            if k in ("text",):
                safe_params[k] = f"<{len(str(v))} chars>"
            elif k in ("password", "secret"):
                safe_params[k] = "<redacted>"
            else:
                safe_params[k] = v
        entry = {
            "time": datetime.datetime.now().isoformat(),
            "pid": pid,
            "method": method,
            "params": safe_params,
            "success": success,
        }
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass  # Logging failure should never crash the daemon


# --- IPC handler helpers ---

def handle_ping(params):
    return {"pong": True, "pid": os.getpid()}


def handle_status(params):
    uptime = time.time() - _start_time
    return {
        "pid": os.getpid(),
        "uptime_seconds": round(uptime),
        "start_time": _start_time,
    }


def handle_refresh_monitors(params):
    """Re-enumerate monitors (after hotplug).

    Delegates to utils.monitors.refresh_monitors().
    """
    from daemon.utils.monitors import refresh_monitors, get_monitor_count
    refresh_monitors()
    count = get_monitor_count()
    return {"monitors_detected": count, "action": "refresh_monitors"}



def handle_shutdown(params):
    # Return response first, THEN shutdown
    # Schedule delayed shutdown to ensure the response is sent to client
    def _delayed_shutdown():
        import time
        time.sleep(0.5)
        clean_pid_file()
        if _shutdown_hook:
            _shutdown_hook()
        os._exit(0)
    threading.Thread(target=_delayed_shutdown, daemon=True).start()
    return {"shutdown": True}
