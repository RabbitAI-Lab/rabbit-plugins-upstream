#!/usr/bin/env python3
"""Tests for the disclosure gates: redaction, consent, and the publish schema.

These cover the three ways memory content can leave the machine — the external
judge, the local embedding server, and the public PR — plus the two flags that
used to let an unattended run through a consent gate.

Run: python3 scripts/test_privacy.py
"""
import io
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

import rate
import report_schema

SECRETS = (
    "Mail ops@example.com or ring +34 612 345 678. Key sk-abcdefghijklmnop1234 "
    "lives in /home/globalcaos/.config/secret.txt and the hash is "
    "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef."
)


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def capture_request(payload_out, response):
    """Replace urlopen so nothing leaves the machine during a test."""
    def fake_urlopen(req, timeout=None):
        payload_out.append(req)
        return FakeResponse(json.dumps(response).encode())
    return fake_urlopen


# --- Redaction ---------------------------------------------------------------

def test_redact_covers_every_pattern():
    out = rate.redact(SECRETS)
    for leaked in ["ops@example.com", "612 345 678", "sk-abcdefghijklmnop1234",
                   "/home/globalcaos", "deadbeefdeadbeef"]:
        assert leaked not in out, f"redact left {leaked!r} in: {out}"
    for tag in ["[EMAIL]", "[PHONE]", "[KEY]", "[PATH]"]:
        assert tag in out, f"expected {tag} in: {out}"

def test_redact_url_credentials():
    """The password must go. Which placeholder replaces it is cosmetic: the
    email pattern runs first and claims 'hunter2@github.com', so the tag reads
    [EMAIL] rather than [CREDS]. Both remove the secret."""
    out = rate.redact("clone https://user:hunter2@github.com/x/y.git")
    assert "hunter2" not in out, out
    assert "[EMAIL]" in out or "[CREDS]" in out, out

def test_excerpt_truncates_then_redacts():
    text = "x" * 500 + " ops@example.com"
    out = rate.excerpt(text)
    assert len(out) <= rate.EXCERPT_CHARS, f"excerpt is {len(out)} chars"
    out2 = rate.excerpt("ops@example.com " + "y" * 100)
    assert "ops@example.com" not in out2 and "[EMAIL]" in out2

def test_excerpt_is_idempotent():
    """Callers apply it defensively; a second pass must not corrupt the first."""
    once = rate.excerpt(SECRETS)
    assert rate.excerpt(once) == once

def test_excerpt_accepts_non_strings():
    assert rate.excerpt({"content": "hi"})  # dict row fallback must not raise


# --- The local judge is a separate process, so it gets redacted text too ------

def test_local_judge_transmits_redacted_text():
    sent, real = [], urllib.request.urlopen
    urllib.request.urlopen = capture_request(sent, {"embeddings": [[1.0, 0.0], [1.0, 0.0]]})
    try:
        rate.judge_with_embeddings("query", SECRETS)
    finally:
        urllib.request.urlopen = real
    assert sent, "local judge made no request"
    body = sent[0].data.decode()
    assert "127.0.0.1" in sent[0].full_url
    for leaked in ["ops@example.com", "sk-abcdefghijklmnop1234", "/home/globalcaos"]:
        assert leaked not in body, f"local judge leaked {leaked!r}"
    assert "[EMAIL]" in body


# --- The consent preview must be the request that is actually sent ------------

def test_openai_payload_is_redacted():
    payload = rate.build_openai_payload("q", SECRETS)
    content = payload["messages"][0]["content"]
    for leaked in ["ops@example.com", "sk-abcdefghijklmnop1234", "/home/globalcaos"]:
        assert leaked not in content, f"payload leaked {leaked!r}"

def test_preview_shows_the_exact_bytes_that_get_sent():
    """The point of the canonical builder: no drift between shown and sent."""
    payload = rate.build_openai_payload("q", SECRETS)
    preview = rate.render_openai_preview(payload, 30, True)

    sent, real = [], urllib.request.urlopen
    urllib.request.urlopen = capture_request(
        sent, {"choices": [{"message": {"content": "4"}}]})
    try:
        rate.judge_with_openai("q", SECRETS, "sk-test-key")
    finally:
        urllib.request.urlopen = real

    assert sent, "no request was built"
    sent_body = json.loads(sent[0].data.decode())
    assert sent_body == payload, "sent body differs from the previewed payload"
    # Every line of the rendered body appears verbatim in the preview.
    for line in json.dumps(payload, indent=2, ensure_ascii=False).splitlines():
        assert line in preview, f"preview omits line: {line}"
    assert sent[0].full_url == rate.OPENAI_ENDPOINT == "https://api.openai.com/v1/chat/completions"

def test_preview_never_shows_the_api_key():
    preview = rate.render_openai_preview(rate.build_openai_payload("q", "c"), 30, True)
    assert "sk-" not in preview


# --- Report schema -----------------------------------------------------------

