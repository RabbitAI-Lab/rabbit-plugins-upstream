#!/usr/bin/env python3
"""播客时间轴生成与校准工具。

两种模式：
  --estimate  按段落字数估算（260 字/分钟），无需 MP3，用于写 notes.md 初稿
  --calibrate 用 ffprobe 读取实际 MP3 各段时长，精确校准已有时间轴

用法：
  # 估算：从 script.md 生成时间轴
  python3 scripts/generate_timeline.py --script script.md --estimate

  # 校准：用已合成的 MP3 精确校准
  python3 scripts/generate_timeline.py --script script.md --mp3 podcast.mp3 --calibrate

输出格式（与 notes.md 时间轴一致）：
  - 00:00 开场：为什么没人再手写 prompt
  - 02:16 CoT：让 LLM 学会推理
  - ...
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

sys.path.insert(0, str(Path(__file__).parent))
# 解析与旁白节奏常量共用 script_md：synthesis 改参数，这里的估算自动跟随
from script_md import (NARRATION_LEAD_SILENCE_MS, NARRATION_SPEECH_RATE,
                       NARRATION_TAIL_SILENCE_MS, NORMAL_SILENCE_MS,
                       is_narration, parse_by_segments)

# 中文对谈语速（字/分钟）——纯估算参数，只在本工具使用
CHARS_PER_MIN = 260
# 由合成用的 speech_rate 推导（如 -12 → 0.88x），不再手抄一份系数
NARRATION_SPEED_FACTOR = 1 + NARRATION_SPEECH_RATE / 100


def estimate_timeline(filepath: str) -> List[Tuple[str, int]]:
    """按字数估算各段时间。返回 [(segment_title, seconds), ...]"""
    timeline = []
    for title, lines in parse_by_segments(filepath):
        seg_seconds = 0.0
        for speaker, text in lines:
            char_count = len(re.sub(r'\s+', '', text))
            if is_narration(speaker):
                seg_seconds += (char_count / CHARS_PER_MIN) * 60 * (1 / NARRATION_SPEED_FACTOR)
                seg_seconds += (NARRATION_LEAD_SILENCE_MS + NARRATION_TAIL_SILENCE_MS) / 1000  # 进出场静音
            else:
                seg_seconds += (char_count / CHARS_PER_MIN) * 60
                seg_seconds += NORMAL_SILENCE_MS / 1000  # 轮间静音
        timeline.append((title, max(1, int(seg_seconds))))

    return timeline


def calibrate_timeline(script_path: str, mp3_path: str) -> List[Tuple[str, int]]:
    """用 ffprobe 读取 MP3 总时长，按各段字数比例分配精确秒数。"""
    total = get_duration_seconds(mp3_path)
    if total <= 0:
        print(f"❌ 无法读取 MP3 时长: {mp3_path}", file=sys.stderr)
        sys.exit(1)

    estimates = estimate_timeline(script_path)
    total_est = sum(s for _, s in estimates)
    if total_est <= 0:
        print("❌ 估算总时长为 0", file=sys.stderr)
        sys.exit(1)

    # 按比例分配实际时长：起点从累计估算比例整体折算（而非逐段取整后累加），
    # 避免向下取整误差单调累积导致后段时间戳系统性偏早
    timeline = []
    cum_est = 0
    for title, est_s in estimates:
        timeline.append((title, round(total * cum_est / total_est)))
        cum_est += est_s

    return timeline


def get_duration_seconds(path: str) -> int:
    result = subprocess.run([
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", path
    ], capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout.strip():
        return 0
    return int(float(result.stdout.strip()))


def format_timestamp(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"


def main():
    parser = argparse.ArgumentParser(description="播客时间轴生成与校准")
    parser.add_argument("--script", required=True, help="script.md 路径")
    parser.add_argument("--mp3", help="已合成的 MP3 路径（--calibrate 模式必需）")
    parser.add_argument("--estimate", action="store_true", help="按字数估算时间轴")
    parser.add_argument("--calibrate", action="store_true", help="用 MP3 校准时间轴")
    args = parser.parse_args()

    if not args.estimate and not args.calibrate:
        parser.error("请指定 --estimate 或 --calibrate")

    if args.calibrate and not args.mp3:
        parser.error("--calibrate 需要 --mp3 参数")

    if args.estimate:
        timeline = estimate_timeline(args.script)
        print("**时间轴**（估算）\n")
        cumulative = 0
        for title, seconds in timeline:
            print(f"- {format_timestamp(cumulative)} {title}")
            cumulative += seconds
        print(f"\n估算总时长: {format_timestamp(cumulative)}")
    else:
        timeline = calibrate_timeline(args.script, args.mp3)
        print("**时间轴**\n")
        for title, start_s in timeline:
            print(f"- {format_timestamp(start_s)} {title}")
        total = get_duration_seconds(args.mp3)
        print(f"\n实际总时长: {format_timestamp(total)}")


if __name__ == "__main__":
    main()
