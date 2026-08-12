#!/usr/bin/env python3
"""Side-effecting SMTP draft and send CLI for the OpenClaw email-assistant skill."""

from __future__ import annotations

import argparse
import json
import os
import re
import secrets
import smtplib
import socket
import ssl
import tempfile
import uuid
from datetime import datetime, timezone
from email.message import EmailMessage
from email.utils import formatdate, getaddresses, make_msgid
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence


MAX_BODY_CHARS = 50_000
ENV_LINE = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(.*)$")


class SafeError(Exception):
    def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise SafeError("invalid_request", message)


def load_local_env() -> None:
    """Load scripts/.env without overriding values already present in the process."""
    if env_bool("EMAIL_ASSISTANT_DISABLE_LOCAL_ENV", False):
        return
    env_path = Path(__file__).with_name(".env")
    if not env_path.is_file():
        return
    try:
        lines = env_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise SafeError("configuration_error", "could not read local scripts/.env") from exc
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = ENV_LINE.match(line)
        if not match:
            continue
        name, raw_value = match.groups()
        if name in os.environ:
            continue
        value = raw_value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ[name] = value


def emit(payload: Dict[str, Any], exit_code: int = 0) -> None:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    raise SystemExit(exit_code)


def env_int(name: str, default: int, minimum: int, maximum: int) -> int:
    raw = os.environ.get(name, str(default))
    try:
        value = int(raw)
    except ValueError as exc:
        raise SafeError("configuration_error", f"{name} must be an integer") from exc
    if not minimum <= value <= maximum:
        raise SafeError("configuration_error", f"{name} must be between {minimum} and {maximum}")
    return value


def env_bool(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def env_first(*names: str) -> Optional[str]:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return None


def config(require_send: bool = False) -> Dict[str, Any]:
    user = env_first("EMAIL_ADDRESS", "EMAIL_SMTP_USER", "EMAIL_IMAP_USER")
    password = env_first("EMAIL_PASSWORD", "EMAIL_SMTP_PASSWORD", "EMAIL_IMAP_PASSWORD")
    missing = []
    if not os.environ.get("EMAIL_SMTP_HOST"):
        missing.append("EMAIL_SMTP_HOST")
    if not user:
        missing.append("EMAIL_ADDRESS")
    if not password:
        missing.append("EMAIL_PASSWORD")
    if missing:
        raise SafeError(
            "configuration_error",
            "SMTP is not configured",
            {"missing": missing, "next_action": "configure_smtp"},
        )
    security = os.environ.get("EMAIL_SMTP_SECURITY", "ssl").strip().lower()
    if security not in {"ssl", "starttls"}:
        raise SafeError("configuration_error", "EMAIL_SMTP_SECURITY must be ssl or starttls")
    send_enabled = env_bool("EMAIL_SMTP_SEND_ENABLED", False)
    if require_send and not send_enabled:
        raise SafeError(
            "send_disabled",
            "SMTP sending is disabled; set EMAIL_SMTP_SEND_ENABLED=true after operational review",
        )
    default_port = 465 if security == "ssl" else 587
    from_address = os.environ.get("EMAIL_SMTP_FROM", user)
    validate_address_list("EMAIL_SMTP_FROM", from_address, allow_empty=False)
    return {
        "host": os.environ["EMAIL_SMTP_HOST"],
        "port": env_int("EMAIL_SMTP_PORT", default_port, 1, 65535),
        "user": user,
        "password": password,
        "from": from_address,
        "security": security,
        "timeout": env_int("EMAIL_SMTP_TIMEOUT", 15, 1, 60),
        "send_enabled": send_enabled,
    }


def resolve_output_dir(output_dir: Path) -> Path:
    output_root = Path(
        os.environ.get("EMAIL_ASSISTANT_OUTPUT_ROOT", str(Path.cwd()))
    ).expanduser().resolve()
    resolved = (
        output_dir.expanduser().resolve()
        if output_dir.is_absolute()
        else (output_root / output_dir).resolve()
    )
    try:
        resolved.relative_to(output_root)
    except ValueError as exc:
        raise SafeError("invalid_request", "output directory is outside EMAIL_ASSISTANT_OUTPUT_ROOT") from exc
    return resolved


def resolve_artifact_path(path: Path) -> Path:
    output_root = Path(
        os.environ.get("EMAIL_ASSISTANT_OUTPUT_ROOT", str(Path.cwd()))
    ).expanduser().resolve()
    resolved = path.expanduser().resolve()
    try:
        resolved.relative_to(output_root)
    except ValueError as exc:
        raise SafeError("invalid_request", "draft artifact is outside EMAIL_ASSISTANT_OUTPUT_ROOT") from exc
    if not resolved.is_file():
        raise SafeError("invalid_request", "draft artifact does not exist")
    return resolved


def save_json(payload: Dict[str, Any], output_dir: Path, prefix: str) -> Dict[str, Any]:
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filename = f"{prefix}-{timestamp}-{uuid.uuid4().hex[:8]}.json"
    temporary_path: Optional[Path] = None
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{prefix}-", suffix=".tmp", dir=output_dir
        )
        temporary_path = Path(temporary_name)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_path, 0o600)
        destination = output_dir / filename
        os.replace(temporary_path, destination)
        temporary_path = None
        return {
            "path": str(destination.resolve()),
            "size_bytes": destination.stat().st_size,
        }
    except OSError as exc:
        raise SafeError("storage_error", "Could not securely save the email draft JSON") from exc
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass


