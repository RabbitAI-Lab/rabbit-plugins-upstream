"""
Macro recording and playback handlers.

Recording: uses pynput to hook global mouse/keyboard events in a background
           thread.  Events are timestamped and stored in memory (or saved to
           a JSON file on stop).

Playback: replays a recorded JSON file by calling the daemon's built-in
          handlers (mouse_move, mouse_click, keyboard_press) directly —
          NOT via the IPC pipe — for low latency.

Dependencies:
    - pynput (optional, for recording)
    - Playback only requires the existing SendInput layer.

Privacy:
    Global hooks are active ONLY while recording is running.
    Recorded data is stored locally; never transmitted.
"""
import json
import os
import threading
import time


# --- Recording state ---
_recording = {}  # recording_id -> {"events": [...], "start_time": float, "thread": Thread}
_recording_lock = threading.Lock()
_next_rec_id = 0

# pynput (optional)
_listener_modules = None
_listener_import_error = None
try:
    from pynput import mouse as _pynput_mouse
    from pynput import keyboard as _pynput_keyboard
    _listener_modules = (_pynput_mouse, _pynput_keyboard)
except Exception as e:
    _listener_import_error = str(e)


# --- Helpers ---

def _generate_recording_id():
    global _next_rec_id
    with _recording_lock:
        _next_rec_id += 1
        return f"rec_{_next_rec_id:04d}"


# --- Keyboard handler (feeds events into recording) ---

def _make_on_press(rec_id, events, start_time, stop_event):
    """Return a callback for pynput.keyboard.Listener.on_press."""
    from pynput.keyboard import Key, KeyCode

    def on_press(key):
        if stop_event.is_set():
            return False
        ts = time.perf_counter() - start_time
        try:
            if isinstance(key, KeyCode):
                k = key.char
            else:
                k = key.name  # e.g. "enter", "f9"
            if k is not None:
                events.append({"type": "keyboard_press", "key": k, "ts": round(ts, 3)})
        except Exception:
            pass
        return True

    return on_press


def _make_on_release(rec_id, events, start_time, stop_event):
    """Return a callback for pynput.keyboard.Listener.on_release."""
    from pynput.keyboard import Key, KeyCode

    def on_release(key):
        if stop_event.is_set():
            return False
        ts = time.perf_counter() - start_time
        try:
            if isinstance(key, KeyCode):
                k = key.char
            else:
                k = key.name
            if k is not None:
                events.append({"type": "keyboard_release", "key": k, "ts": round(ts, 3)})
        except Exception:
            pass
        return True

    return on_release


def _make_on_click(rec_id, events, start_time, stop_event):
    """Return a callback for pynput.mouse.Listener.on_click."""
    def on_click(x, y, button, pressed):
        if stop_event.is_set():
            return False
        ts = time.perf_counter() - start_time
        btn = button.name  # "left", "right", "middle"
        action = "mouse_click" if pressed else "mouse_release"
        events.append({
            "type": action,
            "button": btn,
            "x": int(x),
            "y": int(y),
            "ts": round(ts, 3),
        })
        return True

    return on_click


def _make_on_move(rec_id, events, start_time, stop_event,
                  throttle_ms=50, throttle_px=5):
    """Return a callback for pynput.mouse.Listener.on_move.

    Throttles by both time and space:
      - time: at most one event per `throttle_ms` (default 50ms = ~20fps)
      - space: ignore events that are within `throttle_px` of the last
               recorded position (default 5px, avoids redundant events
               when mouse is stationary or shaking minimally).
    """
    _last_move_ts = [0.0]
    _last_pos = [0, 0]

    def on_move(x, y):
        if stop_event.is_set():
            return False
        now = time.perf_counter()
        dt_ms = (now - _last_move_ts[0]) * 1000
        dx = abs(x - _last_pos[0])
        dy = abs(y - _last_pos[1])
        # Skip if within both time and distance thresholds
        if dt_ms < throttle_ms and dx < throttle_px and dy < throttle_px:
            return True
        _last_move_ts[0] = now
        _last_pos[0] = int(x)
        _last_pos[1] = int(y)
        ts = now - start_time
        events.append({
            "type": "mouse_move",
            "x": int(x),
            "y": int(y),
            "ts": round(ts, 3),
        })
        return True

    return on_move


# --- Handlers ---

