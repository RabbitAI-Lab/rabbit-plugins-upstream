"""
Global hotkey registration and dispatch.

Architecture:
  - A background thread runs a Win32 message pump (PumpMessages).
  - All RegisterHotKey calls MUST be on that thread (Windows requirement).
    So register/unregister requests are queued via a deque, and the pump
    thread processes them at the top of each message loop iteration.
  - When WM_HOTKEY fires, the action/params are submitted to the daemon's
    ThreadPoolExecutor — never executed in the pump thread.

Thread safety:
  - _hotkeys dict is protected by _hotkeys_lock (used by list_hotkeys).
  - _pump_queue deque + _pump_event are the producer-consumer channel
    for register/unregister requests.
"""
import ctypes
import json
import queue
import threading
import time
import traceback

import win32api
import win32con
import win32gui
import pywintypes


_pump_thread = None
_pump_hwnd = None
_pump_running = threading.Event()

_hotkeys = {}        # {id_int: reg_info}
_hotkeys_lock = threading.Lock()

_executor = None

# Queue for register/unregister requests from any thread to the pump thread
_pump_queue = queue.Queue()


def _get_modifier_name(mod):
    parts = []
    if mod & win32con.MOD_ALT:      parts.append("ALT")
    if mod & win32con.MOD_CONTROL:  parts.append("CTRL")
    if mod & win32con.MOD_SHIFT:    parts.append("SHIFT")
    if mod & win32con.MOD_WIN:      parts.append("WIN")
    return "+".join(parts) if parts else "none"


# --- Pump thread ---

WM_HOTKEY_EXEC = win32con.WM_USER + 100


def _pump_thread_main():
    global _pump_hwnd
    try:
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = _window_proc
        wc.lpszClassName = "OCDesktopHotkeyPump"
        wc.hInstance = win32api.GetModuleHandle(None)
        win32gui.RegisterClass(wc)

        _pump_hwnd = win32gui.CreateWindowEx(
            0, wc.lpszClassName, "OCDesktopHotkeyPump",
            0, 0, 0, 0, 0,
            0, 0, wc.hInstance, None,
        )
        _pump_running.set()

        # Pump messages — interleave with queue processing
        while True:
            # Process pending queue items before pumping
            _process_pump_queue()
            # Pump a single message (or wait if none)
            ret = win32gui.PumpWaitingMessages()
            if ret == -1:  # WM_QUIT
                break
            # Small sleep to prevent busy-wait
            time.sleep(0.01)

        # Cleanup
        if _pump_hwnd:
            win32gui.DestroyWindow(_pump_hwnd)
            _pump_hwnd = None
        win32gui.UnregisterClass(wc.lpszClassName, wc.hInstance)
    except Exception:
        traceback.print_exc()
    finally:
        _pump_hwnd = None
        _pump_running.clear()


def _process_pump_queue():
    """Process pending register/unregister requests from other threads."""
    user32 = ctypes.windll.user32
    while not _pump_queue.empty():
        try:
            req = _pump_queue.get_nowait()
            kind = req.get("kind")
            if kind == "register":
                id_int = req["id_int"]
                mod = req["modifiers"]
                key = req["key"]
                result = user32.RegisterHotKey(_pump_hwnd, id_int, mod, key)
                if result == 0:
                    err = ctypes.GetLastError()
                    sync_data = {"ok": False, "error": err}
                else:
                    # Store registration
                    with _hotkeys_lock:
                        _hotkeys[id_int] = {
                            "id": req["hotkey_id"],
                            "modifiers": mod,
                            "vk": key,
                            "modifier_name": _get_modifier_name(mod),
                            "action": req["action"],
                            "params": req["params"],
                        }
                    sync_data = {"ok": True}
                req["sync_event"].put(sync_data)

            elif kind == "unregister":
                id_int = req.get("id_int")
                unreg_all = req.get("all", False)
                if unreg_all:
                    with _hotkeys_lock:
                        for iid in list(_hotkeys.keys()):
                            user32.UnregisterHotKey(_pump_hwnd, iid)
                        _hotkeys.clear()
                elif id_int is not None:
                    user32.UnregisterHotKey(_pump_hwnd, id_int)
                    with _hotkeys_lock:
                        _hotkeys.pop(id_int, None)
                req["sync_event"].put({"ok": True})
        except queue.Empty:
            break
        except Exception:
            pass


def _window_proc(hwnd, msg, wparam, lparam):
    if msg == win32con.WM_HOTKEY:
        _on_hotkey(wparam, lparam)
        return 0
    return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)


