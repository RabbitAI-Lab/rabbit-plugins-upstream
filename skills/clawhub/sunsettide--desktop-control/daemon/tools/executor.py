"""
Tool call executor — routes LLM function_call payloads to actual handler functions.

Design:
  - Maps tool names to their handler functions (lazy-loaded from actual handlers).
  - All handlers are called **directly** (not via IPC), keeping latency low.
  - Arguments from LLM are passed as-is to handlers (already Python dict).
  - Results are collected and returned in a batch.

Serial execution by default: if a tool call fails, remaining calls still execute
(unless the user specifies `stop_on_error=True`).
"""
import json
import traceback
from typing import Any, Dict, List


# ── Handler mapping (lazy-loaded) ──────────────────────────────────────────

_HANDLER_CACHE = {}


def _get_handler(name: str):
    """Lazy-load and cache a handler function by name."""
    if name in _HANDLER_CACHE:
        return _HANDLER_CACHE[name]

    handlers = {
        # Vision-click
        "find_text":               ("daemon.handlers.vision_click", "handle_find_text"),
        "click_text":              ("daemon.handlers.vision_click", "handle_click_text"),
        "type_to_text":            ("daemon.handlers.vision_click", "handle_type_to_text"),
        "mouse_smart_action":      ("daemon.handlers.vision_click", "handle_mouse_smart_action"),
        # Mouse
        "mouse_move":              ("daemon.handlers.mouse", "handle_move"),
        "mouse_click":             ("daemon.handlers.mouse", "handle_click"),
        # Keyboard
        "keyboard_type":           ("daemon.handlers.keyboard", "handle_type"),
        "keyboard_press":          ("daemon.handlers.keyboard", "handle_press"),
        "keyboard_hotkey":         ("daemon.handlers.keyboard", "handle_hotkey"),
        # Window
        "window_focus":            ("daemon.handlers.window", "handle_focus"),
        "window_list":             ("daemon.handlers.window", "handle_list"),
        # Screenshot
        "screenshot_save":         ("daemon.handlers.screenshot", "handle_screenshot_save"),
        "screen_ocr":              ("daemon.handlers.ocr", "handle_screen_ocr"),
        # Screen context (defined below)
        "screen_context":          ("daemon.tools.screen_context", "handle_screen_context"),
        # Script
        "script_run":              ("daemon.handlers.script_handler", "handle_script_run"),
        "script_run_sync":         ("daemon.handlers.script_handler", "handle_script_run_sync"),
        # Script gen
        "script_generate":         ("daemon.handlers.script_gen_handler", "handle_script_generate"),
        # Sessions
        "session_create":          ("daemon.handlers.session_handler", "handle_session_create"),
        "session_switch":          ("daemon.handlers.session_handler", "handle_session_switch"),
    }

    entry = handlers.get(name)
    if entry is None:
        return None

    module_path, func_name = entry
    try:
        mod = __import__(module_path, fromlist=[func_name])
        handler = getattr(mod, func_name)
        _HANDLER_CACHE[name] = handler
        return handler
    except (ImportError, AttributeError) as e:
        _HANDLER_CACHE[name] = None
        return None


# ── Parameter validation schemas ──────────────────────────────────────────
# Pre-flight checks before dispatching to handler.
# If a required field is missing, return a clear error *before* touching anything.

_REQUIRED_PARAMS = {
    "find_text":              ["text"],
    "click_text":             ["text"],
    "type_to_text":           ["text", "input"],
    "mouse_move":             ["x", "y"],
    "keyboard_type":          ["text"],
    "keyboard_press":         ["key"],
    "keyboard_hotkey":        ["keys"],
    "window_focus":           ["title"],
    "goal_run":               ["goal"],
    "script_generate":        ["prompt"],
    "script_run":             ["script"],
    "script_run_sync":        ["script"],
    "session_create":         [],
    "tools_call":             ["tool_calls"],
}


def _validate_arguments(name: str, arguments: dict) -> list:
    """Check required params for a tool call. Returns list of missing fields."""
    if not isinstance(arguments, dict):
        return ["arguments must be a JSON object"]
    required = _REQUIRED_PARAMS.get(name, [])
    missing = [k for k in required if k not in arguments or arguments.get(k) is None]
    return missing


# ── Execution ──────────────────────────────────────────────────────────────

def execute_tool_call(name: str, arguments: dict) -> dict:
    """Execute a single tool call.

    Args:
        name: Tool name (e.g. "click_text").
        arguments: Parameters dict from the LLM.

    Returns:
        {"result": {...}} or {"error": "..."}
    """
    handler = _get_handler(name)
    if handler is None:
        return {"error": f"Unknown tool: '{name}'"}

    # Pre-flight parameter validation
    missing = _validate_arguments(name, arguments)
    if missing:
        return {"error": f"Missing required parameter(s): {', '.join(missing)}"}

    try:
        result = handler(arguments)
        return {"result": result}
    except Exception as e:
        tb = traceback.format_exc()
        return {"error": str(e), "traceback": tb}


def execute_tool_calls(tool_calls: List[Dict], stop_on_error: bool = False) -> dict:
    """Execute a batch of tool calls.

    Args:
        tool_calls: List of {"id": str, "name": str, "arguments": dict}.
        stop_on_error: If True, stop on first failure.

    Returns:
        {"results": [{"id": ..., "result": ..., "error": ...}]}
    """
    results = []

    for tc in tool_calls:
        call_id = tc.get("id", "unknown")
        name = tc.get("name", "")
        arguments = tc.get("arguments", {})
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError:
                results.append({"id": call_id, "error": f"Invalid JSON arguments: {arguments}"})
                if stop_on_error:
                    break
                continue

        outcome = execute_tool_call(name, arguments)

        entry = {"id": call_id, "name": name}
        if "result" in outcome:
            entry["result"] = outcome["result"]
        else:
            entry["error"] = outcome.get("error", "Unknown error")

        results.append(entry)

        if stop_on_error and "error" in entry:
            break

    return {"results": results}