def handle_macro_start_recording(params):
    """Start recording mouse and keyboard events.

    Params:
        save_path: optional path to save events on stop (default: memory only)

    Returns:
        {"recording_id": "rec_0001", "status": "recording"}
    """
    if _listener_modules is None:
        msg = _listener_import_error or "pynput is not installed"
        raise ValueError(
            f"Recording unavailable: {msg}. "
            f"Install: pip install pynput"
        )

    rec_id = _generate_recording_id()
    events = []
    start_time = time.perf_counter()
    stop_event = threading.Event()

    pynput_mouse, pynput_keyboard = _listener_modules

    # Start mouse listener
    mouse_listener = pynput_mouse.Listener(
        on_move=_make_on_move(rec_id, events, start_time, stop_event),
        on_click=_make_on_click(rec_id, events, start_time, stop_event),
    )
    mouse_listener.daemon = True
    mouse_listener.start()

    # Start keyboard listener
    kb_listener = pynput_keyboard.Listener(
        on_press=_make_on_press(rec_id, events, start_time, stop_event),
        on_release=_make_on_release(rec_id, events, start_time, stop_event),
    )
    kb_listener.daemon = True
    kb_listener.start()

    # Store recording state
    rec_info = {
        "events": events,
        "start_time": start_time,
        "stop_event": stop_event,
        "mouse_listener": mouse_listener,
        "kb_listener": kb_listener,
        "save_path": params.get("save_path"),
    }
    with _recording_lock:
        _recording[rec_id] = rec_info

    return {"recording_id": rec_id, "status": "recording"}


def handle_macro_stop_recording(params):
    """Stop a recording and optionally save to file.

    Params:
        recording_id: the recording to stop (required)
        save_path:    optional file path to save the JSON

    Returns:
        {"recording_id": "...", "event_count": N, "duration": seconds,
         "saved_to": "..." or None}
    """
    rec_id = params.get("recording_id")
    if not rec_id:
        raise ValueError("Missing required parameter 'recording_id' for macro_stop_recording.")

    with _recording_lock:
        rec_info = _recording.pop(rec_id, None)

    if rec_info is None:
        raise ValueError(f"Recording '{rec_id}' not found.")

    # Stop listeners
    rec_info["stop_event"].set()
    try:
        rec_info["mouse_listener"].stop()
    except Exception:
        pass
    try:
        rec_info["kb_listener"].stop()
    except Exception:
        pass

    events = rec_info["events"]
    duration = round(time.perf_counter() - rec_info["start_time"], 2)

    # Build script
    script = {
        "version": "1.0",
        "recording_id": rec_id,
        "duration": duration,
        "events": events,
    }

    saved_to = None
    save_path = params.get("save_path", rec_info.get("save_path"))
    if save_path:
        try:
            os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(script, f, ensure_ascii=False, indent=2)
            saved_to = save_path
        except Exception as e:
            raise ValueError(f"Failed to save recording to '{save_path}': {e}")

    return {
        "recording_id": rec_id,
        "event_count": len(events),
        "duration": duration,
        "saved_to": saved_to,
    }


def handle_macro_playback(params):
    """Play back a recorded macro file.

    Params:
        file_path: path to the JSON macro file (required)
        speed:     playback speed multiplier (default 1.0)
        loop:      number of times to loop (-1 = infinite, default 1)

    Returns:
        {"events_played": N, "duration": seconds}
    """
    file_path = params.get("file_path")
    if not file_path:
        raise ValueError("Missing required parameter 'file_path' for macro_playback.")
    if not os.path.isfile(file_path):
        raise ValueError(f"File not found: {file_path}")

    try:
        with open(file_path, encoding="utf-8") as f:
            script = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        raise ValueError(f"Failed to load macro file: {e}")

    events = script.get("events", [])
    if not events:
        return {"events_played": 0, "duration": 0}

    speed = float(params.get("speed", 1.0))
    loop = int(params.get("loop", 1))

    total_events = 0
    start_wall = time.perf_counter()

    # Import sendinput directly (not via IPC)
    from daemon.utils.sendinput import mouse_move, mouse_click, keyboard_press, VK

    iteration = 0
    while True:
        iteration += 1
        script_start = time.perf_counter()

        for evt in events:
            evt_type = evt.get("type")
            # Calculate delay from the *previous* event's timestamp
            # The first event has ts=0, so no wait
            delay = evt.get("ts", 0) / speed - (time.perf_counter() - script_start)
            if delay > 0:
                time.sleep(delay)

            try:
                if evt_type == "mouse_move":
                    mouse_move(int(evt["x"]), int(evt["y"]))
                elif evt_type == "mouse_click":
                    x = evt.get("x"); y = evt.get("y")
                    mouse_click(x, y, evt.get("button", "left"))
                elif evt_type == "keyboard_press":
                    key_name = evt.get("key", "").lower()
                    code = VK.get(key_name)
                    if code:
                        keyboard_press(code)
                    elif len(key_name) == 1:
                        # Single character — type via hotkey-like approach
                        from daemon.utils.sendinput import keyboard_type
                        keyboard_type(key_name)
                total_events += 1
            except Exception:
                pass  # Silent skip on playback errors

        if loop > 0 and iteration >= loop:
            break
        if loop < 0:
            pass  # infinite

    wall_time = round(time.perf_counter() - start_wall, 2)
    return {"events_played": total_events, "duration": wall_time}
