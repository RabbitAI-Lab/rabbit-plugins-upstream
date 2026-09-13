#!/usr/bin/env python3
"""Self-test for souvenir_sleuth.py — destination matching, aliases, budget
filter, trap heuristics, and JSON output."""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "souvenir_sleuth.py"
sys.path.insert(0, str(SCRIPT.parent))
import souvenir_sleuth as ss  # noqa: E402


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True)


def test_kb_integrity():
    kb = json.loads(ss.KB_PATH.read_text(encoding="utf-8"))
    assert len(kb) >= 13
    for key, card in kb.items():
        assert card["name"] and card["currency"]
        assert 1 <= card["haggling_index"] <= 5
        assert card["specialties"], f"{key} has no specialties"
        for s in card["specialties"]:
            assert {"item", "local_price", "buy_zones", "authenticity",
                    "customs"} <= set(s)
            lo, hi = s["local_price"]
            assert 0 < lo < hi, f"bad price range for {key}/{s['item']}"
            assert s["customs"] in ("green", "yellow", "orange", "red")
    print("  knowledge base integrity ... OK")


def test_matching():
    kb = json.loads(ss.KB_PATH.read_text(encoding="utf-8"))

    def key_of(q):
        m = ss.match_destination(q, kb)
        assert m is not None, f"no match for {q}"
        return m[0]

    assert key_of("Kyoto") == "kyoto"
    assert key_of("kyoto, japan") == "kyoto"
    assert key_of("CDMX") == "mexicocity"
    assert key_of("New Orleans") == "neworleans"
    assert key_of("NOLA") == "neworleans"
    assert key_of("Marrakesh") == "marrakech"
    assert key_of("machu picchu") == "cusco"
    assert ss.match_destination("Atlantis", kb) is None
    print("  destination matching + aliases ... OK")


def test_trap_probability():
    p1, h1 = ss.trap_probability("Colosseum snow globe")
    assert p1 >= 0.5 and "snow globe" in h1
    p2, _ = ss.trap_probability("handwoven wool scarf from cooperative")
    assert p2 < 0.25
    p3, _ = ss.trap_probability("Eiffel tower keychain")
    assert p3 >= 0.5
    print("  trap heuristics ... OK")


def test_cli():
    r = run("--list")
    assert r.returncode == 0 and "Kyoto" in r.stdout
    r = run("--destination", "Fez", "--item", "mini Eiffel keychain")
    assert r.returncode == 0
    assert "TRAP CHECK" in r.stdout and "TOURIST TRAP" in r.stdout
    assert "Argan oil" in r.stdout and "leather" in r.stdout.lower()
    r = run("--destination", "kyoto", "--budget", "1000")
    assert "filter ≤ 1,000" in r.stdout
    assert "Kiyomizu-yaki" not in r.stdout      # 2000+ JPY filtered out
    assert "Yatsuhashi" in r.stdout             # 600 JPY stays
    r = run("--destination", "nowhere-land")
    assert r.returncode == 1
    print("  CLI (dossier, trap check, budget, unknown city) ... OK")


def test_json(tmpdir):
    out = Path(tmpdir) / "fez.json"
    r = run("--destination", "Fès", "--json", str(out), "--item", "snow globe")
    assert r.returncode == 0, r.stderr
    data = json.loads(out.read_text())
    assert data["key"] == "fez" and data["currency"] == "MAD"
    assert data["trap_check"]["probability"] >= 0.5
    assert any("tannery" in s["desc"].lower() for s in data["specialties"])
    print("  JSON dossier output ... OK")


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        test_kb_integrity()
        test_matching()
        test_trap_probability()
        test_cli()
        test_json(td)
    print("\nALL TESTS PASSED ✅")
