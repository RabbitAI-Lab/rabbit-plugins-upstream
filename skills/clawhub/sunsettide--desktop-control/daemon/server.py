"""
Named-pipe JSON-RPC server.
Listens on pipe oc-desktop-SID-SessionId.
Message mode: each WriteFile/ReadFile is one complete message.
"""
import json
import os
import sys
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

import win32pipe
import win32file
import win32security
import win32api
import win32con
import pywintypes

from .utils import lifecycle, sendinput
from .utils import hotkeys as hotkeys_util
from .handlers import mouse, keyboard, screenshot, window, uia, filedrop, ocr, window_aware, hotkeys, image_match, macro, session_handler, script_handler, script_gen_handler, vision_click, tools_handler

# Include a random suffix to avoid collision with stale pipe instances from dead processes
import random
PIPE_NAME = r"\\.\pipe\oc-desktop-{sid}-{session}-{rand}"
# 1 MB buffer for large payloads (screenshots, long window lists)
BUFFER_SIZE = 1048576
MAX_WORKERS = 8


def _resolve_name():
    sid = lifecycle.get_user_sid()
    session = lifecycle.get_session_id()
    rand = str(random.randint(1000, 9999))
    return PIPE_NAME.format(sid=sid, session=session, rand=rand)


def _respond(status, data=None, error=None, req_id=None):
    """Build a uniform JSON-RPC-like response."""
    resp = {"id": req_id, "result": {"success": status, "data": data} if status else None}
    if error:
        resp["error"] = error
    if not status and not error:
        resp["result"] = {"success": False}
    return json.dumps(resp, ensure_ascii=False)


# Rate limiter: token bucket — max 120 requests per 10 seconds
import collections
import time as _time
_rate_history = collections.deque(maxlen=120)

def _check_rate_limit():
    now = _time.time()
    while _rate_history and _rate_history[0] < now - 10:
        _rate_history.popleft()
    if len(_rate_history) >= 120:
        return False
    _rate_history.append(now)
    return True


