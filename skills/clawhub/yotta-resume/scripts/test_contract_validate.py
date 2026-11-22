#!/usr/bin/env python3
"""Offline contract tests for yotta-resume 0.2.0."""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
VALIDATOR = HERE / "contract_validate.py"
CLI = HERE / "yotta_resume.py"
TODAY = "2026-11-21"

ROLE_IDS = (
    "soc",
    "incident_response",
    "offensive_security",
    "appsec",
    "security_engineering",
    "grc_data_security",
)
LEVELS = ("junior", "mid", "senior", "lead")


def _question_hash(question):
    payload = {
        key: value
        for key, value in question.items()
        if key != "content_hash"
    }
    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def valid_bundle():
    roles = []
    for role_id in ROLE_IDS:
        roles.append({
            "id": role_id,
            "display_name": role_id,
            "aliases": [role_id + "-alias"],
            "nice_work_roles": ["Work Role"],
            "evidence_dimensions": ["scope", "result"],
            "interview_dimensions": ["triage", "boundary"],
            "risk_rules": ["require_authorization"],
            "resume_evidence_requirements": ["scope", "action", "result"],
        })

    question = {
        "question_id": "sec-soc-mid-0001",
        "role_family": "soc",
        "level": "mid",
        "dimension": "incident_triage",
        "kind": "scenario",
        "prompt": "给定告警序列，说明研判、升级和验证依据。",
        "expected_evidence": ["scope", "decision", "verification"],
        "followups": ["为什么这样定级？"],
        "answer_boundary": "只讨论授权范围内的防御研判。",
        "source_refs": ["nist-nice"],
        "status": "active",
        "last_verified_at": TODAY,
        "stale_after_days": 180,
        "freshness_label": "latest",
    }
    question["content_hash"] = _question_hash(question)

    return {
        "security-role-map.json": {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "levels": list(LEVELS),
            "role_families": roles,
        },
        "security-role-map.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "security-role-map",
            "type": "object",
        },
        "source-registry.json": {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "sources": [{
                "source_id": "nist-nice",
                "layer": "A",
                "title": "NIST NICE Framework",
                "publisher": "NIST",
                "url": "https://www.nist.gov/itl/applied-cybersecurity/nice",
                "published_at": "2025-04-28",
                "retrieved_at": TODAY,
                "last_verified_at": TODAY,
                "refresh_interval_days": 30,
                "stale_after_days": 90,
                "usage_policy": "facts_only",
                "license_review_status": "review_required",
                "status": "active",
            }],
        },
        "source-registry.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "source-registry",
            "type": "object",
        },
        "source-watch-state.json": {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "generated_at": TODAY,
            "sources": [{
                "source_id": "nist-nice",
                "content_sha256": "a" * 64,
                "etag": None,
                "last_modified": None,
                "checked_at": TODAY,
            }],
        },
        "source-watch-state.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "source-watch-state",
            "type": "object",
        },
        "question-bank.json": {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "bank_version": "0.0.0",
            "generated_at": TODAY,
            "questions": [question],
        },
        "question-bank.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "question-bank",
            "type": "object",
        },
        "evidence-ledger.json": {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "entries": [],
        },
        "evidence-ledger.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "evidence-ledger",
            "type": "object",
        },
        "dual-role-contract.json": {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "default_policy": "deny",
            "roles": ["candidate", "hr"],
            "data_classes": [
                "private_evidence_ledger",
                "raw_resume",
                "public_resume",
                "analysis_report",
                "interview_plan",
                "scorecard",
                "audit_log",
            ],
            "permissions": {
                "candidate": {
                    "private_evidence_ledger": ["read", "write"],
                    "raw_resume": ["read", "write"],
                    "public_resume": ["read", "write"],
                    "analysis_report": ["read", "write"],
                    "interview_plan": ["read"],
                    "scorecard": [],
                    "audit_log": ["read"],
                },
                "hr": {
                    "private_evidence_ledger": [],
                    "raw_resume": [],
                    "public_resume": ["read"],
                    "analysis_report": [],
                    "interview_plan": ["read"],
                    "scorecard": ["read", "write"],
                    "audit_log": ["read"],
                },
            },
            "protected_attributes": [
                "age",
                "gender",
                "marital_status",
                "ethnicity",
                "religion",
                "origin",
                "disability",
                "photo",
            ],
            "scoring_fields": ["skills", "experience", "evidence"],
            "cross_role_export": {
                "requires_field_manifest": True,
                "requires_confirmation": True,
                "default_export_class": "public_resume",
                "independent_workdirs": True,
                "independent_outputs": True,
            },
        },
        "dual-role-contract.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "dual-role-contract",
            "type": "object",
        },
        "industry-registry.json": {
            "schema_version": "1.0",
            "contract_version": "1.0",
            "generated_at": TODAY,
            "default_industry": "generic",
            "detection": {
                "strategy": "keyword_score_v1",
                "min_high_confidence_hits": 4,
                "ambiguity_margin": 1,
            },
            "extensions": {
                "allow_new_profiles": True,
                "required_fields": [
                    "id",
                    "display_name",
                    "keywords",
                    "evidence_dimensions",
                    "question_dimensions",
                    "role_map_ref",
                    "is_fallback",
                ],
            },
            "industries": [
                {
                    "id": "cybersecurity",
                    "display_name": "网络安全",
                    "keywords": ["SIEM", "SOC", "应急响应"],
                    "evidence_dimensions": ["scope", "action", "result"],
                    "question_dimensions": ["triage", "boundary"],
                    "role_map_ref": "security-role-map.json",
                    "is_fallback": False,
                },
                {
                    "id": "generic",
                    "display_name": "通用",
                    "keywords": [],
                    "evidence_dimensions": ["scope", "action", "result"],
                    "question_dimensions": ["facts", "boundary"],
                    "role_map_ref": None,
                    "is_fallback": True,
                },
            ],
        },
        "industry-registry.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "industry-registry",
            "type": "object",
        },
        "interview-session.schema.json": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "interview-session",
            "type": "object",
            "required": [
                "session_id",
                "status",
                "inputs",
                "selection",
                "questions",
                "answers",
                "current_question_id",
                "current_phase"
            ],
            "properties": {
                "schema_version": {
                    "const": "1.0"
                },
                "status": {
                    "enum": [
                        "in_progress",
                        "completed"
                    ]
                }
            }
        },
    }


class ContractFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "data"
        self.root.mkdir()
        self.bundle = valid_bundle()
        self.write_bundle()

    def tearDown(self):
        self.temp.cleanup()

    def write_bundle(self):
        for filename, payload in self.bundle.items():
            (self.root / filename).write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

    def rewrite(self, filename, payload):
        self.bundle[filename] = payload
        (self.root / filename).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def run_json(self, executable, *extra):
        completed = subprocess.run(
            [
                sys.executable,
                str(executable),
                "--root",
                str(self.root),
                "--format",
                "json",
                "--today",
                TODAY,
                *extra,
            ],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError:
            payload = {}
        return completed, payload

    def error_codes(self, payload):
        return {
            item.get("code")
            for item in payload.get("errors", [])
            if isinstance(item, dict)
        }


class ContractValidatorTest(ContractFixture):
    def test_valid_bundle_checks_all_fifteen_release_files(self):
        completed, payload = self.run_json(VALIDATOR)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertTrue(payload.get("ok"))
        self.assertEqual(payload.get("checked_files"), 15)
        self.assertEqual(payload.get("industry_count"), 2)
        self.assertEqual(payload.get("errors"), [])

    def test_duplicate_industry_id_is_rejected(self):
        registry = self.bundle["industry-registry.json"]
        registry["industries"].append(dict(registry["industries"][0]))
        self.rewrite("industry-registry.json", registry)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("INDUSTRY_DUPLICATE", self.error_codes(payload))

    def test_missing_fallback_industry_is_rejected(self):
        registry = self.bundle["industry-registry.json"]
        registry["industries"][-1]["is_fallback"] = False
        self.rewrite("industry-registry.json", registry)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("INDUSTRY_FALLBACK_INVALID", self.error_codes(payload))

    def test_duplicate_role_family_is_rejected(self):
        role_map = self.bundle["security-role-map.json"]
        role_map["role_families"].append(dict(role_map["role_families"][0]))
        self.rewrite("security-role-map.json", role_map)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("ROLE_DUPLICATE", self.error_codes(payload))

    def test_duplicate_question_prompt_is_rejected(self):
        bank = self.bundle["question-bank.json"]
        duplicate = dict(bank["questions"][0])
        duplicate["question_id"] = "sec-soc-mid-0002"
        duplicate["content_hash"] = _question_hash(duplicate)
        bank["questions"].append(duplicate)
        self.rewrite("question-bank.json", bank)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("QUESTION_PROMPT_DUPLICATE", self.error_codes(payload))

    def test_unknown_level_is_rejected(self):
        bank = self.bundle["question-bank.json"]
        bank["questions"][0]["level"] = "expert"
        bank["questions"][0]["content_hash"] = _question_hash(bank["questions"][0])
        self.rewrite("question-bank.json", bank)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("LEVEL_UNKNOWN", self.error_codes(payload))

    def test_expired_source_is_rejected(self):
        registry = self.bundle["source-registry.json"]
        registry["sources"][0]["last_verified_at"] = "2025-01-01"
        self.rewrite("source-registry.json", registry)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("SOURCE_EXPIRED", self.error_codes(payload))

    def test_missing_question_source_is_rejected(self):
        bank = self.bundle["question-bank.json"]
        bank["questions"][0]["source_refs"] = ["missing-source"]
        bank["questions"][0]["content_hash"] = _question_hash(bank["questions"][0])
        self.rewrite("question-bank.json", bank)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("QUESTION_SOURCE_MISSING", self.error_codes(payload))

    def test_d_only_question_source_is_rejected(self):
        registry = self.bundle["source-registry.json"]
        registry["sources"][0]["layer"] = "D"
        self.rewrite("source-registry.json", registry)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("QUESTION_SOURCE_WEAK", self.error_codes(payload))

    def test_stale_question_cannot_be_labelled_latest(self):
        bank = self.bundle["question-bank.json"]
        bank["questions"][0]["last_verified_at"] = "2025-01-01"
        bank["questions"][0]["content_hash"] = _question_hash(bank["questions"][0])
        self.rewrite("question-bank.json", bank)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("QUESTION_STALE", self.error_codes(payload))

    def test_source_watch_state_cannot_reference_unknown_source(self):
        state = self.bundle["source-watch-state.json"]
        state["sources"][0]["source_id"] = "missing-source"
        self.rewrite("source-watch-state.json", state)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("SOURCE_STATE_UNKNOWN", self.error_codes(payload))

    def test_source_watch_state_hash_must_be_sha256(self):
        state = self.bundle["source-watch-state.json"]
        state["sources"][0]["content_sha256"] = "not-a-hash"
        self.rewrite("source-watch-state.json", state)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("SOURCE_STATE_HASH_INVALID", self.error_codes(payload))

    def test_unconfirmed_evidence_cannot_be_exported(self):
        ledger = self.bundle["evidence-ledger.json"]
        ledger["entries"].append({
            "evidence_id": "EV-001",
            "section": "experience",
            "claim": "完成告警治理",
            "scenario": "SOC",
            "goal": "降低误报",
            "responsibility": "lead",
            "actions": ["优化规则"],
            "methods": ["SIEM"],
            "scale": "1000 条/日",
            "result": "误报下降 30%",
            "supporting_artifacts": ["看板"],
            "boundaries": "仅本人负责规则部分",
            "user_confirmed": False,
            "source_refs": ["nist-nice"],
            "sensitivity": "internal",
            "export_allowed": True,
        })
        self.rewrite("evidence-ledger.json", ledger)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("LEDGER_UNCONFIRMED_EXPORT", self.error_codes(payload))

    def test_evidence_confirmation_and_export_flags_must_be_boolean(self):
        ledger = self.bundle["evidence-ledger.json"]
        ledger["entries"].append({
            "evidence_id": "EV-002",
            "section": "experience",
            "claim": "完成告警治理",
            "scenario": "SOC",
            "goal": "降低误报",
            "responsibility": "lead",
            "actions": ["优化规则"],
            "methods": ["SIEM"],
            "scale": "1000 条/日",
            "result": "误报下降 30%",
            "supporting_artifacts": ["看板"],
            "boundaries": "仅本人负责规则部分",
            "user_confirmed": "false",
            "source_refs": ["nist-nice"],
            "sensitivity": "internal",
            "export_allowed": True,
        })
        self.rewrite("evidence-ledger.json", ledger)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("LEDGER_FIELD_TYPE_INVALID", self.error_codes(payload))

    def test_question_source_refs_must_be_strings(self):
        bank = self.bundle["question-bank.json"]
        bank["questions"][0]["source_refs"] = [["bad-source-ref"]]
        bank["questions"][0]["content_hash"] = _question_hash(bank["questions"][0])
        self.rewrite("question-bank.json", bank)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("QUESTION_SOURCE_REF_INVALID", self.error_codes(payload))
        self.assertNotIn("Traceback", completed.stderr)

    def test_hr_cannot_read_private_evidence_ledger(self):
        contract = self.bundle["dual-role-contract.json"]
        contract["permissions"]["hr"]["private_evidence_ledger"] = ["read"]
        self.rewrite("dual-role-contract.json", contract)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("ROLE_ACCESS_DENIED", self.error_codes(payload))

    def test_protected_attribute_cannot_be_scored(self):
        contract = self.bundle["dual-role-contract.json"]
        contract["scoring_fields"].append("age")
        self.rewrite("dual-role-contract.json", contract)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("PROTECTED_ATTRIBUTE_SCORED", self.error_codes(payload))

    def test_cross_role_export_requires_confirmation(self):
        contract = self.bundle["dual-role-contract.json"]
        contract["cross_role_export"]["requires_confirmation"] = False
        self.rewrite("dual-role-contract.json", contract)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("CROSS_ROLE_CONFIRMATION_REQUIRED", self.error_codes(payload))

    def test_unknown_permission_action_is_rejected(self):
        contract = self.bundle["dual-role-contract.json"]
        contract["permissions"]["hr"]["public_resume"] = ["admin"]
        self.rewrite("dual-role-contract.json", contract)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("ROLE_ACTION_INVALID", self.error_codes(payload))

    def test_permission_data_classes_must_be_strings(self):
        contract = self.bundle["dual-role-contract.json"]
        contract["data_classes"].append({"bad": "class"})
        self.rewrite("dual-role-contract.json", contract)
        completed, payload = self.run_json(VALIDATOR)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("DATA_CLASSES_INVALID", self.error_codes(payload))
        self.assertNotIn("Traceback", completed.stderr)

    def test_invalid_today_is_a_controlled_error(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--root",
                str(self.root),
                "--format",
                "json",
                "--today",
                "not-a-date",
            ],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(completed.returncode, 2)
        payload = json.loads(completed.stdout)
        self.assertIn("TODAY_INVALID", {item["code"] for item in payload["errors"]})
        self.assertNotIn("Traceback", completed.stderr)

    def test_invalid_today_text_output_has_no_traceback(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--root",
                str(self.root),
                "--format",
                "text",
                "--today",
                "not-a-date",
            ],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("TODAY_INVALID", completed.stdout)
        self.assertNotIn("Traceback", completed.stderr)

    def test_validator_output_is_deterministic(self):
        first_completed, first = self.run_json(VALIDATOR)
        second_completed, second = self.run_json(VALIDATOR)
        self.assertEqual(first_completed.returncode, 0)
        self.assertEqual(second_completed.returncode, 0)
        self.assertEqual(first, second)


class BundledContractTest(ContractFixture):
    def run_bundled(self):
        return subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                "--root",
                str(SKILL_DIR / "data"),
                "--format",
                "json",
                "--today",
                TODAY,
            ],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )

    def test_bundled_contracts_are_complete(self):
        completed = self.run_bundled()
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["checked_files"], 15)
        self.assertEqual(payload["role_family_count"], 6)
        self.assertEqual(payload["level_count"], 4)
        self.assertEqual(payload["question_count"], 162)
        self.assertEqual(payload["industry_count"], 5)

    def test_main_cli_contracts_command_succeeds(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(CLI),
                "contracts",
                "--root",
                str(SKILL_DIR / "data"),
                "--format",
                "json",
                "--today",
                TODAY,
            ],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertTrue(json.loads(completed.stdout)["ok"])

    def test_main_cli_contracts_command_returns_six_on_failure(self):
        contract = self.bundle["dual-role-contract.json"]
        contract["permissions"]["hr"]["private_evidence_ledger"] = ["read"]
        self.rewrite("dual-role-contract.json", contract)
        completed = subprocess.run(
            [
                sys.executable,
                str(CLI),
                "contracts",
                "--root",
                str(self.root),
                "--format",
                "json",
                "--today",
                TODAY,
            ],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(completed.returncode, 6)
        payload = json.loads(completed.stdout)
        self.assertIn(
            "ROLE_ACCESS_DENIED",
            {item["code"] for item in payload["errors"]},
        )

    def test_npm_package_includes_contract_files(self):
        npm = shutil.which("npm.cmd") or shutil.which("npm")
        self.assertTrue(npm, "npm executable not found")
        completed = subprocess.run(
            [npm, "pack", "--dry-run", "--json", "--ignore-scripts"],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        package = payload[0] if isinstance(payload, list) else next(iter(payload.values()))
        files = {item["path"] for item in package["files"]}
        self.assertIn("data/security-role-map.json", files)
        self.assertIn("data/dual-role-contract.schema.json", files)
        self.assertIn("data/industry-registry.json", files)
        self.assertIn("data/industry-registry.schema.json", files)
        self.assertIn("data/interview-session.schema.json", files)
        self.assertIn("data/source-watch-state.json", files)
        self.assertIn("data/source-watch-state.schema.json", files)
        self.assertNotIn("scripts/source_watch.py", files)
        self.assertNotIn("scripts/bank_pipeline.py", files)
        self.assertNotIn("references/source-updates.md", files)
        self.assertIn("references/data-contracts.md", files)
        self.assertIn("examples/audit-report.example.md", files)

    def test_npm_package_excludes_history_and_candidate_directories(self):
        npm = shutil.which("npm.cmd") or shutil.which("npm")
        self.assertTrue(npm, "npm executable not found")
        history = SKILL_DIR / "data" / "history"
        probe = history / "package-probe.json"
        history.mkdir(exist_ok=True)
        probe.write_text("{}\n", encoding="utf-8")
        try:
            completed = subprocess.run(
                [npm, "pack", "--dry-run", "--json", "--ignore-scripts"],
                cwd=str(SKILL_DIR),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            payload = json.loads(completed.stdout)
            package = payload[0] if isinstance(payload, list) else next(iter(payload.values()))
            files = {item["path"] for item in package["files"]}
            self.assertNotIn("data/history/package-probe.json", files)
        finally:
            probe.unlink(missing_ok=True)
            try:
                history.rmdir()
            except OSError:
                pass


if __name__ == "__main__":
    unittest.main()
