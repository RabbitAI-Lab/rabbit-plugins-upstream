#!/usr/bin/env python3
"""Source-only maintenance CLI for yotta-resume source snapshots and question bank."""

import argparse
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))
sys.path.insert(0, str(HERE))

import bank_pipeline  # noqa: E402
import source_watch  # noqa: E402


VERSION = "0.2.0"

try:
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


def _format_choice():
    return {"choices": ("json", "text"), "default": "text"}


def cmd_sources_check(args):
    try:
        report = source_watch.check_sources(
            args.root or SKILL_ROOT / "data",
            args.snapshots,
            args.out,
            today=args.today,
        )
    except source_watch.SourceWatchError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("来源候选写入失败：{}".format(error), file=sys.stderr)
        return 7
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("来源候选检查：{}".format("CHANGED" if report["changed"] else "UNCHANGED"))
        print("来源变化：{}".format(report["source_change_count"]))
        if report.get("candidate"):
            print("候选目录：{}".format(report["candidate"]))
    return 0


def cmd_sources_fetch(args):
    if args.all and args.source_id:
        print("--all 与 --source-id 不能同时使用。", file=sys.stderr)
        return 2
    if not args.all and not args.source_id:
        print("必须指定 --source-id 或 --all。", file=sys.stderr)
        return 2
    try:
        report = source_watch.fetch_sources(
            args.root or SKILL_ROOT / "data",
            args.out,
            source_ids=None if args.all else tuple(args.source_id),
            today=args.today,
            timeout=args.timeout,
            max_bytes=args.max_bytes,
        )
    except source_watch.SourceWatchError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("来源快照写入失败：{}".format(error), file=sys.stderr)
        return 7
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("来源快照：{} 项".format(report["source_count"]))
        print("目录：{}".format(report["snapshot_dir"]))
    return 0


def _emit_pipeline_report(report, fmt, text_lines):
    if fmt == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("\n".join(text_lines(report)))


def cmd_bank_propose(args):
    try:
        report = bank_pipeline.propose_candidate(
            args.root or SKILL_ROOT / "data",
            args.source_candidate,
            args.patches,
            args.out,
            target_version=args.target_version,
            today=args.today,
        )
    except bank_pipeline.BankPipelineError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except source_watch.SourceWatchError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("题库候选写入失败：{}".format(error), file=sys.stderr)
        return 7
    _emit_pipeline_report(
        report,
        args.format,
        lambda item: [
            "题库候选：{}".format(item["candidate_id"]),
            "版本：{} -> {}".format(
                item["base_bank_version"],
                item["target_bank_version"],
            ),
            "来源变化：{}".format(item["source_change_count"]),
            "题目变化：{}".format(item["question_change_count"]),
            "候选目录：{}".format(item["candidate"]),
        ],
    )
    return 0


def cmd_bank_review(args):
    try:
        report = bank_pipeline.review_candidate(
            args.candidate,
            reviewer=args.reviewer,
            decision=args.decision,
            review_notes_path=args.review_notes,
            confirmations=args.confirm,
            reviewed_at=args.reviewed_at,
        )
    except bank_pipeline.BankPipelineError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("复核记录写入失败：{}".format(error), file=sys.stderr)
        return 7
    _emit_pipeline_report(
        report,
        args.format,
        lambda item: [
            "人工复核：{}".format(item["decision"]),
            "候选哈希：{}".format(item["candidate_sha256"]),
        ],
    )
    return 0


def cmd_bank_validate(args):
    try:
        report = bank_pipeline.validate_candidate(
            args.candidate,
            args.root or SKILL_ROOT / "data",
            today=args.today,
        )
    except bank_pipeline.BankPipelineError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("候选校验写入失败：{}".format(error), file=sys.stderr)
        return 7
    _emit_pipeline_report(
        report,
        args.format,
        lambda item: [
            "候选校验：PASS",
            "契约文件：{}".format(item["checked_files"]),
            "题目：{}".format(item["question_count"]),
            "目标版本：{}".format(item["bank_version"]),
        ],
    )
    return 0


def cmd_bank_apply(args):
    try:
        report = bank_pipeline.apply_candidate(
            args.candidate,
            args.root or SKILL_ROOT / "data",
            today=args.today,
            now=args.now,
        )
    except bank_pipeline.BankPipelineError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("题库应用写入失败：{}".format(error), file=sys.stderr)
        return 7
    _emit_pipeline_report(
        report,
        args.format,
        lambda item: [
            "题库应用：PASS",
            "版本：{}".format(item["bank_version"]),
            "历史快照：{}".format(item["snapshot_id"]),
        ],
    )
    return 0


