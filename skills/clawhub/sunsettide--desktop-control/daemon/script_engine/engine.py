"""
Script execution engine.

Parses a declarative JSON script and executes each step sequentially.
Supports:
  - Direct handler calls (mouse_move, window_focus, etc.)
  - Conditionals (if/else)
  - Loops (for-N, while-expression)
  - Retry with backoff
  - Variable substitution ({{var_name}})
  - Safe eval for conditions (whitelist-only)

Architecture:
  - The engine calls handler functions **directly** (not via IPC),
    for low-latency execution.
  - Each step result is collected and returned at the end.
  - Async execution: long-running scripts run in a background thread
    so the daemon remains responsive. Use script_run to start and
    script_status/script_cancel to manage.
"""
import json
import re
import time
import traceback
import threading
import uuid
from concurrent.futures import ThreadPoolExecutor

from daemon.utils.session import get_manager


# --- Safe eval environment ---

_SAFE_GLOBALS = {
    "__builtins__": {},
    "True": True, "False": False, "None": None,
    "abs": abs, "int": int, "float": float, "str": str,
    "len": len, "min": min, "max": max, "round": round,
}

_SAFE_LOCALS = {}


def _register_safe_function(name, func):
    """Register a function accessible in condition expressions."""
    _SAFE_LOCALS[name] = func


def _safe_eval(expr):
    """Evaluate a condition expression in a restricted environment."""
    try:
        return bool(eval(expr, _SAFE_GLOBALS, _SAFE_LOCALS))
    except Exception as e:
        raise RuntimeError(f"Condition evaluation failed: '{expr}'. {e}")


# --- Handler mapping ---

# Lazy import all handlers to avoid circular deps at module load
def _get_handlers():
    from daemon.handlers.mouse import (
        handle_move, handle_click, handle_drag, handle_scroll, handle_position,
    )
    from daemon.handlers.keyboard import handle_type, handle_press, handle_hotkey
    from daemon.handlers.screenshot import (
        handle_screenshot, handle_screenshot_save, handle_pixel_color,
    )
    from daemon.handlers.window import (
        handle_list, handle_focus, handle_info, handle_minimize,
        handle_maximize, handle_close, handle_move as win_move,
        handle_resize, handle_set_topmost,
    )
    from daemon.handlers.uia import handle_find, handle_click as uia_click, handle_get_text
    from daemon.handlers.ocr import handle_screen_ocr
    from daemon.handlers.image_match import handle_image_find
    from daemon.handlers.filedrop import handle_file_drag_drop

    return {
        # Mouse
        "mouse_move": handle_move,
        "mouse_click": handle_click,
        "mouse_drag": handle_drag,
        "mouse_scroll": handle_scroll,
        "mouse_position": handle_position,
        # Keyboard
        "keyboard_type": handle_type,
        "keyboard_press": handle_press,
        "keyboard_hotkey": handle_hotkey,
        # Screenshot
        "screenshot": handle_screenshot,
        "screenshot_save": handle_screenshot_save,
        "pixel_color": handle_pixel_color,
        # Window
        "window_list": handle_list,
        "window_focus": handle_focus,
        "window_info": handle_info,
        "window_minimize": handle_minimize,
        "window_maximize": handle_maximize,
        "window_close": handle_close,
        "window_move": win_move,
        "window_resize": handle_resize,
        "window_set_topmost": handle_set_topmost,
        # UIA
        "uia_find": handle_find,
        "uia_click": uia_click,
        "uia_get_text": handle_get_text,
        # Advanced
        "screen_ocr": handle_screen_ocr,
        "image_find": handle_image_find,
        "file_drag_drop": handle_file_drag_drop,
        # Meta
        "log": _handle_log,
        "sleep": _handle_sleep,
        "nop": lambda p: {},
    }


# --- Meta handlers ---

def _handle_log(params):
    """Log a message to the script result."""
    msg = params.get("message", "")
    return {"logged": msg}


_SLEEP_EVENT = threading.Event()