def overwrite_json(path: Path, payload: Dict[str, Any]) -> None:
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    temporary_path: Optional[Path] = None
    try:
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}-", suffix=".tmp", dir=path.parent
        )
        temporary_path = Path(temporary_name)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_path, 0o600)
        os.replace(temporary_path, path)
        temporary_path = None
    except OSError as exc:
        raise SafeError("storage_error", "message was sent but the draft artifact could not be updated") from exc
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass


def validate_header_value(name: str, value: str) -> str:
    if any(char in value for char in "\r\n\x00"):
        raise SafeError("invalid_request", f"{name} contains invalid header characters")
    return value.strip()


def split_addresses(value: str) -> List[str]:
    parts = [item.strip() for item in value.split(",")]
    return [item for item in parts if item]


def validate_address_list(name: str, value: str, allow_empty: bool) -> List[str]:
    if any(char in value for char in "\r\n\x00"):
        raise SafeError("invalid_request", f"{name} contains invalid header characters")
    addresses = split_addresses(value)
    if not addresses and not allow_empty:
        raise SafeError("invalid_request", f"{name} is required")
    parsed = getaddresses(addresses)
    invalid = [raw for raw, address in parsed if not address or "@" not in address]
    if invalid or len(parsed) != len(addresses):
        raise SafeError("invalid_request", f"{name} contains an invalid email address")
    return addresses


def read_body(args: argparse.Namespace) -> str:
    if bool(args.body) == bool(args.body_file):
        raise SafeError("invalid_request", "provide exactly one of --body or --body-file")
    if args.body_file:
        body_path = args.body_file.expanduser().resolve()
        try:
            body = body_path.read_text(encoding="utf-8")
        except OSError as exc:
            raise SafeError("invalid_request", "could not read --body-file") from exc
    else:
        body = args.body
    if not body or not body.strip():
        raise SafeError("invalid_request", "body is required")
    if len(body) > MAX_BODY_CHARS:
        raise SafeError("invalid_request", f"body exceeds {MAX_BODY_CHARS} characters")
    return body.replace("\r\n", "\n").replace("\r", "\n")


def build_message(draft: Dict[str, Any]) -> EmailMessage:
    message = EmailMessage()
    message["From"] = draft["from"]
    message["To"] = ", ".join(draft["to"])
    if draft["cc"]:
        message["Cc"] = ", ".join(draft["cc"])
    message["Subject"] = draft["subject"]
    message["Date"] = formatdate(localtime=False)
    message["Message-ID"] = draft["message_id"]
    if draft.get("reply_to_source_ref"):
        message["X-Email-Assistant-Source-Ref"] = draft["reply_to_source_ref"]
    message.set_content(draft["body_text"])
    return message


def connect_smtp(cfg: Dict[str, Any]) -> smtplib.SMTP:
    try:
        if cfg["security"] == "ssl":
            client: smtplib.SMTP = smtplib.SMTP_SSL(
                cfg["host"], cfg["port"], timeout=cfg["timeout"], context=ssl.create_default_context()
            )
        else:
            client = smtplib.SMTP(cfg["host"], cfg["port"], timeout=cfg["timeout"])
            client.starttls(context=ssl.create_default_context())
        client.login(cfg["user"], cfg["password"])
        return client
    except smtplib.SMTPAuthenticationError as exc:
        raise SafeError("authentication_failed", "SMTP authentication failed") from exc
    except (smtplib.SMTPException, OSError, socket.timeout, ssl.SSLError) as exc:
        raise SafeError("connection_failed", "Unable to establish an authenticated TLS SMTP session") from exc


def mask_account(value: str) -> str:
    local, separator, domain = value.partition("@")
    if not separator:
        return (local[:1] or "*") + "***"
    return (local[:1] or "*") + "***@" + domain


def command_health() -> None:
    cfg = config(require_send=False)
    client: Optional[smtplib.SMTP] = None
    try:
        client = connect_smtp(cfg)
        emit({
            "status": "ok",
            "account": mask_account(cfg["user"]),
            "host": cfg["host"],
            "port": cfg["port"],
            "security": cfg["security"],
            "send_enabled": cfg["send_enabled"],
        })
    finally:
        if client is not None:
            try:
                client.quit()
            except (smtplib.SMTPException, OSError):
                pass


