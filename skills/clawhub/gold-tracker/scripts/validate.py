#!/usr/bin/env python3
"""
黄金追踪 - 项目验证器
检查数据完整性、格式一致性和常见问题。
零第三方依赖。
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

errors = []
warnings = []


def err(msg):
    errors.append(msg)
    print(f"[错误] {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"[警告] {msg}")


def check_state():
    f = ROOT / "state.json"
    if not f.exists():
        err("state.json 不存在")
        return
    try:
        data = json.loads(f.read_text())
    except Exception as e:
        err(f"state.json JSON 格式错误: {e}")
        return

    for field in ["date", "current_price", "last_update"]:
        if field not in data:
            err(f"state.json 缺少字段: {field}")

    price = data.get("current_price")
    if price is not None and isinstance(price, (int, float)):
        if not (1000 <= price <= 10000):
            err(f"state.json 金价超出合理范围: ${price}")
    elif price is not None:
        err(f"state.json current_price 不是数字: {type(price).__name__}")

    if isinstance(data.get("change_pct"), str):
        err("state.json change_pct 是字符串，应为数字")


def check_logs():
    d = ROOT / "logs"
    if not d.exists():
        warn("logs/ 目录不存在（新安装时正常）")
        return

    for f in sorted(d.iterdir()):
        if f.suffix not in (".yaml", ".yml"):
            continue
        text = f.read_text(encoding="utf-8")

        if "run_id:" not in text:
            err(f"{f.name}: 缺少 run_id")
        if "price_usd:" not in text:
            err(f"{f.name}: 缺少 price_usd")

        ts_match = re.search(r'timestamp:\s*"?([^"\n]+)"?', text)
        if ts_match and "+08:00" not in ts_match.group(1) and "Z" not in ts_match.group(1):
            warn(f"{f.name}: 时间戳可能缺少时区")

        impacts = re.findall(r'impact:\s*"?([^"\n]+)"?', text)
        for imp in impacts:
            imp = imp.strip()
            if imp in ("看涨", "看跌", "利多", "利空", "🟢利多", "🔴利空"):
                warn(f"{f.name}: impact 未标准化: '{imp}'")


def check_alerts():
    d = ROOT / "alerts"
    if not d.exists():
        return

    for f in sorted(d.iterdir()):
        if f.suffix not in (".md", ".json"):
            continue

        if f.suffix == ".md":
            text = f.read_text(encoding="utf-8")
            timestamps = re.findall(r'##\s*\[(\d{2}:\d{2})\]', text)
            seen = set()
            for ts in timestamps:
                if ts in seen:
                    err(f"{f.name}: 存在重复提醒 [{ts}]")
                seen.add(ts)

        if f.suffix == ".json":
            try:
                data = json.loads(f.read_text())
                if not isinstance(data, list):
                    err(f"{f.name}: JSON 格式错误，应为数组")
                    continue

                seen_ids = set()
                for alert in data:
                    alert_id = alert.get("alert_id")
                    if alert_id:
                        if alert_id in seen_ids:
                            err(f"{f.name}: 存在重复 alert_id: {alert_id}")
                        seen_ids.add(alert_id)

                    required_fields = ["alert_id", "type", "price", "change_pct", "threshold_pct", "benchmark", "message", "status", "created_at"]
                    for field in required_fields:
                        if field not in alert:
                            warn(f"{f.name}: 缺少字段: {field}")

                    status = alert.get("status")
                    if status and status not in ["pending", "sent", "acknowledged", "resolved", "dismissed"]:
                        warn(f"{f.name}: 无效状态: {status}")

            except Exception as e:
                err(f"{f.name}: JSON 解析错误: {e}")


def check_archive():
    d = ROOT / "archive"
    if not d.exists():
        return

    for month in sorted(d.iterdir()):
        if not month.is_dir():
            continue
        for f in sorted(month.iterdir()):
            if f.suffix not in (".yaml", ".yml"):
                continue
            text = f.read_text(encoding="utf-8")
            runs = [r for r in text.split("---") if r.strip()]
            if len(runs) > 1:
                warn(f"{month.name}/{f.name}: 包含 {len(runs)} 个 run（建议拆分）")


def main():
    print("=" * 56)
    print("黄金追踪项目验证器")
    print("=" * 56)

    check_state()
    check_logs()
    check_alerts()
    check_archive()

    print()
    print("=" * 56)
    print(f"结果: {len(errors)} 个错误, {len(warnings)} 个警告")
    print("=" * 56)

    if errors:
        sys.exit(1)
    print("[通过] 所有关键检查通过")


if __name__ == "__main__":
    main()
