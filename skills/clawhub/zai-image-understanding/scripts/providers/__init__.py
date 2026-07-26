"""提供商工厂模块 - 统一创建 Z.ai 提供商实例"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config import CloudConfig

class BaseProvider:
    """所有 Provider 的抽象基类"""
    
    def analyze(self, base64_image: str, prompt: str) -> dict:
        """
        分析图片
        
        Args:
            base64_image: Base64 编码的图片数据 (不含 data:image/... 前缀)
            prompt: 提示词
            
        Returns:
            dict: {
                "text": str,           # 生成的文本描述
                "model": str,          # 使用的模型名称
                "tokens": dict,        # 可选的 token 使用情况 {"prompt": int, "completion": int, "total": int}
            }
        """
        raise NotImplementedError

# 导入 Z.ai 提供商
from .zai import ZaiProvider

# 提供商映射表 - 仅支持 Z.ai
PROVIDER_MAP = {
    "zai": ZaiProvider,
}

def get_provider(provider_name: str, config: CloudConfig):
    """
    根据名称获取提供商实例
    
    Args:
        provider_name: 提供商名称 (仅支持 "zai")
        config: 对应的配置对象
    
    Returns:
        BaseProvider 实例
    """
    provider_class = PROVIDER_MAP.get(provider_name.lower())
    if not provider_class:
        raise ValueError(f"不支持的提供商: {provider_name}. 仅支持: {list(PROVIDER_MAP.keys())}")
    
    return provider_class(config)

__all__ = ["get_provider", "BaseProvider", "ZaiProvider"]