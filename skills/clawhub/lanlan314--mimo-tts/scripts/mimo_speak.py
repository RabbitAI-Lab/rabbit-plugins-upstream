#!/usr/bin/env python3
"""
MiMo V2.5 TTS — 语音合成并发送到飞书

用法:
    python3 mimo_speak.py "要合成的文字" [音色]

默认音色: 冰糖 (中文女声)
支持的预设音色:
  - 冰糖 (中文女声) ★ 推荐
  - 茉莉 (中文女声)
  - 苏打 (中文男声)
  - 白桦 (中文男声)
  - Mia (英文女声)
  - Chloe (英文女声)
  - Milo (英文男声)
  - Dean (英文男声)

环境变量:
  MIMO_API_KEY — MiMo API 密钥 (必需)
"""

import os
import sys
import base64
import json
import subprocess

# ============ 配置 ============
API_KEY = os.environ.get("MIMO_API_KEY", "")

TEXT = sys.argv[1] if len(sys.argv) > 1 else ""
if not TEXT:
    print('{"error": "请提供要合成的文字"}')
    sys.exit(1)

VOICE = sys.argv[2] if len(sys.argv) > 2 else "冰糖"

# ============ TTS 合成 ============
payload = json.dumps({
    "model": "mimo-v2.5-tts",
    "messages": [
        {"role": "user", "content": "日常自然对话语气，语速适中，亲切自然"},
        {"role": "assistant", "content": TEXT}
    ],
    "audio": {"format": "wav", "voice": VOICE}
}, ensure_ascii=False)

print(json.dumps({"status": "synthesizing", "text": TEXT, "voice": VOICE}))

try:
    proc = subprocess.run(
        ["curl", "-s", "-X", "POST", "https://api.xiaomimimo.com/v1/chat/completions",
         "-H", f"api-key: {API_KEY}",
         "-H", "Content-Type: application/json",
         "-d", payload],
        capture_output=True, text=True, timeout=30
    )
    
    result = json.loads(proc.stdout)
    if "error" in result:
        print(json.dumps({"error": str(result["error"])}))
        sys.exit(1)
    
    audio_data = result["choices"][0]["message"]["audio"]["data"]
    audio_bytes = base64.b64decode(audio_data)

    os.makedirs("/tmp/mimo_tts", exist_ok=True)
    wav_path = "/tmp/mimo_tts/output.wav"
    with open(wav_path, "wb") as f:
        f.write(audio_bytes)

    print(json.dumps({"status": "done", "wav_path": wav_path}))

except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
