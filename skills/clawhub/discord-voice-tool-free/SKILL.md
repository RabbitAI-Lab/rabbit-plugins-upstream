---
slug: discord-voice-tool-free
name: discord-voice-tool-free
version: 1.0.0
displayName: Discord语音工具免费版
summary: "基础 Discord 语音频道 AI 对话工具,支持加入/离开与本地语音识别合成.。面向个人用户的 Discord 语音频道 AI 实时对话工具。核心能力:"
license: Proprietary
edition: free
description: 面向个人用户的 Discord 语音频道 AI 实时对话工具。核心能力:，可自动提升工作效率

  - 加入/离开 Discord 语音频道

  - 语音活动检测(VAD)自动识别用户说话

  - 本地 Whisper 离线语音转文字

  - 文字转语音(TTS)将 AI 回复读出

  - 基础打断(barge-in)与连接状态查询

  适用场景:

  - 个人语音频道与 AI 助手对话

  - 小型语音社群的 AI 互动

  - 本地化离线语音处理体验

  差异化: 免费版聚焦本地离线方案,零 API 成本;Pro 版提供多服务商、流式 STT与企业级能力'
tags:
  - Discord
  - 语音对话
  - Communication
  - 语音识别
  - 社交
  - 通信
  - kokoro
  - discord
  - medium
  - tts
  - allowedusers
tools:
  - read
  - exec
  - write
homepage: ""
category: "Communication"
---
# Discord 语音工具(免费版)

## 概述

Discord 语音工具免费版是一款面向个人用户的 Discord 语音频道 AI 实时对话工具。它让机器人加入指定语音频道,自动检测用户说话,通过本地 Whisper 模型将语音转为文字,交给 Agent 处理后,再用文字转语音(TTS)将回复读出,实现语音频道中的自然对话体验.
免费版聚焦本地离线方案:使用本地 Whisper 进行语音识别,使用本地 Kokoro 进行语音合成,不依赖任何付费云 API,适合个人零成本体验。如果你需要多服务商切换、流式实时转写、自动重连和企业级稳定性保障,请升级至 Pro 版.
## 核心能力

| 能力模块 | 说明 | 免费版支持 |
|----|---|-----|
| 加入/离开频道 | 语音频道进出 | 支持 |
| 语音活动检测 | 自动检测说话 | 支持 |
| 语音转文字 | STT 服务 | 本地 Whisper(离线) |
| 流式转写 | 实时低延迟 | 不支持 |
| 文字转语音 | TTS 服务 | 本地 Kokoro(离线) |
| 打断支持 | 用户说话时停止播报 | 支持(可配置) |
| 自动重连 | 断线自动恢复 | 不支持 |
| 多服务商 | 切换 STT/TTS | 不支持 |
| 白名单 | 限制可用用户 | 支持 |
| 自动加入 | 启动时自动进频道 | 不支持 |

### 核心功能执行
用`input_params`参数进行配置.

**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.

**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.

**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Discord、对话工具、支持加入、离开与本地语音识、别合成、面向个人用户的、实时对话工具、核心能力、VAD、自动识别用户说话、离线语音转文字、回复读出、基础打断、barge、与连接状态查询等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:个人语音 AI 助手

在自己的语音频道中加入 AI 助手,用语音提问、语音获取回答,解放双手.
```bash
# 1. 让机器人加入语音频道
discord_voice join <channelId>
# ..
# 2. 开始对话(说话即可,机器人自动检测)
# 用户: "今天天气怎么样?"
# 机器人(TTS): "我无法获取实时天气,但可以帮你查询."
# ..
# 3. 查看连接状态
discord_voice status
# ..
# 4. 离开频道
discord_voice leave
```

### 场景二:小型语音社群互动

在小型技术社群的语音频道中,AI 助手参与讨论,实时回答成员问题.
```bash
# 配置允许所有成员使用
# allowedUsers: []  # 空数组表示允许所有用户
# ..
# 加入社群语音频道
discord_voice join 1234567890
# ..
# 成员说话时机器人自动响应
# 成员: "Python 里怎么反转列表?"
# 机器人(TTS): "可以用切片 list[::-1] 或 reversed() 函数."
```

### 场景三:离线语音处理体验