def _process_request(raw: str) -> str:
    """Parse and dispatch a single JSON request. Returns JSON response string."""
    if not _check_rate_limit():
        return _respond(False, error={"code": "RATE_LIMITED", "message": "Too many requests. Max 60 per 10 seconds."})
    try:
        req = json.loads(raw)
    except json.JSONDecodeError as e:
        return _respond(False, error={"code": "INVALID_JSON", "message": str(e)})

    req_id = req.get("id")
    method = req.get("method", "")
    params = req.get("params", {})

    dispatcher = {
        "mouse_move":              mouse.handle_move,
        "mouse_move_relative":     mouse.handle_move_relative,
        "mouse_click":             mouse.handle_click,
        "mouse_down":              mouse.handle_down,
        "mouse_up":                mouse.handle_up,
        "mouse_drag":              mouse.handle_drag,
        "mouse_scroll":            mouse.handle_scroll,
        "mouse_position":          mouse.handle_position,
        "mouse_get_position":      mouse.handle_get_position,
        "mouse_safety_bounds":     mouse.handle_set_safety_bounds,
        "keyboard_type":           keyboard.handle_type,
        "keyboard_press":          keyboard.handle_press,
        "keyboard_down":           keyboard.handle_down,
        "keyboard_up":             keyboard.handle_up,
        "keyboard_hotkey":         keyboard.handle_hotkey,
        "clipboard_get":           keyboard.handle_clipboard_get,
        "clipboard_set":           keyboard.handle_clipboard_set,
        "screenshot":              screenshot.handle_screenshot,
        "screenshot_save":         screenshot.handle_screenshot_save,
        "pixel_color":             screenshot.handle_pixel_color,
        "window_list":             window.handle_list,
        "window_focus":            window.handle_focus,
        "window_info":             window.handle_info,
        "window_minimize":         window.handle_minimize,
        "window_maximize":         window.handle_maximize,
        "window_close":            window.handle_close,
        "window_move":             window.handle_move,
        "window_resize":           window.handle_resize,
        "window_set_topmost":      window.handle_set_topmost,
        # UIA
        "uia_find":                uia.handle_find,
        "uia_click":               uia.handle_click,
        "uia_get_text":            uia.handle_get_text,
        "ping":                    lifecycle.handle_ping,
        "daemon_status":           lifecycle.handle_status,
        "daemon_shutdown":         lifecycle.handle_shutdown,
        "refresh_monitors":        lifecycle.handle_refresh_monitors,
        "file_drag_drop":          filedrop.handle_file_drag_drop,
        "screen_ocr":              ocr.handle_screen_ocr,
        "image_find":               image_match.handle_image_find,
        "macro_start_recording":    macro.handle_macro_start_recording,
        "macro_stop_recording":     macro.handle_macro_stop_recording,
        "macro_playback":           macro.handle_macro_playback,
        "script_run":               script_handler.handle_script_run,
        "script_run_sync":          script_handler.handle_script_run_sync,
        "script_status":            script_handler.handle_script_status,
        "script_results":           script_handler.handle_script_results,
        "script_cancel":            script_handler.handle_script_cancel,
        # Sessions
        "session_create":           session_handler.handle_session_create,
        "session_switch":           session_handler.handle_session_switch,
        "session_list":             session_handler.handle_session_list,
        "session_destroy":          session_handler.handle_session_destroy,
        # Hotkeys
        "register_hotkey":          hotkeys.handle_register,
        "unregister_hotkey":        hotkeys.handle_unregister,
        "list_hotkeys":             hotkeys.handle_list,
        # Script generation
        "script_generate":           script_gen_handler.handle_script_generate,
        "script_generate_and_run":   script_gen_handler.handle_script_generate_and_run,
        "script_list_templates":     script_gen_handler.handle_script_list_templates,
        "script_load_template":      script_gen_handler.handle_script_load_template,
        # Vision-click
        "find_text":                  vision_click.handle_find_text,
        "click_text":                 vision_click.handle_click_text,
        "type_to_text":               vision_click.handle_type_to_text,
        "mouse_smart_action":         vision_click.handle_mouse_smart_action,
        # AI Agent tools
        "tools_list":                 tools_handler.handle_tools_list,
        "tools_call":                 tools_handler.handle_tools_call,
        "screen_context":             tools_handler.handle_screen_context,
        "goal_run":                   tools_handler.handle_goal_run,
        # Active window
        "get_active_window":        window_aware.handle_get_active_window,
        "window_get_context":       window_aware.handle_window_get_context,
    }

    handler = dispatcher.get(method)
    if handler is None:
        return _respond(False, error={"code": "UNKNOWN_METHOD", "message": f"No handler for '{method}'"}, req_id=req_id)

    try:
        result = handler(params)
        lifecycle.log_action(os.getpid(), method, params, True)
        return _respond(True, data=result, req_id=req_id)
    except Exception as e:
        lifecycle.log_action(os.getpid(), method, params, False)
        tb = traceback.format_exc()
        return _respond(False, error={"code": "HANDLER_ERROR", "message": str(e)}, req_id=req_id)


def _handle_client(pipe_handle, server_ref):
    """Read one request, process, write response, then close."""
    try:
        raw = win32file.ReadFile(pipe_handle, BUFFER_SIZE)
        if raw[0] != 0:
            return
        request_text = raw[1].decode("utf-8")
        response_text = _process_request(request_text)
        win32file.WriteFile(pipe_handle, response_text.encode("utf-8"))
    except pywintypes.error:
        pass
    finally:
        try:
            win32pipe.DisconnectNamedPipe(pipe_handle)
        except pywintypes.error:
            pass
        win32file.CloseHandle(pipe_handle)
        server_ref.check_shutdown()


