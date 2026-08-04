# Copyright (c) 2026 Joyxj2devs Team
"""
Gift Claimer Orchestrator - 便捷调用层
包装 dispatch_tool 为易用的方法，自动注入状态。
"""
from typing import Any, Dict, List, Optional


class GiftOrchestrator:
    """Gift Claimer 便捷调用器"""

    def __init__(self, state_manager, dispatch_tool):
        self.state = state_manager
        self.dispatch = dispatch_tool

    def claim_plan(self) -> Dict[str, Any]:
        """规划今日领取计划"""
        scenes = self.state.get_scenes()
        history = self.state.get_history(7)
        return self._call("gift.claim.plan_claim", {"scenes": scenes, "history": history})

    def check_yesterday(self) -> Dict[str, Any]:
        """检查昨日是否遗漏"""
        history = self.state.get_history(2)
        return self._call("gift.claim.check_yesterday", {"history": history})

    def verify_today(self) -> Dict[str, Any]:
        """验证今日领取状态"""
        scenes = self.state.get_scenes()
        history = self.state.get_history(1)
        return self._call("gift.claim.verify_today", {"scenes": scenes, "history": history})

    def analyze_scene(self, scene: Dict[str, Any]) -> Dict[str, Any]:
        """分析场景配置"""
        return self._call("gift.scene.analyze_scene", {"scene": scene})

    def extract_keywords(self, ocr_results: List[Dict]) -> Dict[str, Any]:
        """从 OCR 结果提取关键词"""
        learn_data = self.state.get_learn_data()
        return self._call("gift.learn.extract_ocr_keywords", {"ocr_results": ocr_results, "learn_data": learn_data})

    def extract_patterns(self, scene: Dict) -> Dict[str, Any]:
        """提取成功模式"""
        history = self.state.get_history(30)
        return self._call("gift.scene.extract_patterns", {"history": history, "scene": scene})

    def task_status(self) -> Dict[str, Any]:
        """获取任务计划状态"""
        task = self.state.get_task_status()
        return self._call("gift.task.task_status", {
            "installed": task.get("installed", False),
            "schedule_time": task.get("schedule_time", "00:05"),
        })

    def plan_task(self) -> Dict[str, Any]:
        """生成定时任务计划"""
        scenes = self.state.get_scenes()
        task = self.state.get_task_status()
        return self._call("gift.task.plan_task_schedule", {
            "scenes": scenes, "installed": task.get("installed", False),
        })

    def manage_learn_data(self) -> Dict[str, Any]:
        """管理学习数据"""
        learn_data = self.state.get_learn_data()
        history = self.state.get_history(30)
        return self._call("gift.learn.manage_learn_data", {"learn_data": learn_data, "history": history})

    def feedback(self, strategy: str, helpful: bool) -> Dict[str, Any]:
        """记录反馈"""
        learn_data = self.state.get_learn_data()
        weights = learn_data.get("weights", {})
        return self._call("gift.learn.feedback", {"strategy": strategy, "helpful": helpful, "weights": weights})

    def run_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """运行任意 gift 域工具"""
        return self._call(tool_name, kwargs)

    def get_subtools(self) -> List[Dict[str, Any]]:
        """列出所有子工具"""
        return self._call("gift_original.list_subtools", {})

    def _call(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """统一调用 dispatch_tool，对 None 做安全校验"""
        if self.dispatch is None:
            return {
                "error": "dispatch_tool not configured",
                "tool_name": tool_name,
            }
        try:
            return self.dispatch(tool_name=tool_name, **params)
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "tool_name": tool_name,
            }
