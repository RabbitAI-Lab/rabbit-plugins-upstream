#!/usr/bin/env python3
"""Z.ai GLM Vision API 提供商 (兼容 OpenAI 格式)"""

import os
import sys
from pathlib import Path
from typing import Any, Dict

import requests

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import CloudConfig
from providers import BaseProvider


class ZaiProvider(BaseProvider):
    """Z.ai GLM-4V Vision API (OpenAI 兼容格式)"""
    
    def __init__(self, config: CloudConfig):
        self.config = config
        self.model = config.model
        self.api_key = os.getenv(config.api_key_env)
        self.base_url = getattr(config, 'base_url', "https://open.bigmodel.cn/api/paas/v4").rstrip("/")
        self.timeout = config.timeout_seconds
        
        if not self.api_key:
            raise ValueError(f"环境变量 {config.api_key_env} 未设置")
        
        self.chat_endpoint = f"{self.base_url}/chat/completions"
    
    def analyze(self, base64_image: str, prompt: str) -> Dict[str, Any]:
        """调用 Z.ai GLM Vision API"""
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 16384,
            "temperature": 0.1,
            "stream": False
        }
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        
        try:
            response = requests.post(
                self.chat_endpoint,
                json=payload,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            choice = data.get("choices", [{}])[0]
            message = choice.get("message", {})
            text = message.get("content", "")
            
            usage = data.get("usage", {})
            tokens = {
                "prompt": usage.get("prompt_tokens", 0),
                "completion": usage.get("completion_tokens", 0),
                "total": usage.get("total_tokens", 0),
            }
            
            return {
                "text": text,
                "model": data.get("model", self.model),
                "tokens": tokens,
            }
            
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"Z.ai API 错误: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            raise RuntimeError(f"Z.ai 调用失败: {e}")