def _fixture_db(tmp: Path) -> Path:
    db = tmp / "bench.db"
    conn = sqlite3.connect(str(db))
    conn.executescript("""
        CREATE TABLE memories (id INTEGER PRIMARY KEY, content TEXT, memory_type TEXT,
          importance REAL, strength REAL, created_at TEXT, is_deleted INTEGER DEFAULT 0);
        CREATE TABLE associations (id INTEGER PRIMARY KEY, association_type TEXT);
        CREATE TABLE hierarchy (id INTEGER PRIMARY KEY, level INTEGER);
        CREATE TABLE consolidation_log (timestamp TEXT, memories_processed INT,
          memories_decayed INT, memories_pruned INT, clusters_formed INT, summaries_created INT);
    """)
    conn.execute("INSERT INTO memories (content, memory_type, importance, strength,"
                 " created_at, is_deleted) VALUES (?,?,?,?,datetime('now'),0)",
                 ("The gateway restart procedure. " + SECRETS, "procedural", 0.9, 0.8))
    conn.execute("INSERT INTO associations (association_type) VALUES ('semantic')")
    conn.execute("INSERT INTO hierarchy (level) VALUES (0)")
    conn.execute("INSERT INTO consolidation_log VALUES (datetime('now','-1 day'),1,0,0,0,0)")
    conn.commit()
    conn.close()
    return db


def _collect(tmp: Path) -> dict:
    """Run the real collector, so the schema is tested against real output."""
    out = tmp / "report.json"
    subprocess.run([sys.executable, str(SCRIPT_DIR / "collect.py"),
                    "--db", str(_fixture_db(tmp)), "--output", str(out)],
                   capture_output=True, check=True)
    return json.loads(out.read_text())


def test_real_collector_output_validates():
    """If collect.py grows a field, this fails here — not at submit time."""
    with tempfile.TemporaryDirectory() as d:
        errors, _ = report_schema.check_report(_collect(Path(d)))
        assert not errors, f"collect.py output failed the schema: {errors}"

def test_unknown_top_level_field_is_refused():
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        report["debug_dump"] = "whatever"
        errors, _ = report_schema.check_report(report)
        assert any("debug_dump" in e and "unknown" in e for e in errors), errors

def test_unknown_nested_field_is_refused():
    """The old preview only ever looked at top-level keys."""
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        report["system"]["hostname"] = "oscar-laptop"
        errors, _ = report_schema.check_report(report)
        assert any("system.hostname" in e for e in errors), errors

def test_wrong_type_is_refused():
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        report["memory_stats"]["memories"]["total_active"] = "lots"
        errors, _ = report_schema.check_report(report)
        assert any("total_active" in e for e in errors), errors

def test_missing_required_field_is_refused():
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        del report["instance_id"]
        errors, _ = report_schema.check_report(report)
        assert any("instance_id" in e and "missing" in e for e in errors), errors

def test_memory_content_smuggled_into_a_key_is_refused():
    """type_distribution keys come from the DB, so they are attacker-shaped."""
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        report["memory_stats"]["memories"]["type_distribution"]["x" * 200] = 1
        errors, _ = report_schema.check_report(report)
        assert any("max 120" in e or "reads like content" in e for e in errors), errors

def test_newline_in_a_value_is_refused():
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        report["schema_version"] = "2.0.0\nsecond line of memory content"
        errors, _ = report_schema.check_report(report)
        assert any("newline" in e for e in errors), errors

def test_secretish_value_warns_but_does_not_block():
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        report["memory_stats"]["memories"]["type_distribution"]["ops@example.com"] = 1
        errors, warnings = report_schema.check_report(report)
        assert not errors, errors
        assert any("EMAIL" in w for w in warnings), warnings

def test_timestamps_do_not_produce_warnings():
    """A warning that fires on every report is a warning nobody reads."""
    with tempfile.TemporaryDirectory() as d:
        _, warnings = report_schema.check_report(_collect(Path(d)))
        assert not warnings, f"clean report produced noise: {warnings}"

def test_contributor_mismatch_is_refused():
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        report["contributor"] = "someone_else"
        errors, _ = report_schema.check_report(report, contributor="globalcaos")
        assert any("attribute it to someone else" in e for e in errors), errors

def test_preview_lists_every_field():
    with tempfile.TemporaryDirectory() as d:
        report = _collect(Path(d))
        preview = report_schema.render_preview(report, "r.json", [], [])
        for path, _ in report_schema.walk(report):
            assert path in preview, f"preview omits {path}"


# --- Neither consent gate may be opened by an unattended run -----------------

def _run_headless(cmd, cwd=None):
    """Run with no terminal on stdin and no route to the network."""
    env = dict(os.environ,
               OPENAI_API_KEY="sk-dummy-not-real",
               https_proxy="http://127.0.0.1:1",
               HTTPS_PROXY="http://127.0.0.1:1")
    return subprocess.run(cmd, capture_output=True, text=True, timeout=120,
                          stdin=subprocess.DEVNULL, env=env, cwd=cwd)

