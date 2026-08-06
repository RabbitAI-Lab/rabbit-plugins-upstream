#!/usr/bin/env python3
"""Download the latest Dict-Sqlite.db from i18n-Dict-Extender releases.

This script fetches the pre-built SQLite dictionary database from the
VM-Chinese-translate-group/i18n-Dict-Extender GitHub repository, which is
auto-updated weekly with translations from CFPA + community mod sources.

Usage:
    python3 fetch_dict.py              # Download to scripts/Dict-Sqlite.db
    python3 fetch_dict.py --force      # Force re-download even if up-to-date
    python3 fetch_dict.py --check      # Only check for updates, don't download
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

REPO = "VM-Chinese-translate-group/i18n-Dict-Extender"
ASSET_NAME = "Dict-Sqlite.db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Dict-Sqlite.db")

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def get_latest_release():
    """Query GitHub API for the latest release info."""
    url = f"https://api.github.com/repos/{REPO}/releases/latest"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "mc-mod-translate-skill",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    tag = data.get("tag_name", "")
    published = data.get("published_at", "")
    assets = data.get("assets", [])

    asset = None
    for a in assets:
        if a.get("name") == ASSET_NAME:
            asset = a
            break

    if not asset:
        print("ERROR: Dict-Sqlite.db asset not found in latest release.", file=sys.stderr)
        sys.exit(1)

    return {
        "tag": tag,
        "published": published,
        "download_url": asset["browser_download_url"],
        "size": asset["size"],
        "digest": asset.get("digest", ""),
    }


def get_local_size():
    """Get the size of the existing DB file, or 0 if it doesn't exist."""
    if os.path.exists(DB_PATH):
        return os.path.getsize(DB_PATH)
    return 0


def download(url, dest_path, expected_size):
    """Download a file with progress indication."""
    print(f"Downloading {ASSET_NAME} ({expected_size / 1024 / 1024:.1f} MB)...")

    req = urllib.request.Request(url, headers={
        "User-Agent": "mc-mod-translate-skill",
    })

    with urllib.request.urlopen(req, timeout=300) as resp:
        total = int(resp.headers.get("Content-Length", expected_size))
        downloaded = 0
        chunk_size = 1024 * 256  # 256 KB chunks

        with open(dest_path + ".tmp", "wb") as f:
            while True:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)
                pct = downloaded * 100 // total if total else 0
                print(f"\r  {downloaded / 1024 / 1024:.1f} / {total / 1024 / 1024:.1f} MB ({pct}%)", end="", flush=True)

        print()

    # Verify size
    actual_size = os.path.getsize(dest_path + ".tmp")
    if actual_size != expected_size:
        print(f"WARNING: Downloaded size ({actual_size}) != expected ({expected_size})", file=sys.stderr)

    # Atomic rename
    os.replace(dest_path + ".tmp", dest_path)
    print(f"Saved to: {dest_path}")


def main():
    p = argparse.ArgumentParser(description="Download latest Dict-Sqlite.db from i18n-Dict-Extender")
    p.add_argument("--force", action="store_true", help="Force re-download even if up-to-date")
    p.add_argument("--check", action="store_true", help="Only check for updates, don't download")
    p.add_argument("--output", default=DB_PATH, help=f"Output path (default: {DB_PATH})")
    args = p.parse_args()

    dest = args.output

    print(f"Checking latest release from {REPO}...")
    info = get_latest_release()
    print(f"  Tag:      {info['tag']}")
    print(f"  Published: {info['published']}")
    print(f"  Size:     {info['size'] / 1024 / 1024:.1f} MB")

    local_size = os.path.getsize(dest) if os.path.exists(dest) else 0
    print(f"  Local:    {local_size / 1024 / 1024:.1f} MB" if local_size else "  Local:    not downloaded")

    if args.check:
        if local_size == info["size"]:
            print("\nStatus: UP-TO-DATE")
        else:
            print(f"\nStatus: UPDATE AVAILABLE (local: {local_size}, remote: {info['size']})")
        return

    if local_size == info["size"] and not args.force:
        print("\nAlready up-to-date. Use --force to re-download.")
        return

    download(info["download_url"], dest, info["size"])
    print(f"\nDone. Database ready at: {dest}")


if __name__ == "__main__":
    main()
