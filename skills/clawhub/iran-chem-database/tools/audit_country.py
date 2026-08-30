#!/usr/bin/env python3
"""Audit every supplier source against the Iranian-suppliers-ONLY policy (v2.11).

Checks the curated web seed list and the social channel seeds, and prints any
entry that the country gate would refuse. Exit code 1 => a non-Iranian source
is present, which is a policy violation.

    python3 tools/audit_country.py [--json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.discovery.country_gate import IRAN, collect_disqualifiers  # noqa: E402
from src.discovery.seed_list import SUPPLIER_SEEDS  # noqa: E402
from src.discovery.social_seed_list import (FOREIGN_CHANNELS,  # noqa: E402
                                            SOCIAL_CHANNELS,
                                            country_provenance,
                                            is_iranian_channel)


def main() -> int:
    as_json = "--json" in sys.argv
    violations = []

    for seed in SUPPLIER_SEEDS:
        dq = collect_disqualifiers(url=seed["url"], content=seed.get("notes") or "")
        if dq:
            violations.append({"kind": "web_seed", "id": seed["url"],
                               "name": seed["name"], "reason": dq[0].signal,
                               "value": dq[0].value, "country": dq[0].country})

    for handle, meta in SOCIAL_CHANNELS.items():
        if not is_iranian_channel(handle):
            violations.append({"kind": "social_channel", "id": handle,
                               "reason": "not audited Iranian",
                               "country": meta.get("country")})
        elif not meta.get("country_evidence"):
            violations.append({"kind": "social_channel", "id": handle,
                               "reason": "missing country evidence"})

    report = {
        "policy": "iranian_suppliers_only",
        "allowed_countries": [IRAN],
        "web_seeds_checked": len(SUPPLIER_SEEDS),
        "social_channels_checked": len(SOCIAL_CHANNELS),
        "foreign_denylist_size": len(FOREIGN_CHANNELS),
        "violations": violations,
        "vendors": [country_provenance(h) for h in SOCIAL_CHANNELS],
    }
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Iranian-suppliers-ONLY audit")
        print(f"  web seeds checked      : {report['web_seeds_checked']}")
        print(f"  social channels checked: {report['social_channels_checked']}")
        print(f"  foreign deny-list      : {report['foreign_denylist_size']} handles")
        if violations:
            print(f"\n  VIOLATIONS ({len(violations)}):")
            for v in violations:
                print(f"    [{v['kind']}] {v['id']}: {v['reason']}")
        else:
            print("\n  PASS — every supplier source is verified Iranian.")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
