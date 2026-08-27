#!/usr/bin/env python3
"""Regression cases for the v1.5.11 numeric/source and formula hard gate."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GUARD = ROOT / "scripts" / "claim_guard.py"
ENV = {**os.environ, "PYTHONUTF8": "1"}
PERIOD = "2026-W01"
SOURCE_HASH = hashlib.sha256(b"claim-guard-smoke-source").hexdigest()


def source(source_id: str, field: str) -> dict[str, str]:
    return {
        "source_id": source_id,
        "source_file": "smoke-source.csv",
        "sheet": "data",
        "range": "A1",
        "field": field,
        "source_sha256": SOURCE_HASH,
    }


def claim(claim_id: str, metric: str, value: Any, status: str, source_id: str, field: str, **extra: Any) -> dict[str, Any]:
    return {
        "claim_id": claim_id,
        "metric": metric,
        "value": value,
        "unit": "数值",
        "period": PERIOD,
        "status": status,
        "source_ref": source(source_id, field),
        **extra,
    }


def payload(claims: list[dict[str, Any]]) -> dict[str, Any]:
    return {"schema_version": "1.0", "run_id": "run-claim-guard-smoke", "client_scope": "smoke", "period": PERIOD, "claims": claims}


def run_case(work: Path, name: str, data: dict[str, Any] | None, expected: int) -> tuple[str, bool, str]:
    claims_path = work / f"{name}.json"
    receipt_path = work / f"{name}.receipt.json"
    if data is not None:
        claims_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = subprocess.run([
        sys.executable, str(GUARD), "validate", "--claims", str(claims_path), "--output", str(receipt_path)
    ], capture_output=True, text=True, encoding="utf-8", env=ENV)
    text = result.stdout + result.stderr
    return name, result.returncode == expected and receipt_path.is_file(), text


def main() -> int:
    checks: list[tuple[str, bool, str]] = []
    with tempfile.TemporaryDirectory(prefix="omni-ecom-claim-guard-") as temp:
        work = Path(temp)
        checks.append(run_case(work, "missing_ledger", None, 2))
        checks.append(run_case(work, "verified_spend", payload([
            claim("C-spend", "ad_spend", 2293.87, "verified", "store_overview", "全站推广花费（本店）"),
        ]), 0))
        checks.append(run_case(work, "conversion_uses_buyers", payload([
            claim("C-visitors", "visitors", 100, "verified", "traffic", "访客数"),
            claim("C-buyers", "paid_buyers", 5, "verified", "traffic", "支付买家数"),
            claim("C-conv", "conversion_rate", 0.05, "derived", "traffic", "转化率", formula={"name": "conversion_rate", "numerator": "paid_buyers", "denominator": "visitors", "expression": "paid_buyers / visitors"}, inputs=["C-buyers", "C-visitors"]),
        ]), 0))
        checks.append(run_case(work, "conversion_gmv_mislabel", payload([
            claim("C-visitors", "visitors", 100, "verified", "traffic", "访客数"),
            claim("C-gmv", "gmv", 1000, "verified", "traffic", "支付GMV"),
            claim("C-conv", "conversion_rate", 10, "derived", "traffic", "转化率", formula={"name": "conversion_rate", "numerator": "gmv", "denominator": "visitors", "expression": "GMV / visitors"}, inputs=["C-gmv", "C-visitors"]),
        ]), 2))
        checks.append(run_case(work, "roas_source_mismatch", payload([
            claim("C-spend", "ad_spend", 100, "verified", "store_overview", "推广花费"),
            claim("C-gmv", "attributed_gmv", 1000, "verified", "traffic", "归因GMV"),
            claim("C-roas", "roas", 10, "derived", "traffic", "ROI", formula={"name": "roas", "numerator": "attributed_gmv", "denominator": "ad_spend", "expression": "attributed_gmv / ad_spend"}, inputs=["C-gmv", "C-spend"], attribution={"source_id": "traffic", "window": PERIOD, "level": "campaign"}),
        ]), 2))
        checks.append(run_case(work, "roas_same_attribution", payload([
            claim("C-spend", "ad_spend", 100, "verified", "ad_backend", "花费"),
            claim("C-gmv", "attributed_gmv", 1000, "verified", "ad_backend", "归因GMV"),
            claim("C-roas", "roas", 10, "derived", "ad_backend", "ROI", formula={"name": "roas", "numerator": "attributed_gmv", "denominator": "ad_spend", "expression": "attributed_gmv / ad_spend"}, inputs=["C-gmv", "C-spend"], attribution={"source_id": "ad_backend", "window": PERIOD, "level": "campaign"}),
        ]), 0))
        checks.append(run_case(work, "unknown_numeric", payload([
            claim("C-unknown", "roas", 9.06, "unknown", "unknown", "未提供投放报表"),
        ]), 2))
    passed = sum(1 for _, ok, _ in checks if ok)
    status = "PASS" if passed == len(checks) else "FAIL"
    print(json.dumps({"status": status, "checks": f"{passed}/{len(checks)}", "cases": [{"name": n, "pass": ok} for n, ok, _ in checks]}, ensure_ascii=False, indent=2))
    if status != "PASS":
        for name, ok, detail in checks:
            if not ok:
                print(f"[{name}]\n{detail}", file=sys.stderr)
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
