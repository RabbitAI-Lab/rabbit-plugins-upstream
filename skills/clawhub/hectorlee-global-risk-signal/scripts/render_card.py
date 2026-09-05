#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_card.py — 信号卡渲染（「盘前雷达」输出层）

读模板 + 打分结果，替换全部占位符，生成当天的「盘前雷达」信号卡 HTML。
生成的文件可直接在浏览器打开 / 截图，用于小红书、知乎等平台分享。

设计原则：
  1. 纯标准库，零第三方依赖。
  2. 只做「填值 + 替换占位符」，不改版式（版式在 templates/card.html 里）。
  3. 风险条由本脚本按 risk_level 生成 5 格 HTML。
  4. 二维码后续接入：footer 目前是占位假码，发布后改为真实二维码（skillhub 安装页）。

用法：
  python3 render_card.py                      # 生成到 output/ 目录（文件名带日期）
  python3 render_card.py /path/out.html       # 指定输出路径
"""

import json
import os
import re
import sys
import time

import score_and_report

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(SCRIPT_DIR, "templates", "card.html")
DEFAULT_OUT = os.path.join(SCRIPT_DIR, "..", "output")

# 卡片上的 7 个外围指标 key（对应模板 {{xxx}} 与 {{xxx_cls}}）
CARD_KEYS = ["a50", "cny", "nasdaq_fut", "spx_fut", "dxy", "vix", "ust10y"]


def build_risk_bars(level):
    """生成 5 格风险条 HTML（前 level 格点亮，其余灰）。"""
    parts = []
    for i in range(5):
        cls = "on" if i < level else "off"
        parts.append(f'<div class="rk-bar {cls}"></div>')
    return "".join(parts)


def render(report):
    """读模板 + 填值，返回最终 HTML。"""
    with open(TEMPLATE, encoding="utf-8") as f:
        html = f.read()

    cm = report["card_market"]
    vs = report["verdict_style"]
    sc = report["scenario"]

    mapping = {
        "{{date}}": report["date"],
        "{{weekday}}": report["weekday"],
        "{{verdict}}": report["verdict"],
        "{{reason}}": report["reason"],
        "{{verdict_color}}": vs["color"],
        "{{verdict_box_bg}}": vs["box_bg"],
        "{{verdict_box_border}}": vs["box_border"],
        "{{risk_bars}}": build_risk_bars(report["risk_level"]),
        "{{risk_level}}": str(report["risk_level"]),
        "{{risk_text}}": report["risk_text"],
        "{{geo_risk}}": report["geo_level"],
        "{{geo_note}}": report["geo_note"],
        "{{bull_pct}}": f"{sc['bull_pct']}%",
        "{{bull_text}}": sc["bull_text"],
        "{{bear_pct}}": f"{sc['bear_pct']}%",
        "{{bear_text}}": sc["bear_text"],
    }
    # 7 指标：数值 + 方向 class
    for key in CARD_KEYS:
        mapping["{{" + key + "}}"] = cm[key]["text"]
        mapping["{{" + key + "_cls}}"] = cm[key]["cls"]

    for k, v in mapping.items():
        html = html.replace(k, v)
    return html


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    report = score_and_report.collect()
    html = render(report)

    # 默认输出到 output/ 目录，文件名带日期
    if out_path is None:
        date = report["date"].replace("-", "")
        os.makedirs(DEFAULT_OUT, exist_ok=True)
        out_path = os.path.join(DEFAULT_OUT, f"card_{date}.html")
    out_path = os.path.abspath(out_path)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 残留占位符检查
    leftover = re.findall(r"\{\{[^}]+\}\}", html)
    print(f"已生成信号卡: {out_path}")
    print(f"方向: {report['verdict']} | 风险: {report['risk_level']}/5 {report['risk_text']}")
    print(f"理由: {report['reason']}")
    print(f"多空: 偏多 {report['scenario']['bull_pct']}% / 偏空 {report['scenario']['bear_pct']}%")
    if leftover:
        print(f"[警告] 残留未替换占位符 {len(leftover)} 个: {leftover[:5]}")
    else:
        print("[OK] 全部占位符已替换，无残留")


if __name__ == "__main__":
    main()
