# Copyright (c) 2026 Joyxj2devs Team
"""
Privacymask - 状态管理器

管理脱敏配置、历史日志、自定义规则持久化。
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional


class PrivacymaskStateManager:
    """
    Privacymask 状态管理器

    管理：
    - 脱敏配置（默认规则、默认类别、输出目录）
    - 脱敏历史日志
    - 自定义规则持久化
    """

    def __init__(self, data_dir: Optional[str] = None):
        self.data_dir = Path(data_dir) if data_dir else Path.home() / ".privacymask"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.config_path = self.data_dir / "config.json"
        self.history_path = self.data_dir / "history.jsonl"
        self.custom_rules_path = self.data_dir / "custom_rules.json"
        self._config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if self.config_path.exists():
            try:
                return json.loads(self.config_path.read_text())
            except (json.JSONDecodeError, OSError):
                pass
        return self._default_config()

    def _default_config(self) -> Dict[str, Any]:
        return {
            "output_base_dir": "",
            "default_rules": [],
            "default_categories": [
                "cn_personal", "cn_enterprise", "cn_financial",
                "intl_pii", "intl_financial", "cn_health",
            ],
            "auto_mask_directory": True,
            "max_findings_preview": 50,
            "report_format": "json",
        }

    def save_config(self) -> None:
        self.config_path.write_text(json.dumps(self._config, ensure_ascii=False, indent=2))

    def get(self, key: str) -> Any:
        return self._config.get(key)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value
        self.save_config()

    def get_all(self) -> Dict[str, Any]:
        return dict(self._config)

    def add_history(self, entry: Dict[str, Any]) -> None:
        """添加脱敏历史记录"""
        try:
            with open(self.history_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except OSError:
            pass

    def get_history(self, limit: int = 10) -> list:
        """获取脱敏历史"""
        if not self.history_path.exists():
            return []
        try:
            lines = self.history_path.read_text().strip().split("\n")
            return [json.loads(l) for l in lines[-limit:] if l.strip()]
        except (json.JSONDecodeError, OSError):
            return []

    def clear_history(self) -> None:
        if self.history_path.exists():
            self.history_path.unlink()

    def load_custom_rules(self) -> Dict[str, Any]:
        """加载自定义规则"""
        if self.custom_rules_path.exists():
            try:
                return json.loads(self.custom_rules_path.read_text())
            except (json.JSONDecodeError, OSError):
                return {}
        return {}

    def save_custom_rules(self, rules: Dict[str, Any]) -> None:
        """保存自定义规则"""
        self.custom_rules_path.write_text(json.dumps(rules, ensure_ascii=False, indent=2))
