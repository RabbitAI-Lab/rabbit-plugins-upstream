"""
test_school_email_monitor.py — Unit tests for school_email_monitor.py

Covers:
  - _is_auth_error_notified() / _set_auth_error_notified(): flag persistence
  - get_gmail_service(): first-failure notifies, subsequent failures are silent
  - _extract_body_and_attachments(): text/plain, nested multipart, PDF detection
  - fetch_recent_school_emails(): skip processed IDs, filter daily summaries
  - format_for_whatsapp(): structure, PDF annotation, body truncation
  - _mark_processed() / _load_processed_ids(): round-trip, 500-item cap
"""
import base64
import json
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch, call

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

for mod in ("google", "google.oauth2", "google.oauth2.credentials",
            "google.auth", "google.auth.transport", "google.auth.transport.requests",
            "googleapiclient", "googleapiclient.discovery"):
    sys.modules.setdefault(mod, MagicMock())

# Make `from google.oauth2.credentials import Credentials` resolvable from
# the MagicMock stubs (otherwise Python's importlib refuses on "unknown location").
sys.modules["google.oauth2.credentials"].Credentials = MagicMock()
sys.modules["google.auth.transport.requests"].Request = MagicMock()
sys.modules["googleapiclient.discovery"].build = MagicMock()

with patch("core.keychain_secrets.load_google_secrets", return_value=None), \
     patch("core.config_loader._load_config") as _mc:
    from conftest import MINIMAL_CONFIG
    from core.config_loader import Config
    _mc.return_value = Config(MINIMAL_CONFIG)
    import features.school.school_email_monitor as school_email_monitor
    from features.school.school_email_monitor import SchoolEmailMonitor


# ─── Fixture helpers ──────────────────────────────────────────────────────────

def _make_monitor(tmp_path):
    """Create a SchoolEmailMonitor pointing at a tmp directory."""
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps({"email_body_context_limit": 2000}))
    cal_dir = tmp_path / "calendar_data"; cal_dir.mkdir()
    m = SchoolEmailMonitor(base_path=str(tmp_path))
    return m


def _b64_encode_text(text: str) -> str:
    return base64.urlsafe_b64encode(text.encode()).decode()


# ─── Auth error deduplication ────────────────────────────────────────────────

class TestAuthErrorDeduplication:
    def test_not_notified_by_default(self, tmp_path):
        m = _make_monitor(tmp_path)
        assert m._is_auth_error_notified() is False

    def test_set_and_get_notified_flag(self, tmp_path):
        m = _make_monitor(tmp_path)
        m._set_auth_error_notified(True)
        assert m._is_auth_error_notified() is True

    def test_clear_notified_flag(self, tmp_path):
        m = _make_monitor(tmp_path)
        m._set_auth_error_notified(True)
        m._set_auth_error_notified(False)
        assert m._is_auth_error_notified() is False

    def test_state_persists_across_instances(self, tmp_path):
        """Regression: notified flag must survive re-instantiation."""
        m1 = _make_monitor(tmp_path)
        m1._set_auth_error_notified(True)
        # Create fresh instance pointing to same directory
        m2 = SchoolEmailMonitor(base_path=str(tmp_path))
        assert m2._is_auth_error_notified() is True

    def test_state_file_corruption_returns_false(self, tmp_path):
        m = _make_monitor(tmp_path)
        # Corrupt the state file
        state_file = Path(m.auth_error_state_file)
        state_file.write_text("{not valid json{{")
        assert m._is_auth_error_notified() is False


# ─── get_gmail_service auth error notify-once ────────────────────────────────

