#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync this repository's skill into a local WorkBuddy skills directory.

One-way sync: repo -> local runtime.

Supported layouts
-----------------
flat (this repository)
    The repository root IS the skill root: ``SKILL.md``, ``references/`` and
    ``scripts/`` live at the top level.  The skill is installed as
    ``<target>/<name>``, where ``<name>`` is read from the ``name:`` field of
    the root ``SKILL.md`` (fallback: the repository folder name).

nested
    The repository contains ``skills/<name>/...`` sub-directories; every
    skill found there is synced to ``<target>/<name>``.

Behaviour
---------
* new / changed files are copied over (content comparison, not timestamps)
* stale files are removed
* protected local metadata (_user_meta.json, _icon.png, ...) is never touched
* repo-level files (README*.md, LICENSE, logo.png, this script) are never
  installed into the skills directory

Usage
-----
    py -3 scripts/sync_to_local.py                          # sync into ~/.workbuddy/skills
    py -3 scripts/sync_to_local.py --dry-run                # preview, do not write
    py -3 scripts/sync_to_local.py --target D:/path/skills  # custom skills directory
"""

import argparse
import filecmp
import os
import re
import shutil
import sys
from pathlib import Path

PROTECTED = {
    "_user_meta.json",
    "_skillhub_meta.json",
    "_meta.json",
    "_icon.png",
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
}

SKIP_DIRS = {"__pycache__", ".git"}

README_RE = re.compile(r"(?i)^readme(\..+)?\.md$")
REPO_LEVEL_NAMES = {"LICENSE", "logo.png"}
SYNC_SCRIPT_REL = "scripts/sync_to_local.py"

REPO_ROOT = Path(__file__).resolve().parent.parent
NESTED_ROOT = REPO_ROOT / "skills"


def default_target():
    return Path.home() / ".workbuddy" / "skills"


def repo_level(rel):
    """True for repository-only entries (rel is relative to the skill root)."""
    p = Path(rel)
    if len(p.parts) == 1:
        if (README_RE.match(p.name) or p.name in REPO_LEVEL_NAMES
                or p.name.startswith(".")):
            return True
    if p.parts and p.parts[0].startswith("."):
        return True
    if p.as_posix() == SYNC_SCRIPT_REL:
        return True
    return False


def flat_skill_name():
    """Skill name from the `name:` field of the root SKILL.md, else folder name."""
    skill_md = REPO_ROOT / "SKILL.md"
    if skill_md.is_file():
        in_frontmatter = False
        for line in skill_md.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.strip() == "---":
                if in_frontmatter:
                    break
                in_frontmatter = True
                continue
            if in_frontmatter:
                m = re.match(r"""\s*name\s*:\s*['"]?([A-Za-z0-9._-]+)['"]?\s*$""", line)
                if m:
                    return m.group(1)
    return REPO_ROOT.name


def discover_skills():
    """Return [(skill_name, skill_root, nested_layout)]."""
    if NESTED_ROOT.is_dir():
        names = sorted(p.name for p in NESTED_ROOT.iterdir() if p.is_dir())
        if names:
            return [(n, NESTED_ROOT / n, True) for n in names]
    if (REPO_ROOT / "SKILL.md").is_file():
        return [(flat_skill_name(), REPO_ROOT, False)]
    return []


def sync_skill(name, src_root, target, nested, dry_run):
    dst = target / name
    n_copy = n_rm = 0

    def skip(rel, fn):
        if fn in PROTECTED:
            return True
        if not nested and repo_level(Path(rel) / fn):
            return True
        return False

    for root, dirs, files in os.walk(src_root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        rel = Path(root).relative_to(src_root)
        for fn in sorted(files):
            if skip(rel, fn):
                continue
            src = Path(root) / fn
            df = dst / rel / fn
            if df.exists() and filecmp.cmp(src, df, shallow=False):
                continue
            n_copy += 1
            print("  [copy] %s/%s" % (name, rel / fn))
            if not dry_run:
                df.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, df)

    if dst.is_dir():
        for root, dirs, files in os.walk(dst):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
            rel = Path(root).relative_to(dst)
            for fn in sorted(files):
                if skip(rel, fn):
                    continue
                df = Path(root) / fn
                if not (src_root / rel / fn).exists():
                    n_rm += 1
                    print("  [remove] %s/%s" % (name, rel / fn))
                    if not dry_run:
                        try:
                            df.unlink()
                        except OSError as exc:
                            print("  ! could not remove: %s" % exc)

    print("%s: %d copied, %d removed" % (name, n_copy, n_rm))
    print("")
    return n_copy, n_rm


def main():
    parser = argparse.ArgumentParser(
        description="Sync this repository's skill into a local skills directory (repo -> local).")
    parser.add_argument("--target", default=None,
                        help="target skills directory (default: ~/.workbuddy/skills)")
    parser.add_argument("--dry-run", action="store_true",
                        help="show changes without writing")
    args = parser.parse_args()

    skills = discover_skills()
    if not skills:
        sys.exit("no skill found: expected SKILL.md at the repository root, "
                 "or skills/<name>/ sub-directories")

    target = Path(args.target).expanduser() if args.target else default_target()
    if not target.is_dir():
        sys.exit("target directory not found: %s (create it or pass --target)" % target)

    copied = removed = 0
    print("repo   : %s" % REPO_ROOT)
    print("layout : %s" % ("nested (skills/<name>/)" if skills[0][2]
                           else "flat (repo root = skill root)"))
    print("target : %s%s" % (target, " (dry-run)" if args.dry_run else ""))
    print("skills : %d" % len(skills))
    print("")

    for name, src_root, nested in skills:
        n_copy, n_rm = sync_skill(name, src_root, target, nested, args.dry_run)
        copied += n_copy
        removed += n_rm

    print("Done. copied=%d removed=%d%s" % (copied, removed,
          " (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