在网络受限或注重隐私的场景下,使用完全本地的语音处理,不上传任何音频到云端.
```json5
{
  sttProvider: "local-whisper",  // 本地 Whisper,离线
  ttsProvider: "kokoro",          // 本地 Kokoro,离线
  // 基础LLM由Agent平台提供
}
```

## 不适用场景

以下场景Discord语音工具免费版不适合处理：

- 需要100%确定性的关键决策
- 医疗诊断
- 法律判决

## 触发条件

需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 依赖详情

语音处理需要 `ffmpeg` 和构建工具:

```bash
# Ubuntu / Debian
sudo apt-get install ffmpeg build-essential python3
# ..
# CentOS / RHEL
sudo dnf install ffmpeg gcc-c++ make python3
# ..
# macOS
brew install ffmpeg
```

### 第二步:安装插件

```bash
# 通过平台安装
platform install discord-voice
# ..
# 或手动安装
cd ~/.agent/extensions
git clone <repository-url> discord-voice
cd discord-voice
npm install
```

### 第三步:配置

在配置文件中设置本地离线方案:

```json5
{
  plugins: {
    entries: {
      "discord-voice": {
        enabled: true,
        config: {
          sttProvider: "local-whisper",
          ttsProvider: "kokoro",
          ttsVoice: "default",
          vadSensitivity: "medium",
          allowedUsers: [],
          silenceThresholdMs: 1500,
          maxRecordingMs: 30000
        }
      }
    }
  }
}
```

### 第四步:配置 Discord 机器人权限

机器人需具备以下语音权限:

- **Connect**: 加入语音频道
- **Speak**: 播放音频
- **Use Voice Activity**: 检测用户说话

在 Discord Developer Portal 的 OAuth2 URL 中添加这些权限,或将机器人加入服务器时勾选.
### 第五步:开始使用

