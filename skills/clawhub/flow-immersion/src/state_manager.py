# Flow Immersion Client - 状态管理与运行时
# 本 Skill 持有所有运行时状态，通过 MCP Toolbox 调用无状态逻辑

import json
import time
import threading
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional, Callable, List


@dataclass
class PomodoroState:
    """番茄钟运行时状态（客户端持有）"""
    phase: str = "idle"           # idle/work/break/long_break
    task: str = ""
    start_time: float = 0         # epoch
    elapsed_seconds: int = 0
    total_seconds: int = 1500     # 25 * 60
    current_round: int = 0
    total_rounds: int = 4
    config: Dict = field(default_factory=dict)
    completed_rounds: int = 0
    aborted: bool = False

    def to_dict(self):
        return asdict(self)


class StateManager:
    """
    客户端状态管理器

    核心职责:
    - 持有所有运行时状态（计时器、会话、配置）
    - 线程安全读写
    - 提供状态快照给 MCP Toolbox 调用
    - 持久化到 JSON 文件
    """

    def __init__(self, data_dir: str = None):
        self._data_dir = Path(data_dir) if data_dir else Path(__file__).parent.parent / "data"
        self._data_dir.mkdir(parents=True, exist_ok=True)

        self._lock = threading.Lock()
        self._state = {
            "timer": PomodoroState(),
            "adhd_session": None,
            "config": self._load_default_config(),
            "today_sessions": [],
        }

        self._timer_thread = None
        self._timer_callback: Optional[Callable] = None
        self._on_tick: Optional[Callable] = None
        self._stop_event = threading.Event()

    def _load_default_config(self):
        return {
            "timer": {"work_minutes": 25, "break_minutes": 5,
                       "long_break_minutes": 15, "rounds": 4},
            "adhd": {"companion_enabled": False, "check_in_interval": 15},
            "immersion": {"auto_wallpaper": True, "default_preset": "minimal"},
            "tracking": {"track_distractions": True},
            "personalize": {"theme": "dark"},
        }

    # ─── 番茄钟状态 ───

    def get_timer_state(self) -> Dict:
        """获取计时器状态快照"""
        with self._lock:
            return self._state["timer"].to_dict()

    def set_timer_state(self, **kwargs):
        """更新计时器状态"""
        with self._lock:
            for k, v in kwargs.items():
                if hasattr(self._state["timer"], k):
                    setattr(self._state["timer"], k, v)

    def get_full_state(self) -> Dict:
        """获取完整状态（传给 MCP Toolbox 的 state 参数）"""
        with self._lock:
            return {
                "timer": self._state["timer"].to_dict(),
                "adhd_session": self._state["adhd_session"],
                "config": self._state["config"],
                "today_sessions": self._state["today_sessions"],
                "platform": "windows",
            }

    # ─── 番茄钟运行时 ───

    def start_timer(self, work_minutes: int = 25, break_minutes: int = 5,
                    task: str = "", callback: Callable = None,
                    long_break_minutes: int = 15, rounds: int = 4):
        """启动番茄钟"""
        with self._lock:
            timer = self._state["timer"]
            timer.phase = "work"
            timer.task = task
            timer.start_time = time.time()
            timer.elapsed_seconds = 0
            timer.total_seconds = work_minutes * 60
            timer.current_round = 0
            timer.total_rounds = rounds
            timer.completed_rounds = 0
            timer.aborted = False
            timer.config = {
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
        """暂停计时器"""
        with self._lock:
            self._state["timer"].phase = "paused"

        self._stop_event.set()

    def resume_timer(self):
        """恢复计时器"""
        with self._lock:
            timer = self._state["timer"]
            timer.phase = "work"
            timer.start_time = time.time()

        self._stop_event.clear()
        if not self._timer_thread or not self._timer_thread.is_alive():
            self._timer_thread = threading.Thread(target=self._timer_loop, daemon=True)
            self._timer_thread.start()

    def stop_timer(self, completed: bool = False):
        """停止计时器"""
        self._stop_event.set()
        with self._lock:
            timer = self._state["timer"]
            timer.phase = "idle"
            timer.aborted = not completed
            if completed:
                timer.completed_rounds += 1
                self._record_session(timer)

        self._stop_event.set()

    def _timer_loop(self):
        """计时器后台循环"""
        tick_interval = 1  # 1秒更新一次

        while not self._stop_event.is_set():
            with self._lock:
                if self._state["timer"].phase == "paused":
                    break

            time.sleep(tick_interval)

            with self._lock:
                timer = self._state["timer"]
                timer.elapsed_seconds += tick_interval

                # 调用 tick 回调
                if self._on_tick:
                    try:
                        self._on_tick(timer.to_dict())
                    except Exception:
                        pass

                # 检查是否到时间
                if timer.elapsed_seconds >= timer.total_seconds and timer.phase in ("work", "break", "long_break"):
                    self._phase_complete(timer)
                    return

    def _phase_complete(self, timer):
        """阶段完成"""
        if timer.phase == "work":
            timer.completed_rounds += 1
            self._record_session(timer)

            if timer.completed_rounds >= timer.total_rounds:
                timer.phase = "idle"
            else:
                is_long = (timer.completed_rounds % timer.total_rounds == 0)
                if is_long:
                    timer.phase = "long_break"
                    timer.total_seconds = timer.config.get("long_break_minutes", 15) * 60
                else:
                    timer.phase = "break"
                    timer.total_seconds = timer.config.get("break_minutes", 5) * 60
                timer.elapsed_seconds = 0
                timer.start_time = time.time()

        elif timer.phase == "break":
            timer.phase = "work"
            timer.elapsed_seconds = 0
            timer.start_time = time.time()
            timer.total_seconds = timer.config.get("work_minutes", 25) * 60
            # 继续计时循环

        elif timer.phase == "long_break":
            timer.phase = "work"
            timer.elapsed_seconds = 0
            timer.start_time = time.time()
            timer.total_seconds = timer.config.get("work_minutes", 25) * 60

    def _record_session(self, timer):
        """记录会话"""
        session = {
            "task": timer.task,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "work_minutes": timer.config.get("work_minutes", 25),
            "actual_minutes": timer.elapsed_seconds // 60,
            "completed": not timer.aborted,
        }
        self._state["today_sessions"].append(session)

    def set_on_tick(self, callback: Callable):
        """设置计时器 tick 回调"""
        self._on_tick = callback

    # ─── ADHD 会话 ───

    def start_adhd_session(self, task: str, config: Dict = None):
        """启动 ADHD 会话"""
        with self._lock:
            if config:
                # 兼容 handle_start_session 返回的 micro_steps_template
                micro_steps = config.get("steps") or config.get("micro_steps_template") or []
            else:
                micro_steps = []
            self._state["adhd_session"] = {
                "task": task,
                "created_at": datetime.now().isoformat(),
                "micro_steps": micro_steps,
                "completed_steps": [],
                "check_in_count": 0,
                "dopamine_count": 0,
                "distractions": [],
                "status": "active",
            }

    def add_adhd_step(self, step: str):
        """添加微步骤"""
        with self._lock:
            session = self._state["adhd_session"]
            if session:
                session["micro_steps"].append({
                    "description": step,
                    "completed": False,
                    "order": len(session["micro_steps"]) + 1,
                })

    def complete_adhd_step(self, index: int = None):
        """完成微步骤"""
        with self._lock:
            session = self._state["adhd_session"]
            if session and session.get("micro_steps"):
                if index is None:
                    # 完成第一个未完成的
                    for i, s in enumerate(session["micro_steps"]):
                        if not s["completed"]:
                            session["micro_steps"][i]["completed"] = True
                            session["completed_steps"].append(i)
                            break
                elif 0 <= index < len(session["micro_steps"]):
                    session["micro_steps"][index]["completed"] = True
                    session["completed_steps"].append(index)

    def get_adhd_status(self) -> Dict:
        """获取 ADHD 会话状态"""
        with self._lock:
            return dict(self._state["adhd_session"]) if self._state["adhd_session"] else {"status": "inactive"}

    # ─── 配置 ───

    def load_config(self):
        """加载配置"""
        config_file = self._data_dir / "config.json"
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    self._state["config"] = json.load(f)
            except Exception:
                pass

    def save_config(self):
        """保存配置"""
        config_file = self._data_dir / "config.json"
        with self._lock:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(self._state["config"], f, ensure_ascii=False, indent=2)

    def update_config(self, path: str, value):
        """更新配置（支持点分隔路径）"""
        keys = path.split(".")
        d = self._state["config"]
        for key in keys[:-1]:
            if key not in d:
                d[key] = {}
            d = d[key]
        d[keys[-1]] = value
        self.save_config()

    # ─── 持久化 ───

    def save_sessions(self):
        """保存会话到文件"""
        sessions_file = self._data_dir / "sessions.json"
        all_sessions = self._load_all_sessions() + self._state["today_sessions"]
        with open(sessions_file, 'w', encoding='utf-8') as f:
            json.dump(all_sessions, f, ensure_ascii=False, indent=2)

    def _load_all_sessions(self):
        """加载所有历史会话"""
        sessions_file = self._data_dir / "sessions.json"
        if sessions_file.exists():
            try:
                with open(sessions_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            except Exception:
                return []
        return []

    def get_today_sessions(self) -> List[Dict]:
        """获取今日会话"""
        return self._state["today_sessions"]

    def get_all_sessions(self, limit: int = 50) -> List[Dict]:
        """获取所有会话（含历史）"""
        all_sessions = self._load_all_sessions() + self._state["today_sessions"]
        return all_sessions[-limit:]

    # ─── 清理 ───

    def cleanup(self):
        """清理资源"""
        self._stop_event.set()
        if self._timer_thread:
            self._timer_thread.join(timeout=2)
