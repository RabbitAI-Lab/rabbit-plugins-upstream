"""
Script generation and validation engine.

Three modes of operation:
  1. **LLM generate**: natural language → JSON script (via configured LLM)
  2. **Template load**: pre-built template + params → JSON script
  3. **JSON input**: user-provided script → validate only

Entry points:
  - generate_and_run(params)   — NL → generate → optionally execute
  - generate_script(params)    — NL → generate → return for review
  - validate_script(script)    — Schema validation only
"""
import hashlib
import json
import logging
import os
import time

from daemon.script_engine.engine import execute_script_async

logger = logging.getLogger(__name__)

# ── Script cache directory ─────────────────────────────────────────────────

SCRIPT_CACHE = os.path.join(
    os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
    "DesktopControl", "Scripts",
)


def _ensure_cache_dir():
    os.makedirs(SCRIPT_CACHE, exist_ok=True)


# ── JSON Schema validation ─────────────────────────────────────────────────

STEP_ACTIONS = {
    "mouse_move", "mouse_click", "mouse_drag", "mouse_scroll", "mouse_position",
    "keyboard_type", "keyboard_press", "keyboard_hotkey",
    "screenshot", "screenshot_save", "pixel_color",
    "window_list", "window_focus", "window_info", "window_minimize",
    "window_maximize", "window_close", "window_move", "window_resize",
    "window_set_topmost",
    "uia_find", "uia_click", "uia_get_text",
    "screen_ocr", "image_find", "file_drag_drop",
    "sleep", "log", "nop",
    "if", "loop", "retry", "set",
}

CONTROL_FLOW = {"if", "loop", "retry", "set"}

# ── Fuzzy action fix ───────────────────────────────────────────────────────
# Maps common LLM typos/variations to correct action names
_FUZZY_ACTION_MAP = {
    # Mouse
    "mouseclick": "mouse_click",
    "mouse_move_to": "mouse_move",
    "movemouse": "mouse_move",
    "move_mouse": "mouse_move",
    "clickmouse": "mouse_click",
    "click_at": "mouse_click",
    "doubleclick": "mouse_click",
    "rightclick": "mouse_click",
    "scroll": "mouse_scroll",
    "mousescroll": "mouse_scroll",
    # Keyboard
    "type": "keyboard_type",
    "typetext": "keyboard_type",
    "type_text": "keyboard_type",
    "presskey": "keyboard_press",
    "press_key": "keyboard_press",
    "hitkey": "keyboard_press",
    "hotkey": "keyboard_hotkey",
    "shortcut": "keyboard_hotkey",
    "keyshortcut": "keyboard_hotkey",
    # Screenshot
    "capture": "screenshot_save",
    "screencapture": "screenshot_save",
    "screencap": "screenshot_save",
    "takephoto": "screenshot_save",
    "screenshotfull": "screenshot",
    # Window
    "focus": "window_focus",
    "focuswindow": "window_focus",
    "activatewindow": "window_focus",
    "closewindow": "window_close",
    "minimizewindow": "window_minimize",
    "maximizewindow": "window_maximize",
    "movewindow": "window_move",
    "resizewindow": "window_resize",
    "settopmost": "window_set_topmost",
    "bringtofront": "window_focus",
    # Vision
    "ocr": "screen_ocr",
    "screenshotocr": "screen_ocr",
    "findimage": "image_find",
    "imagefind": "image_find",
    "matchimage": "image_find",
    "imagematch": "image_find",
    # Misc
    "wait": "sleep",
    "waits": "sleep",
    "delay": "sleep",
    "pixelcheck": "pixel_color",
    "getpixel": "pixel_color",
    # UIA
    "uifind": "uia_find",
    "uiclick": "uia_click",
    "uiread": "uia_get_text",
    "uigettext": "uia_get_text",
}


def _fuzzy_fix_script(script: dict) -> tuple:
    """Attempt to fix common action name typos in a script.

    Returns:
        (fixed_script, fix_count): tuple of the (possibly) fixed script
        and the number of steps that were corrected.
    """
    steps = script.get("steps", [])
    if not steps or not isinstance(steps, list):
        return script, 0

    fix_count = 0
    for step in steps:
        if not isinstance(step, dict):
            continue
        action = step.get("action", "")
        if not action:
            continue
        lower_action = action.lower().replace(" ", "").replace("-", "").replace("_", "")
        corrected = _FUZZY_ACTION_MAP.get(lower_action)
        if corrected and corrected != action:
            step["action"] = corrected
            fix_count += 1

    return script, fix_count


def validate_script(script: dict) -> dict:
    """Validate a script dict against the engine schema.

    Returns:
        {"valid": True} or {"valid": False, "errors": [str, ...]}
    """
    errors = []

    # Must be a dict
    if not isinstance(script, dict):
        return {"valid": False, "errors": ["Script must be a JSON object (not array or primitive)."]}

    # Must have steps
    steps = script.get("steps")
    if not steps:
        return {"valid": False, "errors": ["Script must contain a 'steps' array with at least one step."]}

    if not isinstance(steps, list):
        return {"valid": False, "errors": ["'steps' must be an array."]}

    # Validate each step
    for idx, step in enumerate(steps):
        _validate_step(step, idx, errors)

    if errors:
        return {"valid": False, "errors": errors}
    return {"valid": True}


