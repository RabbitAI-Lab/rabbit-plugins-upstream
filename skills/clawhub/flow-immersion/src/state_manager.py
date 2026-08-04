# Copyright (c) 2026 Joyxj2devs Team
# Flow Immersion - 状态管理与运行时 (v5.3.0)
# 完整适配 flow-immersion-mcp 数据模型：番茄钟/ADHD/配置/会话/壁纸/规划/统计

import json
import time
import threading
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional, Callable, List


DEFAULT_CONFIG = {
    "version": "1.0.0",
    "user_profile": {"name": "用户", "chronotype": "bear"},
    "timer": {
        "work_minutes": 25,
        "break_minutes": 5,
        "long_break_minutes": 15,
        "rounds": 4,
    },
    "adhd": {
        "companion_enabled": True,
        "companion_type": "ambient",
        "checkin_interval_minutes": 20,
        "micro_task_enabled": True,
    },
    "immersion": {
        "hide_desktop_icons": True,
        "wallpaper_type": "static",
        "wallpaper_source": "bundled",
        "wallpaper_path": "",
        "bundled_wallpaper": "ocean",
        "search_enabled": False,
        "music_enabled": True,
        "music_volume": 0.5,
        "music_source": "bundled",
        "music_path": "",
        "bundled_music": "ambient",
    },
    "storage": {"path": "", "auto_backup": True},
}

WALLPAPER_PRESETS = {
    "ocean": {"color": "#001F3F", "name": "海洋", "scene": "专注/编码/夜间"},
    "forest": {"color": "#006400", "name": "森林", "scene": "写作/思考"},
    "sunset": {"color": "#FF4500", "name": "夕阳", "scene": "创意/设计"},
    "night": {"color": "#2F2F2F", "name": "夜间", "scene": "高强度专注"},
    "minimal": {"color": "#D3D3D3", "name": "极简", "scene": "长时间工作"},
    "zen": {"color": "#F5F5DC", "name": "禅意", "scene": "阅读/冥想"},
    "neon": {"color": "#800080", "name": "霓虹", "scene": "游戏/休闲"},
    "natural": {"color": "#8B4513", "name": "自然", "scene": "通用"},
}


@dataclass
class PomodoroState:
    """番茄钟运行时状态（客户端持有）"""
    phase: str = "idle"
    task: str = ""
    start_time: float = 0
    elapsed_seconds: int = 0
    total_seconds: int = 1500
    current_round: int = 0
    total_rounds: int = 4
    work_minutes: int = 25
    break_minutes: int = 5
    long_break_minutes: int = 15
    config: Dict = field(default_factory=dict)
    completed_rounds: int = 0
    aborted: bool = False
    session_id: str = ""

    def to_dict(self):
        d = asdict(self)
        d["remaining_seconds"] = max(0, self.total_seconds - self.elapsed_seconds)
        return d

    @property
    def progress_pct(self) -> float:
        if self.total_seconds <= 0:
            return 0.0
        return round(min(100, self.elapsed_seconds / self.total_seconds * 100), 1)


