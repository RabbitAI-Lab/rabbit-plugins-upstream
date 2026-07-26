"""
desktop-control IPC client — subprocess called by OpenClaw for each action.
~80 lines, minimal imports, fast startup.
Automatically ensures the daemon is running via PID file + pipeline check.

Usage (called from SKILL.md templates):
    python client/client.py mouse_move '{"x": 500, "y": 300}'
    python client/client.py screenshot '{}'
    python client/client.py window_list '{}'
    # ... prints JSON response to stdout
"""
import json
import os
import subprocess
import sys
import time

import win32pipe
import win32file
import pywintypes

PIPE_TIMEOUT = 15000  # ms for WaitNamedPipe
# 1 MB buffer for large payloads (screenshots)
BUFFER_SIZE = 1048576


def _ensure_daemon():
    """PID file → process alive → info file exists. Start if needed."""
    import daemon.utils.lifecycle as lc
    pid = lc.read_pid_file()
    if pid and lc.pid_is_running(pid) and os.path.exists(PIPE_INFO_FILE):
        return
    lc.clean_pid_file()
    if os.path.exists(PIPE_INFO_FILE):
        try:
            os.remove(PIPE_INFO_FILE)
        except OSError:
            pass

    daemon_script = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                  "daemon", "main.py")
    env = os.environ.copy()
    # Pass through TESSERACT_PATH if set at user/system level
    tess_path = os.environ.get("TESSERACT_PATH", "") or ""
    if not tess_path:
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Environment") as key:
                tess_path = winreg.QueryValueEx(key, "TESSERACT_PATH")[0]
        except Exception:
            pass
    if tess_path:
        env["TESSERACT_PATH"] = tess_path

    subprocess.Popen(
        [sys.executable, daemon_script],
        creationflags=subprocess.DETACHED_PROCESS,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env,
    )

    # Wait for info file (daemon writes it after pipe is ready)
    for _ in range(150):
        if os.path.exists(PIPE_INFO_FILE):
            return
        time.sleep(0.1)

    sys.stderr.write(json.dumps({
        "id": None,
        "result": None,
        "error": {"code": "DAEMON_STARTUP_TIMEOUT",
                   "message": "Desktop-control daemon did not start within 15 seconds"},
    }))
    sys.exit(1)


PIPE_INFO_FILE = os.path.join(os.environ.get("TEMP", os.path.expanduser("~")),
                                 "oc_desktop_pipe.txt")


def _resolve_pipe():
    """Read the pipe name from the info file written by the daemon."""
    if os.path.exists(PIPE_INFO_FILE):
        with open(PIPE_INFO_FILE) as f:
            return f.read().strip()
    # Fallback: compute it ourselves
    import daemon.utils.lifecycle as lc
    sid = lc.get_user_sid()
    session = lc.get_session_id()
    return rf"\\.\pipe\oc-desktop-{sid}-{session}"


def send_request(method: str, params: dict, retries: int = 3) -> dict:
    """Connect to the daemon pipe, send a request, return parsed response."""
    _ensure_daemon()

    pipe_name = _resolve_pipe()
    last_error = None
    for attempt in range(retries):
        try:
            handle = win32file.CreateFile(
                pipe_name,
                win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                0, None, win32file.OPEN_EXISTING, 0, None,
            )
            last_error = None
            break
        except pywintypes.error as e:
            last_error = e
            if "231" in str(e):  # ERROR_PIPE_BUSY
                time.sleep(0.2 * (attempt + 1))
                continue
            if "2" in str(e) or "3" in str(e):  # FILE_NOT_FOUND / PATH_NOT_FOUND
                # Daemon process was killed — clean stale PID file and restart
                import daemon.utils.lifecycle as lc
                lc.clean_pid_file()
                _ensure_daemon()
                time.sleep(0.5)
                continue
            return {"id": None, "result": None,
                    "error": {"code": "PIPE_CONNECT_FAIL", "message": str(e)}}

    if last_error:
        return {"id": None, "result": None,
                "error": {"code": "PIPE_CONNECT_FAIL", "message": str(last_error)}}

    # Enable message mode
    win32pipe.SetNamedPipeHandleState(handle,
                                       win32pipe.PIPE_READMODE_MESSAGE,
                                       None, None)

    # Build request
    req = json.dumps({"id": "req_001", "method": method, "params": params},
                      ensure_ascii=False)

    try:
        win32file.WriteFile(handle, req.encode("utf-8"))
        # Read in a loop to handle ERROR_MORE_DATA (large responses)
        chunks = []
        while True:
            hr, data = win32file.ReadFile(handle, BUFFER_SIZE)
            if hr == 0 or hr == 234:  # 234 = ERROR_MORE_DATA
                chunks.append(data)
                if hr == 0:
                    break
            else:
                return {"id": None, "result": None,
                        "error": {"code": "PIPE_READ_FAIL", "message": f"hr={hr}"}}
        full = b"".join(chunks)
        return json.loads(full.decode("utf-8"))
    except pywintypes.error as e:
        return {"id": None, "result": None,
                "error": {"code": "PIPE_IO_ERROR", "message": str(e)}}
    finally:
        win32file.CloseHandle(handle)


if __name__ == "__main__":
    # Ensure the skill root is on sys.path so daemon.utils can be found
    _script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _script_dir not in sys.path:
        sys.path.insert(0, _script_dir)

    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: client.py <method> [json_params]"}))
        sys.exit(1)

    method = sys.argv[1]
    params = json.loads(sys.argv[2]) if len(sys.argv) >= 3 else {}
    result = send_request(method, params)
    # Force stdout to UTF-8 to handle Unicode characters in window titles
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    print(json.dumps(result, ensure_ascii=False))
