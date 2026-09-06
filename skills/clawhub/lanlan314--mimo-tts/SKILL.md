---
name: mimo-tts
description: 小米MiMo语音合成（TTS）技能，支持将文本转换为自然语音。当用户要求朗读、语音合成、文字转语音、TTS、读一段话、把文字转成声音时使用（作为千问TTS的备选方案）。
---

# 小米 MiMo 语音合成技能 (mimo-tts)

## ⚠️ 环境变量配置

| 环境变量 | 说明 | 获取方式 |
|----------|------|---------|
| `MIMO_API_KEY` | MiMo API 密钥 | [MiMo控制台 API Keys](https://platform.xiaomimimo.com/#/console/api-keys) |

```bash
export MIMO_API_KEY="your-mimo-api-key-here"
```

## API 信息

- **Base URL**: `https://api.xiaomimimo.com/v1`
- **TTS 端点**: `POST /v1/audio/speech` (OpenAI-compatible)
- **模型**: `mimo-v2-tts` (需确认)

## 快速使用

### 基本语音合成

```bash
curl -X POST 'https://api.xiaomimimo.com/v1/audio/speech' \
  -H "Authorization: Bearer $MIMO_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "mimo-v2-tts",
    "input": "要转换的文本内容",
    "voice": "male-qn-qingse"
  }'
```

## 脚本说明

### scripts/speak.sh
纯 Bash 脚本，**仅生成本地音频文件**，不需要飞书凭证
```bash
# 需要 MIMO_API_KEY 环境变量
./speak.sh "要转换的文本" [模型名]
# 输出: /tmp/mimo_tts_xxx.ogg
```

## 依赖说明

- `ffmpeg` - 音频格式转换
- `jq` - JSON 处理

## 备注

- MiMo TTS API 兼容 OpenAI Audio API 格式
- 具体音色选项需参考 MiMo 官方文档
- 音频输出格式为 ogg（Opus），可直接用于飞书
