#!/usr/bin/env python3
"""Offline tests for smtp_workflow.py; no real SMTP server or credentials are used."""

from __future__ import annotations

import importlib.util
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).with_name("smtp_workflow.py")
SPEC = importlib.util.spec_from_file_location("smtp_workflow", MODULE_PATH)
assert SPEC and SPEC.loader
smtp_workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(smtp_workflow)


class FakeSMTP:
    instances = []

    def __init__(self, host, port, timeout=None, context=None):
        self.calls = []
        FakeSMTP.instances.append(self)

    def login(self, user, password):
        self.calls.append(("login", user, password))
        return (235, b"ok")

    def send_message(self, message, from_addr=None, to_addrs=None):
        self.calls.append(("send_message", from_addr, tuple(to_addrs or [])))
        return {}

    def quit(self):
        self.calls.append(("quit",))
        return (221, b"bye")


class SmtpWorkflowTests(unittest.TestCase):
    def setUp(self):
        FakeSMTP.instances.clear()
        self.output_root_context = tempfile.TemporaryDirectory()
        self.output_root = Path(self.output_root_context.name)
        self.env = {
            "EMAIL_SMTP_HOST": "smtp.example.com",
            "EMAIL_ADDRESS": "demo@example.com",
            "EMAIL_PASSWORD": "test-only-secret",
            "EMAIL_SMTP_FROM": "Demo Sender <demo@example.com>",
            "EMAIL_ASSISTANT_OUTPUT_ROOT": str(self.output_root),
            "EMAIL_SMTP_SEND_ENABLED": "true",
        }

    def tearDown(self):
        self.output_root_context.cleanup()

    def run_main(self, argv, extra_env=None):
        env = dict(self.env)
        if extra_env:
            env.update(extra_env)
        output = io.StringIO()
        with patch.dict(os.environ, env, clear=True), patch.object(
            smtp_workflow.smtp_send.smtplib, "SMTP_SSL", FakeSMTP
        ), redirect_stdout(output), self.assertRaises(SystemExit) as stopped:
            smtp_workflow.main(argv)
        return stopped.exception.code, json.loads(output.getvalue()), output.getvalue()

    def test_prepare_creates_draft_and_prints_review_without_token(self):
        code, result, serialized = self.run_main([
            "prepare",
            "--to", "ops@example.com",
            "--subject", "Re: Meeting",
            "--body", "收到，我会准时参加会议。",
            "--reply-to-source-ref", "imap:INBOX:42",
        ])

        self.assertEqual(code, 0)
        self.assertEqual(result["status"], "review_required")
        self.assertEqual(result["review"]["to"], ["ops@example.com"])
        self.assertEqual(result["review"]["subject"], "Re: Meeting")
        self.assertEqual(result["review"]["body_text"], "收到，我会准时参加会议。")
        self.assertEqual(result["review"]["reply_to_source_ref"], "imap:INBOX:42")
        self.assertNotIn("confirmation_token", serialized)
        draft = json.loads(Path(result["saved_json"]["path"]).read_text(encoding="utf-8"))
        self.assertIn("confirmation_token", draft)

    def test_review_prints_existing_draft_content_without_token(self):
        _, prepared, _ = self.run_main([
            "prepare", "--to", "ops@example.com", "--subject", "Subject", "--body", "Body"
        ])

        code, result, serialized = self.run_main([
            "review", "--draft-json", prepared["saved_json"]["path"]
        ])

        self.assertEqual(code, 0)
        self.assertEqual(result["review"]["body_text"], "Body")
        self.assertNotIn("confirmation_token", serialized)

    def test_confirm_requires_review_flag_and_sends_existing_draft(self):
        _, prepared, _ = self.run_main([
            "prepare", "--to", "ops@example.com", "--subject", "Subject", "--body", "Body"
        ])
        draft_path = prepared["saved_json"]["path"]

        code, rejected, _ = self.run_main(["confirm", "--draft-json", draft_path])
        self.assertEqual(code, 2)
        self.assertEqual(rejected["error"]["code"], "confirmation_required")
        self.assertFalse(FakeSMTP.instances)

        code, sent, serialized = self.run_main([
            "confirm", "--draft-json", draft_path, "--review-confirmed"
        ])
        self.assertEqual(code, 0)
        self.assertEqual(sent["status"], "sent")
        self.assertNotIn("Subject", serialized)
        self.assertNotIn("ops@example.com", serialized)
        self.assertIn(("send_message", "Demo Sender <demo@example.com>", ("ops@example.com",)), FakeSMTP.instances[0].calls)


if __name__ == "__main__":
    unittest.main()
