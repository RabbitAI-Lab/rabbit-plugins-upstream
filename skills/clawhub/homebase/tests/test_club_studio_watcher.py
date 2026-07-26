"""
test_club_studio_watcher.py — Tests for the Club Studio watcher.

The watcher does NOT classify or parse email content — the agent does
that at runtime with the fetched raw text. These tests cover:
  - Config: backward compat for whatsapp.group_id (scalar) vs. whatsapp.groups[] (array)
  - notify_targets: skips placeholder JIDs, prefers array shape
  - Dedup: msg_id set persistence, 500-item cap
  - Auth-error dedup: first failure sets flag, subsequent silent
  - fetch_emails: filters by sender_domain, marks processed on fetch,
    respects skip_processed, returns raw {id, subject, sender, body, date}
  - CLI entry point contract: parseable JSON status on every path
  - tools.py wrapper (fetch_club_studio_emails) returns the shape the agent expects
"""

from __future__ import annotations

import base64
import json
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


# ─── Make skill importable + stub google modules ─────────────────────────────

sys.path.insert(0, str(Path(__file__).parent.parent))

for mod in (
    "google", "google.oauth2", "google.oauth2.credentials",
    "google.auth", "google.auth.transport", "google.auth.transport.requests",
    "googleapiclient", "googleapiclient.discovery",
):
    sys.modules.setdefault(mod, MagicMock())

sys.modules["google.oauth2.credentials"].Credentials = MagicMock()
sys.modules["google.auth.transport.requests"].Request = MagicMock()
sys.modules["googleapiclient.discovery"].build = MagicMock()


with patch("core.keychain_secrets.load_google_secrets", return_value=None), \
     patch("core.config_loader._load_config") as _mc:
    from conftest import MINIMAL_CONFIG
    from core.config_loader import Config
    _mc.return_value = Config(MINIMAL_CONFIG)
    from features.club_studio.watcher import ClubStudioWatcher


# ─── Test config helper ──────────────────────────────────────────────────────


def _write_config(tmp_path: Path, **overrides):
    cfg = {
        "app": {"owner_phone": "+10000000000"},
        "whatsapp": {
            "groups": [
                {"id": "TEST_FAMILY@g.us", "name": "Family"},
                {"id": "TEST_CLUBSTUDIO@g.us", "name": "Club Studio"},
            ],
        },
        "calendar": {"id": "testcal@group.calendar.google.com"},
        "club_studio": {
            "enabled": True,
            "sender_domain": "clubstudiofitness.com",
            "poll_minutes": 15,
        },
    }
    cfg.update(overrides)
    (tmp_path / "config.json").write_text(json.dumps(cfg))
    (tmp_path / "household").mkdir(exist_ok=True)
    return cfg


def _make_watcher(tmp_path: Path, **overrides) -> ClubStudioWatcher:
    _write_config(tmp_path, **overrides)
    return ClubStudioWatcher(base_path=str(tmp_path))


# ─── Config backward compat ──────────────────────────────────────────────────