class StateManager:
    """
    客户端状态管理器 — 完整适配 flow-immersion-mcp v5.3 数据模型

    - 番茄钟：phase/elapsed/round/progress 等运行时状态
    - ADHD：会话管理、微步骤、多巴胺菜单、紧急协议、复盘
    - 配置：与 default_config.json 一致的嵌套结构
    - 会话持久化：每日 sessions.json + 历史合并
    - 任务规划：今日计划管理
    - 壁纸：8 预设 + 状态
    - 统计：今日/每日/完成率/连续天数
    """

    def __init__(self, data_dir: str = None):
        self._data_dir = Path(data_dir) if data_dir else Path(__file__).parent.parent / "data"
        self._data_dir.mkdir(parents=True, exist_ok=True)

        self._lock = threading.Lock()
        self._timer = PomodoroState()
        self._adhd_session: Optional[Dict] = None
        # 先加载配置（避免模块缓存干扰）
        self._config = self._load_default_config()
        self._today_sessions: List[Dict] = []
        self._today_plan: List[Dict] = []
        self._today_distractions: List[Dict] = []

        self._timer_thread: Optional[threading.Thread] = None
        self._timer_callback: Optional[Callable] = None
        self._on_tick: Optional[Callable] = None
        self._stop_event = threading.Event()

    # ─── 配置 ───

    def _deep_copy(self, obj):
        return json.loads(json.dumps(obj))

    def _load_default_config(self) -> Dict:
        config_file = self._data_dir / "config.json"
        if config_file.exists():
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    merged = self._deep_copy(DEFAULT_CONFIG)
                    for k, v in loaded.items():
                        if isinstance(v, dict) and k in merged:
                            merged[k].update(v)
                        else:
                            merged[k] = v
                    return merged
            except Exception:
                pass
        return self._deep_copy(DEFAULT_CONFIG)

    def get_config(self) -> Dict:
        with self._lock:
            return dict(self._config)

    def update_config(self, path: str, value) -> Dict:
        keys = path.split(".")
        with self._lock:
            d = self._config
            for k in keys[:-1]:
                if k not in d or not isinstance(d[k], dict):
                    d[k] = {}
                d = d[k]
            d[keys[-1]] = value
            self._save_config()
            return self._config

    def reset_config(self) -> Dict:
        with self._lock:
            self._config = self._deep_copy(DEFAULT_CONFIG)
            self._save_config()
            return self._config

    def _save_config(self):
        try:
            config_file = self._data_dir / "config.json"
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(self._config, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    # ─── 番茄钟状态 ───

    def get_timer_state(self) -> Dict:
        with self._lock:
            return self._timer.to_dict()

    def get_full_state(self) -> Dict:
        with self._lock:
            return {
                "timer": self._timer.to_dict(),
                "adhd_session": dict(self._adhd_session) if self._adhd_session else None,
                "config": self._config,
                "today_sessions": self._today_sessions,
                "today_plan": self._today_plan,
                "today_distractions": self._today_distractions,
                "platform": "windows",
            }

    def start_timer(
        self,
        work_minutes: int = 25,
        break_minutes: int = 5,
        task: str = "",
        callback: Callable = None,
        long_break_minutes: int = 15,
        rounds: int = 4,
    ):
        with self._lock:
            t = self._timer
            t.phase = "work"
            t.task = task or "专注任务"
            t.start_time = time.time()
            t.elapsed_seconds = 0
            t.total_seconds = work_minutes * 60
            t.work_minutes = work_minutes
            t.break_minutes = break_minutes
            t.long_break_minutes = long_break_minutes
            t.current_round = 0
            t.total_rounds = rounds
            t.completed_rounds = 0
            t.aborted = False
            t.session_id = datetime.now().strftime("%Y%m%d%H%M%S")
            t.config = {
                "work_minutes": work_minutes,
                "break_minutes": break_minutes,
                "long_break_minutes": long_break_minutes,
                "rounds": rounds,
            }

        self._timer_callback = callback
        self._stop_event.clear()
        self._timer_thread = threading.Thread(target=self._timer_loop, daemon=True)
        self._timer_thread.start()

    def pause_timer(self):
        with self._lock:
            self._timer.phase = "paused"
        self._stop_event.set()

    def resume_timer(self):
        with self._lock:
            self._timer.phase = "work"
            self._timer.start_time = time.time()
        self._stop_event.clear()
        if not self._timer_thread or not self._timer_thread.is_alive():
            self._timer_thread = threading.Thread(target=self._timer_loop, daemon=True)
            self._timer_thread.start()

    def stop_timer(self, completed: bool = False):
        self._stop_event.set()
        with self._lock:
            t = self._timer
            t.phase = "idle"
            t.aborted = not completed
            if completed:
                t.completed_rounds += 1
                self._record_session(t)

    def get_pomodoro_status(self) -> Dict:
        """返回番茄钟完整状态"""
        with self._lock:
            t = self._timer
            status = t.to_dict()
            status["phase"] = t.phase
            status["is_running"] = t.phase in ("work", "break", "long_break")
            status["is_paused"] = t.phase == "paused"
            status["is_idle"] = t.phase == "idle"
            return status

    def _timer_loop(self):
        tick_interval = 1
        while not self._stop_event.is_set():
            with self._lock:
                if self._timer.phase == "paused":
                    break
            time.sleep(tick_interval)
            with self._lock:
                t = self._timer
                t.elapsed_seconds += tick_interval
                if self._on_tick:
                    try:
                        self._on_tick(t.to_dict())
                    except Exception:
                        pass
                if t.elapsed_seconds >= t.total_seconds and t.phase in ("work", "break", "long_break"):
                    self._phase_complete(t)
                    return

    def _phase_complete(self, t):
        if t.phase == "work":
            t.completed_rounds += 1
            self._record_session(t)
            if t.completed_rounds >= t.total_rounds:
                t.phase = "idle"
                return
            if t.completed_rounds % t.total_rounds == 0:
                t.phase = "long_break"
                t.total_seconds = t.config.get("long_break_minutes", 15) * 60
            else:
                t.phase = "break"
                t.total_seconds = t.config.get("break_minutes", 5) * 60
            t.elapsed_seconds = 0
            t.start_time = time.time()
        elif t.phase in ("break", "long_break"):
            t.phase = "work"
            t.elapsed_seconds = 0
            t.start_time = time.time()
            t.total_seconds = t.config.get("work_minutes", 25) * 60

    def _record_session(self, t):
        session = {
            "task": t.task,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "work_minutes": t.config.get("work_minutes", 25),
            "actual_minutes": t.elapsed_seconds // 60,
            "completed": not t.aborted,
            "session_id": t.session_id,
            "timestamp": datetime.now().isoformat(),
        }
        self._today_sessions.append(session)
        self._save_sessions()

    def set_on_tick(self, callback: Callable):
        self._on_tick = callback

    def pomodoro_checkin(self, task: str = None) -> Dict:
        with self._lock:
            t = self._timer
            t.task = task or t.task
            return {"success": True, "task": t.task, "phase": t.phase}

    def record_distraction(
        self, distraction_type: str = "other", description: str = None, duration_minutes: int = 0
    ) -> Dict:
        with self._lock:
            entry = {
                "type": distraction_type,
                "description": description,
                "duration_minutes": duration_minutes,
                "timestamp": datetime.now().isoformat(),
            }
            self._today_distractions.append(entry)
            return {"success": True, "count": len(self._today_distractions)}

    # ─── ADHD ───

    def adhd_start_session(self, task: str = "") -> Dict:
        with self._lock:
            self._adhd_session = {
                "task": task,
                "created_at": datetime.now().isoformat(),
                "micro_steps": [],
                "completed_steps": [],
                "check_in_count": 0,
                "dopamine_count": 0,
                "distractions": [],
                "status": "active",
            }
            return {"success": True, "session": dict(self._adhd_session)}

    def adhd_add_micro_step(self, step: str = "") -> Dict:
        with self._lock:
            if not self._adhd_session:
                return {"error": "未启动 ADHD 会话", "code": 400}
            idx = len(self._adhd_session["micro_steps"]) + 1
            self._adhd_session["micro_steps"].append({
                "description": step,
                "completed": False,
                "order": idx,
                "added_at": datetime.now().isoformat(),
            })
            return {"success": True, "step_count": len(self._adhd_session["micro_steps"])}

    def adhd_complete_micro_step(self, index: int = None) -> Dict:
        with self._lock:
            s = self._adhd_session
            if not s or not s["micro_steps"]:
                return {"error": "无微步骤", "code": 400}
            if index is None:
                for i, st in enumerate(s["micro_steps"]):
                    if not st["completed"]:
                        s["micro_steps"][i]["completed"] = True
                        s["completed_steps"].append(i)
                        return {"success": True, "completed_index": i}
            elif 0 <= index < len(s["micro_steps"]):
                s["micro_steps"][index]["completed"] = True
                s["completed_steps"].append(index)
                return {"success": True, "completed_index": index}
            return {"error": "步骤索引无效", "code": 400}

    def adhd_get_dopamine_menu(self) -> Dict:
        return {
            "success": True,
            "menu": [
                {"id": "break", "label": "休息 5 分钟", "description": "离开屏幕，走动一下"},
                {"id": "water", "label": "喝水", "description": "补充水分，提神醒脑"},
                {"id": "music", "label": "听音乐", "description": "听一首喜欢的歌"},
                {"id": "snack", "label": "吃零食", "description": "补充能量"},
                {"id": "stretch", "label": "伸展运动", "description": "活动一下筋骨"},
            ],
        }

    def adhd_dopamine_reset(self, option_id: str = "") -> Dict:
        with self._lock:
            if self._adhd_session:
                self._adhd_session["dopamine_count"] += 1
            return {"success": True, "option_id": option_id}

    def adhd_get_emergency_reset_protocol(self) -> Dict:
        return {
            "success": True,
            "protocol": [
                "1. 停下来，深呼吸 3 次（4秒吸 - 4秒屏 - 6秒呼）",
                "2. 写下此刻的想法（不用修饰，写下来就好）",
                "3. 起身走动 2 分钟，远离屏幕",
                "4. 喝一杯水",
                "5. 回到座位，从最小可执行步骤重新开始",
            ],
        }

    def adhd_emergency_reset(self) -> Dict:
        with self._lock:
            if self._adhd_session:
                self._adhd_session["distractions"].append({
                    "type": "emergency_reset",
                    "timestamp": datetime.now().isoformat(),
                })
        return self.adhd_get_emergency_reset_protocol()

    def adhd_get_tips(self) -> Dict:
        return {
            "success": True,
            "tips": [
                "把大任务拆成 5 分钟可完成的小步骤",
                "每完成一个微步骤就给自己一个即时奖励",
                "用番茄钟保持节奏，不要一口气做到累",
                "分心是正常的，记下来就好，不要自责",
            ],
        }

    def adhd_get_status(self) -> Dict:
        with self._lock:
            if not self._adhd_session:
                return {"status": "inactive", "has_session": False}
            s = dict(self._adhd_session)
            s["has_session"] = True
            return s

    def adhd_end_session(self) -> Dict:
        with self._lock:
            if self._adhd_session:
                self._adhd_session["status"] = "ended"
                return {"success": True, "session": dict(self._adhd_session)}
            return {"error": "无活跃会话", "code": 400}

    def adhd_reset(self) -> Dict:
        with self._lock:
            self._adhd_session = None
            return {"success": True}

    def adhd_trigger_checkin(self) -> Dict:
        with self._lock:
            if self._adhd_session:
                self._adhd_session["check_in_count"] += 1
                return {"success": True, "check_in_count": self._adhd_session["check_in_count"]}
            return {"error": "无活跃会话", "code": 400}

    def adhd_start_autopsy(self) -> Dict:
        return {
            "success": True,
            "questions": [
                "今天专注了几个番茄钟？",
                "中途分心了几次？主要分心来源是什么？",
                "哪个时段专注效率最高？",
                "明天想改进哪一点？",
            ],
        }

    def adhd_submit_autopsy(self, answers: List[str] = None) -> Dict:
        return {"success": True, "message": "复盘已记录"}

    # ─── 任务规划 ───

    def plan_save(self, items: List[Dict]) -> Dict:
        with self._lock:
            self._today_plan = [
                {"id": i.get("id", f"plan_{len(self._today_plan)+1}"),
                 "title": i.get("title", ""),
                 "estimated_minutes": i.get("estimated_minutes", 30),
                 "priority": i.get("priority", "medium"),
                 "completed": i.get("completed", False)}
                for i in items
            ]
            return {"success": True, "count": len(self._today_plan)}

    def plan_get_today(self) -> Dict:
        with self._lock:
            return {"success": True, "plan": list(self._today_plan)}

    def plan_add_item(self, title: str, estimated_minutes: int = 30, priority: str = "medium") -> Dict:
        with self._lock:
            item = {
                "id": f"plan_{len(self._today_plan)+1}",
                "title": title,
                "estimated_minutes": estimated_minutes,
                "priority": priority,
                "completed": False,
                "added_at": datetime.now().isoformat(),
            }
            self._today_plan.append(item)
            return {"success": True, "item": item}

    def plan_complete_item(self, item_id: str) -> Dict:
        with self._lock:
            for item in self._today_plan:
                if item["id"] == item_id:
                    item["completed"] = True
                    return {"success": True, "item": item}
            return {"error": "未找到计划项", "code": 404}

    def plan_get_templates(self) -> Dict:
        return {
            "success": True,
            "templates": [
                {"name": "深度工作", "description": "4小时马拉松，5个番茄钟", "rounds": 5, "work_minutes": 50},
                {"name": "能量一小时", "description": "1小时，3个番茄钟", "rounds": 3, "work_minutes": 20},
                {"name": "短任务", "description": "25分钟专注 / 5分钟休息", "rounds": 1, "work_minutes": 25},
                {"name": "轻度专注", "description": "30分钟，2个番茄钟", "rounds": 2, "work_minutes": 15},
            ],
        }

    def plan_clear(self) -> Dict:
        with self._lock:
            self._today_plan = []
            return {"success": True}

    # ─── 壁纸 ───

    def get_wallpaper_presets(self) -> Dict:
        return {"success": True, "presets": WALLPAPER_PRESETS}

    def get_wallpaper_status(self) -> Dict:
        with self._lock:
            imp = self._config.get("immersion", {})
            return {
                "success": True,
                "bundled_wallpaper": imp.get("bundled_wallpaper", "ocean"),
                "wallpaper_source": imp.get("wallpaper_source", "bundled"),
            }

    def set_wallpaper_by_preset(self, preset: str) -> Dict:
        if preset not in WALLPAPER_PRESETS:
            return {"error": f"未知壁纸预设: {preset}", "code": 400}
        with self._lock:
            self._config.setdefault("immersion", {})["bundled_wallpaper"] = preset
            self._save_config()
        return {"success": True, "preset": preset, "info": WALLPAPER_PRESETS[preset]}

    # ─── 统计 ───

    def get_stats(self) -> Dict:
        with self._lock:
            today = len(self._today_sessions)
            completed = sum(1 for s in self._today_sessions if s.get("completed"))
            total_min = sum(s.get("actual_minutes", 0) for s in self._today_sessions)
            return {
                "success": True,
                "today_sessions": today,
                "today_completed": completed,
                "today_minutes": total_min,
                "completion_rate": round(completed / today * 100, 1) if today else 0,
                "streak_days": self._calc_streak(),
            }

    def get_daily_stats(self, date: str = None) -> Dict:
        date = date or datetime.now().strftime("%Y-%m-%d")
        all_sessions = self._load_all_sessions()
        day_sessions = [s for s in all_sessions if s.get("date") == date]
        completed = sum(1 for s in day_sessions if s.get("completed"))
        total_min = sum(s.get("actual_minutes", 0) for s in day_sessions)
        return {
            "success": True,
            "date": date,
            "sessions": len(day_sessions),
            "completed": completed,
            "minutes": total_min,
        }

    def get_completion_rate(self, period: str = "daily") -> Dict:
        with self._lock:
            all_sessions = self._load_all_sessions() + self._today_sessions
        if period == "daily":
            day = datetime.now().strftime("%Y-%m-%d")
            sessions = [s for s in all_sessions if s.get("date") == day]
        elif period == "weekly":
            cutoff = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            sessions = [s for s in all_sessions if s.get("date", "") >= cutoff]
        else:
            sessions = all_sessions
        total = len(sessions)
        completed = sum(1 for s in sessions if s.get("completed"))
        return {"success": True, "period": period, "completion_rate": round(completed / total * 100, 1) if total else 0}

    def get_streak(self) -> Dict:
        return {"success": True, "streak_days": self._calc_streak()}

    def _calc_streak(self) -> int:
        all_sessions = self._load_all_sessions() + self._today_sessions
        dates = sorted(set(s.get("date") for s in all_sessions if s.get("completed")))
        if not dates:
            return 0
        today = datetime.now().strftime("%Y-%m-%d")
        streak = 0
        for i in range(len(dates)):
            expected = (datetime.now() - timedelta(days=len(dates) - 1 - i)).strftime("%Y-%m-%d")
            if expected in dates:
                streak += 1
            else:
                break
        return streak

    # ─── 持久化 ───

    def save_sessions(self):
        all_sessions = self._load_all_sessions() + self._today_sessions
        try:
            sessions_file = self._data_dir / "sessions.json"
            with open(sessions_file, "w", encoding="utf-8") as f:
                json.dump(all_sessions, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def _save_sessions(self):
        self.save_sessions()

    def _load_all_sessions(self) -> List[Dict]:
        sessions_file = self._data_dir / "sessions.json"
        if sessions_file.exists():
            try:
                with open(sessions_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            except Exception:
                return []
        return []

    def get_today_sessions(self) -> List[Dict]:
        return self._today_sessions

    def get_all_sessions(self, limit: int = 50) -> List[Dict]:
        all_sessions = self._load_all_sessions() + self._today_sessions
        return all_sessions[-limit:]

    # ─── 清理 ───

    def cleanup(self):
        self._stop_event.set()
        if self._timer_thread:
            self._timer_thread.join(timeout=2)
