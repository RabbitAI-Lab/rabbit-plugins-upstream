#!/usr/bin/env python3
"""Read-only, bounded IMAP JSON CLI for the OpenClaw email-assistant skill."""

from __future__ import annotations

import argparse
import email
import html
import imaplib
import json
import os
import re
import socket
import ssl
import sys
import tempfile
import uuid
from datetime import date, datetime, timezone
from email import policy
from email.header import decode_header
from email.message import Message
from email.utils import getaddresses, parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import smtp_send

MAX_BODY_CHARS = 10_240


class SafeError(Exception):
    def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise SafeError("invalid_query", message)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: List[str] = []
        self.ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag.lower() in {"script", "style", "head"}:
            self.ignored_depth += 1
        elif tag.lower() in {"br", "p", "div", "li", "tr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style", "head"} and self.ignored_depth:
            self.ignored_depth -= 1
        elif tag.lower() in {"p", "div", "li", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.ignored_depth:
            self.parts.append(data)

    def text(self) -> str:
        return normalize_whitespace("".join(self.parts))


def emit(payload: Dict[str, Any], exit_code: int = 0) -> None:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    raise SystemExit(exit_code)


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
        raise SafeError(
            "invalid_query",
            "output directory is outside EMAIL_ASSISTANT_OUTPUT_ROOT",
        ) from exc
    return resolved


def save_query_json(
    payload: Dict[str, Any], output_dir: Path, prefix: str = "email-query"
) -> Dict[str, Any]:
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
        raise SafeError(
            "storage_error", "Could not securely save the email query JSON"
        ) from exc
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass


def env_int(name: str, default: int, minimum: int, maximum: int) -> int:
    raw = os.environ.get(name, str(default))
    try:
        value = int(raw)
    except ValueError as exc:
        raise SafeError("configuration_error", f"{name} must be an integer") from exc
    if not minimum <= value <= maximum:
        raise SafeError("configuration_error", f"{name} must be between {minimum} and {maximum}")
    return value


def env_first(*names: str) -> Optional[str]:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return None


def config() -> Dict[str, Any]:
    user = env_first("EMAIL_ADDRESS", "EMAIL_IMAP_USER")
    password = env_first("EMAIL_PASSWORD", "EMAIL_IMAP_PASSWORD")
    missing = []
    if not os.environ.get("EMAIL_IMAP_HOST"):
        missing.append("EMAIL_IMAP_HOST")
    if not user:
        missing.append("EMAIL_ADDRESS")
    if not password:
        missing.append("EMAIL_PASSWORD")
    if missing:
        raise SafeError(
            "configuration_error",
            "IMAP is not configured",
            {
                "missing": missing,
                "next_action": "choose_mail_provider",
                "provider_guides": ["qq", "gmail", "outlook-microsoft365", "netease-163-126", "custom-imap"],
            },
        )
    folder = os.environ.get("EMAIL_IMAP_FOLDER", "INBOX")
    if any(char in folder for char in "\r\n\x00"):
        raise SafeError("configuration_error", "EMAIL_IMAP_FOLDER contains invalid characters")
    return {
        "host": os.environ["EMAIL_IMAP_HOST"],
        "port": env_int("EMAIL_IMAP_PORT", 993, 1, 65535),
        "user": user,
        "password": password,
        "folder": folder,
        "timeout": env_int("EMAIL_IMAP_TIMEOUT", 15, 1, 60),
    }


def mask_account(value: str) -> str:
    local, separator, domain = value.partition("@")
    if not separator:
        return (local[:1] or "*") + "***"
    return (local[:1] or "*") + "***@" + domain


def connect(cfg: Dict[str, Any]) -> imaplib.IMAP4_SSL:
    try:
        client = imaplib.IMAP4_SSL(
            cfg["host"], cfg["port"], ssl_context=ssl.create_default_context(), timeout=cfg["timeout"]
        )
        client.login(cfg["user"], cfg["password"])
        send_client_id(client)
        status, _ = client.select(cfg["folder"], readonly=True)
        if status != "OK":
            client.logout()
            raise SafeError("mailbox_unavailable", "The configured mailbox cannot be selected read-only")
        return client
    except imaplib.IMAP4.error as exc:
        raise SafeError("authentication_failed", "IMAP authentication or authorization failed") from exc
    except (OSError, socket.timeout, ssl.SSLError) as exc:
        raise SafeError("connection_failed", "Unable to establish a verified TLS connection to the IMAP server") from exc


def send_client_id(client: imaplib.IMAP4_SSL) -> None:
    """Declare client identity for providers such as 163.com before SELECT/EXAMINE."""
    imaplib.Commands["ID"] = ("AUTH", "SELECTED")
    client_id = {
        "name": "OpenClaw Email Assistant",
        "version": "1.0",
        "vendor": "OpenClaw",
    }
    payload = "(" + " ".join(
        f'"{key}" "{value}"' for key, value in client_id.items()
    ) + ")"
    try:
        client._simple_command("ID", payload)
    except (imaplib.IMAP4.error, OSError):
        # RFC 2971 ID is optional for most providers. Continue so non-163
        # servers that reject it still work with the standard read-only flow.
        pass


def logout(client: Optional[imaplib.IMAP4_SSL]) -> None:
    if client is None:
        return
    try:
        client.logout()
    except (imaplib.IMAP4.error, OSError):
        pass


def decode_value(value: Optional[str]) -> str:
    if not value:
        return ""
    parts: List[str] = []
    for content, charset in decode_header(value):
        if isinstance(content, str):
            parts.append(content)
            continue
        encodings = [charset] if charset else []
        encodings.extend(["utf-8", "gb18030", "big5", "latin-1"])
        decoded = None
        for encoding in encodings:
            if not encoding:
                continue
            try:
                decoded = content.decode(encoding)
                break
            except (LookupError, UnicodeDecodeError):
                continue
        parts.append(decoded if decoded is not None else content.decode("utf-8", errors="replace"))
    return normalize_whitespace("".join(parts))


def normalize_whitespace(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t\f\v]+", " ", line).strip() for line in text.split("\n")]
    return "\n".join(line for line in lines if line).strip()


def decode_part(part: Message) -> Tuple[str, Optional[str]]:
    payload = part.get_payload(decode=True)
    if payload is None:
        raw = part.get_payload()
        return (raw if isinstance(raw, str) else "", None)
    candidates = [part.get_content_charset(), "utf-8", "gb18030", "big5", "latin-1"]
    for charset in candidates:
        if not charset:
            continue
        try:
            return payload.decode(charset), None
        except (LookupError, UnicodeDecodeError):
            continue
    return payload.decode("utf-8", errors="replace"), "body_charset_replaced"


def html_to_text(value: str) -> str:
    parser = TextExtractor()
    try:
        parser.feed(value)
        parser.close()
        return parser.text()
    except Exception:
        return normalize_whitespace(re.sub(r"<[^>]*>", " ", html.unescape(value)))


def body_and_attachments(message: Message, max_chars: int) -> Tuple[str, bool, List[Dict[str, Any]], List[str]]:
    plain: List[str] = []
    rich: List[str] = []
    attachments: List[Dict[str, Any]] = []
    warnings: List[str] = []
    parts: Iterable[Message] = message.walk() if message.is_multipart() else [message]
    for part in parts:
        if part.is_multipart():
            continue
        disposition = (part.get_content_disposition() or "").lower()
        filename = decode_value(part.get_filename())
        content_type = part.get_content_type().lower()
        if disposition == "attachment" or filename:
            raw = part.get_payload(decode=True)
            attachments.append({
                "filename": filename or "(unnamed)",
                "content_type": content_type,
                "size": len(raw) if raw is not None else None,
            })
            continue
        if content_type not in {"text/plain", "text/html"}:
            continue
        value, warning = decode_part(part)
        if warning:
            warnings.append(warning)
        (plain if content_type == "text/plain" else rich).append(value)
    text = normalize_whitespace("\n".join(plain)) if plain else html_to_text("\n".join(rich))
    truncated = len(text) > max_chars
    if truncated:
        text = text[:max_chars].rstrip()
        warnings.append("body_truncated")
    if not text:
        warnings.append("body_unavailable")
    return text, truncated, attachments, sorted(set(warnings))


def parse_message(uid: str, raw: bytes, folder: str, max_chars: int) -> Dict[str, Any]:
    message = email.message_from_bytes(raw, policy=policy.default)
    body, truncated, attachments, warnings = body_and_attachments(message, max_chars)
    received_at = None
    if message.get("Date"):
        try:
            received_at = parsedate_to_datetime(str(message.get("Date"))).isoformat()
        except (TypeError, ValueError, OverflowError):
            warnings.append("invalid_date_header")
    return {
        "source_ref": f"imap:{folder}:{uid}",
        "message_id": decode_value(str(message.get("Message-ID", ""))),
        "subject": decode_value(str(message.get("Subject", ""))),
        "from": decode_value(str(message.get("From", ""))),
        "received_at": received_at,
        "unread": None,
        "body_text": body,
        "body_truncated": truncated,
        "parse_status": "partial" if warnings else "complete",
        "attachments": attachments,
        "warnings": sorted(set(warnings)),
    }


def parse_message_metadata(uid: str, raw: bytes, folder: str) -> Dict[str, Any]:
    message = email.message_from_bytes(raw, policy=policy.default)
    warnings: List[str] = []
    received_at = None
    if message.get("Date"):
        try:
            received_at = parsedate_to_datetime(str(message.get("Date"))).isoformat()
        except (TypeError, ValueError, OverflowError):
            warnings.append("invalid_date_header")
    return {
        "source_ref": f"imap:{folder}:{uid}",
        "message_id": decode_value(str(message.get("Message-ID", ""))),
        "subject": decode_value(str(message.get("Subject", ""))),
        "from": decode_value(str(message.get("From", ""))),
        "received_at": received_at,
        "unread": None,
        "size": None,
        "parse_status": "partial" if warnings else "complete",
        "warnings": warnings,
    }


def validate_iso_date(value: Optional[str], option: str) -> Optional[str]:
    if value is None:
        return None
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise SafeError("invalid_query", f"{option} must use YYYY-MM-DD") from exc
    return value


def imap_date(value: str) -> str:
    return date.fromisoformat(value).strftime("%d-%b-%Y")


def raw_bytes(fetch_data: Sequence[Any]) -> Optional[bytes]:
    for item in fetch_data:
        if isinstance(item, tuple) and len(item) > 1 and isinstance(item[1], bytes):
            return item[1]
    return None


def fetch_one(client: imaplib.IMAP4_SSL, uid: str, folder: str, max_chars: int) -> Dict[str, Any]:
    status, data = client.uid("fetch", uid, "(BODY.PEEK[] FLAGS)")
    if status != "OK":
        raise SafeError("message_fetch_failed", f"Could not fetch source imap:{folder}:{uid}")
    raw = raw_bytes(data)
    if raw is None:
        raise SafeError("message_fetch_failed", f"Message source imap:{folder}:{uid} returned no content")
    result = parse_message(uid, raw, folder, max_chars)
    flag_blob = " ".join(
        item[0].decode("ascii", errors="ignore")
        for item in data
        if isinstance(item, tuple) and isinstance(item[0], bytes)
    )
    result["unread"] = "\\Seen" not in flag_blob
    return result


def fetch_one_metadata(client: imaplib.IMAP4_SSL, uid: str, folder: str) -> Dict[str, Any]:
    status, data = client.uid(
        "fetch",
        uid,
        "(BODY.PEEK[HEADER.FIELDS (DATE FROM MESSAGE-ID SUBJECT)] FLAGS RFC822.SIZE)",
    )
    if status != "OK":
        raise SafeError("message_fetch_failed", f"Could not fetch source imap:{folder}:{uid}")
    raw = raw_bytes(data)
    if raw is None:
        raise SafeError("message_fetch_failed", f"Message source imap:{folder}:{uid} returned no metadata")
    result = parse_message_metadata(uid, raw, folder)
    response_blob = " ".join(
        item[0].decode("ascii", errors="ignore")
        for item in data
        if isinstance(item, tuple) and isinstance(item[0], bytes)
    )
    result["unread"] = "\\Seen" not in response_blob
    size_match = re.search(r"RFC822\.SIZE\s+(\d+)", response_blob, re.IGNORECASE)
    if size_match:
        result["size"] = int(size_match.group(1))
    return result


def command_health() -> None:
    cfg = config()
    client: Optional[imaplib.IMAP4_SSL] = None
    try:
        client = connect(cfg)
        emit({
            "status": "ok",
            "account": mask_account(cfg["user"]),
            "host": cfg["host"],
            "folder": cfg["folder"],
            "session_mode": "readonly",
            "credential_scope_verified": False,
        })
    finally:
        logout(client)


def command_query(args: argparse.Namespace) -> None:
    cfg = config()
    output_dir = resolve_output_dir(args.output_dir)
    since = validate_iso_date(args.since, "--since")
    before = validate_iso_date(args.before, "--before")
    if since and before and date.fromisoformat(since) >= date.fromisoformat(before):
        raise SafeError("invalid_query", "--before must be later than --since")
    criteria: List[str] = ["UNSEEN" if args.unread else "ALL"]
    if since:
        criteria.extend(["SINCE", imap_date(since)])
    if before:
        criteria.extend(["BEFORE", imap_date(before)])
    query = {
        "since": since,
        "before": before,
        "unread": args.unread,
        "from_address": args.from_address,
        "from_domain": args.from_domain,
        "keyword": args.keyword,
    }
    client: Optional[imaplib.IMAP4_SSL] = None
    try:
        client = connect(cfg)
        status, data = client.uid("search", None, *criteria)
        if status != "OK" or not data:
            raise SafeError("query_failed", "The IMAP server rejected the bounded search")
        ids = data[0].decode("ascii", errors="ignore").split()
        server_candidate_count = len(ids)
        messages: List[Dict[str, Any]] = []
        errors: List[Dict[str, str]] = []
        keyword = args.keyword.casefold() if args.keyword else None
        from_address = args.from_address.casefold() if args.from_address else None
        domain = args.from_domain.casefold().lstrip("@") if args.from_domain else None
        for uid in reversed(ids):
            try:
                item = fetch_one_metadata(client, uid, cfg["folder"])
            except SafeError as exc:
                errors.append({"code": exc.code, "message": exc.message})
                continue
            addresses = [address.casefold() for _, address in getaddresses([item["from"]])]
            if from_address and from_address not in addresses:
                continue
            if domain and not any(address.rpartition("@")[2] == domain for address in addresses):
                continue
            haystack = "\n".join([item["subject"], item["from"]]).casefold()
            if keyword and keyword not in haystack:
                continue
            messages.append(item)
        matched_count = len(messages)
        result = {
            "status": "partial" if errors else "ok",
            "query": query,
            "matched_count": matched_count,
            "returned_count": len(messages),
            "inspected_count": server_candidate_count,
            "truncated": False,
            "messages": messages,
            "errors": errors,
        }
        saved_json = save_query_json(result, output_dir)
        # Keep complete matching metadata in the mode-600 artifact. OpenClaw's
        # tool result is intentionally only a small, content-free envelope.
        emit({
            "status": result["status"],
            "query": result["query"],
            "matched_count": result["matched_count"],
            "returned_count": result["returned_count"],
            "inspected_count": result["inspected_count"],
            "truncated": result["truncated"],
            "errors": result["errors"],
            "saved_json": saved_json,
        })
    finally:
        logout(client)


def command_read(args: argparse.Namespace) -> None:
    cfg = config()
    output_dir = resolve_output_dir(args.output_dir)
    if not 1 <= args.max_body_chars <= MAX_BODY_CHARS:
        raise SafeError("invalid_query", f"--max-body-chars must be between 1 and {MAX_BODY_CHARS}")
    prefix = f"imap:{cfg['folder']}:"
    if not args.source_ref.startswith(prefix):
        raise SafeError("invalid_query", "source_ref is outside the configured folder")
    uid = args.source_ref[len(prefix):]
    if not uid.isdigit():
        raise SafeError("invalid_query", "source_ref must end with a numeric IMAP UID")

    client: Optional[imaplib.IMAP4_SSL] = None
    try:
        client = connect(cfg)
        message = fetch_one(client, uid, cfg["folder"], args.max_body_chars)
        result = {"status": "ok", "message": message, "errors": []}
        saved_json = save_query_json(result, output_dir, prefix="email-message")
        # The downloader never prints subject, body, attachment names, or other
        # mail content. Callers project bounded fields from the private artifact.
        emit({
            "status": "ok",
            "source_ref": message["source_ref"],
            "body_truncated": message["body_truncated"],
            "parse_status": message["parse_status"],
            "saved_json": saved_json,
        })
    finally:
        logout(client)


def parser() -> argparse.ArgumentParser:
    root = JsonArgumentParser(description="Bounded read-only IMAP access; emits JSON only")
    sub = root.add_subparsers(dest="command", required=True)
    sub.add_parser("health", help="Check TLS, authentication, and read-only mailbox selection")
    query = sub.add_parser("query", help="Save metadata for all messages in an explicit scope")
    query.add_argument("--since")
    query.add_argument("--before")
    query.add_argument("--unread", action="store_true")
    query.add_argument("--from-address")
    query.add_argument("--from-domain")
    query.add_argument("--keyword")
    query.add_argument(
        "--output-dir",
        type=Path,
        default=Path(os.environ.get("EMAIL_ASSISTANT_OUTPUT_DIR", "outputs/email-assistant")),
        help="JSON destination beneath EMAIL_ASSISTANT_OUTPUT_ROOT",
    )
    read = sub.add_parser("read", help="Save one selected message without printing its content")
    read.add_argument("--source-ref", required=True)
    read.add_argument(
        "--max-body-chars", type=int, default=MAX_BODY_CHARS, metavar="1..10240"
    )
    read.add_argument(
        "--output-dir",
        type=Path,
        default=Path(os.environ.get("EMAIL_ASSISTANT_OUTPUT_DIR", "outputs/email-assistant")),
        help="JSON destination beneath EMAIL_ASSISTANT_OUTPUT_ROOT",
    )
    return root


def main(argv: Optional[Sequence[str]] = None) -> None:
    try:
        smtp_send.load_local_env()
        args = parser().parse_args(argv)
        if args.command == "health":
            command_health()
        elif args.command == "query":
            command_query(args)
        elif args.command == "read":
            command_read(args)
    except SafeError as exc:
        error = {"code": exc.code, "message": exc.message}
        error.update(exc.details)
        emit({"status": "error", "error": error}, 2)
    except KeyboardInterrupt:
        emit({"status": "error", "error": {"code": "cancelled", "message": "Operation cancelled"}}, 130)


if __name__ == "__main__":
    main()
