#!/usr/bin/env python3
"""
黄金追踪 - 日志标准化器
统一所有 YAML 日志中的时间戳和影响方向字段值。
保留原始缩进。零第三方依赖。
"""

import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TZ_BEIJING = timezone(timedelta(hours=8))

# 仅允许 6 个标准值，所有非标准值都收敛到最近的标准值
# 标准值列表与 config.yaml output.constraints.allowed_impacts 一致
IMPACT_MAP = {
    # 中文 -> 标准
    "看涨": "bullish", "看跌": "bearish",
    "利多": "bullish", "利空": "bearish",
    "中性": "neutral", "双向": "mixed",
    "中性偏多": "slightly_bullish", "中性偏空": "slightly_bearish",
    "中性偏谨慎": "neutral",
    # 历史变体（强制收敛到 6 个标准值之一）
    "技术利多": "slightly_bullish", "强力利多": "bullish",
    "看涨（已定价）": "slightly_bullish",
    "看涨（中期）": "bullish",
    "边际利多": "slightly_bullish",
    # emoji 变体
    "🟢利多": "bullish", "🔴利空": "bearish", "🟡双向": "mixed",
    "🟡中性": "neutral", "🟡短期因素": "neutral",
    "🟡中性偏空": "slightly_bearish",
    "🟢结构性利多": "bullish",
    "🟢中长期结构性利多": "bullish",
    # 已标准（幂等）
    "bullish": "bullish", "bearish": "bearish",
    "neutral": "neutral", "mixed": "mixed",
    "slightly_bullish": "slightly_bullish",
    "slightly_bearish": "slightly_bearish",
}

ALLOWED_IMPACTS = {"bullish", "bearish", "mixed", "neutral",
                   "slightly_bullish", "slightly_bearish"}


def normalize_ts(ts_str: str) -> str:
    ts_str = ts_str.strip().strip('"')
    if not ts_str:
        return ts_str
    if "+08:00" in ts_str:
        return ts_str
    try:
        if ts_str.endswith("Z"):
            dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
            return dt.astimezone(TZ_BEIJING).isoformat()
        dt = datetime.fromisoformat(ts_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=TZ_BEIJING)
        return dt.astimezone(TZ_BEIJING).isoformat()
    except Exception:
        for fmt in ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M"]:
            try:
                return datetime.strptime(ts_str, fmt).replace(tzinfo=TZ_BEIJING).isoformat()
            except ValueError:
                continue
    return ts_str


def normalize_impact(imp: str) -> str:
    imp = imp.strip().strip('"')
    mapped = IMPACT_MAP.get(imp)
    if mapped is not None:
        return mapped
    # 未在映射表内的值：如果已是标准值则原样返回，否则强制收敛为 neutral 并警告
    if imp in ALLOWED_IMPACTS:
        return imp
    print(f"[警告] 未知 impact 值 '{imp}'，已收敛为 'neutral'", file=__import__('sys').stderr)
    return "neutral"


def normalize_content(text: str) -> str:
    lines = text.splitlines()
    out = []
    for line in lines:
        stripped = line.strip()
        indent = line[: len(line) - len(stripped)]

        if stripped.startswith("timestamp:") and ":" in stripped:
            _, val = stripped.split(":", 1)
            line = f'{indent}timestamp: "{normalize_ts(val)}"'

        elif stripped.startswith("impact:") and ":" in stripped:
            _, val = stripped.split(":", 1)
            line = f'{indent}impact: "{normalize_impact(val)}"'

        out.append(line)
    return "\n".join(out)


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    normalized = normalize_content(original)
    if normalized == original:
        return False
    path.with_suffix(path.suffix + ".bak").write_text(original, encoding="utf-8")
    path.write_text(normalized, encoding="utf-8")
    return True


def process_dir(d: Path):
    if not d.exists():
        return 0
    count = 0
    for f in sorted(d.iterdir()):
        if f.is_dir():
            count += process_dir(f)
        elif f.suffix in (".yaml", ".yml") and not f.name.endswith(".bak"):
            if process_file(f):
                print(f"[已修复] {f.relative_to(ROOT)}")
                count += 1
    return count


def main():
    total = 0
    for sub in ["logs", "archive"]:
        total += process_dir(ROOT / sub)
    print(f"\n[完成] 标准化 {total} 个文件")
    if total:
        print("       备份文件已保存为 .bak（验证后可删除）")


if __name__ == "__main__":
    main()