class TestConfigBackwardCompat:
    def test_scalar_group_id_still_reads(self, tmp_path):
        cfg = {"whatsapp": {"group_id": "LEGACY@g.us", "group_name": "L"}}
        (tmp_path / "config.json").write_text(json.dumps(cfg))
        (tmp_path / "household").mkdir()
        w = ClubStudioWatcher(base_path=str(tmp_path))
        targets = w.notify_targets()
        assert targets == [{"jid": "LEGACY@g.us", "name": "L"}]

    def test_groups_array_reads(self, tmp_path):
        w = _make_watcher(tmp_path)
        targets = w.notify_targets()
        assert len(targets) == 2
        assert targets[0]["jid"] == "TEST_FAMILY@g.us"
        assert targets[1]["jid"] == "TEST_CLUBSTUDIO@g.us"

    def test_placeholder_jid_skipped(self, tmp_path):
        cfg = {
            "whatsapp": {
                "groups": [
                    {"id": "REAL@g.us", "name": "Family"},
                    {"id": "YOUR_CLUB_STUDIO_GROUP_ID@g.us", "name": "Club Studio"},
                ],
            }
        }
        (tmp_path / "config.json").write_text(json.dumps(cfg))
        (tmp_path / "household").mkdir()
        w = ClubStudioWatcher(base_path=str(tmp_path))
        assert w.notify_targets() == [{"jid": "REAL@g.us", "name": "Family"}]

    def test_empty_config_returns_empty_targets(self, tmp_path):
        (tmp_path / "config.json").write_text(json.dumps({}))
        (tmp_path / "household").mkdir()
        w = ClubStudioWatcher(base_path=str(tmp_path))
        assert w.notify_targets() == []

    def test_config_loader_whatsapp_group_reads_array_when_no_scalar(self):
        cfg = Config({
            "whatsapp": {"groups": [{"id": "ARRAY_ONLY@g.us", "name": "A"}]}
        })
        assert cfg.whatsapp_group == "ARRAY_ONLY@g.us"

    def test_config_loader_whatsapp_group_prefers_scalar(self):
        cfg = Config({
            "whatsapp": {
                "group_id": "SCALAR@g.us",
                "groups": [{"id": "ARRAY@g.us", "name": "A"}],
            }
        })
        assert cfg.whatsapp_group == "SCALAR@g.us"

    def test_config_loader_whatsapp_groups_list(self):
        cfg = Config({
            "whatsapp": {"groups": [
                {"id": "A@g.us", "name": "AA"},
                {"id": "B@g.us", "name": "BB"},
            ]}
        })
        groups = cfg.whatsapp_groups
        assert len(groups) == 2
        assert groups[0]["name"] == "AA"


# ─── Dedup ───────────────────────────────────────────────────────────────────


class TestDedup:
    def test_mark_and_load_roundtrip(self, tmp_path):
        w = _make_watcher(tmp_path)
        w._mark_processed("msg-1")
        w._mark_processed("msg-2")
        w2 = ClubStudioWatcher(base_path=str(tmp_path))
        assert "msg-1" in w2.processed_ids
        assert "msg-2" in w2.processed_ids

    def test_500_item_cap(self, tmp_path):
        w = _make_watcher(tmp_path)
        for i in range(600):
            w.processed_ids.add(f"msg-{i}")
        w._save_processed_ids()
        w2 = ClubStudioWatcher(base_path=str(tmp_path))
        assert len(w2.processed_ids) == 500


# ─── Auth-error dedup ────────────────────────────────────────────────────────


class TestAuthErrorDedup:
    def test_not_notified_by_default(self, tmp_path):
        w = _make_watcher(tmp_path)
        assert w._is_auth_error_notified() is False

    def test_set_and_persist(self, tmp_path):
        w = _make_watcher(tmp_path)
        w._set_auth_error_notified(True)
        w2 = ClubStudioWatcher(base_path=str(tmp_path))
        assert w2._is_auth_error_notified() is True


# ─── Fetch ───────────────────────────────────────────────────────────────────


