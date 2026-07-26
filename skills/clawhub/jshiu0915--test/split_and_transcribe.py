#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音频分割和转录脚本
处理长音频文件，分割后使用百度语音识别API转录
此脚本使用long_audio_processor模块
"""

import os
import sys
import json
import time
from pathlib import Path
import logging

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# 导入长音频处理器和百度识别器
try:
    from long_audio_processor import process_long_audio, get_audio_info
    from audio_to_text import BaiduSpeechRecognizer
    MODULES_AVAILABLE = True
except ImportError as e:
    logger.error(f"模块导入失败: {e}")
    logger.error("请确保long_audio_processor.py和audio_to_text.py在同一目录")
    MODULES_AVAILABLE = False
    # 定义空类作为占位符
    class BaiduSpeechRecognizer:
        pass


def main():
    """主函数"""
    if not MODULES_AVAILABLE:
        logger.error("所需模块不可用，无法运行")
        sys.exit(1)

    import tempfile

    # 配置参数
    api_key = ""
    secret_key = ""
    audio_dir = "audio_files"
    text_dir = "text_files"
    segment_duration = 30.0  # 分割为30秒片段，避免文件过大

    # 初始化识别器
    recognizer = BaiduSpeechRecognizer(api_key, secret_key)

    # 获取音频文件
    audio_path = Path(audio_dir)
    if not audio_path.exists():
        logger.error(f"Audio directory does not exist: {audio_path}")
        return

    # 支持的音频文件扩展名
    extensions = ['.wav', '.WAV', '.pcm', '.amr', '.m4a', '.mp3', '.aac']
    audio_files = []
    for ext in extensions:
        audio_files.extend(audio_path.glob(f"*{ext}"))

    if not audio_files:
        logger.error("No audio files found")
        return

    logger.info(f"Found {len(audio_files)} audio file(s)")

    # 处理每个音频文件
    for audio_file in audio_files:
        logger.info(f"Processing audio file: {audio_file.name}")

        # 获取音频信息
        try:
            # 使用process_long_audio函数处理音频
            success, result = process_long_audio(
                recognizer,
                audio_file,
                Path(text_dir),
                segment_duration
            )

            if success:
                logger.info(f"音频处理成功: {audio_file.name}")
                # result是文本内容
            else:
                logger.error(f"音频处理失败 {audio_file.name}: {result}")

        except Exception as e:
            logger.error(f"处理音频文件时出错 {audio_file.name}: {e}")
            continue

    logger.info("音频转录处理完成")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)