#!/usr/bin/env python3
"""Deterministic smoke test for multi-agent collaboration visibility."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build_report_package.py"
WAITER = ROOT / "scripts" / "wait_for_agent_returns.py"
PUBLIC_GUARD = ROOT / "scripts" / "public_output_guard.py"
REVIEW_GUARD = ROOT / "scripts" / "review_guard.py"
COMPLETION_GATE = ROOT / "scripts" / "completion_gate.py"
UTF8_ENV = {
    **os.environ,
    "PYTHONUTF8": "1",
    "OMNI_ECOM_CLIENT_REGISTRY": str(ROOT / "config" / "client-brand-registry.json"),
}
TEAM_VERSION = json.loads((ROOT / "version-info.json").read_text(encoding="utf-8"))["team_version"]


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def handoff(agent_id: str, summary: str) -> dict[str, Any]:
    evidence_id = "E-" + agent_id
    return {
        "schema_version": "1.0",
        "run_id": "run-collaboration-smoke",
        "agent_id": agent_id,
        "agent_version": TEAM_VERSION,
        **({} if agent_id == "omni-ecom-team-lead" else {
            "agent_task_id": "agent-" + agent_id.replace("-", "_"),
            "agent_return_status": "completed",
            "agent_returned_at": "2026-08-11T12:00:00Z",
            "agent_return_file": f"{agent_id}.return.json",
            "agent_return_sha256": "0" * 64,
        }),
        "contribution_summary": summary,
        "scope": {"platform": "演示平台", "store": "脱敏店铺", "period": "2026-W01", "grain": "week"},
        "gate_status": "PASS",
        "status": "ready_for_review",
        "facts": [{"id": "F-" + agent_id, "claim": summary, "evidence_ids": [evidence_id]}],
        "judgments": [],
        "hypotheses": [],
        "actions": [],
        "risks": [],
        "missing_data": [],
        "evidence_ledger": [{
            "id": evidence_id,
            "source": f"{agent_id}-source.json",
            "period": "2026-W01",
            "metric": "collaboration_smoke",
            "value": 1,
            "status": "verified",
        }],
    }


def main() -> int:
    checks: list[tuple[str, bool, str]] = []
    with tempfile.TemporaryDirectory(prefix="omni-ecom-collab-") as temp:
        work = Path(temp)
        files: dict[str, Path] = {}
        summaries = {
            "omni-ecom-team-lead": "完成任务拆解、冲突裁决和最终结论",
            "data-analyst": "完成数据质量闸门与指标复算",
            "platform-ops": "完成平台经营诊断",
            "content-live-growth": "完成内容与直播增长诊断",
            "ad-profit-optimizer": "完成投流与利润边界诊断",
            "delivery-review": "完成报告结构与交付复核",
        }
        for agent_id, summary in summaries.items():
            path = work / f"{agent_id}.json"
            write_json(path, handoff(agent_id, summary))
            files[agent_id] = path

        output = work / "complete"
        claim_ledger = work / "claim-ledger.json"
        smoke_source_hash = __import__("hashlib").sha256(b"collaboration-smoke-source").hexdigest()
        write_json(claim_ledger, {
            "schema_version": "1.0",
            "run_id": "run-collaboration-smoke",
            "client_scope": "smoke-client",
            "period": "2026-W01",
            "claims": [
                {"claim_id": "C-visitors", "metric": "visitors", "value": 100, "unit": "人", "period": "2026-W01", "status": "verified", "source_ref": {"source_id": "traffic", "source_file": "smoke-source.csv", "sheet": "data", "range": "B2", "field": "访客数", "source_sha256": smoke_source_hash}},
                {"claim_id": "C-gmv", "metric": "gmv", "value": 1000, "unit": "CNY", "period": "2026-W01", "status": "verified", "source_ref": {"source_id": "traffic", "source_file": "smoke-source.csv", "sheet": "data", "range": "C2", "field": "支付GMV", "source_sha256": smoke_source_hash}},
                {"claim_id": "C-buyers", "metric": "paid_buyers", "value": 5, "unit": "人", "period": "2026-W01", "status": "verified", "source_ref": {"source_id": "traffic", "source_file": "smoke-source.csv", "sheet": "data", "range": "D2", "field": "支付买家数", "source_sha256": smoke_source_hash}},
                {"claim_id": "C-uv-value", "metric": "uv_value", "value": 10, "unit": "CNY/UV", "period": "2026-W01", "status": "derived", "source_ref": {"source_id": "traffic", "source_file": "smoke-source.csv", "sheet": "data", "range": "C2/B2", "field": "访客价值", "source_sha256": smoke_source_hash}, "formula": {"name": "uv_value", "numerator": "gmv", "denominator": "visitors", "expression": "gmv / visitors"}, "inputs": ["C-gmv", "C-visitors"]},
                {"claim_id": "C-conversion", "metric": "conversion_rate", "value": 0.05, "unit": "%", "period": "2026-W01", "status": "derived", "source_ref": {"source_id": "traffic", "source_file": "smoke-source.csv", "sheet": "data", "range": "D2/B2", "field": "转化率", "source_sha256": smoke_source_hash}, "formula": {"name": "conversion_rate", "numerator": "paid_buyers", "denominator": "visitors", "expression": "paid_buyers / visitors"}, "inputs": ["C-buyers", "C-visitors"]}
            ]
        })
        command = [
            sys.executable,
            str(BUILDER),
            "--handoff", str(files["omni-ecom-team-lead"]),
            "--client-scope", "smoke-client",
            "--collaboration-mode", "comprehensive",
            "--task-type", "weekly_report",
            "--member-handoff", str(files["data-analyst"]),
            "--member-handoff", str(files["platform-ops"]),
            "--member-handoff", str(files["content-live-growth"]),
            "--member-handoff", str(files["ad-profit-optimizer"]),
            "--report-revision", "R1",
            "--claim-ledger", str(claim_ledger),
            "--output-dir", str(output),
        ]
        complete = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("comprehensive_build", complete.returncode == 0, complete.stderr or complete.stdout))

        report_path = output / "report.json"
        report = json.loads(report_path.read_text(encoding="utf-8")) if report_path.is_file() else {}
        checks.append(("team_version", report.get("team_version") == TEAM_VERSION, str(report.get("team_version"))))
        checks.append(("weekly_task_profile", report.get("task_type") == "weekly_report" and report.get("task_profile", {}).get("period_grain") == "week", json.dumps(report.get("task_profile", {}), ensure_ascii=False)))
        pdf_receipt_path = output / "pdf-delivery.json"
        pdf_receipt = json.loads(pdf_receipt_path.read_text(encoding="utf-8")) if pdf_receipt_path.is_file() else {}
        checks.append((
            "default_chart_pdf",
            (output / "report.pdf").is_file()
            and pdf_receipt.get("status") == "pdf_render_verified"
            and int(pdf_receipt.get("chart_count", 0)) >= 3,
            json.dumps(pdf_receipt, ensure_ascii=False),
        ))
        participants = report.get("expert_participation", [])
        contributed = {item.get("agent_id") for item in participants if item.get("participation_status") == "contributed"}
        expected_draft = set(summaries) - {"delivery-review"}
        checks.append((
            "draft_role_visibility",
            len(participants) == 6 and contributed == expected_draft,
            f"roster={len(participants)}, contributed={sorted(contributed)}",
        ))
        pending_review = next((item for item in participants if item.get("agent_id") == "delivery-review"), {})
        checks.append(("delivery_review_visible_as_pending", pending_review.get("participation_status") == "pending_review", json.dumps(pending_review, ensure_ascii=False)))
        markdown = (output / "report.md").read_text(encoding="utf-8") if (output / "report.md").is_file() else ""
        checks.append(("markdown_review_candidate", "本次专家协作记录" in markdown and "awaiting_delivery_review" in markdown and "已冻结的复核候选稿" in markdown, "section/status"))
        task_ids = {
            task_id
            for item in participants
            if item.get("agent_id") != "omni-ecom-team-lead"
            for task_id in item.get("agent_task_ids", [])
        }
        checks.append(("four_analysis_task_ids", len(task_ids) == 4 and "Agent 子任务" in markdown, str(sorted(task_ids))))

        review_before_draft = subprocess.run([
            *command[:-2],
            "--member-handoff", str(files["delivery-review"]),
            "--output-dir", str(work / "review-before-draft"),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        review_before_text = review_before_draft.stdout + review_before_draft.stderr
        checks.append(("delivery_review_before_frozen_draft_blocks", review_before_draft.returncode != 0 and "review_order_invalid" in review_before_text, review_before_text))

        incomplete_output = work / "incomplete"
        incomplete = subprocess.run([
            sys.executable,
            str(BUILDER),
            "--handoff", str(files["omni-ecom-team-lead"]),
            "--client-scope", "smoke-client",
            "--collaboration-mode", "comprehensive",
            "--claim-ledger", str(claim_ledger),
            "--output-dir", str(incomplete_output),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        incomplete_text = (incomplete.stderr or "") + (incomplete.stdout or "")
        blocked = incomplete.returncode != 0 and "collaboration_incomplete" in incomplete_text
        checks.append(("incomplete_collaboration_blocks", blocked, incomplete.stderr or incomplete.stdout))

        untraceable_payload = handoff("data-analyst", summaries["data-analyst"])
        untraceable_payload.pop("agent_task_id", None)
        write_json(files["data-analyst"], untraceable_payload)
        untraceable_output = work / "untraceable"
        untraceable = subprocess.run([
            *command[:-1], str(untraceable_output)
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        untraceable_text = (untraceable.stderr or "") + (untraceable.stdout or "")
        checks.append((
            "missing_agent_task_id_blocks",
            untraceable.returncode != 0 and "collaboration_untraceable" in untraceable_text,
            untraceable_text,
        ))

        unreturned_payload = handoff("data-analyst", summaries["data-analyst"])
        unreturned_payload.pop("agent_return_status", None)
        write_json(files["data-analyst"], unreturned_payload)
        unreturned_output = work / "unreturned"
        unreturned = subprocess.run([
            *command[:-1], str(unreturned_output)
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        unreturned_text = (unreturned.stderr or "") + (unreturned.stdout or "")
        checks.append((
            "missing_agent_return_blocks",
            unreturned.returncode != 0 and "collaboration_unreturned" in unreturned_text,
            unreturned_text,
        ))

        return_dir = work / "agent_returns"
        return_dir.mkdir()
        for agent_id in ("data-analyst", "platform-ops"):
            write_json(return_dir / f"{agent_id}.return.json", {
                "run_id": "run-collaboration-smoke",
                "agent_id": agent_id,
                "return_status": "completed",
                "returned_at": "2026-08-11T12:00:00Z",
                "contribution_summary": summaries[agent_id],
                "response": {"result": "ok"},
            })
        wait_ok = subprocess.run([
            sys.executable, str(WAITER),
            "--return-dir", str(return_dir),
            "--run-id", "run-collaboration-smoke",
            "--expected", "data-analyst,platform-ops",
            "--timeout", "2",
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("return_latch_releases", wait_ok.returncode == 0 and "all_agent_returns_received" in wait_ok.stdout, wait_ok.stdout + wait_ok.stderr))

        wait_timeout = subprocess.run([
            sys.executable, str(WAITER),
            "--return-dir", str(return_dir),
            "--run-id", "run-collaboration-smoke",
            "--expected", "data-analyst,delivery-review",
            "--timeout", "1",
            "--poll-seconds", "0.2",
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("return_latch_fails_closed", wait_timeout.returncode == 2 and "collaboration_wait_timeout" in wait_timeout.stdout, wait_timeout.stdout + wait_timeout.stderr))

        safe_public = work / "safe-public.md"
        current_client = "示例当前客户"
        safe_public.write_text(f"当前客户：{current_client}；采用品牌无关标准经营报告版式。", encoding="utf-8")
        guard_pass = subprocess.run([
            sys.executable, str(PUBLIC_GUARD), "--file", str(safe_public), "--allowed-term", current_client,
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("public_guard_allows_current_client", guard_pass.returncode == 0 and "public_output_guard_passed" in guard_pass.stdout, guard_pass.stdout + guard_pass.stderr))

        registry = json.loads((ROOT / "config" / "client-brand-registry.json").read_text(encoding="utf-8"))
        blocked_term = next(term for term in registry["registered_client_terms"] if term != current_client)
        leaked_public = work / "leaked-public.md"
        leaked_public.write_text(f"错误复用了其他客户：{blocked_term}", encoding="utf-8")
        guard_block = subprocess.run([
            sys.executable, str(PUBLIC_GUARD), "--file", str(leaked_public), "--allowed-term", current_client,
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        guard_text = guard_block.stdout + guard_block.stderr
        checks.append(("public_guard_blocks_cross_client_without_echo", guard_block.returncode == 2 and "client_scope_leak_blocked" in guard_text and blocked_term not in guard_text, guard_text))

        write_json(files["data-analyst"], handoff("data-analyst", summaries["data-analyst"]))
        leaked_handoff = handoff("omni-ecom-team-lead", summaries["omni-ecom-team-lead"])
        leaked_handoff["facts"][0]["claim"] = f"错误引用其他客户 {blocked_term}"
        write_json(files["omni-ecom-team-lead"], leaked_handoff)
        integrated_block = subprocess.run([
            *command[:-1], str(work / "integrated-leak")
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        integrated_text = integrated_block.stdout + integrated_block.stderr
        checks.append(("report_builder_blocks_cross_client", integrated_block.returncode != 0 and "client_scope_leak_blocked" in integrated_text and blocked_term not in integrated_text, integrated_text))

        for agent_id, summary in summaries.items():
            write_json(files[agent_id], handoff(agent_id, summary))
        conflict = work / "conflict-resolution.md"
        conflict.write_text("冲突已按同平台、同期间、同口径裁决。", encoding="utf-8")

        missing_pdf_manifest = work / "missing-pdf-manifest.json"
        missing_pdf = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "prepare",
            "--run-id", "run-collaboration-smoke",
            "--client-scope", "smoke-client",
            "--team-version", TEAM_VERSION,
            "--report-revision", "R1",
            "--artifact", str(output / "report.md"),
            "--artifact", str(output / "report.json"),
            "--artifact", str(output / "pdf-delivery.json"),
            "--artifact", str(conflict),
            "--source", str(files["omni-ecom-team-lead"]),
            "--output", str(missing_pdf_manifest),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        missing_pdf_text = missing_pdf.stdout + missing_pdf.stderr
        checks.append(("missing_pdf_blocks_review", missing_pdf.returncode == 2 and "pdf_delivery_required" in missing_pdf_text, missing_pdf_text))

        original_pdf_receipt = (output / "pdf-delivery.json").read_text(encoding="utf-8")
        bad_pdf_receipt = json.loads(original_pdf_receipt)
        bad_pdf_receipt["chart_count"] = 2
        write_json(output / "pdf-delivery.json", bad_pdf_receipt)
        bad_pdf_manifest = work / "bad-pdf-manifest.json"
        bad_pdf = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "prepare",
            "--run-id", "run-collaboration-smoke",
            "--client-scope", "smoke-client",
            "--team-version", TEAM_VERSION,
            "--report-revision", "R1",
            "--artifact", str(output / "report.md"),
            "--artifact", str(output / "report.json"),
            "--artifact", str(output / "report.pdf"),
            "--artifact", str(output / "pdf-delivery.json"),
            "--source", str(files["omni-ecom-team-lead"]),
            "--output", str(bad_pdf_manifest),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        bad_pdf_text = bad_pdf.stdout + bad_pdf.stderr
        checks.append(("unverified_pdf_blocks_review", bad_pdf.returncode == 2 and "pdf_delivery_not_verified" in bad_pdf_text, bad_pdf_text))
        (output / "pdf-delivery.json").write_text(original_pdf_receipt, encoding="utf-8")

        mutable_return = work / "data-analyst.return.json"
        mutable_return.write_text(files["data-analyst"].read_text(encoding="utf-8"), encoding="utf-8")
        mutable_manifest = work / "mutable-source-manifest.json"
        mutable_review = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "prepare",
            "--run-id", "run-collaboration-smoke",
            "--client-scope", "smoke-client",
            "--team-version", TEAM_VERSION,
            "--report-revision", "R1",
            "--artifact", str(output / "report.md"),
            "--artifact", str(output / "report.json"),
            "--artifact", str(output / "report.pdf"),
            "--artifact", str(output / "pdf-delivery.json"),
            "--source", str(mutable_return),
            "--output", str(mutable_manifest),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        mutable_text = mutable_review.stdout + mutable_review.stderr
        checks.append(("mutable_return_source_blocks_freeze", mutable_review.returncode == 2 and "mutable_return_source_blocked" in mutable_text, mutable_text))

        manifest = work / "review-manifest.json"
        review_attempt_id = "delivery-review-r1-a1"
        attestation = work / "review" / "R1" / f"{review_attempt_id}.attestation.json"
        receipt = work / "release-receipt.json"
        prepare_review = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "prepare",
            "--run-id", "run-collaboration-smoke",
            "--client-scope", "smoke-client",
            "--team-version", TEAM_VERSION,
            "--report-revision", "R1",
            "--artifact", str(output / "report.md"),
            "--artifact", str(output / "report.json"),
            "--artifact", str(output / "report.pdf"),
            "--artifact", str(output / "pdf-delivery.json"),
            "--artifact", str(conflict),
            *[value for agent_id in ("omni-ecom-team-lead", "data-analyst", "platform-ops", "content-live-growth", "ad-profit-optimizer") for value in ("--source", str(files[agent_id]))],
            "--output", str(manifest),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("review_manifest_prepared", prepare_review.returncode == 0 and "review_manifest_prepared" in prepare_review.stdout, prepare_review.stdout + prepare_review.stderr))

        manifest_payload = json.loads(manifest.read_text(encoding="utf-8"))
        review_result = work / "review" / "R1" / f"{review_attempt_id}.return.json"
        result_attestation = attestation
        review_result.parent.mkdir(parents=True, exist_ok=True)
        write_json(review_result, {
            "schema_version": "1.0",
            "run_id": "run-collaboration-smoke",
            "agent_id": "delivery-review",
            "review_attempt_id": review_attempt_id,
            "report_revision": "R1",
            "return_status": "completed",
            "returned_at": "2099-08-13T00:00:00Z",
            "review_status": "passed",
            "reviewed_manifest_sha256": manifest_payload["manifest_sha256"],
            "reviewed_artifacts": [
                {"file": item["file"], "sha256": item["sha256"]}
                for item in manifest_payload["artifacts"]
            ],
            "findings": ["冻结报告、PDF 和来源一致"],
            "required_changes": [],
            "contribution_summary": "一次性独立复核通过",
        })

        review_wait = subprocess.run([
            sys.executable, str(WAITER),
            "--return-dir", str(work),
            "--run-id", "run-collaboration-smoke",
            "--expected", "delivery-review",
            "--contract", "delivery_review",
            "--return-file", f"delivery-review=review/R1/{review_attempt_id}.return.json",
            "--timeout", "2",
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("delivery_review_latch_releases", review_wait.returncode == 0 and "all_agent_returns_received" in review_wait.stdout, review_wait.stdout + review_wait.stderr))

        wrong_attempt = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "attest-result",
            "--manifest", str(manifest),
            "--review-result", str(review_result),
            "--agent-task-id", "agent-delivery_review_wrong_attempt",
            "--review-attempt-id", "delivery-review-r1-a2",
            "--output", str(work / "wrong-attempt.attestation.json"),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("review_attempt_mismatch_blocks", wrong_attempt.returncode == 2 and "review_attempt_mismatch" in (wrong_attempt.stdout + wrong_attempt.stderr), wrong_attempt.stdout + wrong_attempt.stderr))

        attest_from_result = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "attest-result",
            "--manifest", str(manifest),
            "--review-result", str(review_result),
            "--agent-task-id", "agent-delivery_review_result",
            "--review-attempt-id", review_attempt_id,
            "--output", str(result_attestation),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("one_shot_review_result_attested", attest_from_result.returncode == 0 and "delivery_review_result_attested" in attest_from_result.stdout, attest_from_result.stdout + attest_from_result.stderr))

        freeform_attest = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "attest",
            "--manifest", str(manifest),
            "--agent-task-id", "agent-delivery_review_r1",
            "--review-status", "passed",
            "--summary", "最终候选稿、裁决和来源复核通过",
            "--output", str(work / "freeform-attestation.json"),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("freeform_attest_disabled", freeform_attest.returncode == 2 and "freeform_attest_disabled_use_attest_result" in (freeform_attest.stdout + freeform_attest.stderr), freeform_attest.stdout + freeform_attest.stderr))

        verify_pass = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "verify",
            "--manifest", str(manifest),
            "--attestation", str(attestation),
            "--receipt", str(receipt),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("review_release_verified", verify_pass.returncode == 0 and "review_release_verified" in verify_pass.stdout and receipt.is_file(), verify_pass.stdout + verify_pass.stderr))

        public_receipt = work / "public-output-receipt.json"
        public_check = subprocess.run([
            sys.executable, str(PUBLIC_GUARD),
            "--file", str(output / "report.json"),
            "--file", str(output / "report.md"),
            "--file", str(output / "report.pdf"),
            "--output", str(public_receipt),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("public_guard_receipt_created", public_check.returncode == 0 and public_receipt.is_file(), public_check.stdout + public_check.stderr))

        blocked_completion = subprocess.run([
            sys.executable, str(COMPLETION_GATE),
            "--report-dir", str(output),
            "--public-guard-receipt", str(public_receipt),
            "--claim-receipt", str(output / "claim-receipt.json"),
            "--output", str(work / "blocked-completion-receipt.json"),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        checks.append(("completion_before_review_blocks", blocked_completion.returncode == 2 and "review_evidence_missing" in (blocked_completion.stdout + blocked_completion.stderr), blocked_completion.stdout + blocked_completion.stderr))

        completion_receipt = work / "completion-receipt.json"
        completion = subprocess.run([
            sys.executable, str(COMPLETION_GATE),
            "--report-dir", str(output),
            "--public-guard-receipt", str(public_receipt),
            "--manifest", str(manifest),
            "--attestation", str(result_attestation),
            "--release-receipt", str(receipt),
            "--claim-receipt", str(output / "claim-receipt.json"),
            "--output", str(completion_receipt),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        completion_payload = json.loads(completion_receipt.read_text(encoding="utf-8")) if completion_receipt.is_file() else {}
        review_activity = next((item for item in completion_payload.get("expert_activity", []) if item.get("agent_id") == "delivery-review"), {})
        checks.append(("formal_completion_gate_releases", completion.returncode == 0 and completion_payload.get("status") == "formal_delivery_complete" and review_activity.get("agent_task_ids") == ["agent-delivery_review_result"], completion.stdout + completion.stderr))

        original_report = (output / "report.md").read_text(encoding="utf-8")
        (output / "report.md").write_text(original_report + "\n复核后错误改稿\n", encoding="utf-8")
        stale_report = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "verify", "--manifest", str(manifest), "--attestation", str(attestation),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        stale_report_text = stale_report.stdout + stale_report.stderr
        checks.append(("report_edit_after_review_blocks", stale_report.returncode == 2 and "review_stale_blocked" in stale_report_text, stale_report_text))
        (output / "report.md").write_text(original_report, encoding="utf-8")

        original_pdf = (output / "report.pdf").read_bytes()
        (output / "report.pdf").write_bytes(original_pdf + b"stale")
        stale_pdf = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "verify", "--manifest", str(manifest), "--attestation", str(attestation),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        stale_pdf_text = stale_pdf.stdout + stale_pdf.stderr
        checks.append(("pdf_edit_after_review_blocks", stale_pdf.returncode == 2 and "review_stale_blocked" in stale_pdf_text, stale_pdf_text))
        (output / "report.pdf").write_bytes(original_pdf)

        original_source = files["data-analyst"].read_text(encoding="utf-8")
        files["data-analyst"].write_text(original_source + "\n", encoding="utf-8")
        stale_source = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "verify", "--manifest", str(manifest), "--attestation", str(attestation),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        stale_source_text = stale_source.stdout + stale_source.stderr
        checks.append(("source_change_after_review_blocks", stale_source.returncode == 2 and "review_stale_blocked" in stale_source_text, stale_source_text))
        files["data-analyst"].write_text(original_source, encoding="utf-8")

        conditional_attempt_id = "delivery-review-r1-conditional"
        conditional_result = work / "review" / "R1" / f"{conditional_attempt_id}.return.json"
        conditional = work / "review" / "R1" / f"{conditional_attempt_id}.attestation.json"
        write_json(conditional_result, {
            "schema_version": "1.0",
            "run_id": "run-collaboration-smoke",
            "agent_id": "delivery-review",
            "review_attempt_id": conditional_attempt_id,
            "report_revision": "R1",
            "return_status": "completed",
            "returned_at": "2099-08-13T00:00:00Z",
            "review_status": "conditional_pass",
            "reviewed_manifest_sha256": manifest_payload["manifest_sha256"],
            "reviewed_artifacts": [{"file": item["file"], "sha256": item["sha256"]} for item in manifest_payload["artifacts"]],
            "findings": ["行动负责人缺失"],
            "required_changes": ["补齐行动负责人"],
            "contribution_summary": "存在必改项",
        })
        attest_conditional = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "attest-result",
            "--manifest", str(manifest),
            "--review-result", str(conditional_result),
            "--agent-task-id", "agent-delivery_review_conditional",
            "--review-attempt-id", conditional_attempt_id,
            "--output", str(conditional),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        verify_conditional = subprocess.run([
            sys.executable, str(REVIEW_GUARD), "verify", "--manifest", str(manifest), "--attestation", str(conditional),
        ], capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV)
        conditional_text = verify_conditional.stdout + verify_conditional.stderr
        checks.append(("conditional_pass_cannot_release", attest_conditional.returncode == 0 and verify_conditional.returncode == 2 and "review_not_passed_blocked" in conditional_text, conditional_text))

    failed = [item for item in checks if not item[1]]
    result = {
        "status": "PASS" if not failed else "FAIL",
        "total": len(checks),
        "passed": len(checks) - len(failed),
        "failed": len(failed),
        "checks": [{"name": name, "status": "PASS" if ok else "FAIL", "detail": detail.strip()} for name, ok, detail in checks],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
