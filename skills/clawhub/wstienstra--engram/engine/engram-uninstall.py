#!/usr/bin/env python3
"""
engram-uninstall.py — Full revert of Engram install.

Restores every file from .engram-backup/<ts>/manifest.json, removes crons
by marker comment, stops the daemon, archives engram.db to .engram-backup/.
Idempotent: safe to run multiple times.

Usage:
  python3 engram/engram-uninstall.py           # restore + archive
  python3 engram/engram-uninstall.py --purge   # also delete archived db
"""

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    import bpconfig
    _cfg = bpconfig.load_config()
    WORKSPACE = _cfg["workspace"]
    ENGRAM_DIR = _cfg["engram_dir"]
    DB_PATH = _cfg["db_path"]
    SOCK_PATH = _cfg["socket_path"]
    PID_PATH = _cfg["pid_path"]
    SCRIPTS_DIR = _cfg["scripts_dir"]
except Exception:
    ENGRAM_DIR = os.path.dirname(os.path.abspath(__file__))
    WORKSPACE = os.path.dirname(ENGRAM_DIR)
    DB_PATH = os.path.join(ENGRAM_DIR, "engram.db")
    SOCK_PATH = "/tmp/engram-serve.sock"
    PID_PATH = "/tmp/engram-serve.pid"
    SCRIPTS_DIR = os.path.join(WORKSPACE, "scripts")

BACKUP_ROOT = os.path.join(WORKSPACE, ".engram-backup")
CRON_MARKER = "# ENGRAM-MANAGED"


def find_earliest_backup():
    """Find the earliest backup directory with a manifest.json.
    The earliest backup contains the ORIGINAL pre-rewire files."""
    if not os.path.isdir(BACKUP_ROOT):
        return None
    candidates = []
    for name in os.listdir(BACKUP_ROOT):
        manifest = os.path.join(BACKUP_ROOT, name, "manifest.json")
        if os.path.isfile(manifest):
            candidates.append(name)
    if not candidates:
        return None
    candidates.sort()  # ascending — earliest first
    return os.path.join(BACKUP_ROOT, candidates[0])


def find_latest_backup():
    """Find the most recent backup directory with a manifest.json."""
    if not os.path.isdir(BACKUP_ROOT):
        return None
    candidates = []
    for name in os.listdir(BACKUP_ROOT):
        manifest = os.path.join(BACKUP_ROOT, name, "manifest.json")
        if os.path.isfile(manifest):
            candidates.append(name)
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return os.path.join(BACKUP_ROOT, candidates[0])


def stop_daemon():
    """Stop the engram-serve daemon if running."""
    stopped = False
    # Try via PID file
    if os.path.isfile(PID_PATH):
        try:
            with open(PID_PATH, 'r') as f:
                pid = int(f.read().strip())
            os.kill(pid, signal.SIGTERM)
            print(f"  Stopped daemon (PID {pid})")
            stopped = True
        except (ProcessLookupError, ValueError, OSError):
            pass
        try:
            os.remove(PID_PATH)
        except OSError:
            pass

    # Remove socket
    if os.path.exists(SOCK_PATH):
        try:
            os.remove(SOCK_PATH)
        except OSError:
            pass

    return stopped


def remove_crons():
    """Remove crontab entries marked with ENGRAM-MANAGED."""
    try:
        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
        if result.returncode != 0:
            print("  No crontab found (nothing to remove)")
            return 0

        current = result.stdout
        lines = current.split('\n')
        kept = []
        removed = 0
        for line in lines:
            if CRON_MARKER in line:
                removed += 1
            else:
                kept.append(line)

        if removed == 0:
            print("  No Engram crons found")
            return 0

        new_crontab = '\n'.join(kept)
        proc = subprocess.run(["crontab", "-"], input=new_crontab, capture_output=True, text=True)
        if proc.returncode == 0:
            print(f"  Removed {removed} cron line(s)")
        else:
            print(f"  ERROR removing crons: {proc.stderr}")
        return removed
    except FileNotFoundError:
        print("  crontab not available (nothing to remove)")
        return 0
    except Exception as e:
        print(f"  Error removing crons: {e}")
        return 0


