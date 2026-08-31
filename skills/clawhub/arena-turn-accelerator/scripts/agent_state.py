#!/usr/bin/env python3
"""
agent_state.py — per-agent state isolation for arena-turn-accelerator.

WHY (v1.5.0): several different AI agents often share one machine (an Arena
agent, an OpenClaw agent, a Claude Code session, a plain CLI script). All of
them used to write the SAME state files under ~/.arena_turn — one agent's
generation fence, zombie-score history, and spine ledger were another agent's.
A turn counter from agent A made agent B think it was going zombie; a lifecycle
bump from B fenced out A's in-flight answer.

Resolution rule (deliberately backward compatible):
  * agent == "default" (no --agent, no $ARENA_AGENT)  -> legacy ~/.arena_turn
    All existing behaviour, tests, and docs keep working unchanged.
  * agent given explicitly (or via $ARENA_AGENT)      -> ~/.arena_turn/agents/<name>

The name is sanitized to [A-Za-z0-9._-]; anything hostile is refused rather
than silently mangled, so two agents can never be tricked into sharing a dir
by a name collision after sanitizing.

Usage from sibling modules:
    import agent_state
    STATE = agent_state.state_path("context.json")       # full path, dir created
"""
import os
import re

_BASE = os.path.expanduser("~/.arena_turn")
_SAFE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")

KNOWN_AGENTS = ("arena", "openclaw", "claude-code", "cursor", "aider",
                "generic", "default")


def current_agent(explicit=None):
    """explicit --agent flag wins, then $ARENA_AGENT, then "default"."""
    agent = (explicit or os.environ.get("ARENA_AGENT") or "default").strip()
    return agent or "default"


def state_dir(agent=None):
    """Resolve the state directory for `agent` (created on demand by callers)."""
    name = current_agent(agent)
    if name == "default":
        return _BASE                      # legacy path — zero behaviour change
    if not _SAFE.match(name):
        # A hostile/invalid name must fail LOUDLY, never silently fall back to
        # the shared directory — that would contaminate another agent's state
        # (the exact bug this module exists to prevent). SystemExit prints the
        # message cleanly on the CLI with no traceback.
        raise SystemExit(
            f"error: agent name must match [A-Za-z0-9._-] (max 64), got {name!r} "
            f"— refusing to use the shared state dir")
    return os.path.join(_BASE, "agents", name)


def state_path(basename, agent=None):
    """Full path of a state file inside the agent's directory."""
    d = state_dir(agent)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, basename)


def detect_agent_from_env():
    """Best-effort detection of the calling agent runtime (advisory only).

    Used by turn_preflight to *suggest* an agent name when none was given; it
    never overrides an explicit choice, and detection failure is not an error —
    the caller falls back to "default".
    """
    env = os.environ
    if env.get("ARENA_AGENT"):
        return env["ARENA_AGENT"]
    if env.get("CLAUDECODE") == "1" or env.get("CLAUDE_CODE_ENTRYPOINT"):
        return "claude-code"
    if env.get("OPENCLAW") or env.get("CLAWHUB_OPENCLAW") or env.get("CLAWDBOT"):
        return "openclaw"
    if env.get("CURSOR_AGENT") or (env.get("TERM_PROGRAM") or "") == "cursor":
        return "cursor"
    if env.get("ARENA_SANDBOX") or env.get("E2B_SANDBOX"):
        return "arena"
    return None
