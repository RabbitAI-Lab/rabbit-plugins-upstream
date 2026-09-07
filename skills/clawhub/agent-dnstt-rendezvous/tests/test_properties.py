#!/usr/bin/env python3
from __future__ import annotations

import concurrent.futures
import datetime as dt
import json
import random
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
import rendezvous as rv

SECRET = b"property-test-coordination-secret-32-bytes"
PUBKEY = "22" * 32


def make_card(index: int = 0) -> dict:
    now = rv.utcnow()
    card = {
        "schema": rv.SCHEMA,
        "canonicalization": rv.CARD_CANON,
        "role": "dnstt-server",
        "server_agent_id": f"server-{index}",
        "tunnel_domain": f"t{index}.example.com",
        "server_public_key": PUBKEY,
        "server_key_fingerprint": rv.key_fingerprint(PUBKEY),
        "server_listener": f"0.0.0.0:{5300 + index % 100}",
        "upstream_service": f"127.0.0.1:{8000 + index % 100}",
        "authorization_ref": f"LAB-{index}",
        "purpose": "authorized property test",
        "issued_at": rv.iso(now),
        "expires_at": rv.iso(now + dt.timedelta(minutes=30)),
        "nonce": f"{index:032x}"[-32:],
        "constraints": {
            "authorized_infrastructure_only": True,
            "client_listener_loopback_only": True,
            "no_private_key_in_card": True,
            "no_automatic_execution": True,
            "no_resolver_scanning": True,
            "upstream_loopback_only": True,
        },
    }
    return rv.sign_card(card, SECRET)


class RendezvousPropertyTests(unittest.TestCase):
    def test_500_signed_card_round_trips(self):
        for index in range(500):
            card = make_card(index)
            result = rv.verify_card(
                card,
                expected_fingerprint=card["server_key_fingerprint"],
                secret=SECRET,
                require_hmac=True,
            )
            self.assertEqual(result["domain"], card["tunnel_domain"])
            self.assertTrue(result["hmac_authenticated"])

    def test_every_top_level_card_mutation_is_detected(self):
        original = make_card(1)
        for field in sorted(set(original) - {"coordination_hmac_sha256", "card_id"}):
            card = json.loads(json.dumps(original))
            value = card[field]
            if isinstance(value, str):
                card[field] = value + "x"
            elif isinstance(value, dict):
                card[field] = {**value, "no_automatic_execution": False}
            else:
                card[field] = None
            with self.subTest(field=field), self.assertRaises(rv.RendezvousError):
                rv.verify_card(card, expected_fingerprint=None, secret=SECRET)

    def test_endpoint_round_trip_corpus(self):
        corpus = (
            "127.0.0.1:53",
            "0.0.0.0:5300",
            "localhost:7000",
            "dns.example:853",
            "[::1]:7000",
            "[2001:db8::53]:53",
        )
        for endpoint in corpus:
            with self.subTest(endpoint=endpoint):
                host, port = rv.parse_endpoint(endpoint, label="endpoint")
                reparsed = rv.parse_endpoint(rv.endpoint_text(host, port), label="endpoint")
                self.assertEqual((host, port), reparsed)

    def test_atomic_concurrent_writers_never_leave_partial_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "state.json"

            def writer(index: int):
                rv.atomic_write(
                    output,
                    json.dumps({"writer": index, "payload": "x" * 1000}).encode(),
                    force=True,
                )

            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
                list(executor.map(writer, range(64)))
            final = json.loads(output.read_text())
            self.assertIn(final["writer"], range(64))
            self.assertEqual(len(final["payload"]), 1000)

    def test_state_machine_has_no_escape_from_closed(self):
        self.assertEqual(rv.ALLOWED_TRANSITIONS["closed"], set())
        for state, targets in rv.ALLOWED_TRANSITIONS.items():
            self.assertTrue(targets <= set(rv.STATES), state)
            self.assertNotIn(state, targets)

    def test_random_malformed_json_never_leaks_unexpected_exception(self):
        # Deterministic generator is intentional: this is a non-cryptographic fuzz corpus.
        rng = random.Random(7)  # nosec B311
        alphabet = "{}[],:\"\\" + "abcXYZ019" + "\x00\n\r\t"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fuzz.json"
            for _ in range(1000):
                raw = "".join(rng.choice(alphabet) for _ in range(rng.randrange(0, 300)))
                path.write_bytes(raw.encode("utf-8", errors="surrogatepass"))
                try:
                    value = rv.load_json_object(path, maximum=1024, label="fuzz JSON")
                    self.assertIsInstance(value, dict)
                except rv.RendezvousError:
                    pass
                except Exception as exc:  # pragma: no cover - assertion path
                    self.fail(f"unexpected {type(exc).__name__} for {raw!r}")

    def test_secret_scanner_corpus(self):
        secrets = (
            "password=hunter2",
            "token=abc123",
            "github_pat_abcdefghijklmnopqrstuvwxyz0123456789",
            "-----BEGIN OPENSSH PRIVATE KEY-----",
            "A" * 64,
        )
        for value in secrets:
            with self.subTest(value=value):
                self.assertTrue(rv.contains_secret(value))
        safe = (
            "resolver reachable",
            "upstream returned connection refused",
            "card expired; request a new handoff",
        )
        for value in safe:
            with self.subTest(value=value):
                self.assertFalse(rv.contains_secret(value))


if __name__ == "__main__":
    unittest.main()