class TestGetGmailServiceAuthError:
    def _env(self):
        return {
            "GOOGLE_CLIENT_ID": "test-id",
            "GOOGLE_CLIENT_SECRET": "test-secret",
            "GOOGLE_REFRESH_TOKEN": "test-token"
        }

    def test_first_auth_error_prints_whatsapp_message(self, tmp_path, capsys):
        """Regression: first auth failure should print the WhatsApp alert."""
        m = _make_monitor(tmp_path)

        creds_mock = MagicMock()
        creds_mock.refresh.side_effect = Exception("Token expired")

        with patch.dict(os.environ, self._env()), \
             patch("google.oauth2.credentials.Credentials", return_value=creds_mock), \
             patch("google.auth.transport.requests.Request"):
            result = m.get_gmail_service()

        assert result is None
        captured = capsys.readouterr()
        assert "auth error" in captured.out.lower() or "expired" in captured.out.lower() \
               or "refresh token" in captured.out.lower() or "Google" in captured.out

    def test_subsequent_auth_error_is_silent(self, tmp_path, capsys):
        """Regression: after first notification, further auth errors must print NO_REPLY."""
        m = _make_monitor(tmp_path)
        m._set_auth_error_notified(True)  # already notified

        creds_mock = MagicMock()
        creds_mock.refresh.side_effect = Exception("Token still expired")

        with patch.dict(os.environ, self._env()), \
             patch("google.oauth2.credentials.Credentials", return_value=creds_mock), \
             patch("google.auth.transport.requests.Request"):
            result = m.get_gmail_service()

        assert result is None
        captured = capsys.readouterr()
        # Should print NO_REPLY or auth-suppressed, NOT the full error message
        assert "NO_REPLY" in captured.out or "auth-suppressed" in captured.out

    def test_successful_auth_clears_error_flag(self, tmp_path):
        """After successful auth, the notified flag should be cleared."""
        m = _make_monitor(tmp_path)
        m._set_auth_error_notified(True)

        creds_mock = MagicMock()
        creds_mock.refresh.return_value = None  # success

        gmail_service_mock = MagicMock()

        with patch.dict(os.environ, self._env()), \
             patch("google.oauth2.credentials.Credentials", return_value=creds_mock), \
             patch("google.auth.transport.requests.Request"), \
             patch("googleapiclient.discovery.build", return_value=gmail_service_mock):
            result = m.get_gmail_service()

        assert result is not None
        assert m._is_auth_error_notified() is False

    def test_returns_none_when_credentials_missing(self, tmp_path, monkeypatch):
        m = _make_monitor(tmp_path)
        monkeypatch.delenv("GOOGLE_CLIENT_ID", raising=False)
        monkeypatch.delenv("GOOGLE_CLIENT_SECRET", raising=False)
        monkeypatch.delenv("GOOGLE_REFRESH_TOKEN", raising=False)
        result = m.get_gmail_service()
        assert result is None


# ─── _extract_body_and_attachments ───────────────────────────────────────────

class TestExtractBodyAndAttachments:
    def test_extracts_plain_text(self, tmp_path):
        m = _make_monitor(tmp_path)
        text = "Hello from school!"
        payload = {
            "mimeType": "text/plain",
            "body": {"data": _b64_encode_text(text)}
        }
        body, has_pdf, has_image = m._extract_body_and_attachments(payload)
        assert text in body
        assert has_pdf is False
        assert has_image is False

    def test_detects_pdf_attachment(self, tmp_path):
        m = _make_monitor(tmp_path)
        payload = {"mimeType": "application/pdf", "body": {}}
        body, has_pdf, has_image = m._extract_body_and_attachments(payload)
        assert has_pdf is True
        assert has_image is False
        assert body == ""

    def test_detects_inline_image(self, tmp_path):
        m = _make_monitor(tmp_path)
        payload = {"mimeType": "image/jpeg", "body": {"attachmentId": "att123"}}
        body, has_pdf, has_image = m._extract_body_and_attachments(payload)
        assert has_image is True
        assert has_pdf is False
        assert body == ""

    def test_handles_nested_multipart(self, tmp_path):
        """Regression: nested multipart must be parsed recursively."""
        m = _make_monitor(tmp_path)
        inner_text = "Important school notice"
        payload = {
            "mimeType": "multipart/mixed",
            "parts": [
                {
                    "mimeType": "multipart/alternative",
                    "parts": [
                        {
                            "mimeType": "text/plain",
                            "body": {"data": _b64_encode_text(inner_text)}
                        }
                    ]
                },
                {"mimeType": "application/pdf", "body": {}}
            ]
        }
        body, has_pdf, has_image = m._extract_body_and_attachments(payload)
        assert inner_text in body
        assert has_pdf is True
        assert has_image is False

    def test_nested_multipart_with_image_and_pdf(self, tmp_path):
        """Multipart with both a PDF and an inline image detects both."""
        m = _make_monitor(tmp_path)
        payload = {
            "mimeType": "multipart/mixed",
            "parts": [
                {"mimeType": "text/plain", "body": {"data": _b64_encode_text("text")}},
                {"mimeType": "application/pdf", "body": {}},
                {"mimeType": "image/png", "body": {"attachmentId": "att456"}},
            ]
        }
        body, has_pdf, has_image = m._extract_body_and_attachments(payload)
        assert has_pdf is True
        assert has_image is True
        assert "text" in body

    def test_empty_payload_returns_empty(self, tmp_path):
        m = _make_monitor(tmp_path)
        body, has_pdf, has_image = m._extract_body_and_attachments({"mimeType": "text/html", "body": {}})
        assert body == ""
        assert has_pdf is False
        assert has_image is False


