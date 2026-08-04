#!/usr/bin/env python3
"""Ralph Loop — Iterative AI self-improvement loop.

Inspired by Geoffrey Huntley's Ralph Wiggum technique.
Implements persistent iteration: feed a prompt repeatedly until
a completion promise is detected or max iterations reached.

Usage:
    python ralph_loop.py start --prompt "task" --max-iterations 20 --promise "COMPLETE"
    python ralph_loop.py status
    python ralph_loop.py cancel
    python ralph_loop.py history
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# State file location
RALPH_STATE_DIR = Path(__file__).parent.parent / "memory" / "ralph"
RALPH_STATE_FILE = RALPH_STATE_DIR / "state.json"
RALPH_HISTORY_FILE = RALPH_STATE_DIR / "history.jsonl"


def ensure_dirs():
    RALPH_STATE_DIR.mkdir(parents=True, exist_ok=True)


def load_state() -> dict:
    if RALPH_STATE_FILE.exists():
        try:
            return json.loads(RALPH_STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return _default_state()
    return _default_state()


def _default_state() -> dict:
    return {
        "active": False,
        "prompt": "",
        "completion_promise": "COMPLETE",
        "max_iterations": 20,
        "current_iteration": 0,
        "started_at": None,
        "last_iteration_at": None,
        "results": [],
        "status": "idle",
    }


def save_state(state: dict):
    ensure_dirs()
    RALPH_STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def append_history(entry: dict):
    ensure_dirs()
    entry["timestamp"] = datetime.now().isoformat()
    with open(RALPH_HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def cmd_start(args):
    """Start a new Ralph Loop."""
    state = load_state()

    if state["active"]:
        print(json.dumps({
            "status": "error",
            "message": f"Ralph Loop already running (iteration {state['current_iteration']}/{state['max_iterations']}). Use 'cancel' first.",
            "state": state,
        }, ensure_ascii=False, indent=2))
        return

    # Initialize new loop
    state = {
        "active": True,
        "prompt": args.prompt,
        "completion_promise": args.promise or "COMPLETE",
        "max_iterations": args.max_iterations or 20,
        "current_iteration": 0,
        "started_at": datetime.now().isoformat(),
        "last_iteration_at": None,
        "results": [],
        "status": "running",
        "escape_plan": args.escape_plan or "",
    }
    save_state(state)

    append_history({
        "event": "loop_started",
        "prompt": args.prompt[:200],
        "max_iterations": state["max_iterations"],
        "completion_promise": state["completion_promise"],
    })

    # Output the first iteration prompt
    iteration_prompt = _build_iteration_prompt(state, 1)

    print(json.dumps({
        "status": "started",
        "message": f"Ralph Loop started. Max {state['max_iterations']} iterations. Promise: '{state['completion_promise']}'",
        "iteration": 1,
        "prompt": iteration_prompt,
        "state": {k: v for k, v in state.items() if k != "prompt"},
    }, ensure_ascii=False, indent=2))


def cmd_next(args):
    """Advance to next iteration (called after each iteration completes)."""
    state = load_state()

    if not state["active"]:
        print(json.dumps({
            "status": "error",
            "message": "No active Ralph Loop. Use 'start' to begin one.",
        }, ensure_ascii=False, indent=2))
        return

    # Record iteration result
    iteration_result = args.result or ""
    state["current_iteration"] += 1
    state["last_iteration_at"] = datetime.now().isoformat()
    state["results"].append({
        "iteration": state["current_iteration"],
        "result_summary": iteration_result[:500],
        "timestamp": datetime.now().isoformat(),
    })

    # Check completion
    promise_found = state["completion_promise"] in iteration_result

    if promise_found:
        # Loop complete!
        state["active"] = False
        state["status"] = "completed"
        save_state(state)

        append_history({
            "event": "loop_completed",
            "iteration": state["current_iteration"],
            "total_iterations": state["current_iteration"],
            "success": True,
        })

        print(json.dumps({
            "status": "completed",
            "message": f"✅ Ralph Loop completed after {state['current_iteration']} iterations. Completion promise found!",
            "iterations_used": state["current_iteration"],
            "max_iterations": state["max_iterations"],
        }, ensure_ascii=False, indent=2))
        return

    # Check max iterations
    if state["current_iteration"] >= state["max_iterations"]:
        state["active"] = False
        state["status"] = "max_iterations_reached"
        save_state(state)

        append_history({
            "event": "loop_max_iterations",
            "iteration": state["current_iteration"],
            "success": False,
        })

        escape_msg = ""
        if state.get("escape_plan"):
            escape_msg = f"\n\nEscape plan: {state['escape_plan']}"

        print(json.dumps({
            "status": "max_iterations_reached",
            "message": f"⚠️ Ralph Loop reached max iterations ({state['max_iterations']}) without completion.{escape_msg}",
            "iterations_used": state["current_iteration"],
            "summary": state["results"][-5:],  # Last 5 results for context
        }, ensure_ascii=False, indent=2))
        return

    # Continue to next iteration
    save_state(state)
    next_iter = state["current_iteration"] + 1
    iteration_prompt = _build_iteration_prompt(state, next_iter)

    append_history({
        "event": "iteration_completed",
        "iteration": state["current_iteration"],
        "continuing": True,
        "next_iteration": next_iter,
    })

    print(json.dumps({
        "status": "continuing",
        "message": f"Iteration {state['current_iteration']} complete. Continuing to iteration {next_iter}/{state['max_iterations']}.",
        "iteration": next_iter,
        "prompt": iteration_prompt,
    }, ensure_ascii=False, indent=2))


def cmd_status(args):
    """Show current Ralph Loop status."""
    state = load_state()

    print(json.dumps({
        "status": "ok",
        "active": state["active"],
        "current_iteration": state["current_iteration"],
        "max_iterations": state["max_iterations"],
        "completion_promise": state["completion_promise"],
        "started_at": state["started_at"],
        "last_iteration_at": state["last_iteration_at"],
        "loop_status": state["status"],
        "recent_results": state["results"][-3:] if state["results"] else [],
    }, ensure_ascii=False, indent=2))


def cmd_cancel(args):
    """Cancel active Ralph Loop."""
    state = load_state()

    if not state["active"]:
        print(json.dumps({
            "status": "ok",
            "message": "No active Ralph Loop to cancel.",
        }, ensure_ascii=False, indent=2))
        return

    state["active"] = False
    state["status"] = "cancelled"
    save_state(state)

    append_history({
        "event": "loop_cancelled",
        "iteration": state["current_iteration"],
    })

    print(json.dumps({
        "status": "cancelled",
        "message": f"Ralph Loop cancelled after {state['current_iteration']} iterations.",
    }, ensure_ascii=False, indent=2))


def cmd_history(args):
    """Show Ralph Loop history."""
    if not RALPH_HISTORY_FILE.exists():
        print(json.dumps({
            "status": "ok",
            "message": "No Ralph Loop history found.",
            "entries": [],
        }, ensure_ascii=False, indent=2))
        return

    entries = []
    with open(RALPH_HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    limit = args.limit or 20
    entries = entries[-limit:]

    print(json.dumps({
        "status": "ok",
        "total_entries": len(entries),
        "entries": entries,
    }, ensure_ascii=False, indent=2))


def _build_iteration_prompt(state: dict, iteration: int) -> str:
    """Build the prompt for a specific iteration."""
    max_iter = state["max_iterations"]
    promise = state["completion_promise"]
    prompt = state["prompt"]

    header = f"[Ralph Loop — Iteration {iteration}/{max_iter}]"

    if iteration == 1:
        return f"""{header}