def _validate_step(step: dict, idx: int, errors: list, path: str = None):
    """Validate one step in the script."""
    prefix = path or f"steps[{idx}]"

    if not isinstance(step, dict):
        errors.append(f"{prefix}: Step must be a JSON object.")
        return

    action = step.get("action")
    if not action:
        errors.append(f"{prefix}: Missing 'action' field.")
        return

    if action not in STEP_ACTIONS:
        errors.append(f"{prefix}: Unknown action '{action}'. Valid: {sorted(STEP_ACTIONS)}")
        return

    # Validate nested control flow structures
    if action == "if":
        if not step.get("condition"):
            errors.append(f"{prefix}(if): Missing 'condition' field.")
        for branch in ("then", "else"):
            branch_steps = step.get(branch, [])
            if not isinstance(branch_steps, list):
                errors.append(f"{prefix}(if/{branch}): Must be an array of steps.")
            else:
                for bi, bstep in enumerate(branch_steps):
                    _validate_step(bstep, bi, errors, f"{prefix}(if/{branch}[{bi}])")

    elif action == "loop":
        if not step.get("times") and not step.get("while"):
            errors.append(f"{prefix}(loop): Must specify 'times' or 'while'.")
        body = step.get("body", [])
        if not isinstance(body, list):
            errors.append(f"{prefix}(loop/body): Must be an array of steps.")
        else:
            for bi, bstep in enumerate(body):
                _validate_step(bstep, bi, errors, f"{prefix}(loop/body[{bi}])")

    elif action == "retry":
        body = step.get("body", [])
        if not isinstance(body, list):
            errors.append(f"{prefix}(retry/body): Must be an array of steps.")
        else:
            for bi, bstep in enumerate(body):
                _validate_step(bstep, bi, errors, f"{prefix}(retry/body[{bi}])")

    elif action == "set":
        if not step.get("var") and not step.get("name"):
            errors.append(f"{prefix}(set): Missing 'var' field.")


# ── Cache helpers ──────────────────────────────────────────────────────────

def _cache_key(prompt: str) -> str:
    """Generate a deterministic filename from the prompt."""
    h = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:16]
    return f"gen_{h}.json"


def _load_from_cache(prompt: str) -> dict:
    """Try to load a previously generated script from cache."""
    _ensure_cache_dir()
    path = os.path.join(SCRIPT_CACHE, _cache_key(prompt))
    if os.path.isfile(path):
        try:
            with open(path, encoding="utf-8") as f:
                cached = json.load(f)
            logger.info(f"Using cached script for prompt: {path}")
            return cached
        except (json.JSONDecodeError, IOError):
            pass
    return None


def _save_to_cache(prompt: str, script: dict):
    """Save a generated script to cache."""
    _ensure_cache_dir()
    path = os.path.join(SCRIPT_CACHE, _cache_key(prompt))
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(script, f, ensure_ascii=False, indent=2)
        logger.info(f"Script cached at: {path}")
    except IOError as e:
        logger.warning(f"Failed to cache script: {e}")


# ── Main generation workflow ───────────────────────────────────────────────

def generate_script(prompt: str, context: dict = None) -> dict:
    """Generate a JSON script from natural language via LLM.

    Args:
        prompt: Natural language description.
        context: Optional extra context dict.

    Returns:
        {"valid": True, "script": {...}}
        or
        {"valid": False, "errors": [...], "script": None}
    """
    # Check cache first
    cached = _load_from_cache(prompt)
    if cached:
        validation = validate_script(cached)
        if validation["valid"]:
            return {"valid": True, "script": cached, "cached": True}

    # Call LLM
    from .llm_client import generate_script as llm_generate, extract_json, is_configured
    from .prompts import SYSTEM_PROMPT, build_user_prompt

    if not is_configured():
        return {
            "valid": False,
            "script": None,
            "error": "LLM_NOT_CONFIGURED",
            "help": (
                "No LLM backend configured. To enable AI script generation, "
                "set the environment variables listed below, or use "
                "script_list_templates / script_load_template for built-in tasks.\n\n"
                + __import__("daemon.script_gen.llm_client",
                             fromlist=["config_help"]).config_help()
            ),
        }

    try:
        user_prompt = build_user_prompt(prompt, context)
        raw = llm_generate(SYSTEM_PROMPT, user_prompt)
        raw_json = extract_json(raw)
        script = json.loads(raw_json)
    except json.JSONDecodeError as e:
        return {
            "valid": False,
            "script": None,
            "error": f"LLM returned invalid JSON: {e}",
            "raw_response": raw,
        }
    except RuntimeError as e:
        return {
            "valid": False,
            "script": None,
            "error": str(e),
        }

    # Validate the generated script
    validation = validate_script(script)
    if not validation["valid"]:
        # Try fuzzy fix once before giving up
        fixed_script, fix_count = _fuzzy_fix_script(script)
        if fix_count > 0:
            validation2 = validate_script(fixed_script)
            if validation2["valid"]:
                script = fixed_script
                logger.info(f"Fuzzy-fixed {fix_count} action(s) in generated script")
            else:
                return {
                    "valid": False,
                    "script": script,
                    "errors": validation["errors"],
                    "fix_attempted": fix_count,
                    "fix_errors": validation2["errors"],
                    "error": f"Generated script failed validation ({fix_count} fuzzy fixes attempted but not sufficient).",
                }
        else:
            return {
                "valid": False,
                "script": script,
                "errors": validation["errors"],
                "error": "Generated script failed validation. See 'errors' for details.",
            }

    # Cache it
    _save_to_cache(prompt, script)

    return {"valid": True, "script": script}


def generate_and_run(prompt: str, context: dict = None) -> dict:
    """Generate a script from natural language and execute it.

    Returns:
        {"status": "executing", "task_id": "...", "script": {...}}
        or error dict.
    """
    gen_result = generate_script(prompt, context)
    if not gen_result.get("valid"):
        return gen_result

    script = gen_result["script"]
    # Submit for async execution
    run_result = execute_script_async(script)
    return {
        "status": "executing",
        "task_id": run_result["task_id"],
        "script": script,
        "total_steps": run_result["total_steps"],
    }
