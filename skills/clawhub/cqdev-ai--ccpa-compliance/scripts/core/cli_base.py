#!/usr/bin/env python3
"""
UnifiedCLI — 统一命令行接口基类

为所有合规检查工具提供一致的 CLI 体验，包括：
- 标准化的参数解析
- 统一的输出格式（text / json / markdown）
- 多场景支持与扩展点
"""

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from typing import List, Optional


class Severity(Enum):
    """合规检查严重程度"""
    PASS = "通过"
    INFO = "提示"
    WARN = "警告"
    FAIL = "不合规"
    ERROR = "严重违规"

    def __str__(self):
        return self.value


@dataclass
class CheckResult:
    """单个检查项的结果"""
    check_id: str
    description: str
    severity: Severity
    passed: bool
    details: str = ""
    recommendation: str = ""
    regulation_ref: str = ""


@dataclass
class ComplianceReport:
    """统一的合规检查报告"""
    tool_name: str
    regulation: str
    check_time: str = field(default_factory=lambda: datetime.now().isoformat())
    scenario: str = ""
    summary: dict = field(default_factory=lambda: {
        "total": 0, "passed": 0, "warned": 0, "failed": 0
    })
    results: List[dict] = field(default_factory=list)
    
    def add_result(self, r: CheckResult):
        self.results.append({
            "check_id": r.check_id,
            "description": r.description,
            "severity": str(r.severity),
            "passed": r.passed,
            "details": r.details,
            "recommendation": r.recommendation,
            "regulation_ref": r.regulation_ref,
        })
        self.summary["total"] += 1
        if r.severity == Severity.PASS:
            self.summary["passed"] += 1
        elif r.severity in (Severity.WARN, Severity.INFO):
            self.summary["warned"] += 1
        else:
            self.summary["failed"] += 1
    
    def to_dict(self) -> dict:
        return {
            "tool": self.tool_name,
            "regulation": self.regulation,
            "check_time": self.check_time,
            "scenario": self.scenario,
            "summary": self.summary,
            "results": self.results,
        }


class UnifiedCLI:
    """统一命令行接口基类"""

    def __init__(self, tool_name: str, description: str):
        self.tool_name = tool_name
        self.description = description
        self.parser = argparse.ArgumentParser(
            description=description,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=self._epilog()
        )
        self._add_common_args()

    def _epilog(self) -> str:
        return f"""
示例:
  # 基本检查
  python {self.tool_name}.py --scenario user_registration

  # JSON 输出到文件
  python {self.tool_name}.py --scenario cross_border --format json --output report.json

  # 交互模式
  python {self.tool_name}.py --interactive

  # 列出所有检查场景
  python {self.tool_name}.py --list-scenarios
"""

    def _add_common_args(self):
        """统一参数"""
        self.parser.add_argument(
            '--scenario', '-s',
            help='检查场景名称（运行 --list-scenarios 查看所有可用场景）'
        )
        self.parser.add_argument(
            '--interactive', '-i',
            action='store_true',
            help='交互式检查模式'
        )
        self.parser.add_argument(
            '--output', '-o',
            help='输出报告文件路径'
        )
        self.parser.add_argument(
            '--format', '-f',
            choices=['text', 'json', 'markdown'],
            default='text',
            help='输出格式（默认: text）'
        )
        self.parser.add_argument(
            '--list-scenarios',
            action='store_true',
            help='列出所有可用的检查场景'
        )
        self.parser.add_argument(
            '--verbose', '-v',
            action='store_true',
            help='详细输出模式'
        )

    def parse_args(self, argv=None):
        return self.parser.parse_args(argv)

    def print_report(self, report: ComplianceReport, fmt: str = "text"):
        """统一输出"""
        if fmt == "json":
            print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
        elif fmt == "markdown":
            self._print_markdown(report)
        else:
            self._print_text(report)

    def _print_text(self, report: ComplianceReport):
        s = report.summary
        print(f"\n{'='*60}")
        print(f"  {report.tool_name} — {report.regulation}")
        print(f"  检查时间: {report.check_time[:19]}")
        if report.scenario:
            print(f"  场景: {report.scenario}")
        print(f"{'='*60}")
        print(f"  总览: 共 {s['total']} 项 | "
              f"✅ 通过 {s['passed']} | "
              f"⚠️ 提醒 {s['warned']} | "
              f"❌ 问题 {s['failed']}")
        print(f"{'='*60}")
        for r in report.results:
            icon = "✅" if r["severity"] == "通过" else \
                   "⚠️" if r["severity"] in ("提示", "警告") else "❌"
            print(f"\n  {icon} [{r['check_id']}] {r['description']}")
            if r["details"]:
                print(f"    详情: {r['details']}")
            if r["recommendation"]:
                print(f"    建议: {r['recommendation']}")
            if r["regulation_ref"]:
                print(f"    依据: {r['regulation_ref']}")
        print(f"{'='*60}\n")
 
    def _print_markdown(self, report: ComplianceReport):
        s = report.summary
        print(f"# {report.tool_name} — {report.regulation}")
        print(f"\n- **检查时间**: {report.check_time[:19]}")
        if report.scenario:
            print(f"- **场景**: {report.scenario}")
        print(f"\n## 总览")
        print(f"| 总计 | 通过 | 提醒 | 问题 |")
        print(f"|:---:|:---:|:---:|:---:|")
        print(f"| {s['total']} | {s['passed']} | {s['warned']} | {s['failed']} |")
        print(f"\n## 检查明细")
        for r in report.results:
            icon = "✅" if r["severity"] == "通过" else \
                   "⚠️" if r["severity"] in ("提示", "警告") else "❌"
            print(f"\n### {icon} {r['description']}")
            print(f"- **编号**: {r['check_id']}")
            print(f"- **状态**: {r['severity']}")
            if r["details"]:
                print(f"- **详情**: {r['details']}")
            if r["recommendation"]:
                print(f"- **建议**: {r['recommendation']}")
            if r["regulation_ref"]:
                print(f"- **依据**: {r['regulation_ref']}")

    def list_scenarios(self, scenarios: dict):
        """列出可用场景"""
        print(f"\n{'='*50}")
        print(f"  可用检查场景 — {self.tool_name}")
        print(f"{'='*50}")
        for key, info in scenarios.items():
            checks = ", ".join(info.get("checks", []))
            print(f"\n  [{key}] {info['name']}")
            print(f"         检查项: {checks}")
        print()
