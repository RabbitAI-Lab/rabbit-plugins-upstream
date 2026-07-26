"""
Handler wrappers for script generation and template management.

Exposes these IPC methods:
  - script_generate:      NL → generate script, return for review
  - script_generate_and_run: NL → generate → execute
  - script_list_templates: List all built-in templates
  - script_load_template:  Load a template with parameter substitution
"""
from daemon.script_gen.generator import generate_script as _gen, generate_and_run as _gen_run
from daemon.script_gen.templates.registry import list_templates as _list_tpls, load_template as _load_tpl
from daemon.script_gen.llm_client import is_configured


METADATA = {
    "llm_available": False,
}


# ── Keyword-to-template mapping (fallback when LLM is not configured) ──────
# Maps prompt keywords to built-in templates with smart parameter extraction.
_KEYWORD_TEMPLATES = [
    # Keywords: list of (keywords, template_name, param_extractor_fn)
    # param_extractor_fn: (prompt, context) -> params dict
    (["screenshot", "截屏", "截图", "capture", "screen capture"],
     "capture_window",
     lambda p, c: {
         "window_title": c.get("window_title", p.split("的")[-1].split(" ")[0].split(",")[0] if "的" in p else ""),
         "save_path": c.get("save_path", ""),
     }),
    (["type", "输入", "键入", "write", "enter"],
     "type_to_window",
     lambda p, c: {
         "window_title": c.get("window_title", ""),
         "text": c.get("text", ""),
     }),
    (["wait", "click", "等待", "点击"],
     "wait_and_click",
     lambda p, c: {
         "check_x": c.get("check_x", 0),
         "check_y": c.get("check_y", 0),
         "expected_color": c.get("expected_color", "#FFFFFF"),
         "click_x": c.get("click_x", 0),
         "click_y": c.get("click_y", 0),
     }),
    (["ocr", "text", "文字", "识别"],
     "ocr_and_copy",
     lambda p, c: {
         "region_x": c.get("region_x", 0),
         "region_y": c.get("region_y", 0),
         "region_w": c.get("region_w", 800),
         "region_h": c.get("region_h", 600),
     }),
    (["image", "image find", "图像", "图片", "template"],
     "image_find_and_click",
     lambda p, c: {
         "template_path": c.get("template_path", ""),
         "confidence": c.get("confidence", 0.8),
         "click_button": c.get("click_button", "left"),
     }),
]


def _try_keyword_fallback(prompt: str, context: dict = None):
    """Try to match prompt keywords to a built-in template.

    Returns:
        Script dict or None if no match.
    """
    prompt_lower = prompt.lower()
    context = context or {}

    for keywords, template_name, extractor in _KEYWORD_TEMPLATES:
        for kw in keywords:
            if kw.lower() in prompt_lower:
                params = extractor(prompt, context)
                try:
                    script = _load_tpl(template_name, params)
                    return script
                except (ValueError, KeyError):
                    continue
    return None


def _check_llm():
    METADATA["llm_available"] = is_configured()


def handle_script_generate(params):
    """Generate a script from natural language (for review, no execution).

    Params:
        prompt:  Natural language description (required).
        context: Optional dict with extra context (e.g. window_title).

    Returns:
        {"status": "generated"|"error",
         "script": {...},
         "session_id": int}
    """
    prompt = params.get("prompt")
    if not prompt:
        raise ValueError(
            "Missing required parameter 'prompt' for script_generate. "
            "Provide a natural language description of what you want to automate."
        )

    context = params.get("context", {})
    result = _gen(prompt, context)

    if not result.get("valid"):
        error = result.get("error", "Script generation failed.")
        help_text = result.get("help")

        # Try keyword-to-template fallback before giving up
        if error == "LLM_NOT_CONFIGURED":
            fallback_script = _try_keyword_fallback(prompt, context)
            if fallback_script:
                return {
                    "status": "generated",
                    "script": fallback_script,
                    "fallback": "keyword_match",
                }

        response = {
            "status": "error",
            "error": error,
        }
        if help_text:
            response["help"] = help_text
        if result.get("script"):
            response["script"] = result["script"]
        if result.get("errors"):
            response["errors"] = result["errors"]
        return response

    from daemon.utils.session import get_manager
    mgr = get_manager()

    return {
        "status": "generated",
        "script": result["script"],
        "session_id": mgr.current_id,
    }


def handle_script_generate_and_run(params):
    """Generate a script from natural language and execute it.

    Params:
        prompt:  Natural language description (required).
        confirm: If True, only generate and return script (no execution).
                 Default: False (generate and execute).
        context: Optional dict with extra context.

    Returns:
        If confirm=false: {"status": "executing", "task_id": "...", "script": {...}}
        If confirm=true:  {"status": "generated", "script": {...}}
    """
    prompt = params.get("prompt")
    if not prompt:
        raise ValueError(
            "Missing required parameter 'prompt' for script_generate_and_run. "
            "Provide a natural language description of what you want to automate."
        )

    confirm = params.get("confirm", False)
    context = params.get("context", {})

    if confirm:
        # Generate only (safe mode)
        return handle_script_generate(params)

    # Generate and execute
    result = _gen_run(prompt, context)

    if not result.get("valid") and "status" not in result:
        error = result.get("error", "Script generation failed.")
        response = {
            "status": "error",
            "error": error,
        }
        if result.get("help"):
            response["help"] = result["help"]
        if result.get("script"):
            response["script"] = result["script"]
        return response

    from daemon.utils.session import get_manager
    mgr = get_manager()

    return {
        "status": result.get("status", "executing"),
        "task_id": result.get("task_id"),
        "script": result.get("script"),
        "session_id": mgr.current_id,
    }


def handle_script_list_templates(params):
    """List all built-in script templates.

    Returns:
        {"templates": [{"name": str, "description": str, "params": dict}, ...]}
    """
    templates = _list_tpls()
    return {"templates": templates}


def handle_script_load_template(params):
    """Load a built-in template with parameter substitution.

    Params:
        name:   Template name (from script_list_templates). Required.
        params: Dict of parameter values to fill in. Optional.

    Returns:
        {"status": "loaded", "script": {...}}
    """
    name = params.get("name")
    if not name:
        raise ValueError(
            "Missing required parameter 'name' for script_load_template. "
            "Use script_list_templates to see available templates."
        )

    tpl_params = params.get("params", {})
    try:
        script = _load_tpl(name, tpl_params)
    except KeyError as e:
        raise ValueError(str(e))
    except ValueError as e:
        raise ValueError(str(e))

    return {"status": "loaded", "script": script, "template": name}