def test_openai_judge_refuses_without_a_terminal_even_with_the_flag():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        testset = tmp / "ts.json"
        testset.write_text(json.dumps([{"id": "T01", "query": "gateway",
                                        "category": "procedural", "difficulty": "easy"}]))
        r = _run_headless([sys.executable, str(SCRIPT_DIR / "rate.py"),
                           "--db", str(_fixture_db(tmp)), "--testset", str(testset),
                           "--judge", "openai", "--yes-send-to-openai"])
        assert r.returncode != 0, f"unattended run was allowed to send:\n{r.stdout}"
        assert "no terminal to confirm on" in r.stdout, r.stdout
        assert "Nothing was sent" in r.stdout

def test_openai_preview_is_printed_before_the_refusal():
    """Refusing is not enough — the user must still see what would have gone."""
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        testset = tmp / "ts.json"
        testset.write_text(json.dumps([{"id": "T01", "query": "gateway",
                                        "category": "procedural", "difficulty": "easy"}]))
        r = _run_headless([sys.executable, str(SCRIPT_DIR / "rate.py"),
                           "--db", str(_fixture_db(tmp)), "--testset", str(testset),
                           "--judge", "openai", "--yes-send-to-openai"])
        assert "api.openai.com/v1/chat/completions" in r.stdout
        assert '"model": "gpt-4o-mini"' in r.stdout
        # A real excerpt was retrieved, and it was redacted before display.
        assert "[EMAIL]" in r.stdout and "ops@example.com" not in r.stdout

def test_submit_refuses_without_a_terminal_even_with_yes():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        report = tmp / "report.json"
        report.write_text(json.dumps(_collect(tmp)))
        # A gh that screams if the gate ever lets execution reach it.
        shim = tmp / "shim"
        shim.mkdir()
        (shim / "gh").write_text('#!/bin/sh\necho SHIM-GH-REACHED\nexit 1\n')
        (shim / "gh").chmod(0o755)
        env_path = f"{shim}:{os.environ['PATH']}"
        r = subprocess.run(["bash", str(SCRIPT_DIR / "submit.sh"), str(report), "--yes"],
                           capture_output=True, text=True, timeout=120,
                           stdin=subprocess.DEVNULL,
                           env=dict(os.environ, PATH=env_path))
        assert r.returncode != 0, f"unattended run was allowed to publish:\n{r.stdout}"
        assert "no terminal to confirm on" in r.stdout, r.stdout
        assert "SHIM-GH-REACHED" not in r.stdout, "execution reached the gh CLI"

def test_submit_dry_run_previews_every_field_and_uploads_nothing():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        report_data = _collect(tmp)
        report = tmp / "report.json"
        report.write_text(json.dumps(report_data))
        shim = tmp / "shim"
        shim.mkdir()
        (shim / "gh").write_text('#!/bin/sh\necho SHIM-GH-REACHED\nexit 1\n')
        (shim / "gh").chmod(0o755)
        r = subprocess.run(["bash", str(SCRIPT_DIR / "submit.sh"), str(report), "--dry-run"],
                           capture_output=True, text=True, timeout=120,
                           stdin=subprocess.DEVNULL,
                           env=dict(os.environ, PATH=f"{shim}:{os.environ['PATH']}"))
        assert r.returncode == 0, r.stdout + r.stderr
        assert "SHIM-GH-REACHED" not in r.stdout
        for path, _ in report_schema.walk(report_data):
            assert path in r.stdout, f"dry run omits {path}"
        # The commit message and PR body are public too, so they are previewed.
        assert "THE COMMIT MESSAGE" in r.stdout and "THE PULL REQUEST" in r.stdout

def test_submit_refuses_a_report_with_an_unknown_field():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        data = _collect(tmp)
        data["exfiltrated"] = "surprise"
        report = tmp / "report.json"
        report.write_text(json.dumps(data))
        r = subprocess.run(["bash", str(SCRIPT_DIR / "submit.sh"), str(report), "--dry-run"],
                           capture_output=True, text=True, timeout=120,
                           stdin=subprocess.DEVNULL)
        assert r.returncode != 0, "an unknown field passed the gate"
        assert "does not match the expected schema" in r.stdout, r.stdout


if __name__ == "__main__":
    tests = [f for f in dir() if f.startswith("test_")]
    passed = failed = 0
    for t in sorted(tests):
        try:
            globals()[t]()
            print(f"  ✅ {t}")
            passed += 1
        except AssertionError as e:
            print(f"  ❌ {t}: {e}")
            failed += 1
        except Exception as e:
            print(f"  ❌ {t}: {type(e).__name__}: {e}")
            failed += 1
    print(f"\n{'✅' if failed == 0 else '❌'} {passed}/{passed+failed} tests passed")
    sys.exit(1 if failed else 0)
