#!/usr/bin/env python3
"""yotta-resume MVP contract tests."""

import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLI = HERE / "yotta_resume.py"
SKILL_DIR = HERE.parent
sys.path.insert(0, str(HERE))

import yotta_resume as yr  # noqa: E402


RESUME = """# 张三
13800138000 | zhangsan@example.com

## 个人简介
安全工程师，熟悉 SIEM、EDR 和应急响应，工作认真负责，沟通能力强。

## 工作经历
### 某互联网公司 | 安全运营 | 2024.01 - 2025.06
- 负责安全告警处置和日志分析，提升了处理效率。
- 参与漏洞管理平台建设，协助跨部门沟通。
- 主导一次勒索软件应急响应，完成隔离、溯源和恢复。

## 项目经历
### 告警降噪项目 | 2024.03 - 2024.09
- 使用 Python 和 SIEM 优化告警规则，减少重复告警。

## 技能
Python, SIEM, EDR, SQL, Linux

## 教育背景
某大学 | 信息安全 | 本科 | 2020.09 - 2024.06
"""

JD = """岗位职责：
1. 负责 SOC 告警研判、SIEM 规则优化和事件响应；
2. 使用 Python 或 SQL 进行日志分析；
3. 熟悉 MITRE ATT&CK、OWASP；
4. 参与漏洞管理和安全运营指标建设。
任职要求：本科及以上，3 年以上经验。
"""


class AuditTest(unittest.TestCase):
    def test_audit_detects_sections_metrics_and_risks(self):
        report = yr.audit_resume(RESUME, JD)
        self.assertEqual(report["schema_version"], "1.1")
        self.assertIn("experience", report["sections"])
        self.assertIn("skills", report["sections"])
        self.assertGreaterEqual(report["stats"]["bullet_count"], 4)
        self.assertGreaterEqual(report["stats"]["metric_bullets"], 0)
        self.assertTrue(report["issues"])
        codes = {issue["code"] for issue in report["issues"]}
        self.assertIn("weak_claim", codes)
        self.assertIn("missing_metric", codes)
        self.assertIn("sensitive_contact", codes)

    def test_audit_returns_targeted_questions(self):
        report = yr.audit_resume(RESUME, JD)
        self.assertTrue(report["questions"])
        joined = " ".join(item["question"] for item in report["questions"])
        self.assertIn("规模", joined)
        self.assertIn("独立负责", joined)

    def test_audit_provides_original_and_suggestion(self):
        report = yr.audit_resume(RESUME, JD)
        suggestions = report["suggestions"]
        self.assertTrue(suggestions)
        for item in suggestions:
            self.assertTrue(item["original"])
            self.assertTrue(item["suggestion"])
            self.assertIn(item["priority"], ("high", "medium", "low"))

    def test_audit_matches_jd_keywords(self):
        report = yr.audit_resume(RESUME, JD)
        matched = {item.lower() for item in report["jd_match"]["matched"]}
        missing = {item.lower() for item in report["jd_match"]["missing"]}
        self.assertIn("siem", matched)
        self.assertIn("mitre att&ck", missing)
        self.assertIn("owasp", missing)
        self.assertGreater(report["jd_match"]["coverage"], 0)
        self.assertLessEqual(report["jd_match"]["coverage"], 100)

    def test_audit_score_is_bounded(self):
        report = yr.audit_resume(RESUME, JD)
        self.assertGreaterEqual(report["readiness"]["score"], 0)
        self.assertLessEqual(report["readiness"]["score"], 100)
        self.assertEqual(report["readiness"]["score_type"], "structure_rule_score")
        self.assertIn("结构准备度", report["readiness"]["label"])
        self.assertTrue(report["readiness"]["not_market_fit"])
        self.assertIn("ATS", report["disclaimer"])

    def test_audit_without_jd_returns_unknown_coverage(self):
        report = yr.audit_resume(RESUME)
        self.assertIsNone(report["jd_match"]["coverage"])
        self.assertEqual(report["jd_match"]["status"], "not_provided")
        markdown = yr.render_audit_markdown(report)
        self.assertIn("未提供 JD", markdown)
        self.assertNotIn("JD 覆盖：100%", markdown)

    def test_audit_returns_all_weak_claims(self):
        resume = """# 李四

## 工作经历
### A 公司 | 安全工程师 | 2024.01 - 2025.01
- 负责安全告警处置。
- 参与漏洞管理平台建设。
- 协助完成应急响应复盘。
"""
        report = yr.audit_resume(resume)
        weak = [item for item in report["issues"] if item["code"] == "weak_claim"]
        self.assertEqual(len(weak), 3)
        self.assertEqual(len({item["id"] for item in report["issues"]}), len(report["issues"]))
        self.assertTrue(all(item["source_type"] == "rule" for item in weak))

    def test_audit_detects_deterministic_resume_risks(self):
        resume = """# 李四

## 求职意向
意向岗位：渗透测试
意向岗位：安全服务
毕业时间：2026.6

## 工作经历
### A 公司 | 安全工程师 | 2026.03 - 至今
- 累计输出每日防守报告 xx 份。

## 教育背景
### 某大学 | 信息安全 | 本科 | 2024.09 - 2026.07

## 技能
- 精通 Web 渗透；了解内网渗透。
"""
        report = yr.audit_resume(resume)
        codes = {item["code"] for item in report["issues"]}
        self.assertIn("placeholder", codes)
        self.assertIn("duplicate_field", codes)
        self.assertIn("date_conflict", codes)
        self.assertIn("mixed_skill_levels", codes)

    def test_audit_detects_watermark_and_image_gap(self):
        resume = """# 李四

## 工作经历
### A 公司 | 安全工程师 | 2024.01 - 2025.01
- 负责告警处置。
8901845cdf74c93103Ry2dq_FFZXxIS5WPucWOeqmPDUPhRn
8901845cdf74c93103Ry2dq_FFZXxIS5WPucWOeqmPDUPhRn
8901845cdf74c93103Ry2dq_FFZXxIS5WPucWOeqmPDUPhRn
"""
        manifest = {
            "type": "pdf",
            "filename": "resume.pdf",
            "backend": "pymupdf",
            "pages": 3,
            "images": 14,
            "text_chars": 100,
            "sha256": "A" * 64,
        }
        report = yr.audit_resume(resume, source_manifest=manifest)
        codes = {item["code"] for item in report["issues"]}
        self.assertIn("template_watermark", codes)
        self.assertIn("image_text_gap", codes)
        self.assertEqual(report["source_manifest"]["images"], 14)
        self.assertTrue(report["parse_warnings"])
        self.assertTrue(report["unknowns"])

    def test_audit_masks_contact_values_in_findings(self):
        report = yr.audit_resume(RESUME, JD)
        text = json.dumps(report, ensure_ascii=False)
        self.assertNotIn("13800138000", text)
        self.assertNotIn("zhangsan@example.com", text)

    def test_markdown_report_is_human_readable(self):
        report = yr.audit_resume(RESUME, JD)
        text = yr.render_audit_markdown(report)
        self.assertIn("# 元简简历分析", text)
        self.assertIn("结构准备度（规则分）", text)
        self.assertIn("## 工具发现", text)
        self.assertIn("## 高价值追问", text)
        self.assertIn("## 修改建议", text)
        self.assertIn("## 无法判断", text)
        self.assertIn("## 边界", text)
        self.assertIn("不得改写为其他数值", text)


