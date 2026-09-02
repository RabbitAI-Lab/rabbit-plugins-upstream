#!/bin/bash
# MiMo TTS 语音生成（仅生成本地音频文件，不发送飞书）
# 用法: ./speak.sh "要说话的文本" [音色]
# 默认音色: mimo_default
# 注意: 此脚本需要 MIMO_API_KEY 环境变量
#
# 音色选项:
#   mimo_default  - MiMo默认音色
#   default_zh    - MiMo中文女声
#   default_en    - MiMo英文女声

TEXT="$1"
VOICE="${2:-mimo_default}"

if [ -z "$TEXT" ]; then
    echo "用法: $0 \"文本\" [音色]"
    echo "可用音色: mimo_default, default_zh, default_en"
    exit 1
fi

API_KEY="${MIMO_API_KEY}"
if [ -z "$API_KEY" ]; then
    echo "错误: MIMO_API_KEY 未设置"
    exit 1
fi

TMP_WAV="/tmp/mimo_tts_$$.wav"
TMP_OGG="/tmp/mimo_tts_$$.ogg"

# 构建 JSON payload (手动避免jq语法问题)
PAYLOAD=$(cat <<EOF
{
    "model": "mimo-v2-tts",
    "messages": [
        {
            "role": "user",
            "content": "请说: ${TEXT}"
        },
        {
            "role": "assistant",
            "content": "${TEXT}"
        }
    ],
    "audio": {
        "format": "wav",
        "voice": "${VOICE}"
    }
}
EOF)

# 调用 MiMo TTS API (通过 chat completions 接口)
RESPONSE=$(curl -s -X POST 'https://api.xiaomimimo.com/v1/chat/completions' \
    -H "api-key: $API_KEY" \
    -H 'Content-Type: application/json' \
    -d "$PAYLOAD")

# 解析 audio data (base64)
AUDIO_DATA=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('choices',[{}])[0].get('message',{}).get('audio',{}).get('data','') if 'error' not in d else '')" 2>/dev/null)

if [ -z "$AUDIO_DATA" ]; then
    echo "错误: 未能生成音频"
    # 检查是否有 error 字段
    ERROR_MSG=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('error',{}).get('message','') or d.get('error',{}).get('code',''))" 2>/dev/null)
    if [ -n "$ERROR_MSG" ]; then
        echo "API错误: $ERROR_MSG"
    fi
    exit 1
fi

# 解码 base64 并写入 wav 文件
echo "$AUDIO_DATA" | base64 -d > "$TMP_WAV" 2>/dev/null

if [ ! -s "$TMP_WAV" ]; then
    echo "错误: 音频文件生成失败"
    exit 1
fi

# 转换为飞书支持的 ogg 格式 (opus)
if command -v ffmpeg &> /dev/null; then
    ffmpeg -i "$TMP_WAV" -c:a libopus -b:a 64k -ar 48000 "$TMP_OGG" -y 2>/dev/null
    rm -f "$TMP_WAV"
    echo "$TMP_OGG"
else
    echo "$TMP_WAV"
fi