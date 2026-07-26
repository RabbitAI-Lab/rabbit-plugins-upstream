"""
IPC handler wrappers for AI Agent tools.

Exposes:
  - tools_list:     Return all tool declarations (OpenAI Function Calling format)
  - tools_call:     Execute AI-selected tool calls
  - screen_context: Screen state snapshot (text summary)
  - goal_run:       Natural language goal → plan → execute
"""
from daemon.tools.registry import list_tools
from daemon.tools.executor import execute_tool_calls
from daemon.tools.screen_context import handle_screen_context as _screen_context
from daemon.tools.goal_run import handle_goal_run as _goal_run


def handle_tools_list(params):
    """Return all available tool declarations (OpenAI Function Calling format).

    Params: (none required)

    Returns:
        {"tools": [{"type": "function", "function": {...}}, ...]}
    """
    return list_tools()


def handle_tools_call(params):
    """Execute AI-selected tool calls.

    Params:
        tool_calls:     List of {"id": str, "name": str, "arguments": dict}
        stop_on_error:  If True, stop on first failure (default: false)

    Returns:
        {"results": [{"id": "...", "result": ..., "error": ...}]}
    """
    tool_calls = params.get("tool_calls", [])
    if not tool_calls:
        raise ValueError(
            "Missing required parameter 'tool_calls' for tools_call. "
            "Provide an array of tool call objects."
        )

    stop_on_error = params.get("stop_on_error", False)
    return execute_tool_calls(tool_calls, stop_on_error)


def handle_screen_context(params):
    """Get a text summary of the current screen content.

    Params:
        region:        Optional dict {left, top, width, height}.
        monitor:       Optional int — anchor to this monitor.
        lang:          OCR language (default: chi_sim+eng).
        include_layout: Include element layout (default: true).
        max_chars:     Max chars in returned text (default: 2000).

    Returns:
        {"text": "...", "summary": "...", "elements": [...]}
    """
    return _screen_context(params)


def handle_goal_run(params):
    """Execute a natural language goal automatically.

    Params:
        goal:     Natural language description (required).
        timeout:  Max execution seconds (default: 60).
        confirm:  If True, plan only (default: True).
        context:  Optional extra context dict.

    Returns:
        Planned or execution result.
    """
    return _goal_run(params)
