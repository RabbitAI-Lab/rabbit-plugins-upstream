# Flow Immersion Orchestrator - MCP Toolbox 编排器
# 封装对 MCP Toolbox 的统一调用

import json
from typing import Dict, Any, Optional


class ToolboxOrchestrator:
    """
    MCP Toolbox 编排器

    封装对 dispatch_tool() 的调用，自动组装 state 参数。
    客户端通过本类与 MCP Toolbox 服务交互。
    """

    def __init__(self, state_manager=None, toolbox_client=None):
        """
        Args:
            state_manager: StateManager 实例
            toolbox_client: MCP Toolbox 客户端（MCPClient 或类似）
        """
        self.state_manager = state_manager
        self.toolbox = toolbox_client
        self._last_result = None

    def dispatch(self, tool_name: str, **params) -> Dict[str, Any]:
        """
        调用 MCP Toolbox 工具

        自动将客户端状态附加到 state 参数。

        Args:
            tool_name: 工具名，如 "flow.pomodoro.start"
            **params: 工具参数

        Returns:
            dispatch_tool 返回的结果 dict
        """
        # 组装 state 参数
        call_params = dict(params)
        if self.state_manager:
            call_params["state"] = self.state_manager.get_full_state()

        # 通过 M CP 客户端调用
        if self.toolbox:
            try:
                result = self.toolbox.call_tool("dispatch_tool", {
                    "tool_name": tool_name,
                    **call_params,
                })
                self._last_result = result
                return result
            except Exception as e:
                return {
                    "success": False,
                    "error": {"code": "client_error", "message": str(e)},
                    "tool_name": tool_name,
                }
        else:
            # 离线模式：返回模拟结果（用于测试）
            return {
                "success": True,
                "data": {"message": f"[offline] {tool_name} would be called with {call_params}"},
                "tool_name": tool_name,
            }

    def pomodoro(self, action: str, **params) -> Dict:
        """便捷方法：调用番茄钟工具"""
        return self.dispatch(f"flow.pomodoro.{action}", **params)

    def adhd(self, action: str, **params) -> Dict:
        """便捷方法：调用 ADHD 工具"""
        return self.dispatch(f"flow.adhd.{action}", **params)

    def stats(self, action: str, **params) -> Dict:
        """便捷方法：调用统计工具"""
        return self.dispatch(f"flow.stats.{action}", **params)

    def config(self, action: str, **params) -> Dict:
        """便捷方法：调用配置工具"""
        return self.dispatch(f"flow.config.{action}", **params)

    def repair(self, action: str, **params) -> Dict:
        """便捷方法：调用修复工具"""
        return self.dispatch(f"flow.repair.{action}", **params)

    def immersion(self, action: str, **params) -> Dict:
        """便捷方法：调用沉浸工具"""
        return self.dispatch(f"flow.immersion.{action}", **params)

    def planning(self, action: str, **params) -> Dict:
        """便捷方法：调用规划工具"""
        return self.dispatch(f"flow.planning.{action}", **params)
