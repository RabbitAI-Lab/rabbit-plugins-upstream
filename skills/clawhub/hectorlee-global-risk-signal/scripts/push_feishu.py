#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
push_feishu.py — 信号推送（「盘前雷达」输出层 · 订阅推送）

把 score_and_report 的结果打包成 notify-hub 卡片，推送到飞书群（或其它已配置通道）。
这是「盘前雷达」爆款三件套之一：每日订阅推送。

依赖：notify-hub skill（约 ~/.workbuddy/skills/notify-hub/scripts/notify.py）。
      需先用 notify.py 配置好飞书群 webhook（notify config add feishu 我的群 --url ...）。

用法：
  python3 push_feishu.py                     # 生成卡片 JSON 到 output/，不实际发送
  python3 push_feishu.py --send              # 生成并推送到默认目标（feishu:我的群）
  python3 push_feishu.py --send --to feishu:我的群,email:老板   # 广播多通道

设计原则：
  1. 纯标准库，零第三方依赖（推送复用 notify-hub 的 notify.py）。
  2. 配色遵循 A 股习惯：偏多=红、偏空=绿。
  3. 内容只发结论 + 关键信号 + 宏观底色，不转载新闻全文。
"""

import json
import os
import subprocess
import sys
import time

import score_and_report

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(SCRIPT_DIR, "..", "output")
NOTIFY = os.environ.get(
    "NOTIFY_HUB_SCRIPT",
    os.path.expanduser("~/.workbuddy/skills/notify-hub/scripts/notify.py"),
)
DEFAULT_TARGET = "feishu:我的群"

# 卡片上的外围指标（key -> 中文标签）
METRIC_LABELS = [
    ("a50", "A50期货"),
    ("cny", "离岸人民币"),
    ("nasdaq_fut", "纳指期货"),
    ("spx_fut", "标普期货"),
    ("dxy", "美元指数"),
    ("vix", "VIX恐慌"),
    ("ust10y", "美债10Y"),
]

VERDICT_COLOR = {"偏多": "red", "偏空": "green", "中性": "grey"}


def build_card(report):
    """由报告 dict 构造 notify-hub 卡片 DSL dict。"""
    cm = report["card_market"]
    sc = report["scenario"]
    verdict = report["verdict"]

    rows = [[label, cm[key]["text"]] for key, label in METRIC_LABELS]

    sections = [
        {
            "type": "markdown",
            "content": (
                f"**方向：{verdict}** ｜ 风险 **{report['risk_level']}/5"
                f"（{report['risk_text']}）**\n"
                f"偏多 **{sc['bull_pct']}%** / 偏空 **{sc['bear_pct']}%**"
            ),
        },
        {"type": "markdown", "content": f"**{report['reason']}**"},
        {"type": "table", "headers": ["指标", "数值"], "rows": rows},
        {"type": "markdown", "content": f"**宏观底色**：{report['macro']['brief']}"},
    ]

    # 资金面（可选）
    funds = report.get("funds_summary") or {}
    if funds:
        ftext = "｜".join(f"{k} {v}" for k, v in funds.items())
        sections.append({"type": "markdown", "content": f"**资金面**：{ftext}"})

    # 地缘异动
    if report.get("geo_level") != "低":
        sections.append({"type": "markdown", "content": f"**地缘**：{report['geo_note']}"})

    sections.append({
        "type": "note",
        "content": "本信号由「盘前雷达」skill 每日自动生成 · 仅供研究，不构成投资建议",
    })

    return {
        "kind": "card",
        "title": f"盘前雷达 {report['date']} {report['weekday']}",
        "color": VERDICT_COLOR.get(verdict, "grey"),
        "sections": sections,
    }


def main():
    send = "--send" in sys.argv
    target = DEFAULT_TARGET
    if "--to" in sys.argv:
        i = sys.argv.index("--to")
        if i + 1 < len(sys.argv):
            target = sys.argv[i + 1]

    report = score_and_report.collect()
    card = build_card(report)

    os.makedirs(OUT_DIR, exist_ok=True)
    date = report["date"].replace("-", "")
    json_path = os.path.join(OUT_DIR, f"push_card_{date}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(card, f, ensure_ascii=False, indent=2)

    print(f"卡片已生成: {json_path}")
    print(f"标题: {card['title']} ｜ 颜色: {card['color']} ｜ 区块: {len(card['sections'])}")

    if send:
        if not os.path.exists(NOTIFY):
            print(f"[错误] 未找到 notify-hub 脚本: {NOTIFY}")
            print("请先安装 notify-hub skill，或设置 NOTIFY_HUB_SCRIPT 环境变量。")
            sys.exit(1)
        print(f"推送到: {target}")
        r = subprocess.run(
            [sys.executable, NOTIFY, "send", "card", json_path, "--to", target],
            capture_output=True, text=True,
        )
        print(r.stdout or "")
        if r.stderr:
            print("[stderr]", r.stderr)
        print(f"推送{'成功' if r.returncode == 0 else '失败'}（退出码 {r.returncode}）")
        sys.exit(r.returncode)


if __name__ == "__main__":
    main()
