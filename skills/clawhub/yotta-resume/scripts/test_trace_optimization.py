#!/usr/bin/env python3
"""Regression tests for the SkillHub TRACE and R2 question-bank work."""

import hashlib
import io
import json
import re
import errno
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
CLI = HERE / "yotta_resume.py"
TODAY = "2026-11-22"
sys.path.insert(0, str(HERE))

import yotta_resume as yr  # noqa: E402


RESUME = """# 李四
安全工程师

## 工作经历
### 某公司 | 安全工程师 | 2024.01 - 2025.01
- 负责 Kubernetes 集群安全加固，覆盖 20 个命名空间。
- 使用 Terraform 管理云安全策略，完成 12 项基线校验。
- 参与数据分类分级，覆盖 3 个业务域。

## 技能
Kubernetes, Terraform, 数据分类分级, OpenTelemetry
"""

JD = """岗位职责：
- 负责 Kubernetes、Terraform 和云安全基线建设。
- 参与数据分类分级和 OpenTelemetry 日志治理。
- 熟悉 SIEM。
"""


def question_hash(question):
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


class DoctorTest(unittest.TestCase):
    def run_subprocess(self, *extra):
        return subprocess.run(
            [sys.executable, str(CLI), "doctor", *extra],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )

    def test_doctor_reports_core_and_optional_checks(self):
        completed = self.run_subprocess("--format", "json", "--today", TODAY)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["version"], "0.2.0")
        checks = {item["id"]: item for item in payload["checks"]}
        for check_id in (
            "contracts",
            "package_files",
            "pdf_input",
            "pdf_export",
            "temp_dir",
            "interview_state",
            "cli",
        ):
            self.assertIn(check_id, checks)
            self.assertIn(checks[check_id]["status"], ("PASS", "WARN"))
        self.assertEqual(checks["contracts"]["status"], "PASS")
        self.assertEqual(checks["package_files"]["status"], "PASS")
        self.assertEqual(payload["errors"], [])

    def test_doctor_returns_six_for_invalid_contracts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "data"
            root.mkdir()
            for source in (SKILL_DIR / "data").glob("*.json"):
                (root / source.name).write_bytes(source.read_bytes())
            bank = json.loads((root / "question-bank.json").read_text(encoding="utf-8"))
            bank["questions"][0]["source_refs"] = ["missing-source"]
            bank["questions"][0]["content_hash"] = question_hash(bank["questions"][0])
            (root / "question-bank.json").write_text(
                json.dumps(bank, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            completed = self.run_subprocess(
                "--root",
                str(root),
                "--format",
                "json",
                "--today",
                TODAY,
            )
        self.assertEqual(completed.returncode, 6)
        payload = json.loads(completed.stdout)
        self.assertFalse(payload["ok"])
        self.assertTrue(payload["errors"])


class ExportTransactionTest(unittest.TestCase):
    def run_cli(self, argv):
        return subprocess.run(
            [sys.executable, str(CLI), *argv],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )

    def test_pdf_failure_leaves_no_new_partial_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "resume.md"
            docx = root / "resume.docx"
            html = root / "resume.html"
            pdf = root / "resume.pdf"
            source.write_text(RESUME, encoding="utf-8")
            args = [
                "export",
                "--input",
                str(source),
                "--docx",
                str(docx),
                "--html",
                str(html),
                "--pdf",
                str(pdf),
            ]
            original = yr.main
            with mock.patch.object(
                yr,
                "export_pdf",
                side_effect=RuntimeError("simulated PDF failure"),
            ):
                with redirect_stderr(io.StringIO()):
                    code = original(args)
            self.assertEqual(code, 4)
            self.assertFalse(docx.exists())
            self.assertFalse(html.exists())
            self.assertFalse(pdf.exists())

    def test_pdf_failure_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "resume.md"
            docx = root / "resume.docx"
            html = root / "resume.html"
            source.write_text(RESUME, encoding="utf-8")
            docx.write_bytes(b"old-docx")
            html.write_bytes(b"old-html")
            args = [
                "export",
                "--input",
                str(source),
                "--docx",
                str(docx),
                "--html",
                str(html),
                "--pdf",
                str(root / "resume.pdf"),
            ]
            with mock.patch.object(
                yr,
                "export_pdf",
                side_effect=RuntimeError("simulated PDF failure"),
            ):
                with redirect_stderr(io.StringIO()):
                    code = yr.main(args)
            self.assertEqual(code, 4)
            self.assertEqual(docx.read_bytes(), b"old-docx")
            self.assertEqual(html.read_bytes(), b"old-html")

    def test_duplicate_output_paths_are_rejected_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "resume.md"
            target = root / "same-output"
            source.write_text(RESUME, encoding="utf-8")
            completed = self.run_cli(
                [
                    "export",
                    "--input",
                    str(source),
                    "--docx",
                    str(target),
                    "--html",
                    str(target),
                ]
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn("重复", completed.stderr)
            self.assertFalse(target.exists())

    def test_commit_falls_back_when_temp_and_target_are_on_different_devices(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            staged = root / "staged.docx"
            target = root / "target.docx"
            staged.write_bytes(b"new-docx")
            real_replace = yr.os.replace

            def replace_or_exdev(source, destination):
                if Path(source) == staged and Path(destination) == target:
                    raise OSError(
                        errno.EXDEV,
                        "cross-device link",
                        str(source),
                    )
                return real_replace(source, destination)

            with mock.patch.object(yr.os, "replace", side_effect=replace_or_exdev):
                yr._commit_export_outputs(
                    [("DOCX", staged, target)],
                    root / "backups",
                )
            self.assertEqual(target.read_bytes(), b"new-docx")
            self.assertFalse(staged.exists())


class JdBoundaryTest(unittest.TestCase):
    def test_expanded_vocabulary_matches_security_infrastructure_terms(self):
        report = yr.audit_resume(RESUME, JD)
        matched = set(report["jd_match"]["matched"])
        self.assertIn("Kubernetes", matched)
        self.assertIn("Terraform", matched)
        self.assertIn("数据分类分级", matched)
        self.assertIn("OpenTelemetry", matched)

    def test_jd_match_exposes_deterministic_lexicon_boundary(self):
        match = yr.audit_resume(RESUME, JD)["jd_match"]
        self.assertTrue(match["lexicon_version"])
        self.assertTrue(match["limitations"])
        self.assertIn("固定", match["limitations"])


class IndustryDetectionTest(unittest.TestCase):
    def test_security_resume_is_detected_with_high_confidence(self):
        report = yr.audit_resume(RESUME, JD)
        detection = report["industry_detection"]
        self.assertEqual(detection["primary_industry"], "cybersecurity")
        self.assertEqual(detection["display_name"], "网络安全")
        self.assertIn(detection["confidence"], ("high", "medium"))
        self.assertIn("Kubernetes", detection["matched_keywords"])
        self.assertTrue(detection["evidence_dimensions"])

    def test_software_resume_is_detected_without_security_profile(self):
        resume = """# 王五
## 工作经历
- 使用 TypeScript、React 和 Node.js 开发微服务。
- 负责 REST API、单元测试和 CI/CD 流水线。
## 技能
JavaScript, TypeScript, React, Node.js, Docker
"""
        detection = yr.audit_resume(resume)["industry_detection"]
        self.assertEqual(detection["primary_industry"], "software_engineering")
        self.assertIn(detection["confidence"], ("high", "medium"))
        self.assertIn("TypeScript", detection["matched_keywords"])

    def test_industry_detection_uses_generic_fallback_for_unknown_content(self):
        resume = """# 赵六
## 个人简介
认真负责，沟通能力强。
## 工作经历
- 完成日常协作任务。
"""
        detection = yr.audit_resume(resume)["industry_detection"]
        self.assertEqual(detection["primary_industry"], "generic")
        self.assertEqual(detection["status"], "fallback")
        self.assertEqual(detection["confidence"], "low")

    def test_industry_detection_reports_ambiguity_instead_of_guessing(self):
        resume = """# 钱七
## 技能
React, SIEM
"""
        detection = yr.audit_resume(resume)["industry_detection"]
        self.assertEqual(detection["status"], "ambiguous")
        self.assertIsNone(detection["primary_industry"])
        self.assertGreaterEqual(len(detection["candidates"]), 2)

    def test_industry_registry_is_designed_for_future_profiles(self):
        registry = json.loads(
            (SKILL_DIR / "data" / "industry-registry.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(registry["default_industry"], "generic")
        self.assertTrue(registry["extensions"]["allow_new_profiles"])
        industries = {item["id"]: item for item in registry["industries"]}
        self.assertEqual(
            set(industries),
            {
                "cybersecurity",
                "software_engineering",
                "data_ai",
                "business_operations",
                "generic",
            },
        )
        self.assertEqual(
            sum(1 for item in industries.values() if item["is_fallback"]),
            1,
        )
        for industry in industries.values():
            self.assertTrue(industry["evidence_dimensions"])
            if not industry["is_fallback"]:
                self.assertTrue(industry["keywords"])

    def test_markdown_report_includes_industry_detection(self):
        text = yr.render_audit_markdown(yr.audit_resume(RESUME, JD))
        self.assertIn("## 行业识别", text)
        self.assertIn("网络安全", text)

    def test_audit_registry_failure_is_a_controlled_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            resume = Path(tmp) / "resume.md"
            resume.write_text(RESUME, encoding="utf-8")
            stderr = io.StringIO()
            with mock.patch.object(
                yr,
                "_industry_registry",
                side_effect=RuntimeError("industry registry unavailable"),
            ), redirect_stderr(stderr):
                code = yr.main(["audit", "--resume", str(resume), "--format", "json"])
        self.assertEqual(code, 5)
        self.assertIn("industry registry unavailable", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())


class BundledContentTest(unittest.TestCase):
    def test_question_bank_has_complete_mvp_distribution(self):
        bank = json.loads(
            (SKILL_DIR / "data" / "question-bank.json").read_text(encoding="utf-8")
        )
        questions = bank["questions"]
        self.assertEqual(bank["bank_version"], "0.2.0")
        self.assertEqual(len(questions), 162)
        self.assertEqual(
            {
                family: sum(1 for item in questions if item["role_family"] == family)
                for family in {
                    "soc",
                    "incident_response",
                    "offensive_security",
                    "appsec",
                    "security_engineering",
                    "grc_data_security",
                }
            },
            {
                "soc": 27,
                "incident_response": 27,
                "offensive_security": 27,
                "appsec": 27,
                "security_engineering": 27,
                "grc_data_security": 27,
            },
        )
        self.assertEqual(
            {
                kind: sum(1 for item in questions if item["kind"] == kind)
                for kind in ("knowledge", "resume_followup", "scenario")
            },
            {
                "knowledge": 120,
                "resume_followup": 30,
                "scenario": 12,
            },
        )
        self.assertEqual(len({item["question_id"] for item in questions}), 162)
        self.assertEqual(len({item["prompt"] for item in questions}), 162)
        self.assertEqual(
            {item["kind"] for item in questions},
            {"knowledge", "scenario", "resume_followup"},
        )
        for question in questions:
            self.assertEqual(question["content_hash"], question_hash(question))
            self.assertEqual(question["status"], "active")
            self.assertTrue(question["source_refs"])

    def test_question_bank_matches_source_generator(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(SKILL_DIR / "tools" / "build_question_bank.py"),
                "--check",
            ],
            cwd=str(SKILL_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_evidence_ledger_contains_only_safe_example_entry(self):
        ledger = json.loads(
            (SKILL_DIR / "data" / "evidence-ledger.json").read_text(encoding="utf-8")
        )
        self.assertEqual(len(ledger["entries"]), 1)
        entry = ledger["entries"][0]
        self.assertFalse(entry["user_confirmed"])
        self.assertFalse(entry["export_allowed"])
        self.assertIn("EXAMPLE_ONLY", entry["supporting_artifacts"])
        self.assertIn("示例", entry["claim"])

    def test_required_examples_and_reference_indexes_exist(self):
        required = (
            "examples/resume.template.md",
            "examples/jd.example.md",
            "examples/audit-report.example.md",
            "examples/audit-report.example.json",
            "examples/interview-session.example.json",
            "examples/interview-review.example.md",
            "references/faq.md",
            "references/trigger-examples.md",
            "references/workflow-examples.md",
        )
        for relative in required:
            self.assertTrue((SKILL_DIR / relative).is_file(), relative)
        references = (SKILL_DIR / "references" / "README.md").read_text(
            encoding="utf-8"
        )
        for name in (
            "usage.md",
            "faq.md",
            "trigger-examples.md",
            "workflow-examples.md",
            "data-contracts.md",
        ):
            self.assertIn(name, references)

    def test_user_docs_use_doctor_instead_of_packaged_test_commands(self):
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        readme = (SKILL_DIR / "README.md").read_text(encoding="utf-8")
        readme_zh = (SKILL_DIR / "README.zh-CN.md").read_text(encoding="utf-8")
        for text in (skill, readme, readme_zh):
            self.assertIn("doctor", text)
            self.assertNotIn("python scripts/test_yotta_resume.py", text)
            self.assertNotIn("python scripts/test_contract_validate.py", text)

    def test_local_markdown_links_resolve_to_bundled_files(self):
        missing = []
        for markdown in SKILL_DIR.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            targets = re.findall(r"\]\(([^)]+)\)", text)
            targets += re.findall(r'<img\s+[^>]*src="([^"]+)"', text)
            for target in targets:
                target = target.split("#", 1)[0].strip()
                if (
                    not target
                    or target.startswith(("http://", "https://", "mailto:", "#"))
                ):
                    continue
                resolved = (markdown.parent / target).resolve()
                if not resolved.exists():
                    missing.append(
                        "{} -> {}".format(
                            markdown.relative_to(SKILL_DIR).as_posix(),
                            target,
                        )
                    )
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
