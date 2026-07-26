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

IMPACT_MAP = {
    "看涨": "bullish", "看跌": "bearish",
    "利多": "bullish", "利空": "bearish",
    "中性": "neutral", "双向": "mixed",
    "中性偏多": "slightly_bullish", "中性偏空": "slightly_bearish",
    "中性偏谨慎": "neutral_cautious",
    "技术利多": "technical_bullish", "强力利多": "strong_bullish",
    "看涨（已定价）": "bullish_priced_in",
    "看涨（中期）": "bullish_medium",
    "边际利多": "marginally_bullish",
    "🟢利多": "bullish", "🔴利空": "bearish", "🟡双向": "mixed",
    "🟡中性": "neutral", "🟡短期因素": "neutral",
    "🟡中性偏空": "slightly_bearish",
    "🟢结构性利多": "bullish",
    "🟢中长期结构性利多": "bullish",
    "bullish": "bullish", "bearish": "bearish",
    "neutral": "neutral", "mixed": "mixed",
    "slightly_bullish": "slightly_bullish",
    "slightly_bearish": "slightly_bearish",
}


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
    return IMPACT_MAP.get(imp, imp)


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
