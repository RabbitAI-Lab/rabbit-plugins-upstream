#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""release_gate.py — 发版节奏闸门（24 小时纪律的机制层执行）。

任何 skill 发布新版本前必须先过本闸门：
    python3 release_gate.py --slug cite-holmes
    python3 release_gate.py --slug cite-holmes --platform skillhub
    python3 release_gate.py --slug cite-holmes --override "紧急安全修复"   # 需书面理由

通过后、发布成功后，登记台账（供下次闸门判定）：
    python3 release_gate.py --record --slug cite-holmes --version 1.4.0 --platform clawhub

判定来源（任一命中即拒绝）：
  1. 本地台账 ~/.release_ledger.json（发布成功后由 --record 写入）
  2. ClawHub 实时 API latestVersion.createdAt（台账缺失/被清时的兜底）
同一 slug 24 小时内只允许一次新版本（默认）。绕过必须写 --override 理由，
理由会连同时间戳一起记入台账。
"""
import argparse
import datetime
import json
import os
import sys
import urllib.request

LEDGER = os.path.expanduser("~/.release_ledger.json")
CLAWHUB = "https://wry-manatee-359.convex.site/api/v1/skills/{slug}"
TZ = datetime.timezone(datetime.timedelta(hours=8))


def now() -> datetime.datetime:
    return datetime.datetime.now(TZ)


def parse_iso(s: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(s)


def load_ledger() -> dict:
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def save_ledger(d: dict) -> None:
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)


def clawhub_latest_iso(slug: str):
    try:
        with urllib.request.urlopen(f"{CLAWHUB.format(slug=slug)}?cb={int(now().timestamp())}",
                                    timeout=15) as r:
            d = json.load(r)
        lv = d.get("latestVersion") or {}
        ms = lv.get("createdAt")
        if ms:
            return datetime.datetime.fromtimestamp(ms / 1000, TZ), lv.get("version")
    except Exception as e:
        print(f"  [gate] ClawHub 查询不可用（{type(e).__name__}），跳过该来源", file=sys.stderr)
    return None, None


def main() -> int:
    ap = argparse.ArgumentParser(description="24h 发版纪律闸门")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--platform", default="all",
                    help="限定检查某平台（clawhub/skillhub）；默认 all")
    ap.add_argument("--min-hours", type=float, default=24.0)
    ap.add_argument("--override", default=None,
                    help="书面理由：紧急情况绕过 24h 纪律（理由入台账）")
    ap.add_argument("--record", action="store_true",
                    help="发布成功后登记台账（--version/--platform 必填）")
    ap.add_argument("--version", default=None)
    args = ap.parse_args()

    ledger = load_ledger()
    entries = ledger.get(args.slug, [])
    now_dt = now()
    cutoff = datetime.timedelta(hours=args.min_hours)

    if args.record:
        if not args.version:
            ap.error("--record 需要 --version")
        entries.append({"version": args.version, "platform": args.platform,
                        "at": now_dt.isoformat(), "override": args.override})
        ledger[args.slug] = entries
        save_ledger(ledger)
        print(f"[gate] 已登记 {args.slug} {args.version} @ {args.platform}")
        return 0

    blockers = []

    # 来源 1：台账
    for e in entries[-5:]:
        t = parse_iso(e["at"])
        dt_h = (now_dt - t).total_seconds() / 3600
        if dt_h < args.min_hours:
            blockers.append(("ledger", e["version"], e["platform"], t, dt_h))

    # 来源 2：ClawHub 实时
    iso, ver = clawhub_latest_iso(args.slug)
    if iso:
        dt_h = (now_dt - iso).total_seconds() / 3600
        if dt_h < args.min_hours:
            blockers.append(("clawhub", ver or "?", "clawhub", iso, dt_h))

    if not blockers:
        print(f"[gate] PASS：{args.slug} 最近 {args.min_hours:g}h 内无发版记录，允许发布。")
        return 0

    print(f"[gate] BLOCKED：{args.slug} 在最近 {args.min_hours:g} 小时内已有发版，"
          f"24h 纪律不允许再次发布。", file=sys.stderr)
    for src, ver, plat, t, dt_h in blockers:
        print(f"  - {src}: v{ver} @ {plat}，{t.strftime('%m-%d %H:%M')} "
              f"（{dt_h:.1f}h 前）", file=sys.stderr)
    nxt = max((t for _, _, _, t, _ in blockers)) + cutoff
    print(f"[gate] 最早可发时间：{nxt.strftime('%m-%d %H:%M')} +08:00", file=sys.stderr)
    if args.override:
        print(f"[gate] --override 生效（理由：{args.override}），放行——本次绕过将记入台账。",
              file=sys.stderr)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
