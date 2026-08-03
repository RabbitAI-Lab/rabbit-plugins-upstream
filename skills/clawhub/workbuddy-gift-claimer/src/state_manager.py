# Copyright (c) 2026 Joyxj2devs Team
"""
Gift Claimer State Manager - 客户端状态管理
管理领取历史、场景配置、学习数据、任务状态。
"""
import json
import os
from datetime import datetime, date
from pathlib import Path
from typing import Any, Dict, List, Optional


class GiftStateManager:
    """Gift Claimer 客户端状态管理器"""

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.state_file = self.data_dir / "gift_state.json"
        self._state = self._load()

    def _load(self) -> Dict[str, Any]:
        if self.state_file.exists():
            with open(self.state_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "scenes": [],
            "history": [],
            "learn_data": {},
            "task": {"installed": False, "schedule_time": "00:05"},
            "created": datetime.now().isoformat(),
        }

    def _save(self):
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self._state, f, ensure_ascii=False, indent=2)

    def add_scene(self, name: str, scene_type: str = "workbuddy",
                  priority: int = 0, app_name: str = "",
                  trigger: str = "manual") -> Dict[str, Any]:
        scene = {
            "name": name,
            "type": scene_type,
            "priority": priority,
            "app_name": app_name,
            "trigger": trigger,
            "ocr_keywords": [],
            "actions": [],
        }
        # Remove existing with same name
        self._state["scenes"] = [
            s for s in self._state["scenes"] if s.get("name") != name
        ]
        self._state["scenes"].append(scene)
        self._save()
        return scene

    def get_scenes(self) -> List[Dict[str, Any]]:
        return self._state["scenes"]

    def add_history(self, scene: str, success: bool, reward: str = "",
                    failure_reason: str = "", coords: List = None) -> None:
        entry = {
            "date": date.today().isoformat(),
            "time": datetime.now().strftime("%H:%M:%S"),
            "scene": scene,
            "success": success,
            "reward": reward,
            "failure_reason": failure_reason,
            "coords": coords or [],
        }
        self._state["history"].append(entry)
        # Keep last 1000 entries
        if len(self._state["history"]) > 1000:
            self._state["history"] = self._state["history"][-1000:]
        self._save()

    def get_history(self, days: int = 7) -> List[Dict[str, Any]]:
        from datetime import timedelta
        cutoff = (date.today() - timedelta(days=days)).isoformat()
        return [h for h in self._state["history"] if h.get("date", "") >= cutoff]

    def get_today_history(self) -> List[Dict[str, Any]]:
        today = date.today().isoformat()
        return [h for h in self._state["history"] if h.get("date") == today]

    def get_task_status(self) -> Dict[str, Any]:
        return self._state["task"]

    def set_task_installed(self, installed: bool, schedule_time: str = "00:05"):
        self._state["task"]["installed"] = installed
        self._state["task"]["schedule_time"] = schedule_time
        self._save()

    def update_learn_data(self, key: str, value: Any) -> None:
        self._state["learn_data"][key] = value
        self._save()

    def get_learn_data(self) -> Dict[str, Any]:
        return self._state["learn_data"]

    def get_full_state(self) -> Dict[str, Any]:
        return dict(self._state)

    def export_json(self) -> str:
        return json.dumps(self._state, ensure_ascii=False, indent=2)

    def cleanup(self):
        from datetime import timedelta
        cutoff = (date.today() - timedelta(days=30)).isoformat()
        self._state["history"] = [
            h for h in self._state["history"] if h.get("date", "") >= cutoff
        ]
        self._save()
