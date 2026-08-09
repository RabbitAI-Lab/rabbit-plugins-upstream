#!/usr/bin/env python3
"""
notify_closed_bottles — deterministic end-state notifier for the MIAB callback ledger.

Watches the append-only callback ledger (state/callbacks/ledger.jsonl, owned by
claw-callback.py) for events that mean a bottle has reached an END STATE:
`resolve`, `cancel`, or `fail`. For each one, it reconstructs that bottle's full
MIAB history from the ledger (every line whose `id` matches, in order) and posts
it as a single Discord message via `openclaw message send`.

Deliberately NOT an agentTurn / reactive cron hook. Per
docs/specs/miab-messaging-dedup-and-cron-sequencing.md (the incident that
produced the July 2026 double-posting/typo'd-channel bug), any LLM turn put in
the send path is the thing that produces duplicate or mistargeted delivery.
This script is pure stdlib + one subprocess call to a fixed CLI with a fixed
channel id; run it from a `--command` (non-agent) cron job, never an agentTurn.

Read-only over the ledger: never mutates ledger.jsonl or envelope files. The
only files it writes are its own state file (cursor + toggle).

Path resolution (mirrors interagent_queue.py's conventions):
  - CLAW_HOME              : broker root                 (default: ~/.openclaw)
  - CLAW_LEDGER            : explicit ledger path         (overrides CLAW_HOME/state/callbacks/ledger.jsonl)
  - CLAW_CLOSED_STATE      : explicit state-file path     (overrides CLAW_HOME/state/callbacks/closed_bottle_state.json)
  - CLAW_CLOSED_TARGET     : delivery target for `message send --target` (default: channel:1517433532518109195)
  - CLAW_CLOSED_ACCOUNT    : optional --account for `message send`
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

END_EVENTS = {"resolve", "cancel", "fail"}

# --------------------------------------------------------------------------- paths
def claw_home() -> Path:
    return Path(os.environ.get("CLAW_HOME", "~/.openclaw")).expanduser()

def ledger_file() -> Path:
    env = os.environ.get("CLAW_LEDGER")
    if env:
        return Path(env).expanduser()
    return claw_home() / "state" / "callbacks" / "ledger.jsonl"

def state_file() -> Path:
    env = os.environ.get("CLAW_CLOSED_STATE")
    if env:
        return Path(env).expanduser()
    return claw_home() / "state" / "callbacks" / "closed_bottle_state.json"

def target_channel() -> str:
    return os.environ.get("CLAW_CLOSED_TARGET", "channel:1517433532518109195")

def account_id() -> str | None:
    return os.environ.get("CLAW_CLOSED_ACCOUNT")

# --------------------------------------------------------------- agent identity map
AGENT_MAP = {
    "main": "✨ LYRA (Main)",
    "planner": "🥷⚔️ SPECTRE (Planner)",
    "coder": "💥 Cinder (Coder)",
    "reviewer": "🥷👁️ ECHO (Reviewer)",
    "debug": "🔬 Zero (Debug)",
    "utility": "🛠️ Swift (Utility)",
    "sigma": "⚡ SIGMA (Portfolio)",
    "free": "🌌 VOID (Scout)",
    "sweep": "🧹 Callback Reaper",
    "system": "⚙️ System",
}

def who(name):
    return AGENT_MAP.get(name, name or "Unknown")

END_ICON = {"resolve": "✅", "cancel": "❌", "fail": "⚠️"}
END_LABEL = {"resolve": "Resolved", "cancel": "Cancelled", "fail": "Failed/Reaped"}

# --------------------------------------------------------------------------- state
def load_state() -> dict:
    p = state_file()
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"enabled": True, "last_processed_line": 0}

def save_state(state: dict) -> None:
    p = state_file()
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
    tmp.replace(p)

# ----------------------------------------------------------------- summarization
def sanitize(text, limit=500):
    if not text:
        return ""
    lines = [l.strip() for l in str(text).split("\n") if l.strip()]
    cleaned = " ".join(" ".join(lines).split())
    if len(cleaned) > limit:
        return cleaned[: limit - 3] + "..."
    return cleaned

# ----------------------------------------------------------------- history render
def render_step(rec):
    """One ledger record for a bottle -> one short history line."""
    event = rec.get("event")
    by = who(rec.get("by"))
    if event == "create":
        return f"📥 created by {by} -> {who(rec.get('to'))}"
    if event == "forward":
        return f"➡️ forwarded by {by} -> {who(rec.get('to'))}"
    if event == "return":
        return f"↩️ returned by {by}, waking {who(rec.get('wake'))}"
    if event == "resolve":
        return f"✅ resolved by {by}"
    if event == "cancel":
        return f"❌ cancelled by {by}" + (f" ({rec.get('reason')})" if rec.get("reason") else "")
    if event == "fail":
        return f"⚠️ failed/reaped by {by}" + (f" ({rec.get('reason')})" if rec.get("reason") else "")
    if event == "corrupt":
        return f"🗑️ quarantined ({rec.get('reason', 'corrupt envelope')})"
    return f"{event} by {by}"

def load_all_lines():
    lf = ledger_file()
    if not lf.exists():
        return []
    with lf.open("r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]

def format_closed_bottle(cid: str, all_records: list, end_rec: dict) -> str:
    """Build the full-history report message for one just-closed bottle."""
    bottle_records = [r for r in all_records if r.get("id") == cid]
    create_rec = next((r for r in bottle_records if r.get("event") == "create"), None)
    task = sanitize(end_rec.get("task") or (create_rec or {}).get("task", ""), limit=300)
    end_event = end_rec.get("event")
    icon = END_ICON.get(end_event, "🔔")
    label = END_LABEL.get(end_event, end_event)

    lines = [f"{icon} [MIAB Bottle {label}] {cid}"]
    if task:
        lines.append(f"   Task: {task}")
    if end_event == "resolve" and end_rec.get("result"):
        lines.append(f"   Result: {sanitize(end_rec.get('result'), limit=400)}")
    if end_event == "cancel" and end_rec.get("reason"):
        lines.append(f"   Reason: {end_rec.get('reason')}")
    if end_event == "fail" and end_rec.get("reason"):
        lines.append(f"   Reason: {end_rec.get('reason')}")
    lines.append(f"   Hops: {len(bottle_records)}")
    lines.append("   History:")
    for r in bottle_records:
        lines.append(f"     - {render_step(r)}")
    return "\n".join(lines)

# ----------------------------------------------------------------- collection
def collect_new(state, advance):
    """Scan the ledger from the cursor for new end-state events; for each,
    render the full-history message using ALL records for that bottle id
    (not just the ones after the cursor). Returns (messages, status, new_cursor)."""
    lines = load_all_lines()
    total = len(lines)
    cursor = state.get("last_processed_line", 0)
    if cursor > total:
        cursor = 0
    if cursor >= total:
        return [], "No new callback events.", total

    all_records = []
    for l in lines:
        try:
            all_records.append(json.loads(l))
        except Exception:
            all_records.append({})

    messages = []
    for rec in all_records[cursor:]:
        if rec.get("event") in END_EVENTS and rec.get("id"):
            messages.append(format_closed_bottle(rec["id"], all_records, rec))

    new_cursor = total if advance else cursor
    status = f"Scanned {total - cursor} new ledger line(s), found {len(messages)} closed bottle(s)."
    return messages, status, new_cursor

# ----------------------------------------------------------------- delivery
def deliver_one(message: str) -> bool:
    """Deterministic delivery: shell out to `openclaw message send`. No LLM
    in this path. Returns True on success."""
    cmd = ["openclaw", "message", "send", "--channel", "discord",
           "--target", target_channel(), "--message", message]
    acct = account_id()
    if acct:
        cmd += ["--account", acct]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"delivery failed (exit {result.returncode}): {result.stderr.strip()}", file=sys.stderr)
            return False
        return True
    except Exception as e:
        print(f"delivery failed: {e}", file=sys.stderr)
        return False

# --------------------------------------------------------------------------- main
def main():
    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "process"
    state = load_state()

    if cmd == "on":
        state["enabled"] = True
        save_state(state)
        print(json.dumps({"enabled": True, "status": "ON", "target": target_channel()}))
        return

    if cmd == "off":
        state["enabled"] = False
        save_state(state)
        print(json.dumps({"enabled": False, "status": "OFF"}))
        return

    if cmd == "status":
        print(json.dumps({
            "enabled": state.get("enabled", True),
            "status": "ON" if state.get("enabled", True) else "OFF",
            "last_processed_line": state.get("last_processed_line", 0),
            "ledger": str(ledger_file()),
            "state_file": str(state_file()),
            "target": target_channel(),
        }, indent=2))
        return

    if cmd == "peek":
        messages, status, _ = collect_new(state, advance=False)
        print(json.dumps({"messages": messages, "status": status, "delivered": False}, indent=2))
        return

    if cmd == "process":
        if not state.get("enabled", True):
            print(json.dumps({"messages": [], "status": "Notifier DISABLED — skipping sweep.", "delivered": False}))
            return
        lines = load_all_lines()
        total = len(lines)
        cursor = state.get("last_processed_line", 0)
        if cursor > total:
            cursor = 0
        if cursor >= total:
            print(json.dumps({"messages": [], "status": "No new callback events.", "delivered": True}))
            return

        all_records = []
        for l in lines:
            try:
                all_records.append(json.loads(l))
            except Exception:
                all_records.append({})

        delivered_msgs = []
        # Deliver in order; stop advancing the cursor at the first delivery
        # failure so nothing is skipped on the next run (at-least-once,
        # exactly-once in the common case).
        new_cursor = total
        for i, rec in enumerate(all_records[cursor:], start=cursor):
            if rec.get("event") in END_EVENTS and rec.get("id"):
                msg = format_closed_bottle(rec["id"], all_records, rec)
                if deliver_one(msg):
                    delivered_msgs.append(msg)
                else:
                    new_cursor = i
                    break

        state["last_processed_line"] = new_cursor
        save_state(state)
        print(json.dumps({
            "messages": delivered_msgs,
            "status": f"Delivered {len(delivered_msgs)} closed-bottle report(s); cursor now {new_cursor}/{total}.",
            "delivered": True,
        }, indent=2))
        return

    print(json.dumps({"ok": False, "error": f"unknown command: {cmd}",
                      "commands": ["on", "off", "status", "process", "peek"]}), file=sys.stderr)
    sys.exit(2)

if __name__ == "__main__":
    main()