def command_compose(args: argparse.Namespace) -> None:
    cfg = config(require_send=False)
    output_dir = resolve_output_dir(args.output_dir)
    subject = validate_header_value("--subject", args.subject)
    to = validate_address_list("--to", args.to, allow_empty=False)
    cc = validate_address_list("--cc", args.cc or "", allow_empty=True)
    bcc = validate_address_list("--bcc", args.bcc or "", allow_empty=True)
    body = read_body(args)
    reply_to = validate_header_value("--reply-to-source-ref", args.reply_to_source_ref or "")
    draft = {
        "artifact_type": "email-send-draft",
        "status": "draft",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "from": cfg["from"],
        "to": to,
        "cc": cc,
        "bcc": bcc,
        "subject": subject,
        "body_text": body,
        "message_id": make_msgid(domain=cfg["from"].rpartition("@")[2] or None),
        "reply_to_source_ref": reply_to or None,
        "confirmation_token": secrets.token_urlsafe(18),
        "send_enabled_at_compose": cfg["send_enabled"],
    }
    saved_json = save_json(draft, output_dir, "email-draft")
    emit({
        "status": "draft",
        "recipient_count": len(to) + len(cc) + len(bcc),
        "has_bcc": bool(bcc),
        "reply_to_source_ref": reply_to or None,
        "saved_json": saved_json,
        "confirmation_required": True,
    })


def command_send(args: argparse.Namespace) -> None:
    cfg = config(require_send=True)
    draft_path = resolve_artifact_path(args.draft_json)
    try:
        draft = json.loads(draft_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SafeError("invalid_request", "draft artifact is not valid JSON") from exc
    if draft.get("artifact_type") != "email-send-draft":
        raise SafeError("invalid_request", "draft artifact is not an email-send-draft")
    if draft.get("status") in {"sent", "partial_sent"}:
        raise SafeError("already_sent", "draft artifact has already been submitted to SMTP")
    if not secrets.compare_digest(args.confirm_send, str(draft.get("confirmation_token", ""))):
        raise SafeError("confirmation_required", "confirmation token does not match the draft")

    message = build_message(draft)
    recipients = list(draft["to"]) + list(draft["cc"]) + list(draft["bcc"])
    client: Optional[smtplib.SMTP] = None
    try:
        client = connect_smtp(cfg)
        refused = client.send_message(message, from_addr=draft["from"], to_addrs=recipients)
    except smtplib.SMTPRecipientsRefused as exc:
        raise SafeError("recipient_refused", "SMTP server refused all recipients") from exc
    except smtplib.SMTPException as exc:
        raise SafeError("send_failed", "SMTP server failed to send the message") from exc
    finally:
        if client is not None:
            try:
                client.quit()
            except (smtplib.SMTPException, OSError):
                pass
    if refused:
        draft["status"] = "partial_sent"
        draft["sent_at"] = datetime.now(timezone.utc).isoformat()
        draft["refused_count"] = len(refused)
        overwrite_json(draft_path, draft)
        saved_json = save_json(draft, draft_path.parent, "email-partial-sent")
        raise SafeError(
            "partial_send",
            "SMTP server refused one or more recipients; do not retry the same draft blindly",
            {"refused_count": len(refused), "saved_json": saved_json},
        )

    draft["status"] = "sent"
    draft["sent_at"] = datetime.now(timezone.utc).isoformat()
    overwrite_json(draft_path, draft)
    saved_json = save_json(draft, draft_path.parent, "email-sent")
    emit({
        "status": "sent",
        "message_id": draft["message_id"],
        "recipient_count": len(recipients),
        "saved_json": saved_json,
    })


def parser() -> argparse.ArgumentParser:
    root = JsonArgumentParser(description="SMTP draft and send access; emits JSON only")
    sub = root.add_subparsers(dest="command", required=True)
    sub.add_parser("health", help="Check authenticated TLS SMTP availability")

    compose = sub.add_parser("compose", help="Save a sendable email draft artifact")
    compose.add_argument("--to", required=True)
    compose.add_argument("--cc")
    compose.add_argument("--bcc")
    compose.add_argument("--subject", required=True)
    compose.add_argument("--body")
    compose.add_argument("--body-file", type=Path)
    compose.add_argument("--reply-to-source-ref")
    compose.add_argument(
        "--output-dir",
        type=Path,
        default=Path(os.environ.get("EMAIL_ASSISTANT_OUTPUT_DIR", "outputs/email-assistant")),
        help="JSON destination beneath EMAIL_ASSISTANT_OUTPUT_ROOT",
    )

    send = sub.add_parser("send", help="Send a previously saved draft after explicit confirmation")
    send.add_argument("--draft-json", type=Path, required=True)
    send.add_argument("--confirm-send", required=True)
    return root


def main(argv: Optional[Sequence[str]] = None) -> None:
    try:
        load_local_env()
        args = parser().parse_args(argv)
        if args.command == "health":
            command_health()
        elif args.command == "compose":
            command_compose(args)
        elif args.command == "send":
            command_send(args)
    except SafeError as exc:
        error = {"code": exc.code, "message": exc.message}
        error.update(exc.details)
        emit({"status": "error", "error": error}, 2)
    except KeyboardInterrupt:
        emit({"status": "error", "error": {"code": "cancelled", "message": "Operation cancelled"}}, 130)


if __name__ == "__main__":
    main()
