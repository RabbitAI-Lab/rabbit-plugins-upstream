#!/usr/bin/env python3
"""从视频文件中提取音频轨道，使用 ffmpeg。"""

import subprocess
import sys
import os
from pathlib import Path

# Windows 默认 GBK 编码会导致中文和 emoji 输出崩溃
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


def extract_audio(video_path: str, output_path: str | None = None) -> str:
    """从视频中提取音频并返回输出音频路径。
    
    参数:
        video_path: 输入视频文件路径。
        output_path: 输出音频文件路径。如果为 None，则使用同名 .mp3 扩展名。
    
    返回:
        提取的音频文件路径。
    """
    video = Path(video_path)
    if not video.exists():
        print(f"错误：找不到视频文件：{video_path}", file=sys.stderr)
        sys.exit(1)
    
    if output_path is None:
        output_path = str(video.with_suffix(".mp3"))
    
    # 自动创建输出目录
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        "ffmpeg", "-y", "-i", str(video),
        "-vn",                    # 不要视频
        "-acodec", "libmp3lame",  # MP3 编码器
        "-ab", "192k",            # 192kbps 比特率
        "-ar", "16000",           # 16kHz 采样率（适合语音识别）
        "-ac", "1",               # 单声道
        output_path
    ]
    
    print(f"正在提取音频：{video.name}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"错误：ffmpeg 执行失败：\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.exists(output_path):
        print("错误：音频提取未生成输出文件", file=sys.stderr)
        sys.exit(1)
    
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"音频提取完成：{output_path}（{size_mb:.1f} MB）")
    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python extract_audio.py <视频路径> [输出路径]")
        sys.exit(1)
    
    video_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    extract_audio(video_path, output_path)