class ResumeModelTest(unittest.TestCase):
    def test_parse_markdown_resume(self):
        model = yr.parse_markdown_resume(RESUME)
        self.assertEqual(model["name"], "张三")
        self.assertTrue(model["contact"])
        titles = [section["title"] for section in model["sections"]]
        self.assertIn("工作经历", titles)
        self.assertIn("技能", titles)

    def test_export_docx_contains_text(self):
        model = yr.parse_markdown_resume(RESUME)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "resume.docx"
            yr.export_docx(model, target)
            self.assertTrue(target.is_file())
            with zipfile.ZipFile(target) as package:
                self.assertIn("word/document.xml", package.namelist())
                xml = package.read("word/document.xml").decode("utf-8")
            self.assertIn("张三", xml)
            self.assertIn("安全运营", xml)

    def test_extract_docx_text_round_trip(self):
        model = yr.parse_markdown_resume(RESUME)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "resume.docx"
            yr.export_docx(model, target)
            text = yr.extract_text(target)
        self.assertIn("张三", text)
        self.assertIn("告警降噪项目", text)

    def test_render_html_escapes_untrusted_content(self):
        model = {
            "schema_version": "1.0",
            "name": "<script>alert(1)</script>",
            "headline": "安全工程师",
            "contact": [],
            "summary": "",
            "sections": [{"title": "工作经历", "items": [
                {"heading": "A & B", "bullets": ["<b>不能执行</b>"]}
            ]}],
        }
        html = yr.render_resume_html(model)
        self.assertNotIn("<script>alert(1)</script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertIn("A &amp; B", html)
        self.assertIn("&lt;b&gt;不能执行&lt;/b&gt;", html)

    def test_export_html(self):
        model = yr.parse_markdown_resume(RESUME)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "resume.html"
            yr.export_html(model, target)
            text = target.read_text(encoding="utf-8")
        self.assertIn("<!doctype html>", text)
        self.assertIn("张三", text)

    def test_pdf_export_when_browser_exists(self):
        browser = yr.find_pdf_browser()
        if not browser:
            self.skipTest("no Chromium/Edge browser found")
        model = yr.parse_markdown_resume(RESUME)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "resume.pdf"
            try:
                yr.export_pdf(model, target, browser_path=browser)
            except RuntimeError as error:
                if "No usable sandbox" in str(error):
                    self.skipTest("headless browser sandbox is unavailable")
                raise
            self.assertTrue(target.is_file())
            self.assertGreater(target.stat().st_size, 1000)
            self.assertTrue(target.read_bytes().startswith(b"%PDF"))


class CliTest(unittest.TestCase):
    def run_cli(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = yr.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_version(self):
        code, out, _ = self.run_cli(["--version"])
        self.assertEqual(code, 0)
        self.assertEqual(yr.VERSION, "0.2.0")
        self.assertIn("0.2.0", out)

    def test_audit_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            resume = Path(tmp) / "resume.md"
            jd = Path(tmp) / "jd.txt"
            resume.write_text(RESUME, encoding="utf-8")
            jd.write_text(JD, encoding="utf-8")
            code, out, _ = self.run_cli([
                "audit", "--resume", str(resume), "--jd", str(jd), "--format", "json"
            ])
        self.assertEqual(code, 0)
        payload = json.loads(out)
        self.assertEqual(payload["schema_version"], "1.1")

    def test_audit_missing_file_returns_three(self):
        code, _, err = self.run_cli([
            "audit", "--resume", "no-such-resume.md", "--format", "json"
        ])
        self.assertEqual(code, 3)
        self.assertIn("不存在", err)

    def test_malformed_pdf_returns_controlled_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            resume = Path(tmp) / "broken.pdf"
            resume.write_bytes(b"%PDF-1.4\nnot a real pdf\n")
            code, _, err = self.run_cli([
                "audit", "--resume", str(resume), "--format", "json"
            ])
        self.assertEqual(code, 5)
        self.assertIn("PDF", err)
        self.assertNotIn("Traceback", err)

    def test_export_docx_and_html(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "revised.md"
            docx = Path(tmp) / "revised.docx"
            html = Path(tmp) / "revised.html"
            source.write_text(RESUME, encoding="utf-8")
            code, out, _ = self.run_cli([
                "export", "--input", str(source),
                "--docx", str(docx), "--html", str(html)
            ])
            self.assertEqual(code, 0)
            self.assertTrue(docx.is_file())
            self.assertTrue(html.is_file())
        self.assertIn("DOCX", out)

    def test_export_pdf_when_browser_exists(self):
        if not yr.find_pdf_browser():
            self.skipTest("no Chromium/Edge browser found")
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "revised.md"
            pdf = Path(tmp) / "revised.pdf"
            source.write_text(RESUME, encoding="utf-8")
            code, _, err = self.run_cli([
                "export", "--input", str(source), "--pdf", str(pdf)
            ])
            if code != 0 and "No usable sandbox" in err:
                self.skipTest("headless browser sandbox is unavailable")
            self.assertEqual(code, 0)
            self.assertTrue(pdf.read_bytes().startswith(b"%PDF"))


class SafetyTest(unittest.TestCase):
    def test_core_source_has_no_network_imports(self):
        source = (HERE / "yotta_resume.py").read_text(encoding="utf-8")
        for needle in ("import requests", "urllib.request", "urlopen", "http.client"):
            self.assertNotIn(needle, source)

    def test_no_shell_command_built_from_resume_text(self):
        source = (HERE / "yotta_resume.py").read_text(encoding="utf-8")
        self.assertNotIn("shell=True", source)
        self.assertNotIn("os.system(", source)

    def test_docx_export_does_not_include_original_sensitive_values_in_filename(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "13800138000.docx"
            model = yr.parse_markdown_resume(RESUME)
            yr.export_docx(model, target)
            self.assertTrue(target.is_file())

    def test_skill_contract_blocks_alternate_numeric_scores(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("结构准备度（规则分）", text)
        self.assertIn("不得改写为其他数值", text)
        self.assertIn("工具规则发现", text)
        self.assertIn("智能体复核发现", text)


class PdfInputTest(unittest.TestCase):
    def test_plain_text_normalization_joins_wrapped_paragraphs(self):
        raw = """# 李四

## 工作经历
• 负责安全告警处置并完成隔离、
溯源与恢复。
• 参与漏洞管理平台建设。
"""
        normalized = yr._normalise_plain_resume(raw)
        self.assertIn("负责安全告警处置并完成隔离、溯源与恢复。", normalized)
        self.assertIn("• 参与漏洞管理平台建设。", normalized)

    def test_read_pdf_document_extracts_source_manifest(self):
        try:
            import pymupdf
        except ImportError:
            self.skipTest("pymupdf not installed")
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "resume.pdf"
            document = pymupdf.open()
            page = document.new_page()
            page.insert_text(
                (72, 72),
                "SECURITY RESUME\nWORK EXPERIENCE\n- Reduced false alerts by 30 percent.",
            )
            document.save(pdf)
            document.close()
            loaded = yr.read_resume_document(pdf)
        self.assertIn("SECURITY RESUME", loaded["text"])
        manifest = loaded["manifest"]
        self.assertEqual(manifest["type"], "pdf")
        self.assertEqual(manifest["pages"], 1)
        self.assertTrue(manifest["backend"])
        self.assertEqual(len(manifest["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
