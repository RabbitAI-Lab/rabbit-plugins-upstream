#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import io
import json
import os
import random
import string
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
import rendezvous as rv

PUBKEY = "11" * 32
# Fixed non-production fixture; never used as a real credential.
SECRET = "coordination-secret-32-bytes-minimum-value"  # nosec B105


def ns(**values):
    defaults = {
        "output": None,
        "force_output": False,
        "ack_authorized": True,
        "hmac_env": None,
        "allow_unsigned_card": False,
        "require_hmac": False,
        "allow_expired": False,
    }
    defaults.update(values)
    return argparse.Namespace(**defaults)


class RendezvousTests(unittest.TestCase):
    def make_card(
        self,
        root: Path,
        *,
        signed: bool = True,
        expires_minutes: int = 30,
        output_name: str = "card.json",
        allow_lan_client_listener: bool = False,
    ):
        pub = root / "server.pub"
        pub.write_text(PUBKEY + "\n", encoding="utf-8")
        out = root / output_name
        args = ns(
            agent_id="server-agent-a",
            domain="t.example.com",
            pubkey_file=str(pub),
            listen="0.0.0.0:5300",
            upstream="127.0.0.1:8000",
            expires_minutes=expires_minutes,
            authorization_ref="LAB-2026-001",
            purpose="authorized agent message service",
            hmac_env="LINK_SECRET" if signed else None,
            allow_nonloopback_upstream=False,
            allow_lan_client_listener=allow_lan_client_listener,
            output=str(out),
        )
        env = {"LINK_SECRET": SECRET} if signed else {}
        with patch.dict(os.environ, env, clear=False), contextlib.redirect_stdout(io.StringIO()):
            rv.cmd_server_card(args)
        return out, json.loads(out.read_text(encoding="utf-8"))

    def client_args(self, root: Path, card_path: Path, card: dict, **overrides):
        values = {
            "card": str(card_path),
            "expected_fingerprint": card["server_key_fingerprint"],
            "hmac_env": "LINK_SECRET" if "coordination_hmac_sha256" in card else None,
            "local_listen": "127.0.0.1:7000",
            "allow_lan_listener": False,
            "transport": "udp",
            "resolver": "192.0.2.53:53",
            "pubkey_file": str(root / "client-server.pub"),
            "dnstt_client": "dnstt-client",
            "allow_unsigned_card": False,
        }
        values.update(overrides)
        return ns(**values)

    def test_card_is_short_lived_and_contains_no_private_key(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            _, card = self.make_card(Path(tmp))
            self.assertEqual(card["schema"], rv.SCHEMA)
            self.assertEqual(card["canonicalization"], rv.CARD_CANON)
            self.assertNotIn("server_private_key", card)
            self.assertNotIn("privkey", json.dumps(card).lower())
            self.assertEqual(card["server_key_fingerprint"], rv.key_fingerprint(PUBKEY))
            result = rv.verify_card(card, expected_fingerprint=None, secret=SECRET.encode(), require_hmac=True)
            self.assertTrue(result["hmac_authenticated"])

    def test_hmac_card_tampering_fails(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            _, card = self.make_card(Path(tmp))
            card["upstream_service"] = "127.0.0.1:9000"
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.verify_card(card, expected_fingerprint=None, secret=SECRET.encode())
            self.assertEqual(ctx.exception.code, "object_id_mismatch")

    def test_short_hmac_secret_is_rejected(self):
        with patch.dict(os.environ, {"SHORT": "1234567890abcdef"}):
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.hmac_secret("SHORT")
            self.assertEqual(ctx.exception.code, "weak_hmac_secret")
        with self.assertRaises(rv.RendezvousError):
            rv.sign_card({"x": 1}, b"short")

    def test_operational_plan_requires_hmac_unless_explicitly_waived(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            card_path, card = self.make_card(root, signed=False)
            args = self.client_args(root, card_path, card)
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_client_plan(args)
            self.assertEqual(ctx.exception.code, "hmac_required")
            args.allow_unsigned_card = True
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rv.cmd_client_plan(args)
            self.assertFalse(json.loads(output.getvalue())["execute_automatically"])

    def test_client_plan_requires_out_of_band_fingerprint(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            root = Path(tmp)
            card_path, card = self.make_card(root)
            args = self.client_args(root, card_path, card, expected_fingerprint="sha256:" + "00" * 32)
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_client_plan(args)
            self.assertEqual(ctx.exception.code, "fingerprint_mismatch")
            args.expected_fingerprint = card["server_key_fingerprint"]
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rv.cmd_client_plan(args)
            plan = json.loads(output.getvalue())
            self.assertFalse(plan["execute_automatically"])
            self.assertEqual(plan["command_argv"][1], "-udp")
            self.assertFalse((root / "client-server.pub").exists())
            self.assertEqual(plan["public_key_file_to_create"]["content"].strip(), PUBKEY)

    def test_client_listener_is_loopback_by_default(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            root = Path(tmp)
            card_path, card = self.make_card(root)
            args = self.client_args(root, card_path, card, local_listen="0.0.0.0:7000")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_client_plan(args)
            self.assertEqual(ctx.exception.code, "constraint_mismatch")

    def test_lan_listener_requires_signed_card_and_local_override(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            root = Path(tmp)
            card_path, card = self.make_card(root, allow_lan_client_listener=True)
            args = self.client_args(root, card_path, card, local_listen="192.0.2.10:7000")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_client_plan(args)
            self.assertEqual(ctx.exception.code, "nonloopback_client")
            args.allow_lan_listener = True
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rv.cmd_client_plan(args)
            self.assertIn("192.0.2.10:7000", json.dumps(json.loads(output.getvalue())))

    def test_server_plan_rejects_broad_private_key_permissions_and_symlink(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            root = Path(tmp)
            card_path, _ = self.make_card(root)
            private = root / "server.key"
            private.write_text("not-read-by-planner\n", encoding="utf-8")
            private.chmod(0o644)
            args = ns(card=str(card_path), privkey_file=str(private), dnstt_server="dnstt-server", hmac_env="LINK_SECRET")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_server_plan(args)
            self.assertEqual(ctx.exception.code, "private_key_permissions")
            private.chmod(0o600)
            link = root / "key-link"
            link.symlink_to(private)
            args.privkey_file = str(link)
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_server_plan(args)
            self.assertEqual(ctx.exception.code, "private_key_symlink")
            args.privkey_file = str(private)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rv.cmd_server_plan(args)
            plan = json.loads(output.getvalue())
            self.assertIn(str(private), plan["command_argv"])
            self.assertNotIn("not-read-by-planner", json.dumps(plan))

    def test_keygen_plan_refuses_existing_or_symlink_targets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "server.key"
            existing.write_text("do-not-overwrite")
            args = ns(dnstt_server="dnstt-server", privkey_file=str(existing), pubkey_file=str(root / "server.pub"))
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_keygen_plan(args)
            self.assertEqual(ctx.exception.code, "keygen_target_exists")
            existing.unlink()
            target = root / "target"
            target.write_text("x")
            existing.symlink_to(target)
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_keygen_plan(args)
            self.assertEqual(ctx.exception.code, "keygen_target_symlink")
            existing.unlink()
            args.privkey_file = str(root / "same.key")
            args.pubkey_file = str(root / "same.key")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_keygen_plan(args)
            self.assertEqual(ctx.exception.code, "keygen_target_collision")

    def test_strict_json_rejects_duplicates_nonfinite_and_oversize(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.load_card(duplicate)
            self.assertEqual(ctx.exception.code, "duplicate_json_key")
            nonfinite = root / "nan.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.load_card(nonfinite)
            self.assertEqual(ctx.exception.code, "json_nonfinite")
            huge = root / "huge.json"
            huge.write_bytes(b"{" + b" " * rv.MAX_CARD_BYTES + b"}")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.load_card(huge)
            self.assertEqual(ctx.exception.code, "file_too_large")
            huge_int = root / "huge-int.json"
            huge_int.write_text('{"n":' + "9" * 5000 + "}", encoding="utf-8")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.load_card(huge_int)
            self.assertEqual(ctx.exception.code, "invalid_json")
            surrogate = root / "surrogate.json"
            surrogate.write_text('{"x":"\\ud800"}', encoding="utf-8")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.load_card(surrogate)
            self.assertEqual(ctx.exception.code, "json_unsafe_string")

    def test_card_schema_rejects_unknown_fields_bad_constraints_and_endpoints(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            _, original = self.make_card(Path(tmp))
            for mutator, expected_code in (
                (lambda c: c.update({"unknown": True}), "card_unknown_fields"),
                (lambda c: c.update({"constraints": {}}), "invalid_constraints"),
                (lambda c: c.update({"server_listener": "not-an-endpoint"}), "invalid_endpoint"),
            ):
                card = dict(original)
                mutator(card)
                card = rv.sign_card(card, SECRET.encode())
                with self.assertRaises(rv.RendezvousError) as ctx:
                    rv.verify_card(card, expected_fingerprint=None, secret=SECRET.encode())
                self.assertEqual(ctx.exception.code, expected_code)

    def test_card_rejects_future_issue_time_and_excessive_ttl(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            _, original = self.make_card(Path(tmp))
            future = rv.utcnow() + dt.timedelta(hours=2)
            card = dict(original)
            card["issued_at"] = rv.iso(future)
            card["expires_at"] = rv.iso(future + dt.timedelta(minutes=30))
            card = rv.sign_card(card, SECRET.encode())
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.verify_card(card, expected_fingerprint=None, secret=SECRET.encode())
            self.assertEqual(ctx.exception.code, "future_card")
            card = dict(original)
            issued = rv.parse_time(card["issued_at"])
            card["expires_at"] = rv.iso(issued + dt.timedelta(days=2))
            card = rv.sign_card(card, SECRET.encode())
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.verify_card(card, expected_fingerprint=None, secret=SECRET.encode())
            self.assertEqual(ctx.exception.code, "invalid_card_ttl")

    @unittest.skipUnless(hasattr(os, "mkfifo") and hasattr(os, "O_NONBLOCK"), "POSIX FIFO test")
    def test_file_type_swap_to_fifo_cannot_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fifo = root / "race"
            os.mkfifo(fifo)
            regular = root / "regular"
            regular.write_text("x", encoding="utf-8")
            fake_regular_stat = regular.lstat()
            with patch.object(Path, "lstat", return_value=fake_regular_stat), self.assertRaises(
                rv.RendezvousError
            ) as ctx:
                rv.read_bounded_regular(fifo, maximum=100, label="race file")
            self.assertEqual(ctx.exception.code, "file_race_detected")

    def test_public_key_reader_rejects_symlink_oversize_and_embedded_long_hex(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "target"
            target.write_text(PUBKEY)
            link = root / "link"
            link.symlink_to(target)
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.read_public_key(link)
            self.assertEqual(ctx.exception.code, "symlink_forbidden")
            huge = root / "huge"
            huge.write_text("x" * (rv.MAX_PUBLIC_KEY_BYTES + 1))
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.read_public_key(huge)
            self.assertEqual(ctx.exception.code, "file_too_large")
            bad = root / "bad"
            bad.write_text("a" + PUBKEY)
            with self.assertRaises(rv.RendezvousError):
                rv.read_public_key(bad)

    def test_doh_validation_rejects_userinfo_query_fragment_and_whitespace(self):
        bad = (
            "https://user:password@example.com/dns-query",
            "https://example.com/dns-query?token=secret",
            "https://example.com/dns-query#fragment",
            "https://example.com/dns query",
        )
        for value in bad:
            with self.subTest(value=value), self.assertRaises(rv.RendezvousError):
                rv.validate_resolver("doh", value)
        self.assertEqual(rv.validate_resolver("doh", "https://DNS.EXAMPLE/dns-query"), "https://dns.example/dns-query")

    def test_atomic_output_refuses_symlink_and_requires_force_for_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "target"
            target.write_text("ORIGINAL")
            link = root / "out"
            link.symlink_to(target)
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.write_json({"changed": True}, str(link))
            self.assertEqual(ctx.exception.code, "output_symlink")
            self.assertEqual(target.read_text(), "ORIGINAL")
            output = root / "report.json"
            with contextlib.redirect_stdout(io.StringIO()):
                rv.write_json({"one": 1}, str(output))
            self.assertEqual(output.stat().st_mode & 0o777, 0o600)
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.write_json({"two": 2}, str(output))
            self.assertEqual(ctx.exception.code, "output_exists")
            with contextlib.redirect_stdout(io.StringIO()):
                rv.write_json({"two": 2}, str(output), force=True)
            self.assertEqual(json.loads(output.read_text()), {"two": 2})

    def test_status_message_rejects_secrets_and_controls(self):
        for message in (
            "token=github_pat_abcdefghijklmnopqrstuvwxyz1234567890",
            "password=hunter2",
            "-----BEGIN PRIVATE KEY-----",
            "line1\nline2",
        ):
            with self.subTest(message=message), self.assertRaises(rv.RendezvousError):
                rv.validate_status_message(message)
        self.assertEqual(rv.validate_status_message("listener reachable; no service response"), "listener reachable; no service response")

    def test_status_transition_chain_and_hmac_verification(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            root = Path(tmp)
            card_path, card = self.make_card(root)
            common = {
                "card": str(card_path),
                "agent_id": "client-a",
                "role": "client",
                "expected_fingerprint": card["server_key_fingerprint"],
                "hmac_env": "LINK_SECRET",
                "require_hmac": True,
                "allow_expired": False,
            }
            planned_path = root / "planned.json"
            args = ns(**common, state="planned", message="plan received", previous_report=None, output=str(planned_path))
            with contextlib.redirect_stdout(io.StringIO()):
                rv.cmd_status(args)
            planned = json.loads(planned_path.read_text())
            self.assertIn("coordination_hmac_sha256", planned)
            authorized_path = root / "authorized.json"
            args = ns(
                **common,
                state="authorized",
                message="operator approval recorded",
                previous_report=str(planned_path),
                output=str(authorized_path),
            )
            with contextlib.redirect_stdout(io.StringIO()):
                rv.cmd_status(args)
            authorized = json.loads(authorized_path.read_text())
            result = rv.verify_status(
                authorized,
                card_id=card["card_id"],
                secret=SECRET.encode(),
                require_hmac=True,
            )
            self.assertEqual(result["state"], "authorized")
            verify_args = ns(
                card=str(card_path),
                status=str(authorized_path),
                previous_report=None,
                expected_fingerprint=card["server_key_fingerprint"],
                hmac_env="LINK_SECRET",
                require_hmac=True,
            )
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_verify_status(verify_args)
            self.assertEqual(ctx.exception.code, "previous_status_required")
            verify_args.previous_report = str(planned_path)
            verified_output = io.StringIO()
            with contextlib.redirect_stdout(verified_output):
                rv.cmd_verify_status(verify_args)
            self.assertTrue(json.loads(verified_output.getvalue())["valid"])
            args.state = "connected"
            args.previous_report = str(authorized_path)
            args.output = str(root / "bad-transition.json")
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_status(args)
            self.assertEqual(ctx.exception.code, "invalid_state_transition")

    def test_noninitial_status_requires_previous_report(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            root = Path(tmp)
            card_path, card = self.make_card(root)
            args = ns(
                card=str(card_path),
                agent_id="client-a",
                role="client",
                state="connected",
                message="connected",
                previous_report=None,
                expected_fingerprint=card["server_key_fingerprint"],
                hmac_env="LINK_SECRET",
                require_hmac=True,
                allow_expired=False,
            )
            with self.assertRaises(rv.RendezvousError) as ctx:
                rv.cmd_status(args)
            self.assertEqual(ctx.exception.code, "previous_status_required")

    def test_binary_name_rejects_shell_metacharacters(self):
        for value in ("dnstt-client;rm", "$(touch pwned)", "dnstt client", "-evil"):
            with self.subTest(value=value), self.assertRaises(rv.RendezvousError):
                rv.safe_binary(value, label="binary")
        self.assertEqual(rv.safe_binary("/usr/local/bin/dnstt-client", label="binary"), "/usr/local/bin/dnstt-client")
        self.assertEqual(rv.safe_binary(r"C:\Program Files\dnstt-client.exe", label="binary"), r"C:\Program Files\dnstt-client.exe")

    def test_json_complexity_and_unicode_normalization(self):
        deep: object = "x"
        for _ in range(rv.MAX_JSON_DEPTH + 2):
            deep = [deep]
        with self.assertRaises(rv.RendezvousError) as ctx:
            rv.canonical(deep)
        self.assertEqual(ctx.exception.code, "json_too_deep")
        with self.assertRaises(rv.RendezvousError) as ctx:
            rv.canonical({"text": "e\u0301"})
        self.assertEqual(ctx.exception.code, "json_not_nfc")
        with self.assertRaises(rv.RendezvousError) as ctx:
            rv.canonical({"number": 1.2})
        self.assertEqual(ctx.exception.code, "json_float_forbidden")

    def test_error_has_stable_machine_readable_code(self):
        error = rv.RendezvousError("bad card", code="card_bad", hint="regenerate")
        payload = error.as_dict()
        self.assertEqual(payload["error"]["code"], "card_bad")
        self.assertEqual(payload["error"]["hint"], "regenerate")

    def test_debug_events_drop_sensitive_keys_and_values(self):
        original = rv.DEBUG_ENABLED
        rv.DEBUG_ENABLED = True
        output = io.StringIO()
        # Construct at runtime so security scanners do not mistake this redaction
        # fixture for a committed live credential.
        synthetic_token = "".join(("github", "_pat_", "redactionfixture0123456789"))  # noqa: FLY002
        try:
            with contextlib.redirect_stderr(output):
                rv.debug_event(
                    "review",
                    hmac_env="LINK_SECRET",
                    api_token=synthetic_token,
                    harmless="listener-ready",
                )
        finally:
            rv.DEBUG_ENABLED = original
        event = json.loads(output.getvalue())
        self.assertEqual(event["harmless"], "listener-ready")
        self.assertNotIn("hmac_env", event)
        self.assertNotIn("api_token", event)
        self.assertNotIn("github_pat_", output.getvalue())

    def test_diagnose_marks_expired_card(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LINK_SECRET": SECRET}):
            root = Path(tmp)
            card_path, card = self.make_card(root)
            issued = rv.utcnow() - dt.timedelta(hours=1)
            card["issued_at"] = rv.iso(issued)
            card["expires_at"] = rv.iso(issued + dt.timedelta(minutes=30))
            card = rv.sign_card(card, SECRET.encode())
            card_path.write_text(json.dumps(card), encoding="utf-8")
            args = ns(
                card=str(card_path),
                symptom="no-response",
                expected_fingerprint=card["server_key_fingerprint"],
                hmac_env="LINK_SECRET",
                require_hmac=True,
            )
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rv.cmd_diagnose(args)
            report = json.loads(output.getvalue())
            self.assertTrue(report["card_expired"])
            self.assertIn("expired", report["warning"])

    def test_doctor_invariants(self):
        args = ns(card=None, expected_fingerprint=None)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rv.cmd_doctor(args)
        report = json.loads(output.getvalue())
        self.assertTrue(report["ok"])
        self.assertTrue(report["checks"]["no_network_or_subprocess_imports"])

    def test_endpoint_parser_fuzz_never_leaks_unexpected_exception(self):
        # Deterministic generator is intentional: this is a non-cryptographic fuzz corpus.
        rng = random.Random(42)  # nosec B311
        alphabet = string.ascii_letters + string.digits + ".:-_[] ;/$"
        for _ in range(2000):
            value = "".join(rng.choice(alphabet) for _ in range(rng.randrange(0, 80)))
            try:
                host, port = rv.parse_endpoint(value, label="fuzz")
                self.assertTrue(host)
                self.assertTrue(1 <= port <= 65535)
            except rv.RendezvousError:
                pass
            except Exception as exc:  # pragma: no cover - assertion path
                self.fail(f"unexpected exception {type(exc).__name__} for {value!r}")

    def test_operational_plans_require_authorization_ack(self):
        args = ns(ack_authorized=False)
        with self.assertRaises(rv.RendezvousError):
            rv.require_authorized(args)


if __name__ == "__main__":
    unittest.main()
