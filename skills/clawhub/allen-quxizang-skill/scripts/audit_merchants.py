#!/usr/bin/env python3
"""
Copyright (c) 2026 Allen. MIT License.
"""
"""
audit_merchants.py — 商户数据完整性审计
输出每缺哪些字段 + 汇总统计
"""
import json
import sys
from pathlib import Path

REQUIRED = ["id", "name", "category", "altitude", "location", "why_recommend",
            "opening_hours", "price_level", "must_try", "tags"]
RECOMMENDED = ["phone", "wechat", "verified_at", "warning", "note"]

SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = SKILL_ROOT / "data" / "local_merchants.json"

def main():
    raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    merchants = raw if isinstance(raw, list) else raw.get("merchants", [])

    print(f"\n  商户数据完整性审计")

    if isinstance(raw, dict):
        sv = raw.get("schema_version", "?")
        up = raw.get("updated", "?")
        agree = raw.get("total_merchants", "?")
        print(f"  schema: v{sv} | 更新: {up} | 文件声明: {agree} 家")

    print(f"  {'=' * 60}")
    print(f"  总商户数: {len(merchants)}")
    print(f"  必填字段: {', '.join(REQUIRED)}")
    print(f"  建议字段: {', '.join(RECOMMENDED)}")
    print()

    missing_phone = []
    missing_wechat = []
    missing_verified = []
    missing_note = []
    missing_warning = []
    all_ok = True

    for m in merchants:
        rid = m.get("id", "??")
        name = m.get("name", "??")
        issues = []

        for field in REQUIRED:
            if field not in m or m[field] in (None, "", []):
                issues.append(f"缺必填 [{field}]")

        has_phone = "phone" in m and m["phone"]
        has_wechat = "wechat" in m and m["wechat"]
        has_verified = "verified_at" in m and m["verified_at"]
        if not has_phone:
            missing_phone.append(name)
        if not has_wechat:
            missing_wechat.append(name)
        if not has_verified:
            missing_verified.append(name)

        if issues or not has_phone or not has_wechat or not has_verified:
            all_ok = False
            bits = issues[:]
            if not has_phone:
                bits.append("phone 为空")
            if not has_wechat:
                bits.append("wechat 为空")
            if not has_verified:
                bits.append("verified_at 为空")
            print(f"  ⚠️  {name:30s} | {'; '.join(bits)}")

    if all_ok:
        print(f"  ✅ 全部商户字段完整\n")

    print(f"  {'=' * 60}")
    print(f"  统计:")
    phones = len(merchants) - len(missing_phone)
    wechats = len(merchants) - len(missing_wechat)
    verified = len(merchants) - len(missing_verified)
    print(f"    有 phone 字段:     {phones}/{len(merchants)}")
    print(f"    有 wechat 字段:    {wechats}/{len(merchants)}")
    print(f"    有 verified_at:    {verified}/{len(merchants)}")

    coverage = (phones + wechats + verified) / (len(merchants) * 3) * 100
    print(f"    联系方式覆盖率:    {coverage:.0f}%")
    print()

    if not all_ok:
        print(f"  ⚠️  建议: 找到原商户主核实 phone/wechat + 填入 verified_at")
        print(f"     之后运行 python3 scripts/audit_merchants.py 确认清零\n")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
