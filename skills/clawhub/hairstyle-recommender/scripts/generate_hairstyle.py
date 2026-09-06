#!/usr/bin/env python3
"""
RunComfy 发型替换脚本

前置条件:
  1. 在 RunComfy (https://www.runcomfy.com) 注册账号并获取 API Token
  2. 设置环境变量: export RUNCOMFY_TOKEN="你的token"

用法:
  python3 generate_hairstyle.py <图片路径> <输出路径> [提示词]

示例:
  python3 generate_hairstyle.py ~/photo.png ~/Desktop/效果图.png \
    "Mid Fade + 碎盖头，刘海遮住额头"
"""
import base64
import json
import os
import sys
import time
import urllib.request

BASE_URL = "https://model-api.runcomfy.net"

def get_token():
    token = os.environ.get("RUNCOMFY_TOKEN")
    if not token:
        print("❌ 错误: 未设置 RUNCOMFY_TOKEN 环境变量")
        print("   请先在 https://www.runcomfy.com 注册并获取 API Token")
        print("   然后执行: export RUNCOMFY_TOKEN='你的token'")
        sys.exit(1)
    return token

def read_image_as_dataurl(path):
    with open(path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:image/png;base64,{b64}"

def submit_request(token, model_id, payload):
    url = f"{BASE_URL}/v1/models/{model_id}"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))

def poll_status(token, request_id, max_wait=180):
    url = f"{BASE_URL}/v1/requests/{request_id}/status"
    headers = {"Authorization": f"Bearer {token}"}
    start = time.time()
    while time.time() - start < max_wait:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        status = data.get("status", "unknown")
        print(f"  [{int(time.time()-start)}s] Status: {status}", flush=True)
        if status in ("completed", "success"):
            return data
        if status in ("failed", "error"):
            print(f"  ❌ 失败: {data}", flush=True)
            return None
        time.sleep(5)
    print("  ⏱ 超时等待", flush=True)
    return None

def get_result(token, request_id):
    url = f"{BASE_URL}/v1/requests/{request_id}/result"
    headers = {"Authorization": f"Bearer {token}"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def download_image(url, output_path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        with open(output_path, "wb") as f:
            f.write(resp.read())
    print(f"✅ 已保存: {output_path}")

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2]
    custom_prompt = sys.argv[3] if len(sys.argv) > 3 else None

    if not os.path.exists(image_path):
        print(f"❌ 图片不存在: {image_path}")
        sys.exit(1)

    token = get_token()
    print(f"📸 读取图片: {image_path}")
    data_url = read_image_as_dataurl(image_path)

    # 默认提示词
    default_prompt = (
        "Change only the hairstyle. "
        "The person now has a Mid Fade haircut with 6-8cm textured fringe "
        "on top naturally covering the forehead. "
        "The hair on the sides is very short with a smooth gradient fade. "
        "Keep the face, glasses, beard, skin tone, expression, clothing, and background "
        "exactly as they are. Only the hair changes."
    )
    prompt = custom_prompt if custom_prompt else default_prompt

    model_id = "google/nano-banana-2/edit"
    payload = {
        "prompt": prompt,
        "image_urls": [data_url],
    }

    print(f"\n🚀 提交到 {model_id}...")
    resp = submit_request(token, model_id, payload)
    request_id = resp["request_id"]
    print(f"   Request ID: {request_id}")

    print("\n⏳ 等待生成...")
    status = poll_status(token, request_id)
    if status is None:
        sys.exit(1)

    print("\n📥 获取结果...")
    result = get_result(token, request_id)

    # 提取图片 URL
    image_url = None
    if "output" in result:
        if "image_url" in result["output"]:
            image_url = result["output"]["image_url"]
        elif "images" in result["output"] and result["output"]["images"]:
            image_url = result["output"]["images"][0]

    if image_url:
        print(f"\n🎨 下载图片...")
        download_image(image_url, output_path)
    else:
        print(f"\n⚠️ 未找到图片 URL: {json.dumps(result, indent=2)}")

if __name__ == "__main__":
    main()