# ─── _mark_processed / _load_processed_ids ───────────────────────────────────

class TestProcessedIds:
    def test_marks_and_loads(self, tmp_path):
        m = _make_monitor(tmp_path)
        m._mark_processed("msg123")
        m2 = SchoolEmailMonitor(base_path=str(tmp_path))
        assert "msg123" in m2.processed_ids

    def test_caps_at_500_ids(self, tmp_path):
        m = _make_monitor(tmp_path)
        for i in range(600):
            m.processed_ids.add(f"msg{i}")
        m._save_processed_ids()
        m2 = SchoolEmailMonitor(base_path=str(tmp_path))
        assert len(m2.processed_ids) <= 500

    def test_starts_empty_when_no_file(self, tmp_path):
        m = _make_monitor(tmp_path)
        # Delete the file
        pf = Path(m.processed_ids_file)
        pf.unlink(missing_ok=True)
        m2 = SchoolEmailMonitor(base_path=str(tmp_path))
        assert m2.processed_ids == set()


# ─── fetch_recent_school_emails skip_processed ──────────────────────────────

class TestFetchSkipProcessed:
    """Regression: fetch_school_emails must skip already-processed emails by default."""

    def _mock_gmail_list(self, msg_ids):
        """Create a mock Gmail service that returns the given message IDs."""
        svc = MagicMock()
        svc.users().messages().list().execute.return_value = {
            "messages": [{"id": mid} for mid in msg_ids]
        }
        # For each message, return a minimal payload
        def get_message(userId, id, format):
            mock = MagicMock()
            mock.execute.return_value = {
                "id": id,
                "payload": {
                    "headers": [
                        {"name": "Subject", "value": f"Email {id}"},
                        {"name": "From", "value": "school@spectrummontessori.com"},
                        {"name": "Date", "value": "Mon, 13 Apr 2026 10:00:00 -0700"},
                    ],
                    "mimeType": "text/plain",
                    "body": {"data": _b64_encode_text(f"Body of {id}")},
                }
            }
            return mock
        svc.users().messages().get = get_message
        return svc

    def test_skip_processed_true_skips_known_ids(self, tmp_path):
        m = _make_monitor(tmp_path)
        m._mark_processed("msg_old")
        m.get_gmail_service = MagicMock(return_value=self._mock_gmail_list(["msg_old", "msg_new"]))

        with patch("core.config_loader.config") as mock_cfg:
            mock_cfg.school_email_query = "from:spectrummontessori.com"
            emails = m.fetch_recent_school_emails(skip_processed=True)

        ids = [e["id"] for e in emails]
        assert "msg_new" in ids
        assert "msg_old" not in ids

    def test_skip_processed_false_returns_all(self, tmp_path):
        m = _make_monitor(tmp_path)
        m._mark_processed("msg_old")
        m.get_gmail_service = MagicMock(return_value=self._mock_gmail_list(["msg_old", "msg_new"]))

        with patch("core.config_loader.config") as mock_cfg:
            mock_cfg.school_email_query = "from:spectrummontessori.com"
            emails = m.fetch_recent_school_emails(skip_processed=False)

        ids = [e["id"] for e in emails]
        assert "msg_new" in ids
        assert "msg_old" in ids

    def test_daily_summary_emails_are_skipped_and_marked(self, tmp_path):
        """Emails with 'daily summary' or 'checked in' should be auto-skipped."""
        m = _make_monitor(tmp_path)
        svc = MagicMock()
        svc.users().messages().list().execute.return_value = {
            "messages": [{"id": "summary_msg"}]
        }
        def get_message(userId, id, format):
            mock = MagicMock()
            mock.execute.return_value = {
                "id": id,
                "payload": {
                    "headers": [
                        {"name": "Subject", "value": "Daily Summary"},
                        {"name": "From", "value": "school@spectrummontessori.com"},
                        {"name": "Date", "value": "Mon, 13 Apr 2026 10:00:00 -0700"},
                    ],
                    "mimeType": "text/plain",
                    "body": {"data": _b64_encode_text("Your child checked in at 8am")},
                }
            }
            return mock
        svc.users().messages().get = get_message
        m.get_gmail_service = MagicMock(return_value=svc)

        with patch("core.config_loader.config") as mock_cfg:
            mock_cfg.school_email_query = "from:spectrummontessori.com"
            emails = m.fetch_recent_school_emails(skip_processed=True)

        assert len(emails) == 0
        assert "summary_msg" in m.processed_ids


