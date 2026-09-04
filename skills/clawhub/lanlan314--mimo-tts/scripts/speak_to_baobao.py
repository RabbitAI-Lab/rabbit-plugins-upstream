#!/usr/bin/env python3
"""
MiMo V2.5 TTS — 语音合成并发送到飞书
用法: python3 speak_to_baobao.py "要说的文字" [音色]

默认音色: 苏打 (中文)
中文用苏打，英文用Milo
"""

import os, sys, json, base64, subprocess

API_KEY = os.environ.get("MIMO_API_KEY", "")

TEXT = sys.argv[1] if len(sys.argv) > 1 else ""
VOICE = sys.argv[2] if len(sys.argv) > 2 else "苏打"

if not TEXT:
    TEXT = "你好，欢迎使用 MiMo 语音合成。"

payload = json.dumps({
    "model": "mimo-v2.5-tts",
    "messages": [
        {"role": "user", "content": "日常自然对话语气，语速适中，亲切自然"},
        {"role": "assistant", "content": TEXT}
    ],
    "audio": {"format": "wav", "voice": VOICE}
}, ensure_ascii=False)

proc = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://api.xiaomimimo.com/v1/chat/completions",
     "-H", f"api-key: {API_KEY}",
     "-H", "Content-Type: application/json",
     "-d", payload],
    capture_output=True, text=True, timeout=30
)

result = json.loads(proc.stdout)
if "error" in result:
    print(f"Error: {result['error']}")
    sys.exit(1)

audio_data = result["choices"][0]["message"]["audio"]["data"]
audio_bytes = base64.b64decode(audio_data)

os.makedirs("/tmp/mimo_tts", exist_ok=True)
wav_path = "/tmp/mimo_tts/voice.wav"
with open(wav_path, "wb") as f:
    f.write(audio_bytes)

ogg_path = "/tmp/mimo_tts/voice.ogg"
subprocess.run(
    ["ffmpeg", "-y", "-i", wav_path, "-c:a", "libopus", "-b:a", "64k", "-ar", "48000", ogg_path],
    capture_output=True
)

# Upload & send — lark-cli --file 只支持相对路径，必须在 /tmp 下操作
subprocess.run(["cp", ogg_path, "/tmp/speak.ogg"], capture_output=True)
upl = subprocess.run(
    ["lark-cli", "api", "POST", "/open-apis/im/v1/files",
     "--file", "file=speak.ogg",
     "--data", '{"file_type":"opus","file_name":"speak.ogg"}'],
    capture_output=True, text=True, cwd="/tmp"
)

upl_data = json.loads(upl.stdout) if upl.stdout else {}
file_key = upl_data.get("data", {}).get("file_key", "")

if file_key:
    send = subprocess.run(
        ["lark-cli", "im", "+messages-send",
         "--user-id", os.environ.get("FEISHU_USER_OPEN_ID", ""),
         "--msg-type", "audio",
         "--content", json.dumps({"file_key": file_key})],
        capture_output=True, text=True
    )
    send_data = json.loads(send.stdout) if send.stdout else {}
    if send_data.get("ok"):
        print("ok")
    else:
        print(f"send fail: {send.stdout[:100]}")
else:
    print(f"upload fail: {upl.stdout[:200]}")