def _on_hotkey(id_int, lparam):
    """Called on the pump thread when WM_HOTKEY fires."""
    with _hotkeys_lock:
        reg = _hotkeys.get(id_int)
        if reg is None:
            return
        action = reg["action"]
        params = dict(reg["params"])
    if _executor:
        _executor.submit(_run_action, action, params)


def _run_action(action, params):
    from ..server import _process_request
    req = json.dumps({"method": action, "params": params})
    try:
        _process_request(req)
    except Exception:
        pass


# --- Public API ---

def init(executor):
    global _executor, _pump_thread
    _executor = executor
    if _pump_thread is None or not _pump_thread.is_alive():
        _pump_thread = threading.Thread(target=_pump_thread_main, daemon=True)
        _pump_thread.start()
        _pump_running.wait(timeout=5)


def shutdown():
    # Unregister ALL hotkeys *before* stopping the pump thread
    if _pump_hwnd:
        # Post unregister-all request to the pump thread
        sync_event = queue.Queue(maxsize=1)
        _pump_queue.put({
            "kind": "unregister",
            "all": True,
            "sync_event": sync_event,
        })
        try:
            sync_event.get(timeout=2)
        except queue.Empty:
            pass  # pump thread may already be blocked, force-clear
        # Then post WM_QUIT
        try:
            win32gui.PostMessage(_pump_hwnd, win32con.WM_QUIT, 0, 0)
        except Exception:
            pass
    with _hotkeys_lock:
        _hotkeys.clear()


def register(hotkey_id, modifiers, key, action, params):
    if not _pump_hwnd:
        raise RuntimeError("Hotkey pump not initialised")

    with _hotkeys_lock:
        for existing_id_int, existing_reg in list(_hotkeys.items()):
            if existing_reg.get("id") == hotkey_id:
                raise ValueError(
                    f"Hotkey id '{hotkey_id}' is already registered. "
                    f"Unregister it first."
                )
            if (existing_reg["modifiers"] == modifiers and
                    existing_reg["vk"] == key):
                raise ValueError(
                    f"Hotkey combination ({_get_modifier_name(modifiers)}+{key}) "
                    f"is already registered as '{existing_reg.get('id')}'."
                )

    if (modifiers & win32con.MOD_WIN) and key == ord("L"):
        raise ValueError("Cannot register Win+L (system-reserved)")

    id_int = hash(hotkey_id) & 0x7FFFFFFF

    sync_event = queue.Queue(maxsize=1)
    _pump_queue.put({
        "kind": "register",
        "id_int": id_int,
        "hotkey_id": hotkey_id,
        "modifiers": modifiers,
        "key": key,
        "action": action,
        "params": params,
        "sync_event": sync_event,
    })

    try:
        result = sync_event.get(timeout=3)
    except queue.Empty:
        raise RuntimeError("Hotkey registration timed out (pump thread may be blocked)")

    if not result.get("ok"):
        err = result.get("error", 0)
        if err == 1409:
            raise ValueError("Hotkey already registered by another application.")
        raise RuntimeError(f"Hotkey registration failed (error {err}). The key may be system-reserved.")

    return {"id": hotkey_id, "info": f"{_get_modifier_name(modifiers)}+{key} -> {action}"}


def unregister(hotkey_id=None, unregister_all=False):
    if not _pump_hwnd:
        return {"unregistered": 0}

    id_int = None
    if not unregister_all and hotkey_id is not None:
        with _hotkeys_lock:
            for iid, reg in list(_hotkeys.items()):
                if reg.get("id") == hotkey_id:
                    id_int = iid
                    break

    sync_event = queue.Queue(maxsize=1)
    _pump_queue.put({
        "kind": "unregister",
        "id_int": id_int,
        "all": unregister_all,
        "sync_event": sync_event,
    })
    try:
        sync_event.get(timeout=3)
    except queue.Empty:
        pass

    return {"unregistered": 1 if id_int else 0} if not unregister_all else {"unregistered": "all"}


def list_hotkeys():
    with _hotkeys_lock:
        result = []
        for id_int, reg in sorted(_hotkeys.items(), key=lambda x: x[0]):
            result.append({
                "id": reg.get("id"),
                "modifiers": reg.get("modifiers"),
                "key": reg.get("vk"),
                "info": f"{reg.get('modifier_name', '?')}+{reg.get('vk', '?')} -> {reg.get('action', '?')}",
                "action": reg.get("action"),
            })
    return {"hotkeys": result}
