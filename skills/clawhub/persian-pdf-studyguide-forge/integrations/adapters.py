#!/usr/bin/env python3
"""adapters.py — one-import glue for every major agent framework.

The skill's real interface is `scripts/forge.py` (argv + JSON stdout). This
module wraps that single contract in the shapes each framework expects, so no
one has to write bespoke glue — which is what makes different agents produce
different results.

Everything here is optional and dependency-light: importing this module needs
nothing but the standard library. Framework-specific helpers import their
framework lazily, inside the function, so the module still loads when the
framework is absent.

    from integrations.adapters import (
        run,                       # plain python / cron / any script
        openai_tool_spec,          # OpenAI function calling / Agents SDK
        anthropic_tool_spec,       # Anthropic tool use
        gemini_function_declaration,
        as_langchain_tool,         # LangChain / LangGraph
        as_crewai_tool,            # CrewAI
        as_autogen_function,       # AutoGen
        as_llamaindex_tool,        # LlamaIndex
        n8n_execute_command,       # n8n Execute Command node
        github_actions_step,       # CI
    )
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Optional

ROOT = Path(__file__).resolve().parent.parent
FORGE = ROOT / "scripts" / "forge.py"
SPEC = json.loads((ROOT / "integrations/tool-spec.json").read_text("utf-8"))
TOOL_NAME = SPEC["name"]
TOOL_DESCRIPTION = SPEC["description"]
INPUT_SCHEMA = SPEC["input_schema"]


# ──────────────────────────────────────────────────────────────────────────
# the universal call
# ──────────────────────────────────────────────────────────────────────────
def run(command: str = "describe", timeout: Optional[int] = None, **kwargs: Any) -> Dict[str, Any]:
    """Invoke the skill and return its parsed JSON result.

    Identical semantics from every framework, because everything funnels
    through the same subprocess contract.

    Returns the skill's JSON document, annotated with ``_exit`` (the process
    exit code) and, on failure, ``_stderr_tail``.
    """
    job = {k: v for k, v in kwargs.items() if v not in (None, "")}
    job["command"] = command
    proc = subprocess.run([sys.executable, str(FORGE), "--stdin"],
                          input=json.dumps(job), capture_output=True,
                          text=True, cwd=str(ROOT), timeout=timeout)
    try:
        out = json.loads((proc.stdout or "").strip() or "{}")
    except json.JSONDecodeError:
        out = {"error": "non-JSON stdout", "raw": (proc.stdout or "")[:2000]}
    if not isinstance(out, dict):
        out = {"result": out}
    out["_exit"] = proc.returncode
    if proc.returncode != 0:
        out["_stderr_tail"] = "\n".join((proc.stderr or "").splitlines()[-15:])
    return out


def run_text(command: str = "describe", **kwargs: Any) -> str:
    """Same as :func:`run` but returns pretty JSON text — the shape most
    tool-calling frameworks want to hand back to a model."""
    return json.dumps(run(command, **kwargs), ensure_ascii=False,
                      indent=2, sort_keys=True)


# ──────────────────────────────────────────────────────────────────────────
# tool specs — same schema, four vendor wrappers
# ──────────────────────────────────────────────────────────────────────────
def openai_tool_spec() -> dict:
    """OpenAI function-calling / Agents SDK / Codex CLI tool definition."""
    return {"type": "function",
            "function": {"name": TOOL_NAME, "description": TOOL_DESCRIPTION,
                         "parameters": INPUT_SCHEMA}}


def anthropic_tool_spec() -> dict:
    """Anthropic /v1/messages tool definition."""
    return {"name": TOOL_NAME, "description": TOOL_DESCRIPTION,
            "input_schema": INPUT_SCHEMA}


def gemini_function_declaration() -> dict:
    """Gemini functionDeclaration. Gemini's schema dialect rejects
    ``additionalProperties`` and ``default``, so they are stripped."""
    def clean(node):
        if isinstance(node, dict):
            return {k: clean(v) for k, v in node.items()
                    if k not in ("additionalProperties", "default", "$schema")}
        if isinstance(node, list):
            return [clean(x) for x in node]
        return node
    return {"name": TOOL_NAME, "description": TOOL_DESCRIPTION,
            "parameters": clean(INPUT_SCHEMA)}


def mcp_tool_descriptor() -> dict:
    """MCP tools/list entry (see integrations/mcp_server.py for the server)."""
    return {"name": TOOL_NAME, "description": TOOL_DESCRIPTION,
            "inputSchema": INPUT_SCHEMA}


# ──────────────────────────────────────────────────────────────────────────
# framework objects
# ──────────────────────────────────────────────────────────────────────────
def as_langchain_tool():
    """LangChain / LangGraph StructuredTool."""
    from langchain_core.tools import StructuredTool  # lazy import
    return StructuredTool.from_function(
        func=lambda **kw: run_text(**kw),
        name=TOOL_NAME, description=TOOL_DESCRIPTION,
        args_schema=None, infer_schema=False)


def as_crewai_tool():
    """CrewAI BaseTool instance."""
    from crewai.tools import BaseTool  # lazy import

    class ForgeTool(BaseTool):
        name: str = TOOL_NAME
        description: str = TOOL_DESCRIPTION

        def _run(self, command: str = "describe", **kwargs) -> str:
            return run_text(command, **kwargs)

    return ForgeTool()


def as_autogen_function() -> dict:
    """AutoGen register_function payload: {'function', 'name', 'description'}."""
    def forge(command: str = "describe", **kwargs) -> str:
        return run_text(command, **kwargs)
    return {"function": forge, "name": TOOL_NAME, "description": TOOL_DESCRIPTION}


def as_llamaindex_tool():
    """LlamaIndex FunctionTool."""
    from llama_index.core.tools import FunctionTool  # lazy import
    return FunctionTool.from_defaults(
        fn=lambda command="describe", **kw: run_text(command, **kw),
        name=TOOL_NAME, description=TOOL_DESCRIPTION)


def as_openai_agents_tool():
    """openai-agents SDK function tool."""
    from agents import function_tool  # lazy import

    @function_tool(name_override=TOOL_NAME, description_override=TOOL_DESCRIPTION)
    def forge(command: str = "describe", pdf: str = "", work: str = "work",
              title: str = "راهنمای مطالعه", maximum: bool = False) -> str:
        return run_text(command, pdf=pdf, work=work, title=title, maximum=maximum)

    return forge


# ──────────────────────────────────────────────────────────────────────────
# no-code / CI snippets
# ──────────────────────────────────────────────────────────────────────────
def n8n_execute_command(command: str = "doctor", **kwargs) -> str:
    """Command string for an n8n 'Execute Command' node (or any shell runner)."""
    job = json.dumps({**kwargs, "command": command}, ensure_ascii=False)
    return f"echo '{job}' | python3 {FORGE} --stdin"


def github_actions_step(command: str = "selftest", **kwargs) -> dict:
    """A ready-to-paste GitHub Actions step."""
    return {
        "name": f"Persian PDF StudyGuide Forge — {command}",
        "run": "\n".join([
            "sudo apt-get update -qq",
            "sudo apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-fas tesseract-ocr-eng",
            "python3 -m pip install -r requirements.txt",
            n8n_execute_command(command, **kwargs),
        ]),
        "env": {"FORGE_MOCK": "1"},
    }


if __name__ == "__main__":
    print(json.dumps({
        "openai": openai_tool_spec(),
        "anthropic": anthropic_tool_spec(),
        "gemini": gemini_function_declaration(),
        "mcp": mcp_tool_descriptor(),
        "n8n": n8n_execute_command("run", pdf="lecture.pdf"),
    }, ensure_ascii=False, indent=2, sort_keys=True))
