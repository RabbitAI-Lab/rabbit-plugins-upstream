"""
Script template registry.

Each template is a JSON script with placeholder variables in {{var}} format.
Templates are stored as JSON strings (not Python dicts) to avoid Python syntax
conflicts with template variables like {{wait_seconds}} that should remain
as literal strings in the JSON.

See list_templates() and load_template() for the public API.
"""
import copy
import json
import re


# ── Template definitions (as JSON strings) ────────────────────────────────
# Using JSON strings avoids Python trying to interpret {{var}} as expressions.
# _substitute will handle {{var}} replacement at load time.

TEMPLATES = {}

# TODO: properly load from JSON files if the list grows beyond 5-6 templates.
# For now, define inline.

_TEMPLATE_DEFS = [
    {
        "name": "capture_window",
        "description": "Focus a window by title, wait, then save a screenshot",
        "params": {
            "window_title": "Window title to focus (partial match). Required.",
            "save_path": "Full path for screenshot file. Optional (default: TEMP/screenshot_TIMESTAMP.png).",
            "wait_seconds": "Seconds to wait after focusing (default: 1.0).",
        },
        "script_json": json.dumps({
            "version": "1.0",
            "steps": [
                {"action": "log", "params": {"message": "Starting capture_window for '{{window_title}}'"}},
                {"action": "window_focus", "params": {"title": "{{window_title}}"}},
                {"action": "sleep", "params": {"duration": "{{wait_seconds}}"}},
                {"action": "screenshot_save", "params": {"path": "{{save_path}}"}},
                {"action": "log", "params": {"message": "Screenshot saved to {{save_path}}"}},
            ],
        }),
    },
    {
        "name": "type_to_window",
        "description": "Focus a window, type text, and press Enter",
        "params": {
            "window_title": "Window title to focus (partial match). Required.",
            "text": "Text to type. Required.",
            "enter_after": "Press Enter after typing? (true/false, default: true).",
        },
        "script_json": json.dumps({
            "version": "1.0",
            "steps": [
                {"action": "log", "params": {"message": "Starting type_to_window for '{{window_title}}'"}},
                {"action": "window_focus", "params": {"title": "{{window_title}}"}},
                {"action": "sleep", "params": {"duration": 0.5}},
                {"action": "keyboard_type", "params": {"text": "{{text}}"}},
                {"action": "sleep", "params": {"duration": 0.2}},
                {"action": "if", "condition": "{{enter_after}}",
                 "then": [
                     {"action": "keyboard_press", "params": {"key": "enter"}},
                 ]},
            ],
        }),
    },
    {
        "name": "wait_and_click",
        "description": "Wait for a pixel color to appear, then click at coordinates",
        "params": {
            "check_x": "X coordinate to check pixel color.",
            "check_y": "Y coordinate to check pixel color.",
            "expected_color": "Expected hex color (e.g. '#FFFFFF'). Required.",
            "click_x": "X coordinate to click (default: same as check_x).",
            "click_y": "Y coordinate to click (default: same as check_y).",
            "timeout_seconds": "Max wait time in seconds (default: 30).",
            "click_button": "Mouse button: left|right|middle (default: left).",
        },
        "script_json": json.dumps({
            "version": "1.0",
            "steps": [
                {"action": "set", "var": "elapsed", "value": "0"},
                {"action": "loop", "while": "{{elapsed}} < {{timeout_seconds}}",
                 "max_iterations": 300,
                 "body": [
                     {"action": "if", "condition": "pixel_color({{check_x}}, {{check_y}}, '{{expected_color}}')",
                      "then": [
                          {"action": "log", "params": {"message": "Color matched, clicking"}},
                          {"action": "mouse_click", "params": {"x": "{{click_x}}", "y": "{{click_y}}", "button": "{{click_button}}"}},
                          {"action": "set", "var": "elapsed", "value": "9999"},
                      ]},
                     {"action": "sleep", "params": {"duration": 0.1}},
                     {"action": "set", "var": "elapsed", "value": "{{elapsed}} + 0.1"},
                 ]},
            ],
        }),
    },
    {
        "name": "ocr_and_copy",
        "description": "Read text from a screen region and copy it to clipboard",
        "params": {
            "region_x": "Left coordinate of OCR region (default: 0).",
            "region_y": "Top coordinate of OCR region (default: 0).",
            "region_w": "Width of OCR region (default: 800).",
            "region_h": "Height of OCR region (default: 600).",
        },
        "script_json": json.dumps({
            "version": "1.0",
            "steps": [
                {"action": "log", "params": {"message": "Starting OCR read"}},
                {"action": "screen_ocr", "params": {"region": ["{{region_x}}", "{{region_y}}", "{{region_w}}", "{{region_h}}"]}},
            ],
        }),
    },
    {
        "name": "image_find_and_click",
        "description": "Find an image on screen and click its center, with retry",
        "params": {
            "template_path": "Full path to the template image file. Required.",
            "confidence": "Match confidence 0.0-1.0 (default: 0.8).",
            "click_button": "Mouse button: left|right|middle (default: left).",
        },
        "script_json": json.dumps({
            "version": "1.0",
            "steps": [
                {"action": "retry", "max_attempts": 5, "interval": 0.5,
                 "body": [
                     {"action": "image_find", "params": {"template": "{{template_path}}", "confidence": "{{confidence}}"}},
                 ]},
            ],
        }),
    },
]

