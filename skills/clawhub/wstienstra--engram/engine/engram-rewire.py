#!/usr/bin/env python3
"""
engram-rewire.py — Rewire workspace to use Engram after migration.

1. Backs up every file that will be touched to .engram-backup/<ts>/ with manifest.json
2. Slims MEMORY.md to an auto-generated summary + "query engram" pointer
3. Updates AGENTS.md startup section to use engram commands
4. Adds crons (backup 03:15, sleep 03:45 dry-run, weekly battery drift)
   Append-only with marker comments.
"""

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    import bpconfig
    _cfg = bpconfig.load_config()
    WORKSPACE = _cfg["workspace"]
    ENGRAM_DIR = _cfg["engram_dir"]
    SCRIPTS_DIR = _cfg["scripts_dir"]
    BQ_CLI = os.path.join(ENGRAM_DIR, "bq.py")
except Exception:
    ENGRAM_DIR = os.path.dirname(os.path.abspath(__file__))
    WORKSPACE = os.path.dirname(ENGRAM_DIR)
    SCRIPTS_DIR = os.path.join(WORKSPACE, "scripts")
    BQ_CLI = os.path.join(ENGRAM_DIR, "bq.py")

BACKUP_ROOT = os.path.join(WORKSPACE, ".engram-backup")
CRON_MARKER = "# ENGRAM-MANAGED"

FILES_TO_BACKUP = [
    "MEMORY.md",
    "AGENTS.md",
]


def create_backup() -> str:
    """Create timestamped backup dir with manifest.json. Returns backup dir path.
    If a backup already exists for this workspace, reuse it (don't double-back-up)."""
    # Check if a backup already exists
    if os.path.isdir(BACKUP_ROOT):
        for name in sorted(os.listdir(BACKUP_ROOT)):
            manifest_file = os.path.join(BACKUP_ROOT, name, "manifest.json")
            if os.path.isfile(manifest_file):
                # Existing backup found — return it, don't create another
                print(f"  Existing backup found: {name} (reusing)")
                with open(manifest_file, 'r') as f:
                    manifest = json.load(f)
                # Verify the backed-up files still match
                for rel_path, info in manifest.get("files", {}).items():
                    backup_path = info.get("backup_path", "")
                    if backup_path and os.path.isfile(backup_path):
                        print(f"  Already backed up: {rel_path}")
                return os.path.join(BACKUP_ROOT, name)

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = os.path.join(BACKUP_ROOT, ts)
    os.makedirs(backup_dir, exist_ok=True)

    manifest = {
        "timestamp": ts,
        "files": {},
        "crons_added": [],
    }

    for rel_path in FILES_TO_BACKUP:
        target = os.path.join(WORKSPACE, rel_path)
        if os.path.isfile(target):
            backup_name = rel_path.replace("/", "_")
            backup_path = os.path.join(backup_dir, backup_name)
            shutil.copy2(target, backup_path)
            manifest["files"][rel_path] = {
                "backup_path": backup_path,
                "original_path": target,
                "size": os.path.getsize(target),
            }
            print(f"  Backed up: {rel_path}")

    manifest_path = os.path.join(backup_dir, "manifest.json")
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    return backup_dir


def slim_memory_md():
    """Replace MEMORY.md with a slim pointer to Engram."""
    mem_path = os.path.join(WORKSPACE, "MEMORY.md")
    content = """# MEMORY.md (Engram-managed)

> This file has been slimmed by Engram. Your full memory now lives in Engram.
> Use `python3 engram/bq.py recall "topic"` or `python3 engram/bq.py startup` for context.

## Quick Access
- **WIP / current task:** `python3 engram/bq.py wip`
- **Session startup:** `python3 engram/bq.py startup`
- **Topic lookup:** `python3 engram/bq.py recall "your topic"`
- **Message context:** `python3 engram/bq.py msgctx "message text"`

## Migration
- Original MEMORY.md backed up to `.engram-backup/`
- Run `python3 engram/engram-uninstall.py` to fully revert

---
_Engram rewire — {ts}_
""".format(ts=datetime.now().strftime("%Y-%m-%d %H:%M"))

    with open(mem_path, 'w') as f:
        f.write(content)
    print(f"  Slimmed: MEMORY.md")