## Task
{prompt}

## Instructions
1. Work on the task above
2. After completing work, check if the task is fully done
3. If complete, output: <promise>{promise}</promise>
4. If not complete, describe what was done and what remains
5. Focus on making measurable progress each iteration

Remember: Output <promise>{promise}</promise> ONLY when the task is truly complete."""

    else:
        return f"""{header}

## Original Task
{prompt}

## Previous Progress
Review files and git history to understand what was done in previous iterations.

## Instructions
1. Review what has been accomplished so far
2. Identify what still needs to be done
3. Continue working on remaining items
4. If ALL requirements are met, output: <promise>{promise}</promise>
5. If not complete, describe current progress and remaining work

Remember: Output <promise>{promise}</promise> ONLY when the task is truly complete."""


def main():
    parser = argparse.ArgumentParser(description="Ralph Loop — Iterative AI self-improvement")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # start
    p_start = subparsers.add_parser("start", help="Start a new Ralph Loop")
    p_start.add_argument("--prompt", required=True, help="Task prompt")
    p_start.add_argument("--max-iterations", type=int, default=20, help="Max iterations (default: 20)")
    p_start.add_argument("--promise", default="COMPLETE", help="Completion promise string (default: COMPLETE)")
    p_start.add_argument("--escape-plan", default="", help="What to do if max iterations reached")

    # next
    p_next = subparsers.add_parser("next", help="Advance to next iteration")
    p_next.add_argument("--result", default="", help="Result of current iteration")

    # status
    subparsers.add_parser("status", help="Show current status")

    # cancel
    subparsers.add_parser("cancel", help="Cancel active loop")

    # history
    p_history = subparsers.add_parser("history", help="Show loop history")
    p_history.add_argument("--limit", type=int, default=20, help="Max entries to show")

    args = parser.parse_args()

    if args.command == "start":
        cmd_start(args)
    elif args.command == "next":
        cmd_next(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "cancel":
        cmd_cancel(args)
    elif args.command == "history":
        cmd_history(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