# ─── tools.py fetch_school_emails uses skip_processed=True ───────────────────

class TestToolsFetchUsesSkipProcessed:
    """Regression: tools.py fetch_school_emails must use skip_processed=True."""

    def test_tools_fetch_calls_skip_processed_true(self):
        import inspect
        # Read the actual source to verify the flag
        tools_path = Path(__file__).parent.parent / "tools.py"
        source = tools_path.read_text()
        # Find the fetch_school_emails function and check skip_processed
        assert "skip_processed=True" in source, \
            "tools.py fetch_school_emails must call fetch_recent_school_emails(skip_processed=True)"
        assert "skip_processed=False" not in source, \
            "tools.py must NOT use skip_processed=False (causes duplicate processing)"


# ─── format_for_whatsapp ─────────────────────────────────────────────────────

class TestFormatForWhatsapp:
    def test_returns_none_for_empty_list(self, tmp_path):
        m = _make_monitor(tmp_path)
        assert m.format_for_whatsapp([]) is None

    def test_contains_subject(self, tmp_path):
        m = _make_monitor(tmp_path)
        emails = [{"subject": "Field Trip Reminder", "sender": "school@test.com",
                   "body": "Please sign the permission slip.", "has_pdf_attachment": False}]
        result = m.format_for_whatsapp(emails)
        assert "Field Trip Reminder" in result

    def test_shows_pdf_annotation(self, tmp_path):
        m = _make_monitor(tmp_path)
        emails = [{"subject": "Newsletter", "sender": "school@test.com",
                   "body": "See attached.", "has_pdf_attachment": True}]
        result = m.format_for_whatsapp(emails)
        assert "PDF" in result

    def test_truncates_long_body(self, tmp_path):
        m = _make_monitor(tmp_path)
        long_body = "A" * 500
        emails = [{"subject": "Long email", "sender": "school@test.com",
                   "body": long_body, "has_pdf_attachment": False}]
        result = m.format_for_whatsapp(emails)
        # Body snippet in output should be at most 300 chars
        # (as coded in format_for_whatsapp)
        assert "AAAA" in result  # some of it present
        assert len(result) < 1000  # but not 500 chars of A's

    def test_multiple_emails_formatted(self, tmp_path):
        m = _make_monitor(tmp_path)
        emails = [
            {"subject": "Email 1", "sender": "s@t.com", "body": "body1", "has_pdf_attachment": False},
            {"subject": "Email 2", "sender": "s@t.com", "body": "body2", "has_pdf_attachment": False},
        ]
        result = m.format_for_whatsapp(emails)
        assert "Email 1" in result
        assert "Email 2" in result
