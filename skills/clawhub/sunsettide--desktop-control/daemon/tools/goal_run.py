"""
Goal-driven automation — the "one-shot" capability.

Takes a natural language goal and automatically plans and executes
the necessary steps to achieve it.

Architecture (two-tier):
  - Tier A (rule-driven): Fast path for common patterns (e.g.
    "open X, type Y, screenshot"). No LLM needed.
  - Tier B (LLM-enhanced): For complex goals, falls back to the
    script generation engine (daemon.script_gen).

Design:
  - Rule engine matches against predefined patterns.
  - Each pattern extracts parameters and generates a script.
  - Script is executed via script_run (async) or script_run_sync.
  - Default: confirm_before_run=True for safety.
"""
import json
import logging
import re
import time
from typing import List, Optional

from daemon.script_engine.engine import execute_script_async, execute_script

logger = logging.getLogger(__name__)


# ── Goal patterns (rule-driven) ───────────────────────────────────────────
# Each pattern is a (regex, builder_fn) pair.
# builder_fn(match, params) -> script dict (same format as script_engine expects)

_GOAL_PATTERNS = []


def _goal_pattern(regex_str):
    """Decorator to register a goal pattern."""
    def decorator(fn):
        _GOAL_PATTERNS.append((re.compile(regex_str, re.IGNORECASE), fn))
        return fn
    return decorator


@_goal_pattern(r"(?:打开|启动|运行|启动)\s*(\S[\w\s]*?)(?:\s*(?:然后|，|并).*|$)")
def _open_app(match, params):
    """Pattern: 打开 {app}"""
    app = match.group(1).strip()
    steps = [
        {"action": "log", "params": {"message": f"Focusing window: {app}"}},
        {"action": "window_focus", "params": {"title": app}},
        {"action": "sleep", "params": {"duration": 0.5}},
    ]
    return {"version": "1.0", "steps": steps}


@_goal_pattern(r"(?:输入|键入|写入|type)\s*[：:]\s*(.+?)(?:\s*(?:然后|，|并).*|$)")
def _type_text(match, params):
    """Pattern: 输入 {text}"""
    text = match.group(1).strip()
    return {"version": "1.0", "steps": [
        {"action": "keyboard_type", "params": {"text": text}},
    ]}


@_goal_pattern(r"(?:截图|截屏|screenshot|capture).*?((?::|保存到)\s*(\S+))?")
def _screenshot(match, params):
    """Pattern: 截图 或 截图保存到 {path}"""
    filepath = match.group(2) if match.lastindex and match.group(2) else ""
    if not filepath:
        from tempfile import gettempdir
        filepath = gettempdir() + f"\\screenshot_goal_{int(time.time())}.png"
    return {"version": "1.0", "steps": [
        {"action": "screenshot_save", "params": {"path": filepath}},
        {"action": "log", "params": {"message": f"Screenshot saved to {filepath}"}},
    ]}


@_goal_pattern(r"(?:点击|单击|点一下|点|press|click)\s*[：:]?\s*(.+)")
def _click_text_pattern(match, params):
    """Pattern: 点击 {text}"""
    text = match.group(1).strip()
    return {"version": "1.0", "steps": [
        {"action": "click_text", "params": {"text": text, "wait": 0.3}},
    ]}


@_goal_pattern(r"(?:等待|等|wait)\s*(\d+(?:\.\d+)?)\s*(?:秒|s)?")
def _wait_pattern(match, params):
    """Pattern: 等待 {seconds} 秒"""
    seconds = float(match.group(1))
    return {"version": "1.0", "steps": [
        {"action": "sleep", "params": {"duration": seconds}},
    ]}


@_goal_pattern(r"(?:滚动|滚轮|scroll)\s*(上|下|左|右|up|down|left|right)?\s*(\d+)?")
def _scroll_pattern(match, params):
    """Pattern: 滚动 (方向) (步数)"""
    direction = match.group(1) if match.lastindex >= 1 and match.group(1) else "down"
    clicks = int(match.group(2)) if match.lastindex >= 2 and match.group(2) else 3
    dir_map = {"上": "up", "下": "down", "左": "left", "右": "right",
               "up": "up", "down": "down", "left": "left", "right": "right"}
    return {"version": "1.0", "steps": [
        {"action": "mouse_scroll", "params": {"clicks": clicks if direction in ("上", "down") else -clicks, "direction": "vertical"}},
    ]}


# ── Compound pattern: open + type + screenshot ────────────────────────────

