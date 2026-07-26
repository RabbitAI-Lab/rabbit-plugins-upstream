#!/usr/bin/env python3
"""图片处理工具模块"""

import base64
import io
import mimetypes
import re
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

import requests
from PIL import Image


MAX_IMAGE_SIZE = (2048, 2048)
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB


def load_image(image_input: str) -> Union[Image.Image, dict]:
    """
    加载图片，支持：
    - 本地文件路径
    - HTTP/HTTPS URL
    - Base64 Data URI (data:image/...;base64,...)
    
    Returns:
        PIL.Image 对象或 {"error": "错误信息"} 字典
    """
    try:
        # 处理 Base64 Data URI
        if image_input.startswith("data:image"):
            return _load_from_data_uri(image_input)
        
        # 处理 URL
        parsed = urlparse(image_input)
        if parsed.scheme in ("http", "https"):
            return _load_from_url(image_input)
        
        # 处理本地文件
        return _load_from_file(image_input)
        
    except Exception as e:
        return {"error": f"加载图片失败: {e}"}


def _load_from_data_uri(data_uri: str) -> Image.Image:
    """从 Data URI 加载"""
    match = re.match(r"data:image/(\w+);base64,(.+)", data_uri)
    if not match:
        raise ValueError("无效的 Data URI 格式")
    
    mime_type, b64_data = match.groups()
    image_data = base64.b64decode(b64_data)
    
    if len(image_data) > MAX_FILE_SIZE:
        raise ValueError(f"图片过大，超过 {MAX_FILE_SIZE/1024/1024}MB 限制")
    
    return Image.open(io.BytesIO(image_data))


def _load_from_url(url: str) -> Image.Image:
    """从 URL 下载并加载"""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    
    if len(response.content) > MAX_FILE_SIZE:
        raise ValueError(f"图片过大，超过 {MAX_FILE_SIZE/1024/1024}MB 限制")
    
    return Image.open(io.BytesIO(response.content))


def _load_from_file(path: str) -> Image.Image:
    """从本地文件加载"""
    path = Path(path).expanduser().resolve()
    
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {path}")
    
    if path.stat().st_size > MAX_FILE_SIZE:
        raise ValueError(f"图片过大，超过 {MAX_FILE_SIZE/1024/1024}MB 限制")
    
    return Image.open(path)


def resize_image_if_needed(image: Image.Image, max_size: tuple = MAX_IMAGE_SIZE) -> Image.Image:
    """如果图片超过最大尺寸则缩放"""
    if image.width > max_size[0] or image.height > max_size[1]:
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
    return image


def image_to_base64(image: Image.Image, format: str = "JPEG", quality: int = 85) -> str:
    """将 PIL Image 转换为 Base64 字符串"""
    # 转换为 RGB（去除 alpha 通道，JPEG 不支持）
    if image.mode in ("RGBA", "LA", "P"):
        background = Image.new("RGB", image.size, (255, 255, 255))
        if image.mode == "P":
            image = image.convert("RGBA")
        background.paste(image, mask=image.split()[-1] if image.mode in ("RGBA", "LA") else None)
        image = background
    elif image.mode != "RGB":
        image = image.convert("RGB")
    
    buffer = io.BytesIO()
    image.save(buffer, format=format, quality=quality, optimize=True)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def get_mime_type(image: Image.Image, format: str = "JPEG") -> str:
    """获取 MIME 类型"""
    return f"image/{format.lower()}"