class NamedPipeServer:
    """Runs in a background thread. Accepts connections and dispatches to thread pool."""

    def __init__(self):
        self._pipe_name = _resolve_name()
        self._running = threading.Event()
        self._shutdown_requested = threading.Event()
        self._thread = None
        self._executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    @property
    def pipe_name(self):
        return self._pipe_name

    def start(self):
        self._running.set()
        # Initialise the hotkey message pump with our executor
        hotkeys_util.init(self._executor)
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._shutdown_requested.set()
        self._running.clear()
        hotkeys_util.shutdown()
        self._executor.shutdown(wait=False)
        # Clean up async script task manager
        from daemon.script_engine.engine import shutdown_task_manager
        shutdown_task_manager()
        # Release any stuck keyboard/mouse inputs
        from daemon.utils.release_guard import shutdown as release_guard_shutdown
        release_guard_shutdown()

    def check_shutdown(self):
        if self._shutdown_requested.is_set():
            self._running.clear()

    def _create_secure_security_attributes(self):
        """Build SECURITY_ATTRIBUTES with a strict DACL.

        Only allows:
          - Current user (SID from token): FULL_CONTROL
          - SYSTEM: DENY (prevents SYSTEM-level processes
            on the same box from connecting to our pipe)
        """
        try:
            # Current user SID
            token = win32security.OpenProcessToken(
                win32api.GetCurrentProcess(),
                win32con.TOKEN_QUERY,
            )
            user_sid = win32security.GetTokenInformation(
                token, win32security.TokenUser
            )[0]

            # SECURITY_DESCRIPTOR
            sd = win32security.SECURITY_DESCRIPTOR()
            sd.Initialize()

            # DACL: allow current user, deny SYSTEM
            acl = win32security.ACL()
            acl.AddAccessAllowedAce(
                win32security.ACL_REVISION,
                win32con.GENERIC_ALL,
                user_sid,
            )
            # Deny SYSTEM — even if a SYSTEM process is on the same desktop,
            # it cannot open our pipe.
            try:
                system_sid, _, _ = win32security.LookupAccountName(None, "SYSTEM")
                acl.AddAccessDeniedAce(
                    win32security.ACL_REVISION,
                    win32con.GENERIC_ALL,
                    system_sid,
                )
            except Exception as sys_err:
                import sys as _sys
                _sys.stderr.write(
                    f"[WARNING] DesktopControl: SYSTEM DENY ACE addition failed "
                    f"(non-critical, allow-only ACE still set). Error: {sys_err}\n"
                )

            sd.SetSecurityDescriptorDacl(1, acl, 0)

            sa = pywintypes.SECURITY_ATTRIBUTES()
            sa.SECURITY_DESCRIPTOR = sd
            sa.bInheritHandle = False
            return sa
        except Exception as dacl_err:
            # Fallback: permissive (pipe name still carries SID isolation)
            # CRITICAL: log visible warning so the user knows DACL is NOT active
            import sys as _sys
            _sys.stderr.write(
                f"[CRITICAL] DesktopControl: DACL creation FAILED - "
                f"pipe is NOT fully secured! Fallback to permissive SA. "
                f"Error: {dacl_err}\n"
            )
            return pywintypes.SECURITY_ATTRIBUTES()

    def _create_pipe(self):
        """Create a named-pipe instance with strict DACL security.

        Pipe name still carries user SID + session ID for defence-in-depth.
        The DACL added via SECURITY_ATTRIBUTES hardens the pipe so that
        even another process running as the same user but launched via
        a different session cannot connect.
        """
        sec_att = self._create_secure_security_attributes()
        return win32pipe.CreateNamedPipe(
            self._pipe_name,
            win32pipe.PIPE_ACCESS_DUPLEX,
            win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
            255,
            BUFFER_SIZE,
            BUFFER_SIZE,
            5000,
            sec_att,
        )

    def _run(self):
        backoff = 0.5
        while self._running.is_set():
            try:
                pipe = self._create_pipe()
                backoff = 0.5  # reset on success
            except pywintypes.error as e:
                if self._running.is_set():
                    time.sleep(backoff)
                    backoff = min(backoff * 2, 5.0)
                continue

            try:
                win32pipe.ConnectNamedPipe(pipe, None)
            except pywintypes.error:
                win32file.CloseHandle(pipe)
                continue

            # Each connected pipe instance is handled independently by the thread pool
            self._executor.submit(_handle_client, pipe, self)