def _handle_sleep(params, task=None):
    """Sleep for a duration, interruptible via cancel event.

    Returns {"slept": duration} on natural completion.
    If cancelled during sleep, returns {"cancelled": True, "slept": actual}
    so the caller can abort.
    """
    duration = float(params.get("duration", 1))
    if task:
        # Use Event.wait() instead of time.sleep() so cancel can interrupt it.
        # wait(timeout) returns True if event was set (triggered), False on timeout.
        was_set = task._cancel_event.wait(timeout=duration)
        if was_set:
            # Event was triggered (cancelled) — report cancelled
            return {"success": False, "cancelled": True, "slept": 0}
    else:
        time.sleep(duration)
    return {"slept": duration}


# --- Register safe functions for conditions ---

def _window_exists(expr):
    """Check if a window matching the expression exists.
    expr: window title or {title: ..., class_name: ...} JSON."""
    from daemon.handlers.window import handle_list
    result = handle_list({})
    windows = result.get("windows", [])
    for w in windows:
        if expr.lower() in w.get("title", "").lower():
            return True
    return False


def _pixel_color_match(x, y, color_hex):
    """Check if pixel at (x,y) matches the given hex color."""
    from daemon.handlers.screenshot import handle_pixel_color
    result = handle_pixel_color({"x": x, "y": y})
    actual = result.get("hex", "")
    return actual.upper() == str(color_hex).upper().strip()


def _image_find_on_screen(template_path, confidence=0.8):
    """Check if an image template exists on screen.
    Returns True if found, False otherwise.
    """
    from daemon.handlers.image_match import handle_image_find
    result = handle_image_find({
        "template": template_path,
        "confidence": float(confidence),
    })
    return result.get("found", False)


# Expose safe functions for script conditions
_register_safe_function("window_exists", _window_exists)
_register_safe_function("pixel_color", _pixel_color_match)
_register_safe_function("image_find", _image_find_on_screen)
_register_safe_function("window_list", lambda: _get_handlers()["window_list"]({}))


# --- Variable helpers ---

def _resolve_params(params, session_manager):
    """Resolve {{var}} references in params dict."""
    return session_manager.resolve_vars(params)


def _resolve_text_value(value, session_manager):
    """Resolve a single text value with {{var}} substitution."""
    if isinstance(value, str):
        return session_manager.resolve_vars(value)
    return value


# --- Cancel check helper ---

def _check_cancelled(task):
    """Check if a task has been cancelled. Returns True if cancelled."""
    return task is not None and task.should_cancel()


# --- Step execution ---

def _execute_step(step, session_manager, script_vars, task=None):
    """Execute one step of the script. Returns {"success": bool, ...}."""
    # Check cancellation before executing the step
    if _check_cancelled(task):
        return {"success": False, "cancelled": True}

    action = step.get("action", "")

    # --- Control flow (pass task down) ---
    if action == "if":
        return _execute_if(step, session_manager, script_vars, task=task)
    if action == "loop":
        return _execute_loop(step, session_manager, script_vars, task=task)
    if action == "retry":
        return _execute_retry(step, session_manager, script_vars, task=task)
    if action == "set":
        # Set a variable
        var_name = step.get("var", step.get("name", ""))
        var_value = step.get("value", "")
        script_vars[var_name] = _resolve_text_value(var_value, session_manager)
        return {"success": True, "var": var_name, "value": var_value}

    # --- Action dispatch ---
    handlers = _get_handlers()
    handler = handlers.get(action)
    if handler is None:
        return {"success": False, "error": f"Unknown action: {action}"}

    # Resolve variables in params
    params = _resolve_params(step.get("params", {}), session_manager)

    # Merge script variables into params (user params win)
    merged = dict(script_vars)
    merged.update(params)
    merged.pop("script_vars", None)
    merged.pop("session_manager", None)

    # Special handling for sleep (interruptible via cancel event)
    if action == "sleep":
        try:
            result = _handle_sleep(merged, task=task)
            # If sleep was cancelled, propagate the cancelled state
            if isinstance(result, dict) and result.get("cancelled"):
                return {"success": False, "cancelled": True}
            return {"success": True, "result": result}
        except Exception as e:
            return {"success": False, "error": str(e)}

    try:
        result = handler(merged)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


def _execute_if(step, session_manager, script_vars, task=None):
    condition = step.get("condition", "")
    try:
        cond_result = _safe_eval(condition)
    except Exception as e:
        return {"success": False, "error": f"Condition failed: {e}"}

    branch = "then" if cond_result else "else"
    steps = step.get(branch, [])
    results = []
    for s in steps:
        r = _execute_step(s, session_manager, script_vars, task=task)
        results.append(r)
        if not r.get("success"):
            return {"success": False, "branch": branch, "error": r.get("error"), "results": results}
    return {"success": True, "branch": branch, "results": results}