def cmd_bank_rollback(args):
    try:
        report = bank_pipeline.rollback(
            args.snapshot,
            args.root or SKILL_ROOT / "data",
            today=args.today,
            now=args.now,
        )
    except bank_pipeline.BankPipelineError as error:
        print(str(error), file=sys.stderr)
        return error.exit_code
    except OSError as error:
        print("题库回滚写入失败：{}".format(error), file=sys.stderr)
        return 7
    _emit_pipeline_report(
        report,
        args.format,
        lambda item: [
            "题库回滚：PASS",
            "恢复快照：{}".format(item["snapshot_id"]),
            "回滚前备份：{}".format(item["rollback_backup_id"]),
        ],
    )
    return 0


def build_parser():
    parser = argparse.ArgumentParser(
        prog="yotta-resume-maintenance",
        description="元简源码维护工具：来源抓取、题库候选、人工复核、应用与回滚。",
    )
    parser.add_argument("--version", action="version", version=VERSION)
    sub = parser.add_subparsers(dest="command")
    sub.required = True

    sources_parser = sub.add_parser("sources", help="检查来源快照或显式抓取")
    sources_sub = sources_parser.add_subparsers(dest="sources_command")
    sources_sub.required = True

    sources_check = sources_sub.add_parser("check", help="离线比对来源快照并生成候选")
    sources_check.add_argument("--snapshots", required=True)
    sources_check.add_argument("--out", required=True)
    sources_check.add_argument("--root")
    sources_check.add_argument("--today")
    sources_check.add_argument("--format", **_format_choice())
    sources_check.set_defaults(func=cmd_sources_check)

    sources_fetch = sources_sub.add_parser("fetch", help="显式联网抓取来源指纹快照")
    sources_fetch.add_argument("--source-id", action="append")
    sources_fetch.add_argument("--all", action="store_true")
    sources_fetch.add_argument("--out", required=True)
    sources_fetch.add_argument("--root")
    sources_fetch.add_argument("--today")
    sources_fetch.add_argument("--timeout", type=float, default=15)
    sources_fetch.add_argument("--max-bytes", type=int, default=2 * 1024 * 1024)
    sources_fetch.add_argument("--format", **_format_choice())
    sources_fetch.set_defaults(func=cmd_sources_fetch)

    bank_parser = sub.add_parser("bank", help="生成、复核、校验、应用或回滚题库候选")
    bank_sub = bank_parser.add_subparsers(dest="bank_command")
    bank_sub.required = True

    bank_propose = bank_sub.add_parser("propose", help="从来源候选生成题库候选")
    bank_propose.add_argument("--source-candidate", required=True)
    bank_propose.add_argument("--patches")
    bank_propose.add_argument("--target-version", required=True)
    bank_propose.add_argument("--out", required=True)
    bank_propose.add_argument("--root")
    bank_propose.add_argument("--today")
    bank_propose.add_argument("--format", **_format_choice())
    bank_propose.set_defaults(func=cmd_bank_propose)

    bank_review = bank_sub.add_parser("review", help="记录人工复核结论")
    bank_review.add_argument("--candidate", required=True)
    bank_review.add_argument("--reviewer", required=True)
    bank_review.add_argument("--decision", choices=("approve", "reject"), required=True)
    bank_review.add_argument("--review-notes", required=True)
    bank_review.add_argument("--confirm", default="")
    bank_review.add_argument("--reviewed-at")
    bank_review.add_argument("--format", **_format_choice())
    bank_review.set_defaults(func=cmd_bank_review)

    bank_validate = bank_sub.add_parser("validate", help="校验候选契约")
    bank_validate.add_argument("--candidate", required=True)
    bank_validate.add_argument("--root")
    bank_validate.add_argument("--today")
    bank_validate.add_argument("--format", **_format_choice())
    bank_validate.set_defaults(func=cmd_bank_validate)

    bank_apply = bank_sub.add_parser("apply", help="原子应用已复核候选")
    bank_apply.add_argument("--candidate", required=True)
    bank_apply.add_argument("--root")
    bank_apply.add_argument("--today")
    bank_apply.add_argument("--now")
    bank_apply.add_argument("--format", **_format_choice())
    bank_apply.set_defaults(func=cmd_bank_apply)

    bank_rollback = bank_sub.add_parser("rollback", help="校验并恢复历史快照")
    bank_rollback.add_argument("--snapshot", required=True)
    bank_rollback.add_argument("--root")
    bank_rollback.add_argument("--today")
    bank_rollback.add_argument("--now")
    bank_rollback.add_argument("--format", **_format_choice())
    bank_rollback.set_defaults(func=cmd_bank_rollback)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
