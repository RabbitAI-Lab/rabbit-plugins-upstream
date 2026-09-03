#!/usr/bin/env python3
"""
TTS 语音生成并发送到飞书
- 优先使用千问 TTS（需配置 DASHSCOPE_API_KEY）
- 备选微软 Edge TTS
- 通过飞书 Bot API 发送语音消息
"""

import sys
import os
import json
import tempfile
import subprocess
import requests

# 创建不使用代理的 session
session = requests.Session()
session.trust_env = False

# ====== 飞书 Bot 配置（从文件读取）======
CREDS_FILE = os.path.expanduser("~/.openclaw/credentials/lark.secrets.json")
CONFIG_FILE = os.path.expanduser("~/.openclaw/openclaw.json")

def get_feishu_config():
    """从配置文件读取飞书 Bot app_id 和 app_secret"""
    try:
        with open(CREDS_FILE) as f:
            creds = json.load(f)
        app_secret = creds.get("lark", {}).get("appSecret", "")
        
        with open(CONFIG_FILE) as f:
            config = json.load(f)
        # 飞书 Bot 配置在 channels.feishu 下
        app_id = config.get("channels", {}).get("feishu", {}).get("appId", "")
        if app_id:
            return app_id, app_secret
        # 兜底：从 auth.profiles 查找
        profiles = config.get("auth", {}).get("profiles", {})
        for key, val in profiles.items():
            app_id = val.get("appId", "")
            if app_id and app_id.startswith("cli_"):
                return app_id, app_secret
        return None, app_secret
    except Exception as e:
        print(f"读取配置文件失败: {e}")
        return None, None

APP_ID, APP_SECRET = get_feishu_config()
USER_OPEN_ID = os.environ.get("FEISHU_USER_OPEN_ID", "")  # 从环境变量读取接收者


def get_tenant_token():
    """获取 tenant_access_token"""
    resp = session.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": APP_SECRET},
        timeout=10,
        proxies=None
    )
    data = resp.json()
    if data.get("code") != 0:
        raise Exception(f"获取token失败: {data}")
    return data["tenant_access_token"]


def load_dashscope_key():
    """从 .zshrc 或 .bashrc 加载 DASHSCOPE_API_KEY"""
    api_key = os.environ.get("DASHSCOPE_API_KEY", "")
    if api_key:
        return api_key
    for rc_file in [os.path.expanduser("~/.zshrc"), os.path.expanduser("~/.bashrc")]:
        try:
            with open(rc_file) as f:
                for line in f:
                    if line.startswith("export DASHSCOPE_API_KEY="):
                        api_key = line.split("=")[1].strip().strip('"').strip("'")
                        if api_key:
                            return api_key
        except:
            pass
    return ""

def generate_qwen_tts(text, voice="Nofish"):
    """使用千问 TTS 生成音频"""
    api_key = load_dashscope_key()
    if not api_key:
        raise ValueError("DASHSCOPE_API_KEY 未配置")

    resp = session.post(
        "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen3-tts-flash",
            "input": {
                "text": text,
                "voice": voice,
                "language_type": "Chinese"
            }
        },
        timeout=30,
        proxies=None
    )
    data = resp.json()
    audio_url = (
        data.get("data", {}).get("audio", {}).get("url") or
        data.get("audio", {}).get("url") or
        data.get("output", {}).get("audio", {}).get("url")
    )
    if not audio_url:
        raise ValueError(f"千问TTS失败: {data}")
    return audio_url


def generate_edge_tts(text, voice="zh-CN-YunyangNeural"):
    """使用微软 Edge TTS 生成音频"""
    fd, mp3_path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    
    ogg_path = tempfile.mktemp(suffix=".ogg")
    
    # 调用 Edge TTS，移除了 --timeout 参数避免 Node.js 内部报错
    result = subprocess.run(
        ["npx", "node-edge-tts", 
         "-t", text, 
         "-f", mp3_path, 
         "-v", voice],
        cwd="/opt/homebrew/lib/node_modules/openclaw",
        capture_output=True,
        text=True,
        timeout=40
    )
    
    # Node.js 可能抛未捕获异常导致非零退出码，但文件可能已生成
    # 优先检查文件是否存在
    if result.returncode != 0 and not os.path.exists(mp3_path):
        raise Exception(f"Edge TTS 失败（文件未生成）: {result.stderr[:200]}")
    elif result.returncode != 0:
        print(f"Edge TTS 警告（文件已生成）: {result.stderr[:100]}")
    
    # 转换为 OGG (opus)
    conv_result = subprocess.run([
        "ffmpeg", "-i", mp3_path,
        "-c:a", "libopus", "-b:a", "64k", "-ar", "48000",
        ogg_path, "-y"
    ], capture_output=True, timeout=30)
    
    os.unlink(mp3_path)
    
    if conv_result.returncode != 0:
        raise Exception(f"FFmpeg转换失败: {conv_result.stderr[:100]}")
    
    return ogg_path


