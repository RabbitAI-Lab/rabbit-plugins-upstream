---
slug: agentvibes-openclaw-skill
name: agentvibes-openclaw-skill
version: "4.6.6"
displayName: Skill
summary: "AgentVibes TTS,切换声音/设性格/控语速/备份"
  control speed, back...
license: MIT-0
description: |-
  🎤 AgentVibes TTS for ai-assistant Code & OpenClaw — Switch voices, set personality,
  control speed, back。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Creative
tools:
  - - read
- exec
---

# Skill

Professional text-to-speech for ai-assistant Code and Skill平台. Free, offline, no account required.

**Providers:** Piper TTS (914+ voices, all platforms) · macOS Say (built-in) · Windows SAPI (zero setup) · Soprano (neural)

---

## Voice Commands

### /agent-vibes:switch <voice_name>

Switch to a different voice.

```bash
/agent-vibes:switch en_US-amy-medium
/agent-vibes:switch en_GB-alan-medium
/agent-vibes:switch fr_FR-siwis-medium
```

### /agent-vibes:list [first|last] [N]

List available voices.

```bash
/agent-vibes:list                    # Show all voices
/agent-vibes:list first 5            # Show first 5
/agent-vibes:list last 3             # Show last 3
```

### /agent-vibes:preview [first|last] [N]

Preview voices with audio samples.

```bash
/agent-vibes:preview                 # Preview first 3 voices
/agent-vibes:preview 5               # Preview first 5
/agent-vibes:preview last 5          # Preview last 5
```

### /agent-vibes:sample <voice_name>

Play a sample of a specific voice.

```bash
/agent-vibes:sample en_US-ryan-high
```

### /agent-vibes:get

Show the currently active voice.

### /agent-vibes:set-favorite-voice

Mark current voice as your favorite.

---

## Personality & Style

### /agent-vibes:personality [name|list|add|edit|get|reset]

Set a personality style for TTS output.

```bash
/agent-vibes:personality list          # Show available personalities
/agent-vibes:personality sarcastic     # Switch to sarcastic style
/agent-vibes:personality dramatic      # Switch to dramatic style
/agent-vibes:personality reset         # Back to default
```

### /agent-vibes:set-pretext <phrase>

Add a spoken prefix before every TTS message.

```bash
/agent-vibes:set-pretext "AgentVibes"   # Speaks "AgentVibes: ..." before each message
/agent-vibes:set-pretext ""              # Clear pretext
```

---

## Speed & Effects

### /agent-vibes:set-speed <speed>

Control speech rate (0.5x – 3.0x).

```bash
/agent-vibes:set-speed 1.0             # Normal speed
5             # 50% faster
/agent-vibes:set-speed 0.8             # Slower
```

### /agent-vibes:effects [reverb|echo|pitch|eq|reset]

Configure voice effects.

```bash
/agent-vibes:effects reverb hall       # Hall reverb
/agent-vibes:effects reverb none       # No reverb
/agent-vibes:effects reset             # Clear all effects
```

---

## Background Music

### /agent-vibes:background-music [on|off|status|list|switch]

Toggle or change background music played under TTS.

```bash
/agent-vibes:background-music on       # Enable background music
/agent-vibes:background-music off      # Disable
/agent-vibes:background-music list     # Show available tracks
/agent-vibes:background-music switch jazz  # Switch to jazz track
```

---

## Verbosity

### /agent-vibes:verbosity [low|medium|high]

Control how much ai-assistant speaks while working.

```bash
/agent-vibes:verbosity low             # Brief acknowledgments only
/agent-vibes:verbosity medium          # Key decisions (default)
/agent-vibes:verbosity high            # Full reasoning
```

---

## Mute / Replay

### /agent-vibes:mute / /agent-vibes:unmute

Silence or restore TTS output (persists across sessions).

### /agent-vibes:replay [N]

Replay recent audio (last 10 kept).

```bash
/agent-vibes:replay                    # Replay last audio
/agent-vibes:replay 2                  # Replay second-to-last
```

---

## Language & Learning

### /agent-vibes:language <lang>

Set your native language.

```bash
/agent-vibes:language english
/agent-vibes:language japanese
```

### /agent-vibes:learn [on|off]

Enable language learning mode — ai-assistant speaks in both your native and target language.

```bash
/agent-vibes:learn on
/agent-vibes:learn off
```

### /agent-vibes:translate <text>

Translate and speak text in the target language.

---

## Provider Management

### /agent-vibes:provider [list|switch|info]

```bash
/agent-vibes:provider list
/agent-vibes:provider switch piper     # Piper TTS (free, offline, 914+ voices)
/agent-vibes:provider switch macos     # macOS Say (Mac only)
/agent-vibes:provider switch sapi      # Windows SAPI (Windows only, zero setup)
/agent-vibes:provider switch soprano   # Soprano (neural)
```

---

## Providers

| Provider | Platform | Cost | Voices |
| --- | --- | --- | --- |
| **Piper TTS** | All platforms | Free, offline | 914+ in 30+ languages |
| **macOS Say** | macOS only | Free (built-in) | 100+ system voices |
| **Windows SAPI** | Windows only | Free (built-in) | System voices, zero setup |
| **Soprano** | All platforms | Free | Neural voices |

---

## Miscellaneous

### /agent-vibes:whoami

Show current AgentVibes configuration.

### /agent-vibes:version

Show installed version.

### /agent-vibes:update

Update AgentVibes to the latest version.

### /agent-vibes:show / /agent-vibes:hide

Show or hide the AgentVibes status indicator.

### /agent-vibes:cleanup / /agent-vibes:clean

Remove cached audio files.

---

## Default Voices (Piper TTS — Free & Offline)

**English (US):** en_US-lessac-medium · en_US-amy-medium · en_US-ryan-high · en_US-libritts-high (914 speakers)

**English (UK):** en_GB-alan-medium · en_GB-jenny_dioco-medium

**French:** fr_FR-siwis-medium · fr_FR-gilles-low

**German:** de_DE-thorsten-medium · de_DE-eva_k-x_low

**Spanish:** es_ES-davefx-medium · es_MX-ai-assistant-high

**Japanese:** ja_JP-ayanami-medium · **Chinese:** zh_CN-huayan-x_low · **Korean:** ko_KR-kss-medium

**+ 900 more** across 30+ languages. All voices are downloaded from [HuggingFace](https://huggingface.co/rhasspy/piper-voices) — no account required.

---

## Tips

* **Preview first**: Use `/agent-vibes:preview` before committing to a voice
* **Verbosity**: Set to `low` for focused work, `high` for full narration
* **BMAD party mode**: Each agent gets their own voice, music, and personality
* **Replay**: Use `/agent-vibes:replay` to re-hear the last 10 responses
* **Speed**: Combine with personality for a fully custom TTS character

Enjoy your TTS experience! 🎵

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
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

- 🎤 AgentVibes TTS for ai-assistant Code & OpenClaw — Switch voices, set personality,
  control speed, back
- 触发关键词: switch, code, ai-assistant, openclaw, agentvibes, skill

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

## 示例

### 示例1：基础用法

```
# 请参考上方使用说明进行配置和调用
result = "ready"
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
