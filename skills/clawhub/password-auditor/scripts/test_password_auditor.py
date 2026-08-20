#!/usr/bin/env python3
"""Self-test for password_auditor.py — verifies parsing, scoring, reuse
detection, staleness, and report generation without any network access."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent / "password_auditor.py"


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True)


def test_demo_report():
    r = run("--demo")
    assert r.returncode == 0, r.stderr
    assert "SECURITY SCORE" in r.stdout
    assert "Gmail" in r.stdout          # weak Tr0ub4dor&3
    assert "Chase Bank" in r.stdout     # reused + critical tier
    assert "rotate" in r.stdout.lower()
    # no plaintext password may ever appear in output
    for pwd in ("Tr0ub4dor&3", "Summer2024!", "password123", "monkey42"):
        assert pwd not in r.stdout, f"LEAK: {pwd} in report"
    print("  demo report + no-leak check ... OK")


def test_strength_scoring():
    sys.path.insert(0, str(SCRIPT.parent))
    import password_auditor as pa
    assert pa.score_strength("")[0] == 0
    assert pa.score_strength("password123")[0] == 0
    assert pa.score_strength("Tr0ub4dor&3")[0] <= 2
    assert pa.score_strength("qwerty123")[0] <= 1
    s, bits, _ = pa.score_strength("kp$9vXQ2!mZ#wR7tLp3n")
    assert s == 4 and bits > 60, (s, bits)
    s2, b2, _ = pa.score_strength("correct horse battery staple prize")
    assert s2 >= 3, (s2, b2)
    print("  strength scoring ... OK")


def test_bitwarden_csv(tmpdir):
    csv_text = (
        "folder,name,login_uri,login_username,login_password,login_totp,login_updated\n"
        "Email,Gmail,https://mail.google.com,bob@x.com,Summer2024!,,2023-01-15T10:00:00Z\n"
        "Shop,Amazon,https://amazon.com,bob@x.com,Summer2024!,,2026-01-02T10:00:00Z\n"
        "Dev,GitHub,https://github.com,bob@x.com,Zx9$wQ!pLm4&vBn7rqT2,JBSWY3DPEHPK3PXP,2026-06-01T10:00:00Z\n")
    p = Path(tmpdir) / "bw.csv"
    p.write_text(csv_text)
    entries, fmt = pa.load_vault(p)
    assert fmt == "bitwarden", fmt
    assert len(entries) == 3
    res = pa.analyze(entries)          # classification happens here
    gmail = entries[0]
    assert gmail.domain == "mail.google.com"
    assert gmail.tier == "critical"
    gh = entries[2]
    assert gh.has_totp and gh.twofa_capable
    assert res["largest_reuse_component"] == 2
    assert any(f["entry"] == 1 for f in res["findings"].get("reuse", []))
    assert any(f["entry"] == 2 for f in res["findings"].get("reuse", []))
    assert not any(f["entry"] == 3 for f in res["findings"].get("reuse", []))
    print("  bitwarden CSV + reuse/tier/2FA ... OK")


def test_json_and_html(tmpdir):
    out_json = Path(tmpdir) / "r.json"
    out_html = Path(tmpdir) / "r.html"
    r = run("--demo", "--json", str(out_json), "--html", str(out_html))
    assert r.returncode == 0, r.stderr
    data = json.loads(out_json.read_text())
    assert 0 <= data["score"] <= 100
    assert set(data["subscores"]) == {"reuse", "weakness", "breach",
                                      "staleness", "twofa"}
    assert data["plan"] and data["plan"][0]["priority"] == 1
    assert "Summer2024!" not in out_json.read_text()
    html = out_html.read_text()
    assert "Password Audit Dashboard" in html and "Remediation Plan" in html
    assert "password123" not in html
    print("  JSON + HTML reports (no leaks) ... OK")


def test_compare(tmpdir):
    j1, j2 = Path(tmpdir) / "a.json", Path(tmpdir) / "b.json"
    run("--demo", "--json", str(j1))
    run("--demo", "--json", str(j2))
    r = run("--compare", str(j1), str(j2))
    assert r.returncode == 0 and "score" in r.stdout
    print("  report comparison ... OK")


if __name__ == "__main__":
    sys.path.insert(0, str(SCRIPT.parent))
    import password_auditor as pa
    with tempfile.TemporaryDirectory() as td:
        test_demo_report()
        test_strength_scoring()
        test_bitwarden_csv(td)
        test_json_and_html(td)
        test_compare(td)
    print("\nALL TESTS PASSED ✅")
