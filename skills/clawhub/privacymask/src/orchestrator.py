# Copyright (c) 2026 Joyxj2devs Team
"""
Privacymask Skill SDK - 统一技能访问层

将用户自然语言操作路由到对应的 MCP 纯函数。
"""

from pathlib import Path
from typing import Any, Dict, Optional

# ─── 状态管理 ──────────────────────────────────────────────

_DEFAULT_CONFIG = {
    "enabled": True,
    "output_base_dir": "",
    "default_rules": [],
    "default_categories": ["cn_personal", "cn_enterprise", "cn_financial",
                           "intl_pii", "intl_financial"],
    "auto_mask_directory": True,
    "log_file": "",
}


def _get_config() -> Dict[str, Any]:
    """获取当前配置"""
    return dict(_DEFAULT_CONFIG)


def _set_config(key: str, value: Any) -> None:
    """更新配置"""
    _DEFAULT_CONFIG[key] = value


# ─── 操作路由 ──────────────────────────────────────────────

class PrivacymaskOrchestrator:
    """
    Privacymask 技能编排器

    统一入口，路由到各纯函数：
    - scan_mask: 扫描并脱敏单个文件
    - mask_directory: 批量脱敏整文件夹
    - detect: 仅检测不脱敏
    - get_rules: 查看规则列表
    - custom_rule: 自定义规则
    - export_report: 导出报告
    """

    def scan_and_mask(self, params: Optional[Dict[str, Any]] = None,
                      state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """扫描并脱敏单个文件"""
        from tools.privacymask.mask import handle_scan_and_mask
        return handle_scan_and_mask(params or {}, state or {})

    def mask_directory(self, params: Optional[Dict[str, Any]] = None,
                       state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """递归脱敏整文件夹"""
        from tools.privacymask.mask import handle_mask_directory
        return handle_mask_directory(params or {}, state or {})

    def detect_only(self, params: Optional[Dict[str, Any]] = None,
                    state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """仅检测不脱敏（预览）"""
        from tools.privacymask.mask import handle_detect_only
        return handle_detect_only(params or {}, state or {})

    def get_rules(self, params: Optional[Dict[str, Any]] = None,
                  state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """查看脱敏规则"""
        from tools.privacymask.mask import handle_get_rules
        return handle_get_rules(params or {}, state or {})

    def custom_rule(self, params: Optional[Dict[str, Any]] = None,
                    state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """自定义规则管理"""
        from tools.privacymask.mask import handle_custom_rule
        return handle_custom_rule(params or {}, state or {})

    def export_report(self, params: Optional[Dict[str, Any]] = None,
                      state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """导出脱敏报告"""
        from tools.privacymask.mask import handle_export_report
        return handle_export_report(params or {}, state or {})

    def status(self, params: Optional[Dict[str, Any]] = None,
               state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """查看当前状态和配置"""
        config = _get_config()
        return {
            "success": True,
            "enabled": config["enabled"],
            "output_base_dir": config["output_base_dir"] or "未设置",
            "default_rules": config["default_rules"] or "全部规则",
            "default_categories": config["default_categories"],
            "total_builtin_rules": 20,
        }

    def config(self, params: Optional[Dict[str, Any]] = None,
               state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """查看/更新配置"""
        config = _get_config()
        # 如果有 action 参数，执行更新
        action = (params or {}).get("action", "")
        if action and action in config:
            value = (params or {}).get("value")
            if value is not None:
                _set_config(action, value)
                return {"success": True, "message": f"配置已更新: {action}={value}"}
        return {
            "success": True,
            "config": config,
        }


# ─── 自然语言路由 ──────────────────────────────────────────

def _route_by_text(text: str) -> str:
    """根据自然语言文本路由到操作"""
    t = text.lower()
    if "批量" in t or "文件夹" in t or "目录" in t or "batch" in t or "directory" in t:
        return "mask_directory"
    if "预览" in t or "检测" in t or "扫描" in t or "detect" in t or "scan" in t:
        return "detect_only"
    if "规则" in t or "rules" in t or "rule" in t:
        return "get_rules"
    if "自定义" in t or "custom" in t or "新增" in t or "add" in t:
        return "custom_rule"
    if "报告" in t or "report" in t or "导出" in t or "export" in t:
        return "export_report"
    if "状态" in t or "status" in t or "config" in t or "配置" in t:
        return "config"
    return "scan_and_mask"


def execute(command: str, params: Optional[Dict[str, Any]] = None,
            state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    根据命令名称执行对应的操作

    Args:
        command: 操作名称
            - scan_and_mask: 扫描并脱敏单个文件
            - mask_directory: 批量脱敏整文件夹
            - detect_only: 仅检测不脱敏
            - get_rules: 查看脱敏规则
            - custom_rule: 自定义规则管理
            - export_report: 导出脱敏报告
            - status: 查看状态
            - config: 查看/更新配置
        params: 参数字典
        state: 状态字典
    """
    orch = PrivacymaskOrchestrator()

    action_map = {
        "scan_and_mask": orch.scan_and_mask,
        "mask_directory": orch.mask_directory,
        "detect_only": orch.detect_only,
        "get_rules": orch.get_rules,
        "custom_rule": orch.custom_rule,
        "export_report": orch.export_report,
        "status": orch.status,
        "config": orch.config,
    }

    handler = action_map.get(command)
    if not handler:
        return {
            "success": False,
            "error": f"未知操作: {command}",
            "error_code": "unknown_command",
        }

    return handler(params or {}, state or {})


def execute_from_text(text: str, params: Optional[Dict[str, Any]] = None,
                      state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """根据自然语言文本自动路由"""
    command = _route_by_text(text)
    return execute(command, params or {}, state or {})