class TestFetchEmails:
    def test_fetch_returns_raw_email_dicts(self, tmp_path):
        w = _make_watcher(tmp_path)
        service = _mock_service_returning([
            _fake_gmail_msg(
                "m1",
                "Harsh, Congrats on booking your complimentary RIDE class!",
                "Congrats on booking your complimentary class at LOCATION!\n"
                "\nRIDE\n\nJuly 6, 2026\n\n9:30 AM\n",
                sender="noreply@e.fitnessintl.com",
                date_hdr="Sun, 6 Jul 2026 09:00:00 -0700",
            ),
        ])
        emails = w.fetch_emails(service)
        assert len(emails) == 1
        e = emails[0]
        assert e["id"] == "m1"
        assert "Congrats on booking" in e["subject"]
        assert "RIDE" in e["body"]
        assert e["sender"] == "noreply@e.fitnessintl.com"
        assert e["date"] == "Sun, 6 Jul 2026 09:00:00 -0700"

    def test_fetch_marks_processed_on_fetch(self, tmp_path):
        """Emails are marked processed AS THEY ARE FETCHED — not after the
        agent acts on them. This matches the school pattern: if the agent
        crashes mid-workflow we accept the loss to avoid re-notifying."""
        w = _make_watcher(tmp_path)
        service = _mock_service_returning([
            _fake_gmail_msg("m1", "Booking", "body", sender="x", date_hdr="d"),
            _fake_gmail_msg("m2", "Booking", "body", sender="x", date_hdr="d"),
        ])
        emails = w.fetch_emails(service)
        assert len(emails) == 2
        assert "m1" in w.processed_ids
        assert "m2" in w.processed_ids

    def test_fetch_skips_processed_ids(self, tmp_path):
        w = _make_watcher(tmp_path)
        w._mark_processed("m1")
        service = _mock_service_returning([
            _fake_gmail_msg("m1", "S", "b", sender="x", date_hdr="d"),
            _fake_gmail_msg("m2", "S", "b", sender="x", date_hdr="d"),
        ])
        emails = w.fetch_emails(service)
        assert [e["id"] for e in emails] == ["m2"]

    def test_fetch_uses_sender_domain_from_config(self, tmp_path):
        w = _make_watcher(tmp_path, club_studio={
            "enabled": True,
            "sender_domain": "clubstudiofitness.com",
            "poll_minutes": 15,
        })
        service = _mock_service_returning([])
        w.fetch_emails(service)
        list_call = service.users.return_value.messages.return_value.list
        query = list_call.call_args.kwargs["q"]
        assert "from:clubstudiofitness.com" in query

    def test_fetch_gmail_list_error_returns_empty(self, tmp_path):
        w = _make_watcher(tmp_path)
        service = MagicMock()
        service.users.return_value.messages.return_value.list.return_value.execute.side_effect = \
            Exception("Gmail API down")
        emails = w.fetch_emails(service)
        assert emails == []

    def test_html_only_email_body_survives_4000_char_cap(self, tmp_path):
        """The 'WaitList has been added to a class' promotion email ships
        HTML-only with a giant inline <style> block up top. Before the
        strip fix, 4000 chars of body would be entirely @font-face CSS
        and the agent had nothing to classify. Body must contain the
        actual sentence with class name / date / time within the cap.
        """
        big_css = (
            "@font-face{font-family:'Galano';src:url('"
            + "https://images.fitnessintl.com/fonts/GalanoGrotesque.woff2"
            * 40
            + "') format('woff2');}"
        ) * 5
        html = (
            "<!DOCTYPE html><html><head><style>"
            + big_css
            + "</style></head><body>"
            + "<p>Hi Harshit, You have been added to your YOGA SCULPT class "
            + "on Sat, Jul 18, 2026 at 9:15 AM.</p></body></html>"
        )
        w = _make_watcher(tmp_path)
        service = _mock_service_returning([
            _fake_gmail_msg(
                "m1",
                "WaitList has been added to a class",
                html,
                sender="info@clubstudiofitness.com",
                date_hdr="Fri, 17 Jul 2026 20:29:36 -0700",
                mime="text/html",
            ),
        ])
        emails = w.fetch_emails(service)
        assert len(emails) == 1
        body = emails[0]["body"]
        assert "@font-face" not in body
        assert "YOGA SCULPT" in body
        assert "Jul 18" in body
        assert "9:15 AM" in body

    def test_multipart_alternative_prefers_text_plain(self, tmp_path):
        """When both text/plain and text/html are present, the plain
        part wins — HTML noise must not leak into the body."""
        w = _make_watcher(tmp_path)
        service = _mock_service_returning([
            {
                "id": "m1",
                "internalDate": "1700000000000",
                "payload": {
                    "mimeType": "multipart/alternative",
                    "headers": [
                        {"name": "Subject", "value": "Congrats on booking"},
                        {"name": "From", "value": "noreply@clubstudiofitness.com"},
                        {"name": "Date", "value": "Sun, 6 Jul 2026 09:00:00 -0700"},
                    ],
                    "parts": [
                        {
                            "mimeType": "text/plain",
                            "body": {"data": _b64("RIDE July 6 9:30 AM")},
                        },
                        {
                            "mimeType": "text/html",
                            "body": {"data": _b64(
                                "<style>body{color:red}</style>"
                                "<p>RIDE July 6 9:30 AM</p>"
                            )},
                        },
                    ],
                },
            },
        ])
        emails = w.fetch_emails(service)
        body = emails[0]["body"]
        assert "RIDE July 6 9:30 AM" in body
        assert "<style>" not in body
        assert "color:red" not in body

    def test_fetch_gmail_get_error_skips_that_message(self, tmp_path):
        """One bad message shouldn't kill the whole batch."""
        w = _make_watcher(tmp_path)
        service = MagicMock()
        service.users.return_value.messages.return_value.list.return_value.execute.return_value = {
            "messages": [{"id": "m1"}, {"id": "m2"}]
        }
        def _get_side_effect(userId, id, format):
            get_execute = MagicMock()
            if id == "m1":
                get_execute.execute.side_effect = Exception("boom")
            else:
                get_execute.execute.return_value = _fake_gmail_msg(
                    "m2", "S", "body", sender="x", date_hdr="d"
                )
            return get_execute
        service.users.return_value.messages.return_value.get.side_effect = _get_side_effect
        emails = w.fetch_emails(service)
        assert [e["id"] for e in emails] == ["m2"]