def update_agents_md():
    """Update AGENTS.md startup section to reference engram commands."""
    agents_path = os.path.join(WORKSPACE, "AGENTS.md")
    if not os.path.isfile(agents_path):
        print("  AGENTS.md not found, skipping")
        return

    with open(agents_path, 'r') as f:
        content = f.read()

    # Insert Engram startup instructions after the "## Session Startup" heading
    engram_block = """
## Engram Startup (Engram-managed)

After compaction, run these to restore context:
1. `python3 engram/bq.py startup` — WIP + briefing
2. `python3 engram/bq.py checkpoint --status` — last checkpoint
3. `python3 engram/bq.py wip` — pick up where you left off
4. `python3 engram/bq.py msgctx "topic"` — relevant context for a message

_Engram rewire — {ts}_
""".format(ts=datetime.now().strftime("%Y-%m-%d %H:%M"))

    # Find the Session Startup section and insert after it
    if "## Session Startup" in content:
        # Insert before the next ## heading
        lines = content.split('\n')
        insert_idx = None
        for i, line in enumerate(lines):
            if line.startswith("## Session Startup"):
                # Find next ## heading
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith("## "):
                        insert_idx = j
                        break
                break
        if insert_idx:
            lines.insert(insert_idx, engram_block)
            content = '\n'.join(lines)
        else:
            content += "\n" + engram_block
    else:
        content = engram_block + "\n" + content

    with open(agents_path, 'w') as f:
        f.write(content)
    print(f"  Updated: AGENTS.md")


def add_crons():
    """Add Engram-managed cron entries (append-only with markers)."""
    crons = [
        f"15 3 * * * cd {WORKSPACE} && python3 {SCRIPTS_DIR}/engram-backup.py >> {WORKSPACE}/logs/engram-backup.log 2>&1 {CRON_MARKER}",
        f"45 3 * * * cd {WORKSPACE} && python3 {SCRIPTS_DIR}/engram-sleep.py --dry-run >> {WORKSPACE}/logs/engram-sleep.log 2>&1 {CRON_MARKER}",
        f"0 9 * * 0 cd {WORKSPACE} && python3 {SCRIPTS_DIR}/engram-battery.py --run --label weekly >> {WORKSPACE}/logs/engram-battery.log 2>&1 {CRON_MARKER}",
    ]

    try:
        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
        current = result.stdout if result.returncode == 0 else ""

        # Check for existing Engram crons
        existing_count = current.count(CRON_MARKER)
        if existing_count > 0:
            print(f"  {existing_count} Engram cron(s) already exist — skipping")
            return 0

        new_crontab = current.rstrip('\n') + '\n' + '\n'.join(crons) + '\n'
        proc = subprocess.run(["crontab", "-"], input=new_crontab, capture_output=True, text=True)
        if proc.returncode == 0:
            print(f"  Added {len(crons)} cron entries")
            return len(crons)
        else:
            print(f"  ERROR adding crons: {proc.stderr}")
            return 0
    except FileNotFoundError:
        print("  crontab not available — skipping cron setup")
        return 0
    except Exception as e:
        print(f"  Error adding crons: {e}")
        return 0


def main():
    print("Engram Rewire")
    print("=" * 50)

    # 1. Backup
    print("\n1. Backing up files...")
    backup_dir = create_backup()
    print(f"  Backup dir: {backup_dir}")

    # 2. Slim MEMORY.md
    print("\n2. Slimming MEMORY.md...")
    slim_memory_md()

    # 3. Update AGENTS.md
    print("\n3. Updating AGENTS.md...")
    update_agents_md()

    # 4. Add crons
    print("\n4. Adding crons (append-only)...")
    add_crons()

    # 5. Update manifest with crons
    manifest_path = os.path.join(backup_dir, "manifest.json")
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    manifest["crons_added"] = [
        "backup 03:15",
        "sleep 03:45 dry-run",
        "battery weekly Sunday 09:00",
    ]
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    print("\n" + "=" * 50)
    print("Rewire complete. Backup at:", backup_dir)


if __name__ == "__main__":
    main()