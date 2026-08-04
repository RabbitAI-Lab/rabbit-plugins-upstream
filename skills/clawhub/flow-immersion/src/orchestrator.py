# Copyright (c) 2026 Joyxj2devs Team
# Flow Immersion Orchestrator - v5.3.0
# 统一调用 MCP Toolbox dispatch_tool，适配 8 入口 / 多子动作模式

import json
from typing import Dict, Any, Optional


class ToolboxOrchestrator:
    """
    MCP Toolbox 编排器（v5.3.0 适配 flow-immersion-mcp 8 入口模式）

    封装对 dispatch_tool() 的统一调用，自动组装 state 参数。
    8 个入口工具，每个入口支持多个内部子动作。
    """

    # 8 入口 + 描述
    TOOLS = {
        "start_focus": "开始专注（番茄钟+沉浸环境+桌面控制）",
        "control_focus": "控制专注（pause/resume/stop/status/checkin/distraction）",
        "adhd_manage": "ADHD 陪伴管理（微步骤/多巴胺/紧急/复盘）",
        "env_control": "环境控制（壁纸/桌面图标/窗口）",
        "get_stats": "数据统计（今日/每日/完成率/连续天数）",
        "plan_manage": "任务规划（保存/查询/添加/完成/模板）",
        "config_manage": "配置管理（查询/更新/重置/番茄/ADHD/壁纸）",
        "self_repair": "自修复（状态/触发/错误日志）",
    }

    def __init__(self, state_manager=None, toolbox_client=None):
        self.state_manager = state_manager
        self.toolbox = toolbox_client
        self._last_result = None

    def dispatch(self, tool_name: str, action: str = None, **params) -> Dict[str, Any]:
        """
        调用 MCP Toolbox 工具

        Args:
            tool_name: 8 入口之一（start_focus/control_focus/...）
            action: 子动作名（如 pause/resume/status 等）
            **params: 工具参数
        """
        call_params = dict(params)
        if action:
            call_params["action"] = action
        if self.state_manager:
            call_params["state"] = self.state_manager.get_full_state()

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

        # 离线模式：用本地 state_manager 直接执行
        if self.state_manager:
            return self._local_dispatch(tool_name, action, **params)
        return {
            "success": False,
            "error": {"code": "no_backend", "message": "未连接 MCP 服务端"},
            "tool_name": tool_name,
        }

    # ─── 便捷方法 ───

    def start_focus(self, **params) -> Dict:
        return self.dispatch("start_focus", **params)

    def control_focus(self, action: str = "status", **params) -> Dict:
        return self.dispatch("control_focus", action=action, **params)

    def adhd_manage(self, action: str = "status", **params) -> Dict:
        return self.dispatch("adhd_manage", action=action, **params)

    def env_control(self, action: str = "status", **params) -> Dict:
        return self.dispatch("env_control", action=action, **params)

    def get_stats(self, action: str = "all", **params) -> Dict:
        return self.dispatch("get_stats", action=action, **params)

    def plan_manage(self, action: str = "today", **params) -> Dict:
        return self.dispatch("plan_manage", action=action, **params)

    def config_manage(self, action: str = "get", **params) -> Dict:
        return self.dispatch("config_manage", action=action, **params)

    def self_repair(self, action: str = "status", **params) -> Dict:
        return self.dispatch("self_repair", action=action, **params)

    # ─── 本地离线执行（无 MCP 服务端时） ───

    def _local_dispatch(self, tool_name: str, action: str = None, **params) -> Dict:
        sm = self.state_manager

        if tool_name == "start_focus":
            sm.start_timer(
                work_minutes=params.get("work_minutes", 25),
                break_minutes=params.get("break_minutes", 5),
                task=params.get("task", ""),
                long_break_minutes=params.get("long_break_minutes", 15),
                rounds=params.get("rounds", 4),
            )
            if params.get("hide_icons"):
                pass  # 桌面图标需 MCP 后端
            if params.get("wallpaper"):
                return sm.set_wallpaper_by_preset(params["wallpaper"])
            return {"success": True, "mode": params.get("mode", "full"), "offline": True}

        elif tool_name == "control_focus":
            if action == "pause":
                sm.pause_timer()
                return {"success": True}
            elif action == "resume":
                sm.resume_timer()
                return {"success": True}
            elif action == "stop":
                sm.stop_timer(completed=params.get("completed", True))
                return {"success": True}
            elif action == "status":
                return sm.get_pomodoro_status()
            elif action == "checkin":
                return sm.pomodoro_checkin(params.get("task"))
            elif action == "distraction":
                return sm.record_distraction(
                    params.get("distraction_type", "other"),
                    params.get("description"),
                    params.get("duration_minutes", 0),
                )

        elif tool_name == "adhd_manage":
            if action == "status":
                return sm.adhd_get_status()
            elif action == "start":
                return sm.adhd_start_session(params.get("task", ""))
            elif action == "add_step":
                return sm.adhd_add_micro_step(params.get("step", ""))
            elif action == "complete_step":
                return sm.adhd_complete_micro_step(params.get("index"))
            elif action == "dopamine_menu":
                return sm.adhd_get_dopamine_menu()
            elif action == "dopamine_reset":
                return sm.adhd_dopamine_reset(params.get("option_id", ""))
            elif action == "emergency_reset":
                return sm.adhd_emergency_reset()
            elif action == "tips":
                return sm.adhd_get_tips()
            elif action == "end":
                return sm.adhd_end_session()
            elif action == "reset":
                return sm.adhd_reset()
            elif action == "checkin":
                return sm.adhd_trigger_checkin()
            elif action == "autopsy":
                return sm.adhd_start_autopsy()
            elif action == "submit_autopsy":
                return sm.adhd_submit_autopsy(params.get("answers"))

        elif tool_name == "env_control":
            if action == "wallpaper_presets":
                return sm.get_wallpaper_presets()
            elif action == "wallpaper_status":
                return sm.get_wallpaper_status()
            elif action == "hide_icons" or action == "show_icons":
                return {"success": False, "error": "需要 MCP 后端"}

        elif tool_name == "get_stats":
            if action == "all":
                return sm.get_stats()
            elif action == "daily":
                return sm.get_daily_stats(params.get("date"))
            elif action == "completion_rate":
                return sm.get_completion_rate(params.get("period", "daily"))
            elif action == "streak":
                return sm.get_streak()

        elif tool_name == "plan_manage":
            if action == "save":
                return sm.plan_save(params.get("items", []))
            elif action == "today":
                return sm.plan_get_today()
            elif action == "add_item":
                return sm.plan_add_item(
                    params.get("title", ""),
                    params.get("estimated_minutes", 30),
                    params.get("priority", "medium"),
                )
            elif action == "complete_item":
                return sm.plan_complete_item(params.get("item_id", ""))
            elif action == "templates":
                return sm.plan_get_templates()
            elif action == "clear":
                return sm.plan_clear()

        elif tool_name == "config_manage":
            if action == "get":
                return {"success": True, "config": sm.get_config()}
            elif action == "update":
                return sm.update_config(params.get("path", ""), params.get("value"))
            elif action == "reset":
                return sm.reset_config()
            elif action == "wallpaper_presets":
                return sm.get_wallpaper_presets()

        elif tool_name == "self_repair":
            return {"success": True, "status": "ok", "note": "离线模式无法完整自修复"}

        return {"error": f"未知工具或动作: {tool_name}/{action}", "code": 404}
