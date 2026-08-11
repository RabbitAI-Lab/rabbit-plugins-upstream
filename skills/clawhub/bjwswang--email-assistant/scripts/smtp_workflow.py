#!/usr/bin/env python3
"""Friendly two-step SMTP workflow wrapper for compose-review-confirm-send."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent))
import smtp_send


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise smtp_send.SafeError("invalid_request", message)


def emit(payload: Dict[str, Any], exit_code: int = 0) -> None:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    raise SystemExit(exit_code)


def read_draft(path: Path) -> Dict[str, Any]:
    draft_path = smtp_send.resolve_artifact_path(path)
    try:
        draft = json.loads(draft_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise smtp_send.SafeError("invalid_request", "draft artifact is not valid JSON") from exc
    if draft.get("artifact_type") != "email-send-draft":
        raise smtp_send.SafeError("invalid_request", "draft artifact is not an email-send-draft")
    return draft


def review_projection(draft: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "from": draft.get("from"),
        "to": draft.get("to", []),
        "cc": draft.get("cc", []),
        "bcc": draft.get("bcc", []),
        "subject": draft.get("subject"),
        "body_text": draft.get("body_text"),
        "reply_to_source_ref": draft.get("reply_to_source_ref"),
    }


def command_prepare(args: argparse.Namespace) -> None:
    cfg = smtp_send.config(require_send=False)
    output_dir = smtp_send.resolve_output_dir(args.output_dir)
    subject = smtp_send.validate_header_value("--subject", args.subject)
    to = smtp_send.validate_address_list("--to", args.to, allow_empty=False)
    cc = smtp_send.validate_address_list("--cc", args.cc or "", allow_empty=True)
    bcc = smtp_send.validate_address_list("--bcc", args.bcc or "", allow_empty=True)
    body = smtp_send.read_body(args)
    reply_to = smtp_send.validate_header_value("--reply-to-source-ref", args.reply_to_source_ref or "")
    draft = {
        "artifact_type": "email-send-draft",
        "status": "draft",
        "created_at": smtp_send.datetime.now(smtp_send.timezone.utc).isoformat(),
        "from": cfg["from"],
        "to": to,
        "cc": cc,
        "bcc": bcc,
        "subject": subject,
        "body_text": body,
        "message_id": smtp_send.make_msgid(domain=cfg["from"].rpartition("@")[2] or None),
        "reply_to_source_ref": reply_to or None,
        "confirmation_token": smtp_send.secrets.token_urlsafe(18),
        "send_enabled_at_compose": cfg["send_enabled"],
    }
    saved_json = smtp_send.save_json(draft, output_dir, "email-draft")
    emit({
        "status": "review_required",
        "saved_json": saved_json,
        "review": review_projection(draft),
        "next_action": "Ask the user to confirm this exact draft file content, then run confirm.",
    })


def command_review(args: argparse.Namespace) -> None:
    draft = read_draft(args.draft_json)
    emit({
        "status": "review_required",
        "saved_json": {
            "path": str(smtp_send.resolve_artifact_path(args.draft_json)),
            "size_bytes": smtp_send.resolve_artifact_path(args.draft_json).stat().st_size,
        },
        "review": review_projection(draft),
        "next_action": "Ask the user to confirm this exact draft file content, then run confirm.",
    })


def command_confirm(args: argparse.Namespace) -> None:
    if not args.review_confirmed:
        raise smtp_send.SafeError(
            "confirmation_required",
            "pass --review-confirmed only after the user confirms the displayed draft file content",
        )
    draft = read_draft(args.draft_json)
    token = str(draft.get("confirmation_token", ""))
    smtp_send.command_send(argparse.Namespace(draft_json=args.draft_json, confirm_send=token))


def parser() -> argparse.ArgumentParser:
    root = JsonArgumentParser(description="User-friendly two-step SMTP review and send workflow")
    sub = root.add_subparsers(dest="command", required=True)

    prepare = sub.add_parser("prepare", help="Create a draft and print reviewable file content")
    prepare.add_argument("--to", required=True)
    prepare.add_argument("--cc")
    prepare.add_argument("--bcc")
    prepare.add_argument("--subject", required=True)
    prepare.add_argument("--body")
    prepare.add_argument("--body-file", type=Path)
    prepare.add_argument("--reply-to-source-ref")
    prepare.add_argument(
        "--output-dir",
        type=Path,
        default=Path(smtp_send.os.environ.get("EMAIL_ASSISTANT_OUTPUT_DIR", "outputs/email-assistant")),
        help="JSON destination beneath EMAIL_ASSISTANT_OUTPUT_ROOT",
    )

    review = sub.add_parser("review", help="Print reviewable file content for an existing draft")
    review.add_argument("--draft-json", type=Path, required=True)

    confirm = sub.add_parser("confirm", help="Send an existing draft after user review confirmation")
    confirm.add_argument("--draft-json", type=Path, required=True)
    confirm.add_argument("--review-confirmed", action="store_true")
    return root


def main(argv: Optional[Sequence[str]] = None) -> None:
    try:
        smtp_send.load_local_env()
        args = parser().parse_args(argv)
        if args.command == "prepare":
            command_prepare(args)
        elif args.command == "review":
            command_review(args)
        elif args.command == "confirm":
            command_confirm(args)
    except smtp_send.SafeError as exc:
        error = {"code": exc.code, "message": exc.message}
        error.update(exc.details)
        emit({"status": "error", "error": error}, 2)
    except KeyboardInterrupt:
        emit({"status": "error", "error": {"code": "cancelled", "message": "Operation cancelled"}}, 130)


if __name__ == "__main__":
    main()