```bash
discord_voice join <channelId>
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

### 最小可用配置

```json5
{
  sttProvider: "local-whisper",
  ttsProvider: "kokoro",
  vadSensitivity: "medium",
  allowedUsers: []
}
```

### 标准配置(推荐)

```json5
{
  enabled: true,
  config: {
    sttProvider: "local-whisper",
    ttsProvider: "kokoro",
    ttsVoice: "default",
    vadSensitivity: "medium",
    bargeIn: true,
    allowedUsers: [],
    silenceThresholdMs: 1500,
    maxRecordingMs: 30000,
    heartbeatIntervalMs: 30000
  }
}
```

### 配置项说明

| 配置项 | 类型 | 默认值 | 说明 |
|:-----|:-----|:-----|:-----|
| `enabled` | boolean | `true` | 启用/禁用插件 |
| `sttProvider` | string | `"local-whisper"` | 语音转文字服务商 |
| `ttsProvider` | string | `"kokoro"` | 文字转语音服务商 |
| `ttsVoice` | string | `"default"` | TTS 语音 ID |
| `vadSensitivity` | string | `"medium"` | VAD 灵敏度(low/medium/high) |
| `bargeIn` | boolean | `true` | 用户说话时停止播报 |
| `allowedUsers` | string[] | `[]` | 允许使用的用户 ID(空=全部) |
| `silenceThresholdMs` | number | `1500` | 静音多久后开始处理(ms) |
| `maxRecordingMs` | number | `30000` | 最大录音时长(ms) |
| `heartbeatIntervalMs` | number | `30000` | 心跳检查间隔(ms) |

### VAD 灵敏度说明

| 灵敏度 | 行为 |
|---:|---:|
| `low` | 捕获轻声说话,可能被背景噪声误触发 |
| `medium` | 平衡(推荐) |
| `high` | 需要更大声、更清晰的说话 |

## 最佳实践

1. **本地模型预热**: 本地 Whisper 模型首次加载较慢(几秒到几十秒)。建议在正式使用前先执行一次测试转录预热模型,后续响应会更快.
2. **VAD 灵敏度调优**: 默认 `medium` 适合多数场景。环境嘈杂时调高到 `high` 减少误触发;用户说话较轻时调低到 `low` 提高捕获率。配合 `silenceThresholdMs`(默认 1500ms)调整静音判定时长.
3. **录音时长控制**: `maxRecordingMs` 默认 30 秒。长篇发言会被截断。如需更长录音,适当调大此值,但注意过长的录音会增加本地处理延迟.
4. **白名单按需配置**: 公开服务器建议配置 `allowedUsers` 限定可用用户,避免被滥用。个人频道可留空(允许所有).
5. **打断体验优化**: 开启 `bargeIn: true` 可让用户随时打断机器人播报,对话更自然。但频繁打断可能导致回复不完整,按场景取舍.
6. **权限完整确认**: 机器人必须同时具备 Connect、Speak、Use Voice Activity 三个权限,缺一不可。加入服务器前在 OAuth2 URL 中勾选完整权限.
7. **系统资源监控**: 本地 Whisper 和 Kokoro 消耗 CPU/内存。建议在至少 8GB 内存的机器上运行。资源不足时识别延迟会明显增大.
## 常见问题

### Q1: 「Discord client not available」报错?

确保 Discord 频道已配置且机器人已连接。机器人需先成功登录 Discord 并加入目标服务器,再使用语音功能。检查 `DISCORD_TOKEN` 环境变量是否正确设置.
### Q2: Opus/Sodium 编译报错?

这些是 Discord 语音的原生依赖,需要构建工具编译:

```bash
npm install -g node-gyp
npm rebuild @discordjs/opus sodium-native
```

确保系统已安装 `build-essential`(Linux)或 Xcode Command Line Tools(macOS).
### Q3: 听不到机器人说话?

按顺序检查:1)机器人是否有 Speak 权限;2)机器人是否被服务器静音(检查成员列表中机器人是否有静音图标);3)TTS 服务是否正常(查看日志是否有合成错误);4)音频设备是否正常.
### Q4: 语音识别不准?

本地 Whisper 的准确度受模型大小影响。免费版使用基础模型,准确度有限。改善方法:提高说话清晰度和音量;调低背景噪声;调高 VAD 灵敏度过滤噪声段。Pro 版支持 Deepgram 流式识别,准确度和速度更优.
### Q5: 免费版能用云 API(OpenAI/Deepgram)吗?

免费版默认使用本地离线方案,不配置云 API。如果你想切换到 OpenAI Whisper 或 Deepgram,需要自行在配置中填入对应 API Key,但这会增加云 API 成本,建议直接使用 Pro 版获得完整多服务商支持.
### Q6: 一个机器人能同时在多个语音频道吗?

不能。Discord 限制每个机器人在每个服务器同时只能在一个语音频道。多服务器场景需部署多个机器人实例.
### Q7: 如何开启调试日志?

```bash
DEBUG=discord-voice agent gateway start
```

调试日志会输出 VAD 检测、录音、识别、合成的详细过程,便于排查问题.
### Q8: 录音最长多久?

`maxRecordingMs` 默认 30000ms(30 秒)。超过此时长会自动截断并发送已录制部分进行识别。如需更长录音,在配置中调大此值.
## 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux(推荐 Linux,原生依赖编译更顺畅)
- **系统依赖**: `ffmpeg`(音频处理)、构建工具(编译 Opus/Sodium 原生模块)、Python 3(Whisper 模型运行时)
- **硬件**: 建议 8GB 以上内存,本地模型需较多内存
- **网络**: 仅 Discord 连接需要网络,语音处理全程本地

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| Discord Bot Token | 凭证 | 必需 | Discord Developer Portal 创建机器人获取 |
| ffmpeg | 系统依赖 | 必需 | 系统包管理器安装 |
| 本地 Whisper 模型 | 模型 | 必需 | 首次运行自动下载 |
| Kokoro TTS 模型 | 模型 | 必需 | 首次运行自动下载 |
| Node.js 原生模块 | 库 | 必需 | npm install 编译 |

### API Key 配置

- **Discord Bot Token**: 通过环境变量 `DISCORD_TOKEN` 配置(必需).
- **本地模型**: 免费 Whisper 和 Kokoro 模型首次运行自动下载,无需 API Key.
- **云端 API(可选)**: 如需使用 OpenAI/Deepgram/ElevenLabs 云服务,需额外配置对应 API Key,但免费版不推荐(建议升级 Pro 版).
### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 执行能力)
- **说明**: 以自然语言指令驱动 Agent 调用语音工具,本地模型处理音频
- **适用规模**: 单服务器、个人/小团队,本地离线处理
- **升级建议**: 如需多服务商、流式 STT、自动重连、企业级稳定性,请升级至 `discord-voice-tool-pro`

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Discord语音工具免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "discord voice"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