def _match_compound_goal(goal: str) -> Optional[dict]:
    """Match complex goals like '打开记事本，输入hello，截图' by
    extracting individual operations and chaining them.

    This is the primary fast-path for common multi-step tasks.
    """
    steps = []
    matched_any = False

    # Patterns to extract operations from a compound sentence
    operations = [
        # 打开 X
        (r"(?:打开|启动|运行|启动)\s*(\S[\w\s]*)", lambda m: {
            "action": "window_focus", "params": {"title": m.group(1).strip()}
        }),
        # 输入 X
        (r"(?:输入|键入|写入|type)\s*[：:]?\s*(.+?)(?=\s*(?:然后|，|并|截图|等待|$))", lambda m: {
            "action": "keyboard_type", "params": {"text": m.group(1).strip()}
        }),
        # 点击 X
        (r"(?:点击|单击|点一下|点|press|click)\s*[：:]?\s*(.+?)(?=\s*(?:然后|，|并|截图|等待|$))", lambda m: {
            "action": "click_text", "params": {"text": m.group(1).strip(), "wait": 0.3}
        }),
        # 截图
        (r"(?:截图|截屏|screenshot|capture)(?:\s*保存到\s*(\S+))?", lambda m: {
            "action": "screenshot_save",
            "params": {"path": m.group(1) if m.lastindex and m.group(1) else f"{__import__('tempfile').gettempdir()}\\screenshot_{int(time.time())}.png"}
        }),
        # 等待 N 秒
        (r"(?:等待|等|wait)\s*(\d+(?:\.\d+)?)\s*(?:秒|s)?", lambda m: {
            "action": "sleep", "params": {"duration": float(m.group(1))}
        }),
        # 按/按下 X
        (r"(?:按|按下|press)\s*(\S+)", lambda m: {
            "action": "keyboard_press", "params": {"key": m.group(1).strip().lower()}
        }),
    ]

    for pattern, builder in operations:
        m = re.search(pattern, goal, re.IGNORECASE)
        if m:
            step = builder(m)
            if step:
                steps.append(step)
                # Add sleep after focus/click for UI to settle
                if step["action"] in ("window_focus", "click_text"):
                    steps.append({"action": "sleep", "params": {"duration": 0.5}})
                matched_any = True

    if not matched_any:
        return None

    return {"version": "1.0", "steps": steps}


# ── Main entry ────────────────────────────────────────────────────────────

def handle_goal_run(params):
    """Execute a natural language goal.

    Args:
        goal:            Natural language description of the goal (required).
        timeout:         Max execution time in seconds (default: 60).
        max_steps:       Max steps to generate (default: 20).
        confirm:         If True, generate plan but don't execute (default: True).
        context:         Optional extra context dict for LLM mode.

    Returns:
        If confirm=True: {"status": "planned", "steps": [...], "script": {...}}
        If confirm=False: {"status": "executing"|"completed"|"failed", ...}
    """
    goal = params.get("goal")
    if not goal:
        raise ValueError(
            "Missing required parameter 'goal' for goal_run. "
            "Example: {\"goal\": \"打开记事本，输入 Hello World，截图保存\"}"
        )

    timeout = int(params.get("timeout", 60))
    max_steps = int(params.get("max_steps", 20))
    confirm = params.get("confirm", True)
    context = params.get("context", {})

    # Step 1: Try rule-driven planning
    script = _match_compound_goal(goal)

    # Step 2: If no rule matched, try LLM generation
    if script is None:
        from daemon.script_gen.llm_client import is_configured
        if is_configured():
            try:
                from daemon.script_gen.generator import generate_script
                gen_result = generate_script(goal, context)
                if gen_result.get("valid"):
                    script = gen_result["script"]
            except Exception as e:
                return {"status": "error", "error": f"LLM generation failed: {e}"}
        else:
            return {
                "status": "error",
                "error": f"Cannot parse goal: '{goal}'. No matching pattern found.",
                "help": "Try using simpler phrasing, or configure an LLM backend.",
            }

    # Step 3: If still no script, error out
    if script is None:
        return {
            "status": "error",
            "error": f"Cannot parse goal: '{goal}'. LLM not configured and no rule matched.",
        }

    steps = script.get("steps", [])
    if len(steps) > max_steps:
        return {
            "status": "error",
            "error": f"Generated plan has {len(steps)} steps (max {max_steps}). Simplify your goal.",
        }

    # Limit total steps
    if len(steps) == 0:
        return {"status": "error", "error": "Generated plan has no steps."}

    # Step 4: Confirm or execute
    if confirm:
        return {
            "status": "planned",
            "steps": steps,
            "script": script,
            "step_count": len(steps),
        }

    # Execute
    try:
        result = execute_script(script)
    except Exception as e:
        return {"status": "failed", "error": str(e), "steps": steps}

    if result.get("status") == "completed":
        return {
            "status": "completed",
            "steps": steps,
            "step_results": result.get("results", {}),
            "summary": "目标已达成",
        }
    else:
        return {
            "status": "failed",
            "error": result.get("error", "Execution failed"),
            "failed_at": result.get("failed_at"),
            "steps": steps,
            "step_results": result.get("results", {}),
        }