def _execute_loop(step, session_manager, script_vars, task=None):
    times = step.get("times", 0)
    while_cond = step.get("while", "")
    body = step.get("body", [])
    if not body:
        return {"success": True, "iterations": 0}

    max_iter = int(step.get("max_iterations", 1000))

    if times > 0:
        count = 0
        for i in range(min(times, max_iter)):
            # Check cancellation before each iteration
            if _check_cancelled(task):
                return {"success": False, "cancelled": True, "iterations": count}
            script_vars["_loop_index"] = i
            for s in body:
                r = _execute_step(s, session_manager, script_vars, task=task)
                if not r.get("success"):
                    # Only propagate cancel state; let the outer task handle it
                    if r.get("cancelled"):
                        return r
                    return {"success": False, "iteration": i, "error": r.get("error")}
            count += 1
        return {"success": True, "iterations": count}
    elif while_cond:
        count = 0
        while _safe_eval(while_cond) and count < max_iter:
            # Check cancellation before each iteration
            if _check_cancelled(task):
                return {"success": False, "cancelled": True, "iterations": count}
            for s in body:
                r = _execute_step(s, session_manager, script_vars, task=task)
                if not r.get("success"):
                    if r.get("cancelled"):
                        return r
                    return {"success": False, "iteration": count, "error": r.get("error")}
            count += 1
        return {"success": True, "iterations": count}

    return {"success": True, "iterations": 0}


def _execute_retry(step, session_manager, script_vars, task=None):
    max_attempts = int(step.get("max_attempts", 3))
    interval = float(step.get("interval", 1.0))
    body = step.get("body", [])
    last_error = None

    for attempt in range(1, max_attempts + 1):
        # Check cancellation before each attempt
        if _check_cancelled(task):
            return {"success": False, "cancelled": True}

        step_results = []
        all_ok = True
        for s in body:
            r = _execute_step(s, session_manager, script_vars, task=task)
            step_results.append(r)
            if not r.get("success"):
                all_ok = False
                last_error = r.get("error")
                if r.get("cancelled"):
                    return r
                break
        if all_ok:
            return {"success": True, "attempts": attempt, "results": step_results}
        if attempt < max_attempts:
            # Use interruptible sleep for retry interval
            if task:
                task._cancel_event.wait(timeout=interval)
            else:
                time.sleep(interval)

    return {"success": False, "attempts": max_attempts, "error": last_error}


# --- Script progress tracker ---

class ScriptTask:
    """Holds state for one running script task."""

    def __init__(self, task_id, steps):
        self.task_id = task_id
        self.status = "running"  # running | completed | error | cancelled
        self.progress = 0        # steps completed
        self.total = len(steps)
        self.results = {}        # step_id -> result dict
        self.error = None
        self.failed_at = None
        self._cancel_event = threading.Event()

    def should_cancel(self):
        return self._cancel_event.is_set()

    def cancel(self):
        self._cancel_event.set()

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "status": self.status,
            "progress": self.progress,
            "total": self.total,
            "error": self.error,
            "failed_at": self.failed_at,
        }


