#!/usr/bin/env python3
"""vision see.py — 让无视觉主模型通过 Google Vertex AI Gemini 看图。

用法:
    see.py <image_path_or_url> "<question>"
环境:
    GOOGLE_API_KEY / GOOGLE_CLOUD_PROJECT  必填（复用 gen-image-game 同一套）
    VISION_MODEL     默认 gemini-2.5-flash
    VISION_LOCATION  默认 global
纯标准库实现（urllib + base64），无第三方依赖。
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

DEFAULT_MODEL = "gemini-2.5-flash"


def die(msg, code=1):
    print(f"[vision] {msg}", file=sys.stderr)
    sys.exit(code)


def load_b64(path):
    raw = Path(path).read_bytes()
    if raw[:8] == b"\x89PNG\r\n\x1a\n" or raw[:2] == b"\xff\xd8" or raw[:4] == b"GIF8":
        return base64.b64encode(raw).decode("ascii")
    try:
        import io
        from PIL import Image
        buf = io.BytesIO()
        Image.open(path).convert("RGB").save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode("ascii")
    except Exception:
        die(f"无法编码图片 {path}（无 pillow 且非常见格式）")


def main():
    ap = argparse.ArgumentParser(description="让无视觉模型通过 Gemini 看图")
    ap.add_argument("image", help="本地图片路径或 http(s) URL")
    ap.add_argument("question", nargs="?", default="描述这张图片的内容", help="要问的问题")
    args = ap.parse_args()

    api_key = os.environ.get("GOOGLE_API_KEY", "")
    project = os.environ.get("GOOGLE_CLOUD_PROJECT", "")
    model = os.environ.get("VISION_MODEL", DEFAULT_MODEL)
    location = os.environ.get("VISION_LOCATION", "global")
    if not api_key or not project:
        die("缺少 GOOGLE_API_KEY / GOOGLE_CLOUD_PROJECT（export 后重试）")

    if args.image.startswith(("http://", "https://")):
        try:
            data = urllib.request.urlopen(args.image, timeout=60).read()
        except urllib.error.URLError as e:
            die(f"下载图片失败: {e.reason}")
        mime = "image/png"
    else:
        p = Path(args.image)
        if not p.exists():
            die(f"文件不存在: {p}")
        data = load_b64(p)
        mime = "image/png"

    url = (
        f"https://aiplatform.googleapis.com/v1/projects/{project}"
        f"/locations/{location}/publishers/google/models/{model}"
        f":generateContent?key={api_key}"
    )
    payload = {
        "contents": [{
            "role": "user",
            "parts": [
                {"text": args.question},
                {"inlineData": {"mimeType": mime, "data": data}},
            ],
        }],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 4096},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", "replace")[:800]
        die(f"API {e.code}: {err}")
    except urllib.error.URLError as e:
        die(f"网络错误: {e.reason}")

    try:
        parts = body["candidates"][0]["content"]["parts"]
        text = "\n".join(p.get("text", "") for p in parts).strip()
    except (KeyError, IndexError, TypeError):
        die(f"无法解析模型响应: {json.dumps(body, ensure_ascii=False)[:800]}")

    if not text:
        die("模型返回空文本")
    print(text)


if __name__ == "__main__":
    main()