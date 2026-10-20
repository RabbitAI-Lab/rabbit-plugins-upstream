#!/usr/bin/env python3
"""将原始字幕和翻译字幕合并为双语 SRT 文件。"""

import sys
import re
from pathlib import Path

# Windows 默认 GBK 编码会导致中文和 emoji 输出崩溃
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


def parse_srt(srt_path: str) -> list[dict]:
    """解析 SRT 文件为字幕条目列表。
    
    返回:
        包含 {index, start, end, text} 字典的列表。
    """
    with open(srt_path, "r", encoding="utf-8-sig") as f:
        content = f.read().strip()
    
    entries = []
    blocks = re.split(r"\n\n+", content)
    
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        
        index = lines[0].strip()
        time_match = re.match(
            r"(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})",
            lines[1].strip()
        )
        if not time_match:
            continue
        
        text = "\n".join(lines[2:])
        entries.append({
            "index": index,
            "start": time_match.group(1),
            "end": time_match.group(2),
            "text": text
        })
    
    return entries


def merge_bilingual(original_entries: list[dict],
                    translated_entries: list[dict],
                    output_path: str,
                    original_first: bool = True) -> str:
    """将两个 SRT 条目列表合并为双语 SRT 文件。
    
    参数:
        original_entries: 原始语言 SRT 的条目列表。
        translated_entries: 翻译语言 SRT 的条目列表。
        output_path: 输出双语 SRT 文件路径。
        original_first: 如果为 True，原文排在前面。
    
    返回:
        输出 SRT 文件路径。
    """
    # 按序号建立翻译条目的映射
    trans_map = {e["index"]: e for e in translated_entries}
    
    with open(output_path, "w", encoding="utf-8") as f:
        for i, orig in enumerate(original_entries, 1):
            trans = trans_map.get(orig["index"])
            trans_text = trans["text"] if trans else ""
            
            f.write(f"{i}\n")
            f.write(f"{orig['start']} --> {orig['end']}\n")
            
            if original_first:
                f.write(f"{orig['text']}\n")
                if trans_text:
                    f.write(f"{trans_text}\n")
            else:
                if trans_text:
                    f.write(f"{trans_text}\n")
                f.write(f"{orig['text']}\n")
            
            f.write("\n")
    
    print(f"双语 SRT 已保存：{output_path}（{len(original_entries)} 条）")
    return output_path


def merge_from_paths(original_srt: str, translated_srt: str,
                     output_path: str, original_first: bool = True) -> str:
    """便捷封装：通过文件路径合并两个 SRT 文件，并校验条目数一致性。"""
    orig_entries = parse_srt(original_srt)
    trans_entries = parse_srt(translated_srt)
    
    # 校验条目数一致性
    orig_count = len(orig_entries)
    trans_count = len(trans_entries)
    if orig_count != trans_count:
        print(f"警告：原始字幕 {orig_count} 条 ≠ 翻译字幕 {trans_count} 条，"
              f"可能丢失 {abs(orig_count - trans_count)} 条", file=sys.stderr)
    
    return merge_bilingual(orig_entries, trans_entries, output_path, original_first)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("用法：python merge_srt.py <原始.srt> <翻译.srt> <输出.srt> [译文在前]")
        print("  译文在前：传入 'yes' 将译文排在前面（默认：原文在前）")
        sys.exit(1)
    
    original_srt = sys.argv[1]
    translated_srt = sys.argv[2]
    output_path = sys.argv[3]
    original_first = sys.argv[4].lower() != "yes" if len(sys.argv) > 4 else True
    
    merge_from_paths(original_srt, translated_srt, output_path, original_first)
