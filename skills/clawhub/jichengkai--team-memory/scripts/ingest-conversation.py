#!/usr/bin/env python3
"""Capture original transcripts and apply skill-produced classification JSON."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from conversation_ingestion import ConversationError, apply_source, attempt_backup, capture_source
from team_memory_paths import TeamMemoryPathError, print_warnings, resolve_paths, run_with_write_lock


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="保存谈话原文并幂等提交 skill 生成的结构化拆解。")
    parser.add_argument("--skill-dir", default=None)
    subparsers = parser.add_subparsers(dest="command", required=True)
    capture = subparsers.add_parser("capture", help="先保存完整 UTF-8 原文")
    capture.add_argument("--input", required=True, type=Path)
    capture.add_argument("--date", default=None, help="YYYY-MM-DD，缺失时保留待确认")
    capture.add_argument("--participants", nargs="*", default=[], help="多值或逗号分隔姓名")
    capture.add_argument("--supersedes", default=None, help="所修订的前版来源 ID")
    apply = subparsers.add_parser("apply", help="提交包含 source_id 与 items 的拆解 JSON")
    apply.add_argument("--source-id", required=True)
    apply.add_argument("--extraction", required=True, type=Path)
    apply.add_argument("--dry-run", action="store_true")
    # Accept --skill-dir either before or after the subcommand, matching other
    # local helper commands while keeping one locked-root resolution.
    for subparser in (capture, apply):
        subparser.add_argument("--skill-dir", default=argparse.SUPPRESS)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result: dict = {}
    paths = None

    def commit() -> int:
        nonlocal result, paths
        paths = resolve_paths(args.skill_dir, require_lock=True)
        print_warnings(paths.warnings)
        if args.command == "capture":
            participants = [name.strip() for value in args.participants for name in value.replace("，", ",").split(",") if name.strip()]
            result = capture_source(paths, args.input, args.date, participants, args.supersedes)
        else:
            try:
                extraction = json.loads(args.extraction.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                raise ConversationError("拆解文件必须是可读取的 UTF-8 JSON。") from exc
            result = apply_source(paths, args.source_id, extraction, dry_run=args.dry_run)
        return 0

    try:
        code = run_with_write_lock(commit)
        if code:
            return code
        # notebook-sync takes the same shared lock itself. Release our local
        # commit lock first so this child cannot deadlock with its parent.
        if not result.get("dry_run") and paths is not None:
            result["backup"] = attempt_backup(paths)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ConversationError, TeamMemoryPathError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: 本地谈话写入失败（{type(exc).__name__}）；保留已保存内容，请重试。", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