# ─── CLI entry point ─────────────────────────────────────────────────────────


class TestCliEntryPoint:
    """The __main__ block is a debug helper. It must emit parseable JSON
    on every branch so scripting on top of it stays sane."""

    def test_disabled_prints_status_disabled(self, tmp_path, capsys, monkeypatch):
        _write_config(tmp_path, club_studio={
            "enabled": False, "sender_domain": "clubstudiofitness.com",
            "poll_minutes": 15,
        })
        from features.club_studio import watcher as cs_watcher
        monkeypatch.setattr(cs_watcher, "SKILL_DIR", None, raising=False)
        with patch(
            "core.config_loader.SKILL_DIR", str(tmp_path)
        ), patch.object(sys, "argv", ["watcher"]):
            rc = cs_watcher._cli_main()
        out = capsys.readouterr().out
        parsed = json.loads(out.strip().splitlines()[-1])
        assert rc == 0
        assert parsed["status"] == "disabled"

    def test_targets_flag_prints_targets(self, tmp_path, capsys):
        _write_config(tmp_path)
        from features.club_studio import watcher as cs_watcher
        with patch(
            "core.config_loader.SKILL_DIR", str(tmp_path)
        ), patch.object(sys, "argv", ["watcher", "--targets"]):
            rc = cs_watcher._cli_main()
        parsed = json.loads(capsys.readouterr().out.strip())
        assert rc == 0
        assert len(parsed["targets"]) == 2
        assert parsed["targets"][0]["jid"] == "TEST_FAMILY@g.us"

    def test_crash_still_emits_parseable_json(self, tmp_path, capsys):
        """CLAUDE.md principle 4: cron entry always emits parseable status."""
        from features.club_studio import watcher as cs_watcher
        with patch(
            "core.config_loader.SKILL_DIR", str(tmp_path)
        ), patch.object(
            cs_watcher, "ClubStudioWatcher", side_effect=RuntimeError("kaboom")
        ), patch.object(sys, "argv", ["watcher"]):
            rc = cs_watcher._cli_main()
        out = capsys.readouterr().out
        parsed = json.loads(out.strip().splitlines()[-1])
        assert rc == 1
        assert parsed["status"] == "crashed"
        assert "kaboom" in parsed["error"]


