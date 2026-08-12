#!/usr/bin/env python3
"""Offline tests for smtp_send.py; no real SMTP server or credentials are used."""

from __future__ import annotations

import importlib.util
import io
import json
import os
import stat
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("smtp_send.py")
SPEC = importlib.util.spec_from_file_location("smtp_send", MODULE_PATH)
assert SPEC and SPEC.loader
smtp_send = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(smtp_send)


class FakeSMTP:
    instances = []
    refused = {}

    def __init__(self, host, port, timeout=None, context=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.context = context
        self.calls = []
        self.sent_messages = []
        FakeSMTP.instances.append(self)

    def starttls(self, context=None):
        self.calls.append(("starttls", bool(context)))
        return (220, b"ready")

    def login(self, user, password):
        self.calls.append(("login", user, password))
        return (235, b"ok")

    def send_message(self, message, from_addr=None, to_addrs=None):
        self.calls.append(("send_message", from_addr, tuple(to_addrs or [])))
        self.sent_messages.append(message)
        return dict(FakeSMTP.refused)

    def quit(self):
        self.calls.append(("quit",))
        return (221, b"bye")


class SmtpSendTests(unittest.TestCase):
    def setUp(self):
        FakeSMTP.instances.clear()
        FakeSMTP.refused = {}
        self.output_root_context = tempfile.TemporaryDirectory()
        self.output_root = Path(self.output_root_context.name)
        self.env = {
            "EMAIL_SMTP_HOST": "smtp.example.com",
            "EMAIL_ADDRESS": "demo@example.com",
            "EMAIL_PASSWORD": "test-only-secret",
            "EMAIL_SMTP_FROM": "Demo Sender <demo@example.com>",
            "EMAIL_ASSISTANT_OUTPUT_ROOT": str(self.output_root),
            "EMAIL_ASSISTANT_DISABLE_LOCAL_ENV": "true",
        }

    def tearDown(self):
        self.output_root_context.cleanup()

    def run_main(self, argv, extra_env=None):
        env = dict(self.env)
        if extra_env:
            env.update(extra_env)
        output = io.StringIO()
        with patch.dict(os.environ, env, clear=True), patch.object(
            smtp_send.smtplib, "SMTP_SSL", FakeSMTP
        ), patch.object(smtp_send.smtplib, "SMTP", FakeSMTP), redirect_stdout(output), self.assertRaises(SystemExit) as stopped:
            smtp_send.main(argv)
        return stopped.exception.code, json.loads(output.getvalue()), output.getvalue()

    def test_health_masks_account_and_reports_disabled_send(self):
        code, result, serialized = self.run_main(["health"])

        self.assertEqual(code, 0)
        self.assertEqual(result["account"], "d***@example.com")
        self.assertFalse(result["send_enabled"])
        self.assertNotIn("test-only-secret", serialized)
        self.assertIn(("login", "demo@example.com", "test-only-secret"), FakeSMTP.instances[0].calls)

    def test_local_scripts_env_is_loaded_without_overriding_process_env(self):
        with tempfile.TemporaryDirectory() as directory:
            script_dir = Path(directory)
            module_copy = script_dir / "smtp_send.py"
            shutil.copy2(MODULE_PATH, module_copy)
            script_dir.joinpath(".env").write_text(
                "EMAIL_SMTP_HOST=smtp.local.example\n"
                "EMAIL_SMTP_USER=local@example.com\n"
                "EMAIL_SMTP_PASSWORD=local-secret\n"
                "EMAIL_SMTP_FROM='Local Sender <local@example.com>'\n"
                "EMAIL_SMTP_PORT=465\n",
                encoding="utf-8",
            )
            spec = importlib.util.spec_from_file_location("smtp_send_local_env", module_copy)
            assert spec and spec.loader
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            output = io.StringIO()
            with patch.dict(os.environ, {"EMAIL_ADDRESS": "process@example.com"}, clear=True), patch.object(
                module.smtplib, "SMTP_SSL", FakeSMTP
            ), redirect_stdout(output), self.assertRaises(SystemExit) as stopped:
                module.main(["health"])

        self.assertEqual(stopped.exception.code, 0)
        result = json.loads(output.getvalue())
        self.assertEqual(result["host"], "smtp.local.example")
        self.assertEqual(result["account"], "p***@example.com")
        self.assertIn(("login", "process@example.com", "local-secret"), FakeSMTP.instances[-1].calls)

    def test_compose_saves_private_draft_without_printing_content(self):
        code, result, serialized = self.run_main([
            "compose",
            "--to", "ops@example.com",
            "--cc", "lead@example.com",
            "--subject", "Release approval",
            "--body", "Please approve release CR-2048.",
            "--reply-to-source-ref", "imap:INBOX:42",
        ])

        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "draft")
        self.assertEqual(result["recipient_count"], 2)
        self.assertTrue(result["confirmation_required"])
        self.assertNotIn("confirmation_token", result)
        self.assertNotIn("Release approval", serialized)
        self.assertNotIn("ops@example.com", serialized)
        self.assertNotIn("CR-2048", serialized)
        draft_path = Path(result["saved_json"]["path"])
        self.assertEqual(0o600, stat.S_IMODE(draft_path.stat().st_mode))
        draft = json.loads(draft_path.read_text(encoding="utf-8"))
        self.assertEqual(draft["subject"], "Release approval")
        self.assertEqual(draft["body_text"], "Please approve release CR-2048.")
        self.assertEqual(draft["reply_to_source_ref"], "imap:INBOX:42")
        self.assertIn("confirmation_token", draft)

    def test_send_requires_enabled_flag_and_matching_confirmation(self):
        _, draft_result, _ = self.run_main([
            "compose", "--to", "ops@example.com", "--subject", "Subject", "--body", "Body"
        ])
        draft_path = Path(draft_result["saved_json"]["path"])
        token = json.loads(draft_path.read_text(encoding="utf-8"))["confirmation_token"]

        code, disabled, _ = self.run_main([
            "send", "--draft-json", str(draft_path), "--confirm-send", token
        ])
        self.assertEqual(code, 2)
        self.assertEqual(disabled["error"]["code"], "send_disabled")

        code, mismatch, _ = self.run_main([
            "send", "--draft-json", str(draft_path), "--confirm-send", "wrong"
        ], extra_env={"EMAIL_SMTP_SEND_ENABLED": "true"})
        self.assertEqual(code, 2)
        self.assertEqual(mismatch["error"]["code"], "confirmation_required")
        self.assertEqual(len(FakeSMTP.instances), 0)

    def test_send_uses_smtp_and_marks_draft_sent_without_printing_content(self):
        _, draft_result, _ = self.run_main([
            "compose",
            "--to", "ops@example.com",
            "--bcc", "audit@example.com",
            "--subject", "Subject",
            "--body", "Sensitive body",
        ])
        draft_path = Path(draft_result["saved_json"]["path"])
        token = json.loads(draft_path.read_text(encoding="utf-8"))["confirmation_token"]

        code, result, serialized = self.run_main([
            "send",
            "--draft-json", str(draft_path),
            "--confirm-send", token,
        ], extra_env={"EMAIL_SMTP_SEND_ENABLED": "true"})

        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "sent")
        self.assertEqual(result["recipient_count"], 2)
        self.assertNotIn("Subject", serialized)
        self.assertNotIn("Sensitive body", serialized)
        self.assertNotIn("ops@example.com", serialized)
        sender = FakeSMTP.instances[0]
        self.assertIn(("send_message", "Demo Sender <demo@example.com>", ("ops@example.com", "audit@example.com")), sender.calls)
        self.assertEqual(json.loads(draft_path.read_text(encoding="utf-8"))["status"], "sent")

        code, repeat, _ = self.run_main([
            "send",
            "--draft-json", str(draft_path),
            "--confirm-send", token,
        ], extra_env={"EMAIL_SMTP_SEND_ENABLED": "true"})
        self.assertEqual(code, 2)
        self.assertEqual(repeat["error"]["code"], "already_sent")

    def test_partial_send_marks_draft_submitted_and_blocks_retry(self):
        _, draft_result, _ = self.run_main([
            "compose",
            "--to", "ops@example.com, bad@example.com",
            "--subject", "Subject",
            "--body", "Body",
        ])
        draft_path = Path(draft_result["saved_json"]["path"])
        token = json.loads(draft_path.read_text(encoding="utf-8"))["confirmation_token"]
        FakeSMTP.refused = {"bad@example.com": (550, b"no such user")}

        code, result, _ = self.run_main([
            "send",
            "--draft-json", str(draft_path),
            "--confirm-send", token,
        ], extra_env={"EMAIL_SMTP_SEND_ENABLED": "true"})

        self.assertEqual(code, 2)
        self.assertEqual(result["error"]["code"], "partial_send")
        self.assertIn("saved_json", result["error"])
        self.assertEqual(json.loads(draft_path.read_text(encoding="utf-8"))["status"], "partial_sent")

        FakeSMTP.refused = {}
        code, repeat, _ = self.run_main([
            "send",
            "--draft-json", str(draft_path),
            "--confirm-send", token,
        ], extra_env={"EMAIL_SMTP_SEND_ENABLED": "true"})
        self.assertEqual(code, 2)
        self.assertEqual(repeat["error"]["code"], "already_sent")

    def test_output_directory_cannot_escape_authorized_root(self):
        with tempfile.TemporaryDirectory() as outside:
            code, result, _ = self.run_main([
                "compose", "--to", "ops@example.com", "--subject", "Subject", "--body", "Body",
                "--output-dir", outside,
            ])
        self.assertEqual(code, 2)
        self.assertEqual(result["error"]["code"], "invalid_request")


if __name__ == "__main__":
    unittest.main()
