#!/usr/bin/env python3
"""Self-test for flight_claim_checker.py — tier math, thresholds,
extraordinary circumstances, cancellation notice rules, jurisdictions."""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent / "flight_claim_checker.py"
sys.path.insert(0, str(SCRIPT.parent))
import flight_claim_checker as fc  # noqa: E402


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True)


def NS(**kw):
    """argparse-namespace shim."""
    defaults = dict(origin="FRA", destination="JFK", distance=6200,
                    delay=None, disruption="delay", reroute_delay=None,
                    notice=None, date="2026-06-15", carrier="Lufthansa",
                    jurisdiction=None, airline_reason=None, overnight=False,
                    baggage_issue=None, care_reimb=False)
    defaults.update(kw)
    return type("NS", (), defaults)


def test_eu_tiers():
    assert fc.eu_tier_amount(1200) == (250, "≤1,500 km")
    assert fc.eu_tier_amount(2000) == (400, "1,500–3,500 km")
    assert fc.eu_tier_amount(6000) == (600, ">3,500 km")
    assert fc.eu_tier_amount(1200, "GBP") == (220, "≤1,500 km")
    assert fc.eu_tier_amount(6000, "GBP") == (520, ">3,500 km")
    print("  EU/UK distance tiers ... OK")


def test_eu_delay_thresholds():
    r = fc.evaluate(NS(delay=170))          # 2h50m
    assert not r.eligible and "Care" in "".join(r.reasons) or not r.eligible
    r = fc.evaluate(NS(delay=180))          # exactly 3h
    assert r.eligible and r.amount == 600 and r.currency == "EUR"
    r = fc.evaluate(NS(delay=300, distance=1400))
    assert r.amount == 250
    r = fc.evaluate(NS(delay=301, jurisdiction="UK"))
    assert r.amount == 520 and r.currency == "GBP"
    print("  delay thresholds + amounts ... OK")


def test_extraordinary():
    ok, note = fc.evaluate_extraordinary("severe thunderstorm")
    assert ok
    bad, note = fc.evaluate_extraordinary("technical fault")
    assert not bad and "NOT an extraordinary" in note
    bad2, _ = fc.evaluate_extraordinary("crew shortage")
    assert not bad2
    r = fc.evaluate(NS(delay=400, airline_reason="technical fault"))
    assert r.eligible  # defense rejected
    r2 = fc.evaluate(NS(delay=400, airline_reason="storm"))
    assert not r2.eligible and r2.defense_notes
    print("  extraordinary-circumstances engine ... OK")


def test_cancellation_notice():
    # ≥14 days notice → nothing
    r = fc.evaluate(NS(disruption="cancellation", reroute_delay=600,
                       notice=20))
    assert not r.eligible
    # <14 days, reroute lands 5h late → full tier
    r = fc.evaluate(NS(disruption="cancellation", reroute_delay=300,
                       notice=2))
    assert r.eligible and r.amount == 600
    # reroute lands 90m late → within 2h exemption → nothing
    r = fc.evaluate(NS(disruption="cancellation", reroute_delay=90,
                       notice=2))
    assert not r.eligible
    # reroute lands 3h30 late, 6200km tier bound is 4h → 50% reduced
    r = fc.evaluate(NS(disruption="cancellation", reroute_delay=210,
                       notice=2))
    assert r.eligible and r.amount == 300
    # short-haul: 2h30 late, bound 2h → full tier
    r = fc.evaluate(NS(disruption="cancellation", reroute_delay=150,
                       notice=2, distance=1200))
    assert r.eligible and r.amount == 250
    # short-haul 2h30 late but 3h bound mid-haul → 50%
    r = fc.evaluate(NS(disruption="cancellation", reroute_delay=150,
                       notice=2, distance=2000))
    assert r.eligible and r.amount == 200
    print("  cancellation notice tiers ... OK")


def test_denied_boarding():
    r = fc.evaluate(NS(disruption="denied-boarding", delay=180))
    assert r.eligible and r.amount == 600
    r = fc.evaluate(NS(disruption="denied-boarding", delay=180,
                       jurisdiction="US"))
    assert r.eligible and r.amount == 1350 and r.currency == "USD"
    r = fc.evaluate(NS(disruption="denied-boarding", delay=90,
                       jurisdiction="US"))
    assert r.eligible and r.amount == 675
    r = fc.evaluate(NS(disruption="denied-boarding", delay=30,
                       jurisdiction="US"))
    assert not r.eligible
    print("  denied boarding (EU + US bump tiers) ... OK")


def test_us_delay_truth():
    r = fc.evaluate(NS(delay=420, jurisdiction="US", origin="JFK",
                       destination="LAX", carrier="Delta", distance=3970))
    assert not r.eligible
    assert "NO federal compensation" in "".join(r.reasons)
    print("  US delays honestly reported ... OK")


def test_canada_brazil_india():
    r = fc.evaluate(NS(delay=240, jurisdiction="CA"))
    assert r.eligible and r.amount == 400 and r.currency == "CAD"
    r = fc.evaluate(NS(delay=480, jurisdiction="CA"))
    assert r.amount == 700
    r = fc.evaluate(NS(delay=540, jurisdiction="CA"))
    assert r.amount == 1000
    r = fc.evaluate(NS(delay=300, jurisdiction="BR"))
    assert r.eligible  # rebooking rights + damages path
    r = fc.evaluate(NS(delay=90, jurisdiction="IN"))
    assert r.amount == 7500 and r.currency == "INR"
    r = fc.evaluate(NS(delay=150, jurisdiction="IN"))
    assert r.amount == 10000
    print("  CA/BR/IN rules ... OK")


def test_care_and_deadline():
    r = fc.evaluate(NS(delay=330, distance=1200, overnight=True))
    assert any("Meals" in c for c in r.care)
    assert any("refund" in c for c in r.care)
    assert any("hotel" in c.lower() for c in r.care)
    assert r.deadline.startswith("2029-")  # EU ≈ 3y from 2026-06-15
    print("  care entitlements + deadline ... OK")


def test_cli_letter(tmpdir):
    letter = Path(tmpdir) / "claim.txt"
    jsn = Path(tmpdir) / "ruling.json"
    r = run("--from", "MUC", "--to", "LHR", "--distance", "1450",
            "--delay", "300", "--date", "2026-07-14",
            "--carrier", "Lufthansa",
            "--passenger-name", "Jane Doe", "--booking-ref", "ABC123",
            "--letter", str(letter), "--json", str(jsn))
    assert r.returncode == 0, r.stderr
    assert "ELIGIBLE" in r.stdout and "EUR 250" in r.stdout
    txt = letter.read_text()
    assert "Jane Doe" in txt and "ABC123" in txt and "EUR 250" in txt
    assert "14 days" in txt
    data = json.loads(jsn.read_text())
    assert data["eligible"] and data["amount"] == 250
    # US domestic honest answer via CLI
    r2 = run("--from", "JFK", "--to", "LAX", "--distance", "3970",
             "--delay", "420", "--jurisdiction", "US", "--carrier", "Delta")
    assert "NOT ELIGIBLE" in r2.stdout
    print("  CLI + letter generation ... OK")


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        test_eu_tiers()
        test_eu_delay_thresholds()
        test_extraordinary()
        test_cancellation_notice()
        test_denied_boarding()
        test_us_delay_truth()
        test_canada_brazil_india()
        test_care_and_deadline()
        test_cli_letter(td)
    print("\nALL TESTS PASSED ✅")
