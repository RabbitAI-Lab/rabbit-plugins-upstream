#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
push_webhook.py — 云端推送（「盘前雷达」输出层 · GitHub Actions 主轨）

直接 POST 飞书群机器人 webhook，不依赖本机 notify-hub 配置，适合在
GitHub Actions 等云端环境运行（电脑关机也照常推）。

环境变量：
  FEISHU_WEBHOOK  必填，飞书群机器人 webhook 完整 URL
  FEISHU_SECRET   可选，机器人「加签」密钥（若机器人开了签名校验则必填）

用法：
  python3 push_webhook.py            # 采集 + 打分 + 推送到飞书群

设计原则：
  1. 纯标准库，零第三方依赖（云端 runner 上 python3 直接可跑）。
  2. 支持飞书加签（timestamp + HMAC-SHA256 + base64）。
  3. 周末自动跳过（GitHub cron 已限周一~五，此处兜底 workflow_dispatch 手动触发）。
  4. 消息用飞书 post 富文本（带标题栏），信息密度高、可读性好。
"""

import base64
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone

import score_and_report

TZ = timezone(timedelta(hours=8))
UA = "Mozilla/5.0 (GitHub-Actions) WorkBuddy/panqian-radar"


def gen_sign(secret):
    """飞书自定义机器人加签：sign = base64(HMAC-SHA256(key=ts+'\n'+secret, msg=''))。"""
    ts = str(int(time.time()))
    string_to_sign = "{}\n{}".format(ts, secret)
    digest = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    return ts, base64.b64encode(digest).decode("utf-8")


def build_post(report):
    """由报告 dict 构造飞书 post 富文本 content。"""
    cm = report["card_market"]
    sc = report["scenario"]

    lines = [
        [{"tag": "text",
          "text": "方向：{} ｜ 风险 {}/5（{}）".format(
              report["verdict"], report["risk_level"], report["risk_text"])}],
        [{"tag": "text",
          "text": "多空：偏多 {}% / 偏空 {}%".format(sc["bull_pct"], sc["bear_pct"])}],
        [{"tag": "text", "text": "理由：{}".format(report["reason"])}],
        [{"tag": "text",
          "text": "外围指标：A50 {} ｜ 离岸人民币 {} ｜ 纳指期货 {} ｜ 标普期货 {}".format(
              cm["a50"]["text"], cm["cny"]["text"],
              cm["nasdaq_fut"]["text"], cm["spx_fut"]["text"])}],
        [{"tag": "text",
          "text": "美元指数 {} ｜ VIX {} ｜ 美债10Y {}".format(
              cm["dxy"]["text"], cm["vix"]["text"], cm["ust10y"]["text"])}],
        [{"tag": "text", "text": "宏观：{}".format(report["macro"]["brief"])}],
    ]

    funds = report.get("funds_summary") or {}
    if funds:
        ftext = " ｜ ".join("{} {}".format(k, v) for k, v in funds.items())
        lines.append([{"tag": "text", "text": "资金面：{}".format(ftext)}])

    if report.get("geo_level") != "低":
        lines.append([{"tag": "text", "text": "地缘：{}".format(report["geo_note"])}])

    lines.append([{"tag": "text",
                   "text": "本信号由「盘前雷达」skill 每日自动生成 · 仅供研究，不构成投资建议"}])

    return {
        "title": "盘前雷达 {} {}".format(report["date"], report["weekday"]),
        "content": lines,
    }


def post_feishu(webhook, payload):
    """POST 到飞书 webhook，返回响应 dict。"""
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        webhook, data=data,
        headers={"Content-Type": "application/json", "User-Agent": UA},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        body = resp.read().decode("utf-8", "ignore")
    try:
        return json.loads(body)
    except ValueError:
        return {"raw": body}


def main():
    webhook = os.environ.get("FEISHU_WEBHOOK", "").strip()
    secret = os.environ.get("FEISHU_SECRET", "").strip()
    if not webhook:
        print("[错误] 缺少环境变量 FEISHU_WEBHOOK，无法推送")
        sys.exit(1)

    # 周末跳过（GitHub cron 已限周一~五，此处兜底手动触发）
    now = datetime.now(TZ)
    if now.weekday() >= 5:
        print(f"[跳过] 今天是 {now.strftime('%A')}，A 股休市，不推送")
        sys.exit(0)

    report = score_and_report.collect()
    payload = {
        "msg_type": "post",
        "content": {"post": {"zh_cn": build_post(report)}},
    }
    if secret:
        ts, sign = gen_sign(secret)
        payload["timestamp"] = ts
        payload["sign"] = sign

    resp = post_feishu(webhook, payload)
    code = resp.get("code")
    if code == 0:
        print(f"[成功] 飞书推送成功 ｜ {payload['content']['post']['zh_cn']['title']} "
              f"｜ 方向 {report['verdict']} / 风险 {report['risk_level']}/5")
        sys.exit(0)
    else:
        print(f"[失败] 飞书返回: {json.dumps(resp, ensure_ascii=False)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
