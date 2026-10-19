#!/usr/bin/env python3
"""将翻译后的 JSON 段落转换为 SRT 字幕文件。"""

import json
import sys
import re
import io
from pathlib import Path

# 修复 Windows 下 GBK 编码问题
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def format_timestamp(seconds: float) -> str:
    """将秒数转换为 SRT 时间戳格式 HH:MM:SS,mmm。"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def json_to_srt(json_path: str, output_srt: str) -> str:
    """将转录结果 JSON（含 'segments' 字段）转换为 SRT 格式。
    
    参数:
        json_path: 转录结果 JSON 文件路径。
        output_srt: 输出 SRT 文件路径。
    
    返回:
        输出 SRT 文件路径。
    """
    # 读取 JSON，自动修复中文引号导致的解析问题
    with open(json_path, "r", encoding="utf-8") as f:
        raw = f.read()
    
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # 尝试修复常见问题：中文引号被当成 JSON 分隔符
        # 将中文引号替换为转义的 Unicode
        fixed = raw.replace("\u201c", "\\u201c").replace("\u201d", "\\u201d")
        fixed = fixed.replace("\u2018", "\\u2018").replace("\u2019", "\\u2019")
        try:
            data = json.loads(fixed)
            print("提示：已自动修复 JSON 中的中文引号问题")
        except json.JSONDecodeError as e:
            print(f"错误：JSON 解析失败，请使用 json.dump() 生成翻译 JSON 文件。\n原始错误：{e}", file=sys.stderr)
            sys.exit(1)
    
    segments = data.get("segments", [])
    
    with open(output_srt, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            f.write(f"{i}\n")
            f.write(f"{format_timestamp(seg['start'])} --> {format_timestamp(seg['end'])}\n")
            f.write(f"{seg['text']}\n\n")
    
    print(f"SRT 字幕已保存：{output_srt}（{len(segments)} 条）")
    return output_srt


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法：python json_to_srt.py <转录结果.json> <输出.srt>")
        sys.exit(1)
    
    json_to_srt(sys.argv[1], sys.argv[2])
