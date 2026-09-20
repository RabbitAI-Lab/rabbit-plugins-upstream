#!/usr/bin/env python3
"""
Image generator using GrusAI API
支持文生图和图生图
支持模型: nano-banana-fast (默认), gpt-image-2
"""

import os
import sys
import re
import json
import argparse
import requests

# Force UTF-8 stdout/stderr so emoji prints don't crash on Windows GBK consoles
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass


def _local_path_to_data_url(path):
    """Read a local image file and convert it to a base64 data URL for the API."""
    import base64
    import mimetypes
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Reference file not found: {path}")
    mime, _ = mimetypes.guess_type(path)
    if mime is None:
        mime = "image/png"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"


# API Base URLs for different models
API_BASE_URLS = {
    "nano-banana": "https://grsaiapi.com/v1/draw/nano-banana",
    "gpt-image-2": "https://grsaiapi.com/v1/draw/completions",
    # aliases
    "nano-banana-fast": "https://grsaiapi.com/v1/draw/nano-banana",
}

def generate_image(prompt, model="nano-banana-fast", aspect_ratio="auto", 
                  image_size="1K", output="output.png", api_key=None, 
                  reference_urls=None, image_prompt=None):
    """Generate image using GrusAI API"""
    
    # Resolve model to endpoint
    model_key = model.lower()
    if model_key not in API_BASE_URLS:
        # Try to find a match
        for known_model in API_BASE_URLS:
            if known_model in model_key or model_key in known_model:
                model_key = known_model
                break
        else:
            print(f"❌ 未知模型: {model}, 使用 nano-banana-fast")
            model_key = "nano-banana-fast"
    
    api_base = API_BASE_URLS[model_key]
    is_gpt_image_2 = (model_key == "gpt-image-2")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": model,
        "prompt": prompt,
        "aspectRatio": aspect_ratio,
        "imageSize": image_size,
        "shutProgress": True
    }
    
    # 如果有参考图URL，添加到payload
    if reference_urls:
        if isinstance(reference_urls, str):
            reference_urls = [reference_urls]
        payload["urls"] = reference_urls
        print(f"🖼️ 参考图数量: {len(reference_urls)}")
        for i, url in enumerate(reference_urls, 1):
            print(f"   [{i}] {url}")
    
    # 如果有图生图的提示词
    if image_prompt:
        print(f"🎯 图生图提示词: {image_prompt}")
    
    print(f"🎨 正在生成图片...")
    print(f"   提示词: {prompt}")
    print(f"   模型: {model}")
    print(f"   端点: {api_base}")
    
    try:
        response = requests.post(api_base, json=payload, headers=headers, timeout=120, stream=True)
        
        image_url = None
        
        # 流式响应，提取JSON
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                
                if is_gpt_image_2:
                    # gpt-image-2 格式: status + results[].url
                    if '"status":"succeeded"' in line_str:
                        results_match = re.search(r'"results":\[(.*?)\]', line_str)
                        if results_match:
                            result_content = results_match.group(1)
                            url_match = re.search(r'"url":"([^"]+)"', result_content)
                            if url_match:
                                image_url = url_match.group(1)
                                print(f"✅ 生成成功!")
                                print(f"   图片URL: {image_url}")
                                break
                    elif '"status":"failed"' in line_str:
                        print(f"❌ 生成失败")
                        fail_match = re.search(r'"failure_reason":"([^"]+)"', line_str)
                        if fail_match:
                            print(f"   原因: {fail_match.group(1)}")
                        return None
                    elif '"status":"running"' in line_str and '"progress"' in line_str:
                        prog_match = re.search(r'"progress":(\d+)', line_str)
                        if prog_match:
                            print(f"   进度: {prog_match.group(1)}%")
                else:
                    # nano-banana 格式: url in line
                    if '"status":"succeeded"' in line_str:
                        url_match = re.search(r'"url":"([^"]+)"', line_str)
                        if url_match:
                            image_url = url_match.group(1)
                            print(f"✅ 生成成功!")
                            print(f"   图片URL: {image_url}")
                            break
                    
                    elif '"status":"failed"' in line_str:
                        print(f"❌ 生成失败")
                        fail_match = re.search(r'"failure_reason":"([^"]+)"', line_str)
                        if fail_match:
                            print(f"   原因: {fail_match.group(1)}")
                        return None
                    
                    elif '"progress"' in line_str:
                        prog_match = re.search(r'"progress":(\d+)', line_str)
                        if prog_match:
                            print(f"   进度: {prog_match.group(1)}%")
        
        # 下载图片
        if image_url:
            img_response = requests.get(image_url, timeout=60)
            if img_response.status_code == 200:
                with open(output, 'wb') as f:
                    f.write(img_response.content)
                print(f"💾 已保存到: {output}")
            else:
                print(f"❌ 下载图片失败: {img_response.status_code}")
            return image_url
        else:
            print(f"⚠️ 未找到结果")
            return None
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate AI images (支持图生图)")
    
    # 位置参数
    parser.add_argument("prompt", help="Image prompt/description (文生图提示词)")
    
    # 可选参数
    parser.add_argument("--model", default="nano-banana-fast", 
                       help="Model name: nano-banana-fast (默认), gpt-image-2")
    parser.add_argument("--aspect-ratio", default="auto", 
                       help="Image aspect ratio: auto, 1:1, 16:9, 9:16, 3:2, 2:3")
    parser.add_argument("--size", default="1K", help="Image size: 1K, 2K, 4K")
    parser.add_argument("--output", default="/root/downloads/output.png", help="Output filename")
    parser.add_argument("--api-key", default=os.environ.get("GRSAI_API_KEY", ""), help="API key")
    
    # 图生图参数
    parser.add_argument("--urls", default="",
                       help="Reference image: HTTP(S) URL, data URL, 或本地文件路径 (自动 base64 编码为 data URL). 逗号分隔多张")
    parser.add_argument("--image-prompt", default="", help="Image-to-image prompt")
    
    args = parser.parse_args()
    
    # 解析参考图: HTTP(S) URL、data URL,或本地文件路径(自动 base64 编码为 data URL)
    reference_urls = None
    if args.urls:
        raw_items = [item.strip() for item in args.urls.split(",") if item.strip()]
        reference_urls = []
        for item in raw_items:
            if item.startswith(("http://", "https://", "data:")):
                reference_urls.append(item)
            else:
                try:
                    data_url = _local_path_to_data_url(item)
                    reference_urls.append(data_url)
                    print(f"   本地文件已编码: {item}")
                except FileNotFoundError as exc:
                    print(f"   跳过缺失文件: {exc}")
    
    generate_image(
        args.prompt,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        image_size=args.size,
        output=args.output,
        api_key=args.api_key,
        reference_urls=reference_urls,
        image_prompt=args.image_prompt
    )
