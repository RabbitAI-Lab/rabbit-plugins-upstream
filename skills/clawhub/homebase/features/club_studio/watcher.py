#!/usr/bin/env python3
"""
Club Studio Watcher
Fetches Club Studio Fitness emails from Gmail with dedup + auth-error
handling. Returns raw {id, subject, sender, body, date} dicts to the
agent, which classifies (booking / cancellation / waitlist / noise) and
takes actions.

Doctrine (see skills/homebase/CLAUDE.md):
- Python returns data. Agent decides + delivers. No classification here.
- Every state write goes through utils.write_json_atomic.
"""

from __future__ import annotations

import base64
import json
import os
import re
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from core.keychain_secrets import (
    load_google_secrets,
    keyring_module_available,
    last_keyring_error,
)

load_google_secrets()

from utils import write_json_atomic


_STYLE_SCRIPT_RE = re.compile(
    r"<(style|script)\b[^>]*>.*?</\1\s*>", re.DOTALL | re.IGNORECASE
)
_TAG_RE = re.compile(r"<[^>]+>")
_WHITESPACE_RE = re.compile(r"\s+")
_HTML_ENTITIES = {
    "&nbsp;": " ",
    "&amp;": "&",
    "&lt;": "<",
    "&gt;": ">",
    "&quot;": '"',
    "&#39;": "'",
    "&zwnj;": "",
    "&#8203;": "",
}


def _b64_decode(data: str) -> str:
    try:
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
    except Exception:
        return ""


def _html_to_text(html: str) -> str:
    if not html:
        return ""
    text = _STYLE_SCRIPT_RE.sub(" ", html)
    text = _TAG_RE.sub(" ", text)
    for k, v in _HTML_ENTITIES.items():
        text = text.replace(k, v)
    return _WHITESPACE_RE.sub(" ", text).strip()