def restore_files(backup_dir):
    """Restore files from manifest.json."""
    manifest_path = os.path.join(backup_dir, "manifest.json")
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"  ERROR reading manifest: {e}")
        return 0

    restored = 0
    files = manifest.get("files", {})
    for rel_path, backup_info in files.items():
        target = os.path.join(WORKSPACE, rel_path)
        backup_file = backup_info.get("backup_path", "")
        if backup_file and os.path.isfile(backup_file):
            try:
                os.makedirs(os.path.dirname(target), exist_ok=True)
                shutil.copy2(backup_file, target)
                print(f"  Restored: {rel_path}")
                restored += 1
            except OSError as e:
                print(f"  Failed to restore {rel_path}: {e}")
        else:
            print(f"  Skip (backup missing): {rel_path}")

    return restored


def archive_db(backup_dir, purge=False):
    """Archive engram.db to the backup directory."""
    if not os.path.isfile(DB_PATH):
        print("  engram.db not found (already removed?)")
        return

    if purge:
        try:
            os.remove(DB_PATH)
            print(f"  Purged: {DB_PATH}")
        except OSError as e:
            print(f"  Failed to purge: {e}")
        return

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_name = f"engram-{ts}.db"
    archive_path = os.path.join(backup_dir, archive_name)
    try:
        shutil.copy2(DB_PATH, archive_path)
        print(f"  Archived engram.db → {archive_path}")
    except OSError as e:
        print(f"  Failed to archive: {e}")


def remove_engram_dir():
    """Remove the engram/ directory (engine files)."""
    if not os.path.isdir(ENGRAM_DIR):
        return
    # Safety: only remove if it looks like an Engram directory
    marker = os.path.join(ENGRAM_DIR, "engram.json")
    if not os.path.isfile(marker):
        print(f"  Skip removing {ENGRAM_DIR} (no engram.json — not a Engram install)")
        return
    try:
        shutil.rmtree(ENGRAM_DIR)
        print(f"  Removed: {ENGRAM_DIR}")
    except OSError as e:
        print(f"  Failed to remove {ENGRAM_DIR}: {e}")


def remove_staged_scripts():
    """Remove Engram script files from scripts/ directory."""
    if not os.path.isdir(SCRIPTS_DIR):
        return
    engram_scripts = ["engram-backup.py", "engram-sleep.py", "engram-battery.py"]
    for fname in engram_scripts:
        fpath = os.path.join(SCRIPTS_DIR, fname)
        if os.path.isfile(fpath):
            try:
                os.remove(fpath)
                print(f"  Removed: scripts/{fname}")
            except OSError as e:
                print(f"  Failed to remove scripts/{fname}: {e}")
    # Remove scripts dir if empty
    try:
        remaining = os.listdir(SCRIPTS_DIR)
        if not remaining:
            os.rmdir(SCRIPTS_DIR)
            print(f"  Removed empty: {SCRIPTS_DIR}")
    except OSError:
        pass


def remove_migration_report():
    """Remove the migration report if present."""
    report_path = os.path.join(WORKSPACE, "migration-report.md")
    if os.path.isfile(report_path):
        try:
            os.remove(report_path)
            print(f"  Removed: migration-report.md")
        except OSError:
            pass


def main():
    parser = argparse.ArgumentParser(description="Uninstall Engram and restore workspace")
    parser.add_argument("--purge", action="store_true",
                        help="Also delete archived engram.db (no recovery)")
    args = parser.parse_args()

    print("Engram Uninstall")
    print("=" * 50)

    # 1. Stop daemon
    print("\n1. Stopping daemon...")
    stop_daemon()

    # 2. Remove crons
    print("\n2. Removing crons...")
    remove_crons()

    # 3. Find backup and restore (earliest = original pre-rewire files)
    print("\n3. Restoring files from backup...")
    restore_dir = find_earliest_backup()
    archive_dir = find_latest_backup()
    if restore_dir:
        print(f"  Restoring from: {restore_dir}")
        restore_files(restore_dir)
    else:
        print("  No backup found — nothing to restore")

    # 4. Archive or purge engram.db (to latest backup dir)
    print("\n4. Archiving engram.db...")
    if archive_dir:
        archive_db(archive_dir, purge=args.purge)
    else:
        print("  No backup dir to archive to")

    # 5. Remove engram/ directory (engine files)
    print("\n5. Removing engine files...")
    remove_engram_dir()

    # 6. Remove staged scripts and migration report
    print("\n6. Cleaning up staged files...")
    remove_staged_scripts()
    remove_migration_report()

    print("\n" + "=" * 50)
    print("Uninstall complete.")
    if not args.purge and archive_dir:
        print(f"  engram.db archived in: {archive_dir}")
        print("  Use --purge to delete archived db permanently.")
    print("  Workspace restored to pre-install state.")


if __name__ == "__main__":
    main()