---
slug: "beware-piper-tts-free"
name: "beware-piper-tts-free"
version: "1.0.0"
displayName: "Piper TTS Lite"
summary: "基于Piper的本地语音合成基础版,使用默认音色将文本转为MP3语音消息,零云端零密钥。"
license: "MIT"
description: |-
  基于 Piper 神经网络引擎的本地语音合成基础版(免费)。全部推理在本地完成,零云端调用、零 API 密钥.
  核心能力:单段文本转语音、默认音色(en_US-kusal-medium)朗读、MP3 输出与语音消息封装.
  适用于偶发的语音消息投递与短文本朗读。如需多音色切换、长文本分段合并、批量生成与风格控制,请升级至 beware-piper-tts 付费版.
tags:
  - 研发工具
  - Creative
  - 语音合成
tools:
  - read
  - exec
homepage: "https://skillhub.cn"


---
# Piper TTS Lite

基于 Piper 神经网络语音合成引擎的本地 TTS 基础版。所有推理在本地完成,无需 API Key、无需联网(首次下载音色后),单段生成约 0.5-1 秒.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Piper TTS Lite处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill基于Agent平台内置LLM,通常无需额外API Key配置

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 单段语音合成
将一段文本用默认音色 `en_US-kusal-medium` 合成为 MP3 并投递到支持的渠道(Telegram、Discord 等).
```bash
（请参考skill目录中的脚本文件） "Why do programmers prefer dark mode? Because light attracts bugs!"
```
脚本输出 MP3 路径,按以下格式封装即可作为原生语音消息投递:
```text
[[audio_as_voice]]
MEDIA:/tmp/piper/out_20260720_103045.mp3
```

**输入**: 用户提供单段语音合成所需的指令和必要参数.
**处理**: 解析单段语音合成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 2. 默认音色朗读
免费版使用预置的 `en_US-kusal-medium`(清晰男声)音色,适合英文短文本朗读与语音消息投递.
> **升级提示**: 多音色切换(美式女声、英式男声、中文女声)、长文本分段合并、批量生成与 SSML 风格控制仅在 [beware-piper-tts 付费版](#) 中提供.
**处理**: 解析默认音色朗读的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
#
## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|---:|---:|---:|---:|
| 语音消息投递 | "把这句笑话读给我听" | MP3 路径 + 原生语音消息封装 | 单段合成 |
| 短文本朗读 | 一段 100 字以内的英文 | MP3 文件路径 | 单段合成 |

**不适用于**: 长文章转有声(单段过长韵律生硬,需付费版分段合并)、多角色对话体(需付费版多音色切换)、中文朗读(需付费版下载中文音色).
## 使用流程

### 第一步:安装 Piper 与默认音色
```bash
（请参考skill目录中的脚本文件）
# 自动安装 piper-tts、检测 espeak-ng、下载默认音色 en_US-kusal-medium
```

### 第二步:合成并投递语音消息
```bash
（请参考skill目录中的脚本文件） "你的朗读文本"
```
从脚本输出读取 MP3 路径,以 `[[audio_as_voice]]` + `MEDIA:<path>` 格式回传给用户即可.
### 第三步:确认投递
检查用户渠道(Telegram/Discord)中是否出现可播放的原生语音气泡。若仅出现文件附件而非语音气泡,说明渠道不支持 `audio_as_voice` 协议,改为直接发送 MP3 文件链接.
## 案例展示

### 案例1:语音笑话投递
**场景**: 用户在 Telegram 中要求"讲个笑话,要语音版的".
```bash
（请参考skill目录中的脚本文件） "Why do programmers prefer dark mode? Because light attracts bugs!"
```
**输出**:
```
/tmp/piper/out_20260720_103045.mp3
```
**回传**:
```text
[[audio_as_voice]]
MEDIA:/tmp/piper/out_20260720_103045.mp3
```
该消息在 Telegram 中呈现为可播放的原生语音气泡,本地推理耗时约 0.7 秒.
### 案例2:短文本朗读
**场景**: 用户希望把一段英文摘要朗读出来便于通勤时收听.
```bash
（请参考skill目录中的脚本文件） "The quick brown fox jumps over the lazy dog. This is a pangram used to test font rendering."
```
**输出**:
```
/tmp/piper/out_20260720_103112.mp3
```
直接将路径以文件附件形式发送即可.
## 异常处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| Piper 未安装 | `piper: command not found` | 未运行 setup 脚本或 pip 安装失败 | 执行 `（请参考skill目录中的脚本文件）`,确认 Python 3.9+ 可用 |
| espeak-ng 缺失 | `espeak-ng not found, phonemize failed` | 系统未安装音素化器 | macOS `brew install espeak-ng`,Linux `apt install espeak-ng` |
| 音色文件缺失 | `voice model not found: en_US-kusal-medium` | 默认音色未下载 | 重新运行 `（请参考skill目录中的脚本文件）` 下载默认音色 |
| 文本含非法字符 | `phonemize error: invalid character` | 文本含 Piper 不支持的 emoji 或控制字符 | 调用前用 `sed` 剔除 emoji 与控制字符 |
| 输出目录不可写 | `permission denied: /tmp/piper/out.mp3` | 输出路径无写权限 | 显式指定 `--output` 到有权限的目录,如 `~/.piper-out/` |

## 常见问题

### Q1: 免费版能用哪些音色?
A: 免费版仅预置 `en_US-kusal-medium`(清晰男声)一个音色。如需美式女声、英式男声、中文女声等多音色切换,请升级至 beware-piper-tts 付费版.
### Q2: 单段文本最长能读多少字?
A: 建议单段不超过 500 字。超过后韵律可能生硬,且单次推理显存占用升高。长文章请升级付费版使用 `piper-speak-long.sh` 自动分段合并.
### Q3: 支持中文朗读吗?
A: 免费版默认音色为英文音色,朗读中文会出现明显错读。中文朗读需下载 `zh_CN-huayan-medium` 音色,该能力在付费版中提供.
### Q4: 为什么不要开启 `messages.tts.auto: "always"`?
A: 该配置会让 Agent 对每条回复都触发 TTS,导致响应明显变慢,且大量语音消息干扰阅读体验。建议仅在用户明确要求语音时手动触发.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **单一音色**: 仅支持默认英文男声 `en_US-kusal-medium`,不支持音色切换
- **无长文本分段**: 单段过长韵律生硬,不支持自动分段与合并
- **无批量生成**: 一次仅处理一段文本,不支持内容矩阵生产
- **无风格控制**: 不支持语速、停顿、音高调节
- **英文优先**: 默认音色为英文,中文朗读需付费版下载中文音色
- **Windows 原生支持弱**: 需经 WSL 运行,原生 Windows 下 espeak-ng 安装较繁琐

---

> 想要多音色切换、长文本分段合并、批量生成与 SSML 风格控制?升级至 [beware-piper-tts 付费版](#),解锁专业语音内容生产能力.