# Build the TEMPLATES dict
for tdef in _TEMPLATE_DEFS:
    TEMPLATES[tdef["name"]] = tdef


# ── Public API ─────────────────────────────────────────────────────────────

def list_templates():
    """Return a list of all built-in templates with metadata (no scripts)."""
    result = []
    for tpl in TEMPLATES.values():
        result.append({
            "name": tpl["name"],
            "description": tpl.get("description", ""),
            "params": tpl.get("params", {}),
        })
    return result


def load_template(name: str, params: dict = None):
    """Load a template by name and substitute placeholder variables.

    Args:
        name: Template key (e.g. 'capture_window').
        params: Dict of parameter values to substitute into {{var}} placeholders.

    Returns:
        The parsed JSON script dict with variables filled in.

    Raises:
        KeyError: If template name not found.
        ValueError: If required params are missing.
    """
    if name not in TEMPLATES:
        raise KeyError(
            f"Template '{name}' not found. Available: {sorted(TEMPLATES.keys())}"
        )

    tpl = TEMPLATES[name]
    params = params or {}
    required_params = [k for k, v in tpl.get("params", {}).items()
                       if "Required." in v]

    for key in required_params:
        if key not in params:
            raise ValueError(
                f"Template '{name}' requires parameter '{key}'. "
                f"Full params: {tpl.get('params', {})}"
            )

    # Parse the JSON template text
    script = json.loads(tpl["script_json"])

    # Build variables dict: merge params with defaults
    variables = {}
    # Extract defaults from param description (everything after default:)
    import re as _re
    for pk, pv in tpl.get("params", {}).items():
        m = _re.search(r"default:\s*(\S+)", pv, _re.IGNORECASE)
        if m:
            defaults_val = _coerce_type(m.group(1).rstrip(".)"))
            variables[pk] = defaults_val
    # User params override defaults
    variables.update(params)

    # Substitute {{var}} in the script recursively
    resolved_script = _substitute_recursive(script, variables)
    resolved_script["variables"] = variables

    return resolved_script


def _coerce_type(value_str):
    """Try to coerce a string to a more specific type (int, float, bool).

    This is needed because template variables are stored as strings in JSON
    ({{var}}), but the script engine expects typed values for things like
    duration, coordinates, etc.
    """
    # Boolean
    if value_str.lower() == "true":
        return True
    if value_str.lower() == "false":
        return False
    # Int
    try:
        return int(value_str)
    except (ValueError, TypeError):
        pass
    # Float
    try:
        return float(value_str)
    except (ValueError, TypeError):
        pass
    # Return as-is
    return value_str


def _substitute_value(value, variables):
    """Replace {{var}} in a single value, coercing types when possible."""
    if not isinstance(value, str):
        return value

    # Check if the ENTIRE value is a single {{var}} reference
    m = re.fullmatch(r"\{\{(\w+)\}\}", value)
    if m:
        var_name = m.group(1)
        val = variables.get(var_name, value)
        # If the variable value is already typed (int, float, bool), use as-is
        if isinstance(val, (int, float, bool)):
            return val
        # If it's a string, try to coerce
        return _coerce_type(str(val))

    # Partial substitution: e.g. "hello {{name}}"
    def _replace(m):
        var_name = m.group(1)
        val = variables.get(var_name, m.group(0))
        return str(val)
    return re.sub(r"\{\{(\w+)\}\}", _replace, value)


def _substitute_recursive(obj, variables):
    """Recursively replace {{var_name}} in all string values."""
    if isinstance(obj, dict):
        return {k: _substitute_recursive(v, variables) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_substitute_recursive(item, variables) for item in obj]
    elif isinstance(obj, str):
        return _substitute_value(obj, variables)
    return obj
