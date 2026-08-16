---
name: beware-piper-tts
slug: beware-piper-tts
displayName: "Piper TTS"
version: "1.0.1"
summary: "用Piper本地文字转语音发语音消息"
description: "用Piper本地文字转语音发语音消息。Local text-to-speech using Piper for voice message delivery。Use when。触发关键词: using, local, speech, text, piper, tts, beware。开箱即用,无需复杂配置,支持中文交互与结构化输出。"
license: "MIT"
tools:
  - read
---

# Piper TTS

Generate voice messages using , a fast local TTS engine. Zero cloud calls, zero cost, zero API keys.

## Setup

If Piper is not installed, run the setup script:

```bash
scripts/setup-piper.sh
```

This installs `piper-tts` via pip and downloads a default voice (`en_US-kusal-medium`).

## Generating Voice Messages

Use `scripts/piper-speak.sh` to generate and deliver voice:

```bash
scripts/piper-speak.sh "<text>" [voice]
```

* `text`: The text to speak (required)
* `voice`: Piper voice name (default: `en_US-kusal-medium`)

The script outputs an MP3 path. Include it in your reply as:

```text
[[audio_as_voice]]
MEDIA:<path-to-mp3>
```

This delivers the audio as a native voice message on supported channels (Telegram, Discord, etc.).

## 示例

1. User asks: "Tell me a joke as audio"
2. Run: `scripts/piper-speak.sh "Why do programmers prefer dark mode? Because light attracts bugs!"`
3. Get MP3 path from output
4. Reply with `[[audio_as_voice]]` + `MEDIA:<path>`

## Available Voices

After setup, download additional voices:

```bash
scripts/setup-piper.sh --voice en_US-ryan-high
scripts/setup-piper.sh --voice en_GB-northern_english_male-medium
```

Popular voices:

* `en_US-kusal-medium` — Clear male voice (default, recommended)
* `en_US-ryan-high` — High quality US male
* `en_US-hfc_male-medium` — US male
* `en_GB-northern_english_male-medium` — British male
* Browse all: <https://huggingface.co/rhasspy/piper-voices>

## Important Notes

* **Speed**: Local generation is ~0.5-1s. Much faster than cloud TTS.
* **No API keys**: Works completely offline after setup.
* **Platform**: macOS (Apple Silicon + Intel), Linux. Requires Python 3.9+.
* **Do NOT** set `messages.tts.auto: "always"` in Skill平台 config — it makes every response slow. Keep TTS on-demand.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Local text-to-speech using Piper for voice message delivery
- Use when
  the user asks for voice res
- 触发关键词: using, local, speech, text, piper, tts, beware

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Piper TTS？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Piper TTS有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步