class ClubStudioWatcher:
    """Gmail poll + dedup for Club Studio Fitness emails. Returns raw
    email content; the agent classifies and acts.
    """

    def __init__(self, base_path: str = "."):
        self.base_path = base_path
        self.config_file = os.path.join(base_path, "config.json")
        self.processed_ids_file = os.path.join(
            base_path, "household", "club_studio_processed.json"
        )
        self.auth_error_state_file = os.path.join(
            base_path, "household", "club_studio_auth_error_state.json"
        )
        os.makedirs(os.path.dirname(self.processed_ids_file), exist_ok=True)
        self.load_config()
        self.processed_ids = self._load_processed_ids()

    # ─── Config & state ──────────────────────────────────────────────────────

    def load_config(self) -> None:
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        else:
            self.config = {}

    @property
    def enabled(self) -> bool:
        return bool(self.config.get("club_studio", {}).get("enabled", False))

    @property
    def sender_domain(self) -> str:
        return self.config.get("club_studio", {}).get(
            "sender_domain", "clubstudiofitness.com"
        )

    def _load_processed_ids(self) -> set:
        if os.path.exists(self.processed_ids_file):
            with open(self.processed_ids_file, "r") as f:
                return set(json.load(f))
        return set()

    def _save_processed_ids(self) -> None:
        # Cap at 500 to avoid unbounded growth (matches school pattern)
        ids_list = list(self.processed_ids)[-500:]
        write_json_atomic(self.processed_ids_file, ids_list)

    def _mark_processed(self, msg_id: str) -> None:
        self.processed_ids.add(msg_id)
        self._save_processed_ids()

    # ─── Auth-error dedup ────────────────────────────────────────────────────

    def _is_auth_error_notified(self) -> bool:
        try:
            if os.path.exists(self.auth_error_state_file):
                with open(self.auth_error_state_file) as f:
                    return json.load(f).get("notified", False)
        except Exception:
            pass
        return False

    def _set_auth_error_notified(self, notified: bool) -> None:
        try:
            state = {"notified": notified, "updated_at": datetime.now().isoformat()}
            write_json_atomic(self.auth_error_state_file, state)
        except Exception as e:
            print(
                f"[club_studio] Warning: could not save auth_error_state: {e}",
                file=sys.stderr,
            )

    # ─── Gmail auth ──────────────────────────────────────────────────────────

    def get_gmail_service(self):
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build

        client_id = os.environ.get("GOOGLE_CLIENT_ID", "")
        client_secret = os.environ.get("GOOGLE_CLIENT_SECRET", "")
        refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN", "")

        if not all([client_id, client_secret, refresh_token]):
            return None

        creds = Credentials(
            token="",
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
        )

        try:
            creds.refresh(Request())
            self._set_auth_error_notified(False)
            return build("gmail", "v1", credentials=creds)
        except Exception as e:
            if not self._is_auth_error_notified():
                self._set_auth_error_notified(True)
            print(f"[club_studio] Gmail auth failed: {e}", file=sys.stderr)
            return None

    # ─── Body extraction (recursive multipart) ───────────────────────────────

    def _extract_body(self, payload: Dict) -> str:
        """Prefer text/plain; else strip CSS/scripts/tags from HTML.

        Club Studio's "WaitList has been added to a class" promotion email
        is HTML-only with a large inline stylesheet at the top. Returning
        raw HTML would fill the caller's 4000-char cap with @font-face
        declarations before the class name / date / time appears, so the
        agent can't classify or extract fields. Preferring plain text and
        stripping tags makes the readable content survive the cap.
        """
        plain, html = self._collect_parts(payload)
        if plain.strip():
            return plain
        return _html_to_text(html)

    def _collect_parts(self, payload: Dict) -> Tuple[str, str]:
        plain = ""
        html = ""
        mime = payload.get("mimeType", "")
        data = payload.get("body", {}).get("data", "")
        if mime == "text/plain" and data:
            plain += _b64_decode(data)
        elif mime == "text/html" and data:
            html += _b64_decode(data)
        elif mime.startswith("multipart/"):
            for part in payload.get("parts", []):
                p, h = self._collect_parts(part)
                plain += p
                html += h
        elif data:
            html += _b64_decode(data)
        return plain, html

    # ─── Fetch matching emails ───────────────────────────────────────────────

    def fetch_emails(
        self,
        service,
        skip_processed: bool = True,
        max_results: int = 10,
        take: Optional[int] = None,
    ) -> List[Dict]:
        """Return list of {id, subject, sender, body, date} for unprocessed
        Club Studio emails, OLDEST FIRST.

        Sorting matters when waitlist and booking emails for the same class
        both land between polls: real-world event order is waitlist → booking,
        and processing newest-first would tell the family Harsh is going
        before telling them he was waitlisted (and would break the
        waitlist-to-booking promotion the prompt tries to do). Gmail's
        default list order is newest-first; we override it by sorting on
        internalDate ascending.

        Marks emails processed AS THEY ARE TAKEN, not as they are fetched —
        the unpicked remainder stays available for the next poll. This
        differs from earlier revisions (where mark-on-fetch was fine
        because the caller consumed everything).

        Args:
          service: Gmail service (injectable for tests)
          skip_processed: honor the dedup file (default True)
          max_results: how many candidates to pull from Gmail (default 10;
            this is the search page size, not the return size)
          take: how many to return + mark processed (default: all candidates)
        """
        query = f"from:{self.sender_domain} newer_than:2d"
        try:
            results = (
                service.users()
                .messages()
                .list(userId="me", q=query, maxResults=max_results)
                .execute()
            )
        except Exception as e:
            print(f"[club_studio] Gmail list failed: {e}", file=sys.stderr)
            return []

        messages = results.get("messages", [])
        candidates: List[Dict] = []
        for msg in messages:
            msg_id = msg["id"]
            if skip_processed and msg_id in self.processed_ids:
                continue

            try:
                full = (
                    service.users()
                    .messages()
                    .get(userId="me", id=msg_id, format="full")
                    .execute()
                )
            except Exception as e:
                print(
                    f"[club_studio] Gmail get failed for {msg_id}: {e}",
                    file=sys.stderr,
                )
                continue

            headers = full.get("payload", {}).get("headers", [])
            subject = next(
                (h["value"] for h in headers if h["name"].lower() == "subject"),
                "",
            )
            sender = next(
                (h["value"] for h in headers if h["name"].lower() == "from"),
                "",
            )
            date_str = next(
                (h["value"] for h in headers if h["name"].lower() == "date"),
                "",
            )
            body = self._extract_body(full.get("payload", {}))

            candidates.append(
                {
                    "id": msg_id,
                    "subject": subject,
                    "sender": sender,
                    "date": date_str,
                    "body": body[:4000],
                    "_ts": int(full.get("internalDate", 0)),
                }
            )

        # Sort oldest first so waitlist-before-booking ordering is preserved
        # across polls even when they arrive in a single Gmail batch.
        candidates.sort(key=lambda e: e["_ts"])

        picked = candidates if take is None else candidates[:take]
        for e in picked:
            self._mark_processed(e["id"])
            e.pop("_ts", None)

        return picked

    # ─── Group targets from config ───────────────────────────────────────────

    def notify_targets(self) -> List[Dict]:
        """Return [{jid, name}] for every configured WhatsApp group.
        Supports both new shape (whatsapp.groups[]) and legacy scalar
        (whatsapp.group_id). Placeholder JIDs ('YOUR_...') are skipped.
        """
        wa = self.config.get("whatsapp", {})
        groups = wa.get("groups")
        if isinstance(groups, list) and groups:
            out = []
            for g in groups:
                jid = (g or {}).get("id", "").strip()
                if jid and "YOUR" not in jid:
                    out.append({"jid": jid, "name": g.get("name", jid)})
            return out
        legacy_id = wa.get("group_id", "").strip()
        if legacy_id and "YOUR" not in legacy_id:
            return [{"jid": legacy_id, "name": wa.get("group_name", legacy_id)}]
        return []


