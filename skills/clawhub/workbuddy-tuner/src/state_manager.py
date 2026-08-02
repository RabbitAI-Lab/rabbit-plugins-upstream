# Copyright (c) 2026 Joyxj2devs Team
"""
Tuner Skill - 客户端状态管理器

持有 WorkBuddy 调优的状态信息：
- 健康历史快照
- 策略权重表
- 最近优化动作
- 配置信息
"""
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field, asdict


@dataclass
class HealthSnapshot:
    """健康快照"""
    timestamp: int = 0
    health_score: float = 0.0
    level: str = "unknown"
    process_count: int = 0
    wb_rss_mb: int = 0
    cache_gb: float = 0.0
    cache_stale_gb: float = 0.0
    disk_free_gb: float = 0.0
    network_ok: bool = True
    top_strategy: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TunerState:
    """调优客户端状态"""
    snapshots: List[HealthSnapshot] = field(default_factory=list)
    weights: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    actions: List[Dict[str, Any]] = field(default_factory=list)
    config: Dict[str, Any] = field(default_factory=dict)
    platform: str = "windows"


class TunerStateManager:
    """
    WorkBuddy 调优客户端状态管理器
    
    客户端负责：
    1. 持久化健康历史快照
    2. 保存策略权重表
    3. 记录优化动作
    4. 与 MCP Toolbox 交互（传入/接收数据）
    """

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self._state = TunerState()
        self._load()

    # ===== 持久化 =====

    def _load(self):
        """加载状态"""
        state_path = self.data_dir / "tuner_state.json"
        if state_path.exists():
            try:
                with open(state_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self._state.snapshots = [
                    HealthSnapshot(**s) for s in data.get("snapshots", [])
                ]
                self._state.weights = data.get("weights", {})
                self._state.actions = data.get("actions", [])
                self._state.config = data.get("config", {})
                self._state.platform = data.get("platform", "windows")
            except Exception:
                pass

    def save(self):
        """保存状态"""
        state_path = self.data_dir / "tuner_state.json"
        data = {
            "snapshots": [asdict(s) for s in self._state.snapshots],
            "weights": self._state.weights,
            "actions": self._state.actions,
            "config": self._state.config,
            "platform": self._state.platform,
        }
        with open(state_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # ===== 快照管理 =====

    def add_snapshot(self, health_score: float, **kwargs):
        """添加健康快照"""
        snap = HealthSnapshot(
            timestamp=int(time.time()),
            health_score=health_score,
            **kwargs,
        )
        self._state.snapshots.append(snap)
        # 限制快照数量
        if len(self._state.snapshots) > 50:
            self._state.snapshots = self._state.snapshots[-50:]
        self.save()
        return snap

    def get_snapshots(self) -> List[HealthSnapshot]:
        """获取所有快照"""
        return self._state.snapshots

    def get_last_snapshot(self) -> Optional[HealthSnapshot]:
        """获取最新快照"""
        return self._state.snapshots[-1] if self._state.snapshots else None

    # ===== 权重管理 =====

    def get_weights(self) -> Dict[str, Dict[str, Any]]:
        """获取策略权重"""
        return self._state.weights

    def update_weight(self, strategy: str, **updates):
        """更新策略权重（策略数量上限 50，防止无限增长）"""
        if strategy not in self._state.weights:
            # 策略数量限制：防止无界增长
            if len(self._state.weights) >= 50:
                print(f"[tuner] 策略权重已达上限 50，跳过添加: {strategy}")
                return
            self._state.weights[strategy] = {}
        self._state.weights[strategy].update(updates)
        self.save()

    # ===== 动作记录 =====

    def record_action(self, name: str, **kwargs):
        """记录优化动作"""
        action = {
            "timestamp": int(time.time()),
            "name": name,
            **kwargs,
        }
        self._state.actions.append(action)
        # 限制动作数量
        if len(self._state.actions) > 100:
            self._state.actions = self._state.actions[-100:]
        self.save()
        return action

    def get_recent_actions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """获取最近动作"""
        return self._state.actions[-limit:]

    # ===== 完整状态导出 =====

    def get_full_state(self) -> Dict[str, Any]:
        """导出完整状态（供 MCP Toolbox 消费）"""
        return {
            "snapshots": [asdict(s) for s in self._state.snapshots],
            "weights": self._state.weights,
            "recent_actions": self.get_recent_actions(10),
            "config": self._state.config,
            "platform": self._state.platform,
        }

    # ===== 清理 =====

    def cleanup(self):
        """清理（保存 + 释放资源）"""
        self.save()

    def export_json(self) -> str:
        """导出状态为 JSON 字符串"""
        return json.dumps(self.get_full_state(), ensure_ascii=False, indent=2)
