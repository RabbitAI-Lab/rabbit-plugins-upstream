#!/usr/bin/env python3
"""配置加载模块 - 仅支持 Z.ai 云端模式"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class CloudConfig:
    provider: str = "zai"  # 固定为 zai
    model: str = "glm-4.1v-thinking-flash"
    api_key_env: str = "ZAI_API_KEY"
    base_url: str = "https://open.bigmodel.cn/api/paas/v4"
    timeout_seconds: int = 60


@dataclass
class Config:
    mode: str = "cloud"  # 固定为 cloud
    cloud: CloudConfig = field(default_factory=CloudConfig)
    default_prompt: str = "请详细描述这张图片的内容，包括主要物体、场景、文字、颜色、构图等信息。"
    
    @classmethod
    def from_dict(cls, data: dict) -> "Config":
        cloud = CloudConfig(**data.get("cloud", {}))
        return cls(
            mode="cloud",  # 强制 cloud 模式
            cloud=cloud,
            default_prompt=data.get("default_prompt", cls.default_prompt),
        )
    
    def to_dict(self) -> dict:
        return {
            "mode": "cloud",
            "cloud": {
                "provider": self.cloud.provider,
                "model": self.cloud.model,
                "api_key_env": self.cloud.api_key_env,
                "base_url": self.cloud.base_url,
                "timeout_seconds": self.cloud.timeout_seconds,
            },
            "default_prompt": self.default_prompt,
        }


DEFAULT_CONFIG_PATH = Path.home() / ".config" / "zai-image-understanding" / "config.json"
DEFAULT_CONFIG = Config()


def load_config(config_path: Optional[str] = None) -> Config:
    """加载配置文件，不存在则返回默认配置"""
    path = Path(config_path) if config_path else DEFAULT_CONFIG_PATH
    
    if not path.exists():
        # 创建默认配置文件
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG.to_dict(), f, indent=2, ensure_ascii=False)
        return DEFAULT_CONFIG
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Config.from_dict(data)
    except Exception as e:
        print(f"配置加载失败，使用默认配置: {e}")
        return DEFAULT_CONFIG


def save_config(config: Config, config_path: Optional[str] = None) -> None:
    """保存配置到文件"""
    path = Path(config_path) if config_path else DEFAULT_CONFIG_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config.to_dict(), f, indent=2, ensure_ascii=False)