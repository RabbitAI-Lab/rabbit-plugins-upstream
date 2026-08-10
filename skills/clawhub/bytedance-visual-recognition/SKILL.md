---
name: bytedance-visual-recognition
description: >
  ByteDance Visual Recognition — 调用豆包 Doubao-Seed + 智谱 GLM 双后端多模态模型识别图片和视频，
  输出文字或代码。支持单文件识别、批量目录处理、追问（基于上次结果的对话），自动模型降级与重试。
  本地缓存媒体文件（Temp/YYYYMMDD/），持久化识别历史（vision_history.json）和追问上下文（.last_response），
  可选手动 IAM 控制台用量同步。首次运行自动生成 config.json 并显示隐私声明。
  Supports both Chinese and English interactions.
summary: "Doubao + GLM visual recognition — image/video to text/code, local caching, history, batch, follow-up, optional IAM sync"
tags:
  vision: "3.1.6"
  image-recognition: "3.1.6"
  video-recognition: "3.1.6"
  image-to-code: "3.1.6"
  video-to-code: "3.1.6"
  doubao: "3.1.6"
  glm: "3.1.6"
trigger_patterns:
  - "识别图片"
  - "识别视频"
  - "图片识别"
  - "视频识别"
  - "图片转文字"
  - "视频转文字"
  - "图片转代码"
  - "视频转代码"
  - "提取图片文字"
  - "提取视频文字"
  - "图片OCR"
  - "UI转代码"
  - "设计稿转代码"
  - "截图转代码"
  - "录屏转代码"
  - "recognize image"
  - "recognize video"
  - "image to text"
  - "video to text"
  - "image to code"
  - "video to code"
metadata:
  openclaw:
    requires:
      bins:
        - python
    permissions:
      filesystem:
        read: ["config.json", "vision_history.json", ".last_response"]
        write: ["Temp/", "vision_history.json", ".last_response", "config.json"]
      network:
        - host: "ark.cn-beijing.volces.com"
          purpose: "Doubao vision model API"
        - host: "open.bigmodel.cn"
          purpose: "GLM vision model Chat Completions API"
        - host: "open.volcengineapi.com"
          purpose: "Optional manual IAM usage sync"
    emoji: "🔍"
    homepage: https://www.volcengine.com/docs/82379/1569618
    locales: ["zh-CN", "en"]
---

# ByteDance Visual Recognition — 豆包 + GLM 双后端视觉识别
# ByteDance Visual Recognition — Doubao + GLM Dual-Backend Vision

Doubao-Seed (6 models) + Zhipu GLM (2 free models). First run auto-generates `config.json`. Fill in one API Key to start. This skill supports commands and interactions in both Chinese and English. / 支持中英文交互。

## ⚠️ Privacy & Data Notice / 隐私与数据声明

- **Network / 网络**: Selected images/videos and prompts are base64-encoded and sent to Volcengine (Doubao) or Zhipu (GLM) cloud APIs.
- **Local cache / 本地缓存**: Media files temporarily copied to `Temp/YYYYMMDD/`, default 7-day retention (`temp_retention_days` in config.json, range 1-3650).
- **History / 使用记录**: Recognition history stored in `vision_history.json`, follow-up context in `.last_response`, auto-cleaned after 7 days.
- **Credentials / 凭证**: API Keys stored in plaintext `config.json`. Do not use personal keys on shared machines.
- **IAM sync / IAM 同步**: Only triggers via explicit `sync` command when IAM keys are configured. No automatic outbound calls.
- **First run / 首次运行**: A privacy notice is displayed once. Continuing past it constitutes acknowledgment of data handling practices.

## 🚀 Setup (pick one)

### Doubao (Volcengine)

1. https://console.volcengine.com/ark → API Key → create
2. Create inference endpoints, pick from:

| config key | model | priority |
|--------|------|:---:|
| `doubao_vision_21p_id` | Doubao-Seed-2.1-Pro | primary |
| `doubao_vision_21t_id` | Doubao-Seed-2.1-Turbo | secondary |
| `doubao_vision_20p_id` | Doubao-Seed-2.0-Pro | tertiary |
| `doubao_vision_20c_id` | Doubao-Seed-2.0-Code | code-first |
| `doubao_vision_20l_id` | Doubao-Seed-2.0-Lite | fallback |
| `doubao_vision_20m_id` | Doubao-Seed-2.0-Mini | low-cost |

3. Edit `config.json`, replace `""` with actual endpoint IDs.

### GLM (Zhipu, free)

1. https://open.bigmodel.cn → get API Key
2. Edit `config.json`: `"zhipu_api_key": "your-key"`

### Provider filter

`provider_mode` in `config.json`:
- `0` = all (default)
- `1` = Zhipu only
- `2` = Doubao only

### Test

```bash
python doubao_vision_recognize.py --help
python doubao_vision_recognize.py status
```

---

## ⚡ Commands

| command | purpose | example |
|------|------|------|
| `rec <file> --image\|--video --text\|--code` | recognize | `rec a.jpg --image --text` |
| `rec <dir> --batch --image\|--video --text\|--code` | batch | `rec ./img/ --batch --image --text` |
| `ask --text\|--code --prompt "..."` | follow-up | `ask --text -p "details"` |
| `status` | usage stats | |
| `sync` | console sync (manual) | |
| `history` | 7-day history | |

### Parameters

| param | desc |
|------|------|
| `--image` | image input |
| `--video` | video input |
| `--text` | text output |
| `--code` | code output |
| `--prompt` / `-p` | extra instruction |
| `--batch` | directory batch |

---

## 🚫 Behavior Rules

### 1. Execute immediately
- Trigger = execute. The privacy notice is shown once on first run; continuing past it acknowledges data handling.

### 2. Parameter inference
- "recognize/analyze image" → `--image --text`
- "recognize/analyze video" → `--video --text`
- "convert to code / UI to code / design to code" → `--code`
- extra requirements → `--prompt "..."`
- unsure → ask once if image or video

---

## Limits

- Doubao: 180W tokens per model per day, auto-fallback
- GLM: free, auto-retry on failure (4.6V: 10 retries, 4.1V: 5 retries)
- Image ≤ 15MB, Video ≤ 50MB
