#!/usr/bin/env python3
"""Issue the only formal completion receipt after report, review and privacy gates pass."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TASK_ID_RE = re.compile(r"^agent-[0-9A-Za-z_-]+$")
CORE_ARTIFACTS = ("report.json", "report.md", "report.pdf", "pdf-delivery.json")
ANALYSIS_ROLES = (
    "omni-ecom-team-lead",
    "data-analyst",
    "platform-ops",
    "content-live-growth",
    "ad-profit-optimizer",
)


def read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError(f"json_root_invalid:{path.name}")
    return payload


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def require(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)


def artifact(path: Path) -> dict[str, Any]:
    require(path.is_file() and path.stat().st_size > 0, f"artifact_missing:{path.name}")
    return {"file": path.name, "sha256": sha256(path), "bytes": path.stat().st_size}


def validate_public_receipt(receipt: dict[str, Any], report_dir: Path) -> None:
    require(receipt.get("status") == "public_output_guard_passed", "public_output_guard_not_passed")
    entries = receipt.get("artifacts")
    require(isinstance(entries, list), "public_output_guard_receipt_invalid")
    index = {str(item.get("file")): item for item in entries if isinstance(item, dict)}
    for name in ("report.json", "report.md", "report.pdf"):
        path = report_dir / name
        item = index.get(name)
        require(isinstance(item, dict) and item.get("sha256") == sha256(path), "public_output_guard_stale")


def validate_claim_receipt(receipt: dict[str, Any], report_dir: Path) -> None:
    """Require the numeric claim/formula gate to be bound to the frozen report."""
    require(receipt.get("status") == "claim_guard_passed", "claim_guard_not_passed")
    require(int(receipt.get("claims_count", 0)) > 0, "claim_ledger_empty")
    report_path = report_dir / "report.md"
    require(receipt.get("report_file") == "report.md", "claim_report_binding_missing")
    require(receipt.get("report_sha256") == sha256(report_path), "claim_report_binding_stale")
    errors = receipt.get("errors")
    require(not errors, "claim_guard_not_passed")


def validate_comprehensive(
    report: dict[str, Any], manifest: dict[str, Any], attestation: dict[str, Any],
    release_receipt: dict[str, Any],
) -> tuple[str, str]:
    identity = (report.get("run_id"), report.get("client_scope"), report.get("team_version"), report.get("report_revision"))
    for payload in (manifest, attestation, release_receipt):
        require(payload.get("run_id") == identity[0], "completion_identity_mismatch")
    require(manifest.get("client_scope") == identity[1], "completion_identity_mismatch")
    require(manifest.get("team_version") == identity[2], "completion_identity_mismatch")
    require(manifest.get("report_revision") == identity[3], "completion_identity_mismatch")
    require(attestation.get("agent_id") == "delivery-review", "review_attestation_invalid")
    require(attestation.get("return_status") == "completed", "review_attestation_invalid")
    require(attestation.get("review_status") == "passed", "review_not_passed_blocked")
    require(not attestation.get("required_changes"), "review_not_passed_blocked")
    require(attestation.get("report_revision") == identity[3], "review_revision_mismatch")
    review_attempt_id = str(attestation.get("review_attempt_id") or "")
    review_task_id = str(attestation.get("agent_task_id") or "")
    require(bool(review_attempt_id), "review_attempt_id_missing")
    require(bool(TASK_ID_RE.fullmatch(review_task_id)), "review_agent_task_id_invalid")
    require(release_receipt.get("status") == "review_release_verified", "review_release_not_verified")
    require(release_receipt.get("review_attempt_id") == review_attempt_id, "review_attempt_mismatch")
    require(release_receipt.get("review_agent_task_id") == review_task_id, "review_agent_task_mismatch")
    require(release_receipt.get("report_revision") == identity[3], "review_revision_mismatch")
    require(release_receipt.get("manifest_sha256") == manifest.get("manifest_sha256"), "review_manifest_mismatch")
    return review_attempt_id, review_task_id


def build_activity(report: dict[str, Any], review_task_id: str = "", review_summary: str = "") -> list[dict[str, Any]]:
    source = report.get("expert_participation")
    require(isinstance(source, list) and len(source) == 6, "expert_activity_invalid")
    activity: list[dict[str, Any]] = []
    for item in source:
        require(isinstance(item, dict), "expert_activity_invalid")
        agent_id = str(item.get("agent_id") or "")
        status = str(item.get("participation_status") or "not_invoked")
        task_ids = [str(value) for value in item.get("agent_task_ids", []) if str(value)]
        summary = str(item.get("contribution_summary") or "")
        if agent_id == "delivery-review" and review_task_id:
            status = "contributed"
            task_ids = [review_task_id]
            summary = review_summary
        if status == "pending_review":
            status = "not_invoked"
        activity.append({
            "agent_id": agent_id,
            "participation_status": status,
            "agent_task_ids": task_ids,
            "contribution_summary": summary,
        })
    require({item["agent_id"] for item in activity} == set(ANALYSIS_ROLES) | {"delivery-review"}, "expert_activity_invalid")
    return activity


def main() -> int:
    parser = argparse.ArgumentParser(description="Formal delivery completion gate")
    parser.add_argument("--report-dir", required=True)
    parser.add_argument("--public-guard-receipt", required=True)
    parser.add_argument("--manifest")
    parser.add_argument("--attestation")
    parser.add_argument("--release-receipt")
    parser.add_argument("--claim-receipt", required=True, help="数字来源、公式和归因闸门回执")
    parser.add_argument("--version-info", default=str(ROOT / "version-info.json"))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        report_dir = Path(args.report_dir).expanduser().resolve()
        paths = {name: report_dir / name for name in CORE_ARTIFACTS}
        artifacts = [artifact(path) for path in paths.values()]
        report = read_json(paths["report.json"])
        pdf_receipt = read_json(paths["pdf-delivery.json"])
        version_info = read_json(Path(args.version_info).expanduser().resolve())
        require(report.get("team_version") == version_info.get("team_version"), "team_version_mismatch")
        require(pdf_receipt.get("status") == "pdf_render_verified", "pdf_delivery_not_verified")
        require(pdf_receipt.get("team_version") == report.get("team_version"), "pdf_delivery_mismatch")
        require(pdf_receipt.get("report_revision") == report.get("report_revision"), "pdf_delivery_mismatch")
        require(pdf_receipt.get("report_sha256") == sha256(paths["report.pdf"]), "pdf_delivery_mismatch")
        require(int(pdf_receipt.get("chart_count", 0)) >= 3, "pdf_delivery_not_verified")

        public_receipt_path = Path(args.public_guard_receipt).expanduser().resolve()
        public_receipt = read_json(public_receipt_path)
        validate_public_receipt(public_receipt, report_dir)
        artifacts.append(artifact(public_receipt_path))

        collaboration_mode = str(report.get("collaboration_mode") or "")
        review_required = collaboration_mode == "comprehensive"
        review_attempt_id = ""
        review_task_id = ""
        review_summary = ""
        release_sha = ""
        if review_required:
            require(bool(args.manifest and args.attestation and args.release_receipt), "review_evidence_missing")
            manifest_path = Path(args.manifest).expanduser().resolve()
            attestation_path = Path(args.attestation).expanduser().resolve()
            release_path = Path(args.release_receipt).expanduser().resolve()
            manifest = read_json(manifest_path)
            attestation = read_json(attestation_path)
            release_receipt = read_json(release_path)
            review_attempt_id, review_task_id = validate_comprehensive(report, manifest, attestation, release_receipt)
            review_summary = str(attestation.get("contribution_summary") or "独立交付复核通过")
            artifacts.extend([artifact(manifest_path), artifact(attestation_path), artifact(release_path)])
            release_sha = sha256(release_path)

        claim_receipt_path = Path(args.claim_receipt).expanduser().resolve()
        claim_receipt = read_json(claim_receipt_path)
        validate_claim_receipt(claim_receipt, report_dir)
        artifacts.append(artifact(claim_receipt_path))

        activity = build_activity(report, review_task_id, review_summary)
        if review_required:
            by_id = {item["agent_id"]: item for item in activity}
            for agent_id in ANALYSIS_ROLES:
                require(by_id[agent_id]["participation_status"] == "contributed", f"required_agent_missing:{agent_id}")
            for agent_id in ANALYSIS_ROLES[1:]:
                require(bool(by_id[agent_id]["agent_task_ids"]), f"required_agent_task_id_missing:{agent_id}")
            require(by_id["delivery-review"]["participation_status"] == "contributed", "delivery_review_missing")

        result: dict[str, Any] = {
            "schema_version": "1.0",
            "status": "formal_delivery_complete",
            "run_id": report.get("run_id"),
            "client_scope": report.get("client_scope"),
            "team_version": report.get("team_version"),
            "report_revision": report.get("report_revision"),
            "task_type": report.get("task_type"),
            "collaboration_mode": collaboration_mode,
            "review_required": review_required,
            "review_attempt_id": review_attempt_id,
            "review_agent_task_id": review_task_id,
            "claim_guard_status": "claim_guard_passed",
            "public_output_guard_status": "public_output_guard_passed",
            "expert_activity": activity,
            "artifacts": artifacts,
            "completed_at": utc_now(),
        }
        if release_sha:
            result["release_receipt_sha256"] = release_sha
        output = Path(args.output).expanduser().resolve()
        require(not output.exists(), "completion_receipt_already_exists")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({
            "status": result["status"],
            "team_version": result["team_version"],
            "report_revision": result["report_revision"],
            "task_type": result["task_type"],
            "expert_count": len(activity),
            "output": output.name,
        }, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "completion_blocked", "reason": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
