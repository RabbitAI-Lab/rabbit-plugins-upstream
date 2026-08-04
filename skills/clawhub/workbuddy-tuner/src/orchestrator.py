# Copyright (c) 2026 Joyxj2devs Team
"""
Tuner Skill - MCP Toolbox 编排器

封装对 MCP Toolbox 的统一调用，自动注入状态。
支持纯函数分析（tuner.*）和脚本适配器（tuner_original.*）。
"""
from typing import Dict, Any, Optional, List
from state_manager import TunerStateManager


class TunerOrchestrator:
    """
    WorkBuddy 调优编排器
    
    核心方法:
    - diagnose(...):  调用 tuner.diagnose.* 纯函数
    - optimize(...):  调用 tuner.optimize.* 纯函数
    - monitor(...):   调用 tuner.monitor.* 纯函数 / tuner_original.monitor 脚本适配器
    - session_audit(...): 调用 tuner.session_audit.* 纯函数
    - learn(...):  调用 tuner.learn_sync.* 纯函数
    - kb(...):  调用 tuner.kb_sync.* 纯函数
    - trend(...):  调用 tuner.trend.* 纯函数
    - selfcheck(...): 调用 tuner.selfcheck.* 纯函数
    - recover(...): 调用 tuner.recover.* 纯函数
    - run_script(...): 调用 tuner_original.* 脚本适配器
    - get_subtools():  获取当前 Skill 所有子工具
    """

    def __init__(self, state_manager: TunerStateManager, dispatch_tool=None):
        self.sm = state_manager
        self.dispatch_tool = dispatch_tool  # MCP dispatch_tool callable

    def diagnose(self, action: str, **params) -> Dict[str, Any]:
        """调用诊断分析（纯函数）"""
        tool_name = f"tuner.diagnose.{action}"
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def optimize_plan(self, action: str, **params) -> Dict[str, Any]:
        """调用优化计划（纯函数）"""
        tool_name = f"tuner.optimize.plan_{action}"
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def monitor(self, action: str, **params) -> Dict[str, Any]:
        """
        调用实时监控（纯函数）
        
        可用 action:
        - check_context:   会话上下文膨胀检查
        - check_memory:    内存占用实时监控
        - check_cpu:       CPU占用实时监控
        - check_disk:      磁盘空间与IO监控
        - check_network:   网络延迟监控
        - quick_fix:       一键快速优化综合方案
        - setup_alerts:    设置监控阈值与告警规则
        - status_report:   生成实时状态报告
        - auto_scan:       自动扫描+评估报告（定时扫描入口）
        - schedule_config: 配置定时扫描参数
        - report_history:  查看历史报告摘要
        """
        tool_name = f"tuner.monitor.{action}"
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def session_audit(self, action: str, **params) -> Dict[str, Any]:
        """调用会话审计（纯函数）"""
        tool_name = f"tuner.session_audit.{action}"
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def learn(self, action: str, **params) -> Dict[str, Any]:
        """调用学习同步（纯函数）"""
        tool_name = f"tuner.learn_sync.{action}"
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def kb(self, action: str, **params) -> Dict[str, Any]:
        """调用知识库工具（纯函数）"""
        tool_name = f"tuner.kb_sync.{action}"
        return self._call(tool_name, params)

    def trend(self, action: str, **params) -> Dict[str, Any]:
        """调用趋势分析（纯函数）"""
        tool_name = f"tuner.trend.{action}"
        return self._call(tool_name, params)

    def selfcheck(self, action: str = "run", **params) -> Dict[str, Any]:
        """
        调用自巡检（纯函数）
        
        可用 action:
        - run: 执行巡检（默认）
        - history: 列出巡检历史
        - baseline: 查看基线
        - escalation: 检测升级信号
        - plan: 生成下次巡检计划
        """
        tool_name = f"tuner.selfcheck.{action}"
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def recover(self, action: str = "analyze", **params) -> Dict[str, Any]:
        """
        调用重装恢复（纯函数）
        
        可用 action:
        - analyze: 生成前置分析报告
        - checklist: 用户数据连续性保障清单
        - migration_plan: 迁移方案建议（full/selective/analyze）
        - backup_plan: 备份计划
        - report_compare: 重装前后性能变化报告
        - download_guide: 官方下载指引
        """
        tool_name = f"tuner.recover.{action}"
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def run(self, tool_name: str, **params) -> Dict[str, Any]:
        """
        运行脚本适配器（tuner_original.*）
        
        用法:
        - orch.run("tuner_original.diagnose")  # 卡顿扫描
        - orch.run("tuner_original.monitor")   # 实时系统监控
        - orch.run("tuner_original.optimize", subcommand="cache")  # 缓存清理
        - orch.run("tuner_original.recover", subcommand="analyze")  # 重装分析
        """
        state = self.sm.get_full_state()
        return self._call(tool_name, {**params, "state": state})

    def get_subtools(self) -> Dict[str, Any]:
        """获取当前 Skill 所有子工具"""
        return self._call("tuner_original.list_subtools", {})

    def _call(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """统一调用 dispatch_tool"""
        if not self.dispatch_tool:
            return {"error": "dispatch_tool not configured", "tool_name": tool_name}
        try:
            return self.dispatch_tool(tool_name=tool_name, **params)
        except Exception as e:
            return {"success": False, "error": str(e), "tool_name": tool_name}
