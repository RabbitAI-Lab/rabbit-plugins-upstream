#!/usr/bin/env python3
"""
CheckEngine — 检查引擎基类

封装通用的检查流程，包括：
- 场景定义与匹配
- 检查项分组与执行
- 风险等级评估
"""

from typing import Dict, List, Callable, Any
from .cli_base import CheckResult, Severity, ComplianceReport


class CheckEngine:
    """检查引擎 - 管理场景和检查项的注册与执行"""

    def __init__(self, tool_name: str, regulation: str):
        self.tool_name = tool_name
        self.regulation = regulation
        self._scenarios: Dict[str, dict] = {}
        self._checkers: Dict[str, Callable] = {}

    def register_scenario(self, key: str, name: str, checks: List[str],
                          description: str = ""):
        self._scenarios[key] = {
            "name": name,
            "checks": checks,
            "description": description,
        }

    def register_checker(self, check_id: str, fn: Callable):
        """注册检查函数，fn 返回 (passed, details, recommendation, ref)"""
        self._checkers[check_id] = fn

    def get_scenarios(self) -> Dict[str, dict]:
        return dict(self._scenarios)

    def run(self, scenario: str = None, interactive: bool = False,
            data: dict = None) -> ComplianceReport:
        """
        执行检查。

        Args:
            scenario: 场景名称
            interactive: 是否交互模式
            data: 外部传入的参数数据（非交互时使用）
        """
        report = ComplianceReport(
            tool_name=self.tool_name,
            regulation=self.regulation,
            scenario=scenario or "general",
        )

        if scenario and scenario not in self._scenarios:
            print(f"⚠️ 未知场景 '{scenario}'，使用全部检查项")
            check_ids = list(self._checkers.keys())
        elif scenario:
            check_ids = self._scenarios[scenario]["checks"]
        else:
            check_ids = list(self._checkers.keys())

        for cid in check_ids:
            if cid not in self._checkers:
                continue
            fn = self._checkers[cid]
            try:
                if interactive:
                    result = self._run_interactive(cid, fn)
                else:
                    scoped = (data or {}).get(cid, {})
                    result = fn(scoped)
                report.add_result(result)
            except Exception as e:
                report.add_result(CheckResult(
                    check_id=cid,
                    description=f"执行检查时出错",
                    severity=Severity.ERROR,
                    passed=False,
                    details=str(e),
                ))

        return report

    def _run_interactive(self, cid: str, fn: Callable) -> CheckResult:
        """交互模式：逐个提问"""
        print(f"\n📋 [{cid}] — {fn.__doc__ or '检查项'}")
        print("   请输入相关信息（留空跳过）:")
        try:
            user_input = input("   > ").strip()
        except (EOFError, KeyboardInterrupt):
            user_input = ""
        
        if not user_input:
            return CheckResult(
                check_id=cid,
                description=fn.__doc__ or cid,
                severity=Severity.INFO,
                passed=True,
                details="用户跳过此项检查",
            )
        return fn({"user_input": user_input})
