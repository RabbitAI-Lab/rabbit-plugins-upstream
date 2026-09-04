#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Google Gemini 文生图 (free-media-gen)，走 OpenAI 兼容端点 + VPN 可达性门控。

重要实测结论（2026-08-28）：
  - 原生端点 /v1beta/models/{m}:generateContent 对本项目使用的 key 返回
    401 API_KEY_SERVICE_BLOCKED —— 该 key 只能访问 **OpenAI 兼容层**。
  - 因此本脚本改走 /v1beta/openai/chat/completions，正文带
    "modalities": ["image","text"] 请求图像输出。
  - 免费配额提示：gemini-3.1-flash-image 的 free_tier_requests 限额实测为 0，
    免费层通常无法调用（返回 429 RESOURCE_EXHAUSTED, limit: 0）。
    若用户已在 Google 开通付费/配额，本脚本仍可正常工作。

门控语义：只要 Google 域名有 HTTP 响应（含 401/403/429）即视为“可达”，
只有连接失败/超时才算不可达（此前误判 HTTPError 为不可达，已修正）。

用法:
  python gemini_image.py --prompt "一只在月球上散步的猫" [--model gemini-3.1-flash-image-preview] [--out DIR]
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as C  # noqa: E402

OPENAI_CHAT = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
PROBE = "https://generativelanguage.googleapis.com/v1beta/openai/models"


def reachable(url, headers, timeout=15):
    """只要服务器有 HTTP 响应（含 401/403/429）即为可达；仅连接失败才算不可达。"""
    try:
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return True, r.getcode()
    except urllib.error.HTTPError as e:
        return True, e.code
    except Exception:
        return False, 0


def collect_images(body):
    """从多种可能的响应结构中提取图像（data URI / URL / base64）。"""
    found = []  # list of ("b64", data) or ("url", url)

    def add_b64(s):
        found.append(("b64", s))

    def add_url(u):
        found.append(("url", u))

    def scan_images_node(node):
        # OpenAI 兼容形态：message.images[] = [{ "image_url": {"url": "data:..."} , "b64_json": ...}]
        if isinstance(node, dict):
            if node.get("b64_json"):
                add_b64(node["b64_json"])
            iu = node.get("image_url")
            if isinstance(iu, dict) and iu.get("url"):
                u = iu["url"]
                if u.startswith("data:") and "," in u:
                    add_b64(u.split(",", 1)[1])
                else:
                    add_url(u)
            elif isinstance(iu, str) and iu:
                if iu.startswith("data:") and "," in iu:
                    add_b64(iu.split(",", 1)[1])
                else:
                    add_url(iu)
            for v in node.values():
                scan_images_node(v)
        elif isinstance(node, list):
            for v in node:
                scan_images_node(v)

    scan_images_node(body)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--model", default="gemini-3.1-flash-image-preview")
    ap.add_argument("--out", default=None)
    ap.add_argument("--max-retries", type=int, default=2)
    args = ap.parse_args()

    entry = C.get_model_entry(args.model)
    if not entry:
        print(json.dumps({"ok": False, "error": "未知模型 id：%s" % args.model},
                         ensure_ascii=False))
        sys.exit(1)

    key = C.resolve_api_key(entry.get("api_key_ref"), entry.get("provider"))
    headers = {"Authorization": "Bearer %s" % key, "Content-Type": "application/json"}

    ok, code = reachable(PROBE, headers)
    if not ok:
        print(json.dumps({
            "ok": False, "error": "vpn_unreachable",
            "note": ("Google 域名连接失败（无 HTTP 响应）。Gemini 在中国大陆受地域封锁，"
                     "请先开启有效 VPN/代理后重试。")
        }, ensure_ascii=False))
        sys.exit(1)

    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": args.prompt}],
        "modalities": ["image", "text"],
    }

    status, body = C.http_json(OPENAI_CHAT, payload, headers, method="POST",
                               retries=args.max_retries, timeout=180)
    if status != 200:
        quota = isinstance(body, str) and "RESOURCE_EXHAUSTED" in body
        print(json.dumps({
            "ok": False, "http": status,
            "error": "免费配额为 0（quota_exhausted）" if quota else body,
            "note": ("该模型免费配额为 0（429 RESOURCE_EXHAUSTED, limit: 0）。"
                     "需在 Google 开通付费或申请配额后方可使用。" if quota else None),
            "raw": str(body)[:600],
        }, ensure_ascii=False))
        sys.exit(1)

    images = collect_images(body)
    if not images:
        print(json.dumps({"ok": False, "http": status,
                          "error": "响应中未包含图像数据",
                          "raw": str(body)[:600]}, ensure_ascii=False))
        sys.exit(1)

    out_dir = args.out or C.resolve()["generated_images_dir"]
    C.ensure_dir(out_dir)

    urls, saved = [], []
    for i, (kind, val) in enumerate(images):
        p = os.path.join(out_dir, C.out_name("gemini_img", "png", i))
        if kind == "b64":
            with open(p, "wb") as f:
                f.write(base64.b64decode(val))
            saved.append(p)
            urls.append("(b64 -> %s)" % p)
        else:
            urls.append(val)
            if C.download(val, p):
                saved.append(p)

    print(json.dumps({"ok": True, "model": args.model, "urls": urls, "saved": saved},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
