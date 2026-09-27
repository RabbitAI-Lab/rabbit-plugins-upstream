#!/usr/bin/env python3
"""
engram-backup.py — Nightly safe backup of engram/engram.db.

Uses sqlite3's online .backup() API, which is safe to run against a live
WAL-mode database (no need to stop writers). The resulting copy is gzipped
and verified (PRAGMA integrity_check + a sanity row count) before the script
declares success.

Retention:
  - Keep the last 7 daily backups (by date encoded in filename).
  - Additionally keep any backup made on a Sunday for 28 days.
  - Delete anything older than that, but ONLY files matching engram-*.db.gz
    in the backup directory — nothing else is ever touched.

Usage:
  python3 scripts/engram-backup.py

Exit codes:
  0 - success
  1 - backup failed verification (integrity check failed or empty nodes table)
"""

import gzip
import os
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timedelta

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Engram: load paths from config
try:
    import bpconfig
    _cfg = bpconfig.load_config()
    ENGRAM_DB = _cfg["db_path"]
    BACKUP_DIR = _cfg["backups_dir"]
except Exception:
    ENGRAM_DB = os.path.join(WORKSPACE, "engram", "engram.db")
    BACKUP_DIR = os.path.join(WORKSPACE, "backups", "engram")

DAILY_RETENTION_DAYS = 7
SUNDAY_RETENTION_DAYS = 28


def make_backup():
    """Backup engram.db via the sqlite3 .backup() API, then gzip it.

    Returns the path to the final .db.gz file.
    """
    os.makedirs(BACKUP_DIR, exist_ok=True)

    now = datetime.now()
    date_str = now.strftime("%Y%m%d")
    final_path = os.path.join(BACKUP_DIR, f"engram-{date_str}.db.gz")

    fd, tmp_path = tempfile.mkstemp(prefix="engram-backup-", suffix=".db", dir=BACKUP_DIR)
    os.close(fd)

    try:
        src = sqlite3.connect(f"file:{ENGRAM_DB}?mode=ro", uri=True)
        dst = sqlite3.connect(tmp_path)
        try:
            with dst:
                src.backup(dst)
        finally:
            dst.close()
            src.close()

        # gzip the temp db file straight to the final destination
        tmp_gz = final_path + ".tmp"
        with open(tmp_path, "rb") as f_in, gzip.open(tmp_gz, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        os.replace(tmp_gz, final_path)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return final_path


def verify_backup(gz_path):
    """Decompress to a temp file and run integrity_check + a node count.

    Returns (integrity_result, node_count).
    """
    fd, tmp_path = tempfile.mkstemp(prefix="engram-verify-", suffix=".db", dir=BACKUP_DIR)
    os.close(fd)
    try:
        with gzip.open(gz_path, "rb") as f_in, open(tmp_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

        conn = sqlite3.connect(tmp_path)
        try:
            integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
            count = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
        finally:
            conn.close()
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return integrity, count


def parse_backup_date(fname):
    """Extract the YYYYMMDD date from a engram-YYYYMMDD.db.gz filename."""
    try:
        stem = fname[len("engram-"):-len(".db.gz")]
        return datetime.strptime(stem, "%Y%m%d")
    except (ValueError, IndexError):
        return None


def apply_retention():
    """Delete old backups per the retention policy.

    Only touches files matching engram-*.db.gz in BACKUP_DIR.
    """
    now = datetime.now()
    daily_cutoff = now - timedelta(days=DAILY_RETENTION_DAYS)
    sunday_cutoff = now - timedelta(days=SUNDAY_RETENTION_DAYS)

    candidates = []
    for fname in os.listdir(BACKUP_DIR):
        if not (fname.startswith("engram-") and fname.endswith(".db.gz")):
            continue
        fdate = parse_backup_date(fname)
        if fdate is None:
            continue
        candidates.append((fname, fdate))

    removed = []
    for fname, fdate in candidates:
        is_sunday = fdate.weekday() == 6  # Monday=0 ... Sunday=6
        if is_sunday:
            keep = fdate >= sunday_cutoff
        else:
            keep = fdate >= daily_cutoff
        if not keep:
            path = os.path.join(BACKUP_DIR, fname)
            os.remove(path)
            removed.append(fname)

    return removed


def main():
    print(f"[{datetime.now().isoformat()}] Starting engram.db backup...")

    if not os.path.exists(ENGRAM_DB):
        print(f"ERROR: source database not found: {ENGRAM_DB}")
        return 1

    gz_path = make_backup()
    size_bytes = os.path.getsize(gz_path)
    print(f"Backup written: {gz_path} ({size_bytes:,} bytes)")

    integrity, count = verify_backup(gz_path)
    print(f"PRAGMA integrity_check: {integrity}")
    print(f"SELECT COUNT(*) FROM nodes: {count}")

    if integrity != "ok" or count == 0:
        print("FAIL: backup verification failed (integrity not ok or zero nodes)")
        return 1

    removed = apply_retention()
    if removed:
        print(f"Retention: removed {len(removed)} old backup(s): {', '.join(sorted(removed))}")
    else:
        print("Retention: nothing to remove")

    print("Backup completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
