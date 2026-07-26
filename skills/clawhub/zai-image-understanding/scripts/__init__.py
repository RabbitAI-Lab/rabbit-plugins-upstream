"""
Z.ai Image Understanding Skill
==============================

A Linux-compatible skill for image understanding using Z.ai (智谱 AI) GLM-4V Vision API.

Features:
- Z.ai GLM-4V Vision API support (OpenAI-compatible format)
- Image loading from local files, URLs, or base64 data URIs
- Automatic image resizing for large files
- Configurable prompts and models
- Markdown output saving
- Batch processing capability

Quick Start:
1. Install dependencies: pip install -r requirements.txt
2. Configure: Set ZAI_API_KEY environment variable
3. Use: python -m zai_image_understanding.analyze -i /path/to/image.jpg

Example Config (~/.config/zai-image-understanding/config.json):
{
  "mode": "cloud",
  "cloud": {
    "provider": "zai",
    "model": "glm-4.1v-thinking-flash",
    "api_key_env": "ZAI_API_KEY",
    "base_url": "https://open.bigmodel.cn/api/paas/v4",
    "timeout_seconds": 60
  },
  "default_prompt": "请详细描述这张图片的内容，包括主要物体、场景、文字、颜色、构图等信息。"
}
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from utils.config import Config, load_config, save_config, DEFAULT_CONFIG_PATH
from utils.image import load_image, resize_image_if_needed, image_to_base64
from providers import get_provider

__version__ = "0.1.0"
__author__ = "workspace-agent"
__all__ = [
    "analyze_image",
    "load_config",
    "save_config",
    "Config",
]


def analyze_image(
    image_path: str,
    prompt: str = None,
    mode: str = None,
    config_path: str = None,
) -> dict:
    """
    分析图片内容
    
    Args:
        image_path: 图片路径、URL 或 Base64 Data URI
        prompt: 自定义提示词（可选，覆盖配置文件默认值）
        mode: 强制指定运行模式（仅支持 "cloud"）
        config_path: 配置文件路径（可选）
    
    Returns:
        dict: {
            "status": "success" | "error",
            "result": "分析结果文本" (仅成功时),
            "model": "使用的模型名称",
            "tokens": {"prompt": int, "completion": int, "total": int},
            "elapsed_seconds": float,
            "error": "错误信息" (仅错误时)
        }
    """
    # 加载配置
    config = load_config(config_path)
    
    # 获取提示词
    if prompt is None:
        prompt = config.default_prompt
    
    # 强制 cloud 模式（只支持 Z.ai）
    if mode and mode != "cloud":
        return {
            "status": "error",
            "error": f"仅支持 cloud 模式，当前只支持 Z.ai API",
            "model": config.cloud.model,
        }
    
    # 加载图片
    image = load_image(image_path)
    if isinstance(image, dict) and "error" in image:
        return {
            "status": "error",
            "error": image["error"],
            "model": config.cloud.model,
        }
    
    # 调整图片大小
    image = resize_image_if_needed(image)
    
    # 转换为 base64
    image_base64 = image_to_base64(image)
    
    # 获取提供商并分析
    try:
        provider = get_provider(config.cloud.provider, config.cloud)
        result = provider.analyze(image_base64, prompt)
        # 统一返回格式：provider 返回 text，转为 result
        return {
            "status": "success",
            "result": result.get("text", ""),
            "model": result.get("model", config.cloud.model),
            "tokens": result.get("tokens", {}),
        }
    except Exception as e:
        return {
            "status": "error",
            "error": f"分析失败: {type(e).__name__}: {e}",
            "model": config.cloud.model,
        }