class ScriptTaskManager:
    """Manages async script execution tasks.

    Scripts run in a dedicated 4-worker thread pool (separate from the
    request-handling pool) so that long-running scripts do not starve
    other IPC requests or hotkey dispatch.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._tasks = {}  # task_id -> ScriptTask
        self._executor = ThreadPoolExecutor(max_workers=4, thread_name_prefix="script_task")

    def submit(self, script_data):
        """Submit a script for async execution. Returns task_id immediately."""
        task_id = uuid.uuid4().hex[:12]
        steps = script_data.get("steps", [])
        task = ScriptTask(task_id, steps)

        with self._lock:
            self._tasks[task_id] = task

        self._executor.submit(self._run_task, task, script_data)
        return task_id

    def get_status(self, task_id):
        """Get current status of a script task."""
        with self._lock:
            task = self._tasks.get(task_id)
            if task is None:
                return None
            return task.to_dict()

    def cancel(self, task_id):
        """Request cancellation of a running script task."""
        with self._lock:
            task = self._tasks.get(task_id)
            if task is None:
                return False
            if task.status != "running":
                return False
            task.cancel()
            return True

    def get_results(self, task_id):
        """Get full results for a completed task."""
        with self._lock:
            task = self._tasks.get(task_id)
            if task is None:
                return None
            if task.status == "running":
                return {"status": "running", "progress": task.progress, "total": task.total}
            return {
                "status": task.status,
                "results": task.results,
                "error": task.error,
                "failed_at": task.failed_at,
                "progress": task.progress,
                "total": task.total,
            }

    def _run_task(self, task, script_data):
        """Execute script in background. Updates task state as it goes."""
        try:
            session_manager = get_manager()
            script_vars = dict(script_data.get("variables", {}))
            for k, v in script_vars.items():
                session_manager.set_variable(k, v)
            steps = script_data.get("steps", [])

            for idx, step in enumerate(steps):
                if task.should_cancel():
                    with self._lock:
                        task.status = "cancelled"
                    return

                step_id = str(step.get("id", f"_step_{idx}"))
                result = _execute_step(step, session_manager, script_vars, task=task)

                with self._lock:
                    task.results[step_id] = result
                    task.progress = idx + 1
                    if "var" in result:
                        script_vars[result["var"]] = result.get("value")

                if not result.get("success"):
                    with self._lock:
                        if result.get("cancelled"):
                            task.status = "cancelled"
                        else:
                            task.status = "error"
                            task.error = result.get("error")
                            task.failed_at = step_id
                    return

            with self._lock:
                task.status = "completed"

        except Exception as e:
            with self._lock:
                task.status = "error"
                task.error = str(e)

    def shutdown(self):
        self._executor.shutdown(wait=False, cancel_futures=True)


# Global task manager
_task_manager = None
_task_manager_lock = threading.Lock()


def get_task_manager():
    global _task_manager
    with _task_manager_lock:
        if _task_manager is None:
            _task_manager = ScriptTaskManager()
        return _task_manager


def shutdown_task_manager():
    global _task_manager
    with _task_manager_lock:
        if _task_manager is not None:
            _task_manager.shutdown()
            _task_manager = None


# --- Main entry (sync, used internally) ---

def execute_script(script_data):
    """Execute a full script synchronously.

    Args:
        script_data: dict with keys:
            - version (optional)
            - variables (optional, dict)
            - steps (required, list of step dicts)

    Returns:
        {"status": "completed"|"error", "results": {step_id: result}}
    """
    session_manager = get_manager()
    # Merge script variables ({{var}} will be resolved by _resolve_params)
    # We set them as session variables so resolve_vars can pick them up
    script_vars = dict(script_data.get("variables", {}))
    for k, v in script_vars.items():
        session_manager.set_variable(k, v)
    steps = script_data.get("steps", [])

    results = {}
    for step in steps:
        step_id = str(step.get("id", f"_step_{len(results)}"))
        result = _execute_step(step, session_manager, script_vars)
        results[step_id] = result
        # Update script_vars with any variables set by this step
        if "var" in result:
            script_vars[result["var"]] = result.get("value")
            session_manager.set_variable(result["var"], result.get("value"))
        if not result.get("success"):
            return {"status": "error", "error": result.get("error"), "results": results, "failed_at": step_id}

    return {"status": "completed", "results": results}


# --- Async entry (exposed via IPC) ---

def execute_script_async(script_data):
    """Submit script for async execution. Returns immediately.

    Args:
        script_data: dict with steps and optional variables

    Returns:
        {"task_id": "...", "status": "running", "total_steps": N}
    """
    mgr = get_task_manager()
    task_id = mgr.submit(script_data)
    steps = script_data.get("steps", [])
    return {"task_id": task_id, "status": "running", "total_steps": len(steps)}


def get_script_status(task_id):
    """Get the current status of a running script task.

    Returns:
        ScriptTask.to_dict() or None if not found.
    """
    mgr = get_task_manager()
    return mgr.get_status(task_id)


def get_script_results(task_id):
    """Get full results of a completed script task.

    Returns:
        Dict with status, results, error, etc. or running progress.
    """
    mgr = get_task_manager()
    return mgr.get_results(task_id)


def cancel_script(task_id):
    """Request cancellation of a running script."""
    mgr = get_task_manager()
    return mgr.cancel(task_id)