# ─── tools.py wrapper (agent-facing shape) ───────────────────────────────────


class TestToolsWrapper:
    def test_wrapper_shape_disabled(self, tmp_path, monkeypatch):
        _write_config(tmp_path, club_studio={
            "enabled": False, "sender_domain": "clubstudiofitness.com",
            "poll_minutes": 15,
        })
        monkeypatch.setattr(
            "features.club_studio.watcher.load_google_secrets",
            lambda: None,
        )
        with patch("tools.SKILL_DIR", str(tmp_path)):
            import tools
            out = json.loads(tools.fetch_club_studio_emails())
        assert out["status"] == "disabled"
        assert out["emails"] == []
        assert out["targets"] == []

    def test_wrapper_shape_emails_found(self, tmp_path, monkeypatch):
        _write_config(tmp_path)
        fake_service = _mock_service_returning([
            _fake_gmail_msg(
                "m1", "Booking Confirmation", "class body",
                sender="x", date_hdr="d",
            ),
        ])

        # Patch the watcher class Google-auth path
        from features.club_studio import watcher as cs_watcher
        monkeypatch.setattr(
            cs_watcher.ClubStudioWatcher, "get_gmail_service",
            lambda self: fake_service,
        )

        with patch("tools.SKILL_DIR", str(tmp_path)):
            import tools
            out = json.loads(tools.fetch_club_studio_emails())
        assert out["status"] == "emails_found"
        assert out["count"] == 1
        assert out["emails"][0]["id"] == "m1"
        assert len(out["targets"]) == 2

    def test_wrapper_hard_caps_count_at_one(self, tmp_path, monkeypatch):
        """Even if the caller passes count=5, only one email comes back —
        the hard cap is enforced inside the wrapper to work around the
        gemma4:26b silent-stop-after-first-item failure mode."""
        _write_config(tmp_path)
        fake_service = _mock_service_returning([
            _fake_gmail_msg("m1", "Booking", "b", sender="x", date_hdr="d"),
            _fake_gmail_msg("m2", "Booking", "b", sender="x", date_hdr="d"),
            _fake_gmail_msg("m3", "Booking", "b", sender="x", date_hdr="d"),
        ])
        from features.club_studio import watcher as cs_watcher
        monkeypatch.setattr(
            cs_watcher.ClubStudioWatcher, "get_gmail_service",
            lambda self: fake_service,
        )

        with patch("tools.SKILL_DIR", str(tmp_path)):
            import tools
            out = json.loads(tools.fetch_club_studio_emails(count=5))
        # Cap applied even though caller asked for 5
        assert out["count"] == 1


# ─── Helpers ─────────────────────────────────────────────────────────────────


def _b64(text: str) -> str:
    return base64.urlsafe_b64encode(text.encode()).decode()


def _fake_gmail_msg(
    msg_id: str,
    subject: str,
    body: str,
    sender: str = "noreply@clubstudiofitness.com",
    date_hdr: str = "Mon, 6 Jul 2026 12:00:00 -0700",
    mime: str = "text/plain",
) -> dict:
    return {
        "id": msg_id,
        "internalDate": "1700000000000",
        "payload": {
            "mimeType": mime,
            "headers": [
                {"name": "Subject", "value": subject},
                {"name": "From", "value": sender},
                {"name": "Date", "value": date_hdr},
            ],
            "body": {"data": _b64(body)},
        },
    }


def _mock_service_returning(messages: list) -> MagicMock:
    service = MagicMock()
    list_execute = MagicMock()
    list_execute.execute.return_value = {
        "messages": [{"id": m["id"]} for m in messages]
    }
    service.users.return_value.messages.return_value.list.return_value = list_execute

    by_id = {m["id"]: m for m in messages}

    def _get(userId, id, format):  # noqa: N803 — Gmail API kwarg names
        get_execute = MagicMock()
        get_execute.execute.return_value = by_id[id]
        return get_execute

    service.users.return_value.messages.return_value.get.side_effect = _get
    return service
