"""
compliance_core — 合规检查核心模块（内嵌版）
提供统一的 CLI 接口、报告格式化、检查引擎等基础能力。
"""
from .cli_base import UnifiedCLI, CheckResult, Severity
from .report_core import ReportGenerator, ReportFormat
from .check_engine import CheckEngine

__all__ = [
    "UnifiedCLI", "CheckResult", "Severity",
    "ReportGenerator", "ReportFormat",
    "CheckEngine",
]