def download_wav(url):
    """下载千问TTS音频"""
    resp = session.get(
        url, timeout=30)
    fd, wav_path = tempfile.mkstemp(suffix=".wav")
    os.write(fd, resp.content)
    os.close(fd)
    return wav_path


def convert_to_ogg(wav_path):
    """转换 WAV 为 OGG（添加静音填充）"""
    silence_path = tempfile.mktemp(suffix=".wav")
    ogg_path = tempfile.mktemp(suffix=".ogg")
    
    # 生成1.5秒静音
    subprocess.run([
        "ffmpeg", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", "1.5",
        silence_path, "-y"
    ], capture_output=True)
    
    # 拼接：原音频 + 静音
    concat_list = tempfile.mktemp(suffix=".txt")
    with open(concat_list, "w") as f:
        f.write(f"file '{wav_path}'\n")
        f.write(f"file '{silence_path}'\n")
    
    subprocess.run([
        "ffmpeg", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c:a", "libopus", "-b:a", "64k", "-ar", "48000",
        ogg_path, "-y"
    ], capture_output=True, timeout=30)
    
    for f in [wav_path, silence_path, concat_list]:
        try:
            os.unlink(f)
        except:
            pass
    
    return ogg_path


def upload_and_send_ogg(token, ogg_path):
    """上传 OGG 文件并发送语音消息"""
    with open(ogg_path, "rb") as f:
        upload_resp = session.post(
            "https://open.feishu.cn/open-apis/im/v1/files",
            headers={"Authorization": f"Bearer {token}"},
            data={"file_type": "opus", "file_name": "audio.ogg"},
            files={"file": ("audio.ogg", f, "audio/ogg")},
            timeout=15,
            proxies=None
        )
    
    upload_data = upload_resp.json()
    if upload_data.get("code") != 0:
        raise Exception(f"上传失败: {upload_data}")
    
    file_key = upload_data["data"]["file_key"]
    
    # 发送语音消息
    send_resp = session.post(
        "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={
            "receive_id": USER_OPEN_ID,
            "msg_type": "audio",
            "content": json.dumps({"file_key": file_key})
        },
        timeout=10,
        proxies=None
    )
    return send_resp.json()


def main():
    text = sys.argv[1] if len(sys.argv) > 1 else "测试语音"
    voice = sys.argv[2] if len(sys.argv) > 2 else "Nofish"

    print(f"文本: {text[:30]}...")
    print(f"音色: {voice}")

    ogg_path = None
    tts_method = None
    
    # 优先千问 TTS，失败则 Edge TTS 兜底
    try:
        audio_url = generate_qwen_tts(text, voice)
        wav_path = download_wav(audio_url)
        ogg_path = convert_to_ogg(wav_path)
        tts_method = "qwen (Nofish)"
        print("使用千问 TTS（Nofish 音色）")
    except Exception as e:
        print(f"千问 TTS 失败: {e}，切换 Edge TTS...")
        try:
            ogg_path = generate_edge_tts(text, "zh-CN-YunyangNeural")
            tts_method = "edge (免费)"
            print("使用 Edge TTS（云扬音色）")
        except Exception as e2:
            print(f"Edge TTS 失败: {e2}")
            print("无可用TTS服务，语音发送失败")
            sys.exit(1)

    # 获取 token 并发送
    token = get_tenant_token()
    print(f"Token获取成功")

    result = upload_and_send_ogg(token, ogg_path)
    code = result.get("code")
    if code == 0:
        print(f"✅ 语音发送成功 (via {tts_method})")
        msg_id = result.get("data", {}).get("message_id", "")
        print(f"消息ID: {msg_id}")
    else:
        print(f"❌ 发送失败: {result.get('msg')} (code={code})")

    os.unlink(ogg_path)


if __name__ == "__main__":
    main()