# ─── Direct cron / debug entry point ─────────────────────────────────────────
#
# The production cron path goes through the OpenClaw agent, which calls
# `python3 tools.py fetch_club_studio_emails` (a thin wrapper on this
# module). This __main__ block exists for manual debugging / smoke tests:
#
#   python3 -m features.club_studio.watcher              # print raw emails (bodies truncated)
#   python3 -m features.club_studio.watcher --full       # print raw emails with full bodies
#   python3 -m features.club_studio.watcher --targets    # print group JIDs
#
# Emits JSON on stdout so it stays parseable for scripting.


def _cli_main() -> int:
    import traceback

    try:
        if not keyring_module_available():
            print(
                json.dumps(
                    {
                        "status": "env_broken",
                        "error": "keyring module unavailable",
                        "interpreter": sys.executable,
                        "detail": last_keyring_error(),
                    }
                )
            )
            return 0

        from core.config_loader import SKILL_DIR

        watcher = ClubStudioWatcher(base_path=SKILL_DIR)

        if "--targets" in sys.argv:
            print(json.dumps({"targets": watcher.notify_targets()}, indent=2))
            return 0

        if not watcher.enabled:
            print(json.dumps({"status": "disabled"}))
            return 0

        service = watcher.get_gmail_service()
        if service is None:
            print(json.dumps({"status": "auth_failed"}))
            return 0

        emails = watcher.fetch_emails(service)
        if not emails:
            print(json.dumps({"status": "no_new_emails"}))
            return 0

        # Email bodies can contain other people's names/details (class
        # rosters, booking confirmations). Truncate by default so a casual
        # debug run doesn't dump full bodies into terminal scrollback/logs
        # — pass --full to see complete content when actually needed.
        show_full = "--full" in sys.argv
        debug_emails = emails if show_full else [
            {**e, "body": (e.get("body", "")[:150] + "... [truncated, use --full to see complete body]")
                          if len(e.get("body", "")) > 150 else e.get("body", "")}
            for e in emails
        ]

        print(
            json.dumps(
                {
                    "status": "emails_found",
                    "count": len(emails),
                    "emails": debug_emails,
                    "targets": watcher.notify_targets(),
                },
                indent=2,
            )
        )
        return 0
    except Exception as e:
        print(
            json.dumps(
                {
                    "status": "crashed",
                    "error": str(e),
                    "traceback": traceback.format_exc(),
                }
            )
        )
        return 1


if __name__ == "__main__":
    sys.exit(_cli_main())
