#!/usr/bin/env python3
"""
一键生成所有 MiMo TTS 音色样例并发送到飞书
用法: python3 gen_all_voices.py
"""

import os, sys, base64, json, subprocess, time

API_KEY = os.environ.get("MIMO_API_KEY", "")

DIR = "/tmp/mimo_tts"
VOICES = [
    ("冰糖", "中文女声"),
    ("茉莉", "中文女声"),
    ("苏打", "中文男声"),
    ("白桦", "中文男声"),
    ("Mia", "英文女声"),
    ("Chloe", "英文女声"),
    ("Milo", "英文男声"),
    ("Dean", "英文男声"),
]

os.makedirs(DIR, exist_ok=True)

for voice, desc in VOICES:
    print(f"\n=== 合成: {voice} ({desc}) ===")
    
    payload = json.dumps({
        "model": "mimo-v2.5-tts",
        "messages": [
            {"role": "user", "content": "日常自然对话语气，语速适中，亲切自然"},
            {"role": "assistant", "content": f"你好，这是{voice}音色的声音示例。"}
        ],
        "audio": {"format": "wav", "voice": voice}
    }, ensure_ascii=False)
    
    # curl 请求
    proc = subprocess.run(
        ["curl", "-s", "-X", "POST", "https://api.xiaomimimo.com/v1/chat/completions",
         "-H", f"api-key: {API_KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True
    )
    
    try:
        result = json.loads(proc.stdout)
        if "error" in result:
            print(f"  ❌ API 错误: {result['error']}")
            continue
        
        audio_data = result["choices"][0]["message"]["audio"]["data"]
        audio_bytes = base64.b64decode(audio_data)
        
        wav_path = f"{DIR}/{voice}.wav"
        with open(wav_path, "wb") as f:
            f.write(audio_bytes)
        
        ogg_path = f"{DIR}/{voice}.ogg"
        subprocess.run(["ffmpeg", "-y", "-i", wav_path, "-c:a", "libopus", "-b:a", "64k", "-ar", "48000", ogg_path],
                       capture_output=True)
        
        # 上传到飞书
        upload = subprocess.run(
            ["lark-cli", "api", "POST", "/open-apis/im/v1/files",
             "--file", f"file={ogg_path}",
             "--data", json.dumps({"file_type": "opus", "file_name": f"{voice}.ogg"})],
            capture_output=True, text=True, cwd="/tmp"
        )
        
        upload_data = json.loads(upload.stdout) if upload.stdout else {}
        if upload_data.get("ok"):
            file_key = upload_data["data"]["file_key"]
            content = json.dumps({"file_key": file_key})
            send = subprocess.run(
                ["lark-cli", "im", "+messages-send",
                 "--user-id", os.environ.get("FEISHU_USER_OPEN_ID", ""),
                 "--msg-type", "audio",
                 "--content", content],
                capture_output=True, text=True
            )
            send_data = json.loads(send.stdout) if send.stdout else {}
            if send_data.get("ok"):
                print(f"  ✅ {voice} 已发送到飞书")
            else:
                print(f"  ⚠️ 发送失败: {send.stdout[:200]}")
        else:
            print(f"  ⚠️ 上传失败: {upload.stdout[:200]}")
        
        time.sleep(0.5)  # 避免限流
        
    except Exception as e:
        print(f"  ❌ {voice}: {e}")
        if 'proc' in dir() and proc.stdout:
            print(f"  Response: {proc.stdout[:300]}")

print("\n✅ 全部音色已发送完毕！请到飞书听一下选择喜欢的音色吧 🌊")
