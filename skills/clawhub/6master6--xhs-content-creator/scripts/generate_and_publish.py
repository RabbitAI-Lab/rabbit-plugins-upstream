#!/usr/bin/env python3
"""xhs-content-creator end-to-end entry point.

Two modes:
  Generation (default): assembles a my_content.json under runtime/ from
    --image/--title/--body/--topic flags, then shells out to the local
    run_with_xvfb.sh → publish_xhs.py pipeline.
  Reuse (--content-path): skips image staging + JSON writing, hands an
    existing my_content.json straight to the publisher. Used for the
    two-step draft→publish workflow (SKILL.md §1).

Self-contained: all paths derive from this script's location.

This script intentionally does NOT generate content. The calling agent
analyzes the images and produces the title/body/topics.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


# Skill root = parent of scripts/. All paths derive from here so the skill is
# fully self-contained and relocatable.
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

INBOUND_DIR = PROJECT_ROOT / "runtime" / "inbound"
RUN_SCRIPT = PROJECT_ROOT / "deploy" / "run_with_xvfb.sh"
CONTENT_JSON = PROJECT_ROOT / "runtime" / "my_content.json"


# publish_xhs.py exit codes (see scripts/publish_xhs.py main()):
#   0 = ok (published or draft_ready)
#   1 = run_failed (general / network / Playwright) — usually transient
#   2 = content_invalid (validation failure) — won't change on retry
#   3 = duplicate_blocked (DuplicateGuard raised) — won't change on retry
RETRYABLE_EXIT_CODES = {1}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate my_content.json and run local xhs publisher.")
    parser.add_argument("--image", action="append", default=[], dest="images",
                        help="Path to an image file (generation mode). Repeat for multiple images.")
    parser.add_argument("--title", default=None, help="Note title (must be <=20 chars per XHS rules).")
    parser.add_argument("--body", default=None, help="Note body. Use \\n\\n to separate paragraphs.")
    parser.add_argument("--topic", action="append", default=[], dest="topics",
                        help="A hashtag/topic. Repeat for multiple topics.")
    parser.add_argument("--mode", choices=["draft", "publish"], default="draft",
                        help="publisher mode (default: draft).")
    parser.add_argument("--inbound-prefix", default=None,
                        help="Filename prefix inside runtime/inbound/. Defaults to a timestamp slug.")
    parser.add_argument("--content-path", default=None,
                        help="Reuse an existing my_content.json (reuse mode). Skips stage_images "
                             "and write_content_json. Use this for the two-step draft→publish workflow.")
    parser.add_argument("--retry-on-fail", type=int, default=1,
                        help="Retry count when publisher exits with a retryable code (default: 1).")
    parser.add_argument("--retry-delay-seconds", type=int, default=5,
                        help="Seconds to wait between retries (default: 5).")
    return parser.parse_args()


def stage_images(images: list[str], prefix: str) -> list[str]:
    INBOUND_DIR.mkdir(parents=True, exist_ok=True)
    staged: list[str] = []
    for idx, src in enumerate(images, start=1):
        src_path = Path(src).expanduser().resolve()
        if not src_path.is_file():
            raise FileNotFoundError(f"image not found: {src}")
        suffix = src_path.suffix.lower() or ".jpg"
        dst = INBOUND_DIR / f"{prefix}_{idx:02d}{suffix}"
        shutil.copy2(src_path, dst)
        # content_validator (src/content_validator.py) resolves relative image
        # paths against the my_content.json file's parent directory
        # (PROJECT_ROOT/runtime/), so emit "inbound/<filename>" instead of
        # "runtime/inbound/<filename>" to avoid the duplicated runtime segment.
        rel = dst.relative_to(CONTENT_JSON.parent)
        staged.append(str(rel))
    return staged


def write_content_json(payload: dict) -> None:
    if CONTENT_JSON.exists():
        backup = CONTENT_JSON.with_suffix(
            f".json.bak.{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        )
        shutil.copy2(CONTENT_JSON, backup)
    CONTENT_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def run_publisher(content_json: Path, mode: str) -> dict:
    # Forward mode explicitly so the bash wrapper does not need to read .env.
    env_overrides: dict[str, str] = {"MODE": mode}
    return _invoke_publisher(content_json, env_overrides)


def _invoke_publisher(content_json: Path, env_overrides: dict[str, str]) -> dict:
    cmd = [str(RUN_SCRIPT), str(content_json)]
    proc = subprocess.run(
        cmd,
        cwd=str(PROJECT_ROOT),
        env={**__import__("os").environ, **env_overrides},
        capture_output=True,
        text=True,
        timeout=600,
        check=False,
    )
    last_json: dict | None = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                last_json = json.loads(line)
            except json.JSONDecodeError:
                continue
    return {
        "returncode": proc.returncode,
        "last_json": last_json,
        "stdout_tail": proc.stdout.splitlines()[-5:],
        "stderr_tail": proc.stderr.splitlines()[-5:],
    }


def run_publisher_with_retry(
    content_json: Path,
    mode: str,
    retry_count: int,
    retry_delay: int,
) -> tuple[dict, int]:
    """Run publisher with bounded retries on transient failures.

    Returns (final_result, attempts_used). attempts_used is 1-based.
    Only exit codes listed in RETRYABLE_EXIT_CODES are retried; the rest
    (e.g. validation failures, duplicate blocks) fail fast because retrying
    would just reproduce the same non-transient error.
    """
    attempts = 0
    result: dict | None = None
    while attempts <= retry_count:
        attempts += 1
        result = run_publisher(content_json, mode)
        if result["returncode"] == 0:
            return result, attempts
        if result["returncode"] not in RETRYABLE_EXIT_CODES or attempts > retry_count:
            return result, attempts
        # Sleep before the next attempt.
        if retry_delay > 0:
            time.sleep(retry_delay)
    return result, attempts  # type: ignore[return-value]


def title_len_xhs(title: str) -> int:
    """Per SKILL.md §1.5: emoji weight 2 chars, everything else weight 1."""
    n = 0
    for c in title:
        cp = ord(c)
        if 0x1F300 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x27BF:
            n += 2
        else:
            n += 1
    return n


def emit_error(status: str, error: str, **extra) -> None:
    payload = {"status": status, "error": error}
    payload.update(extra)
    print(json.dumps(payload, ensure_ascii=False), file=sys.stdout)


def main() -> int:
    args = parse_args()

    # ----- Resolve content source (reuse vs generation) ----------------------
    if args.content_path:
        # Reuse mode: skip stage_images + write_content_json.
        content_path = Path(args.content_path).expanduser().resolve()
        if not content_path.exists():
            emit_error("error", f"--content-path not found: {content_path}")
            return 3
        try:
            payload = json.loads(content_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            emit_error("error", f"--content-path is not valid JSON: {exc}")
            return 3
        for required in ("title", "body", "topics", "images"):
            if required not in payload:
                emit_error("error", f"--content-path JSON missing required field: {required}")
                return 3
        staged_paths = list(payload.get("images", []))
    else:
        # Generation mode.
        if not args.images:
            emit_error("error", "missing --image (or pass --content-path for reuse mode)")
            return 2
        if not args.title or not args.body:
            emit_error("error", "missing --title and/or --body (or pass --content-path for reuse mode)")
            return 2
        if len(args.images) > 9:
            emit_error("error", "too many images (>9)", count=len(args.images))
            return 2
        n_title = title_len_xhs(args.title)
        if n_title > 20:
            emit_error("error",
                       f"title too long for xhs (got {n_title} chars, max 20)",
                       title=args.title)
            return 2
        prefix = args.inbound_prefix or datetime.now().strftime("xhs_%Y%m%d_%H%M%S")
        try:
            staged_paths = stage_images(args.images, prefix)
        except FileNotFoundError as exc:
            emit_error("error", str(exc))
            return 3
        payload = {
            "title": args.title,
            "body": args.body,
            "topics": args.topics,
            "images": staged_paths,
            "mode": args.mode,
        }
        try:
            write_content_json(payload)
        except OSError as exc:
            emit_error("error", f"write_content_json failed: {exc}")
            return 3
        content_path = CONTENT_JSON

    # ----- Run publisher with retry ------------------------------------------
    publisher_result, attempts = run_publisher_with_retry(
        content_path,
        args.mode,
        args.retry_on_fail,
        args.retry_delay_seconds,
    )

    final = {
        "status": "ok" if publisher_result["returncode"] == 0 else "publisher_failed",
        "mode": args.mode,
        "content_json": str(content_path),
        "images": staged_paths,
        "publisher": publisher_result,
        "retry_attempts": attempts,
        "reuse_mode": bool(args.content_path),
    }
    if publisher_result["last_json"]:
        final["publisher_status"] = publisher_result["last_json"].get("status")
        final["publisher_run_id"] = (
            Path(publisher_result["last_json"].get("run_dir", "")).name
            if publisher_result["last_json"].get("run_dir")
            else None
        )
        final["publisher_fingerprint"] = publisher_result["last_json"].get("fingerprint")
    print(json.dumps(final, ensure_ascii=False))
    return publisher_result["returncode"]


if __name__ == "__main__":
    raise SystemExit(main())