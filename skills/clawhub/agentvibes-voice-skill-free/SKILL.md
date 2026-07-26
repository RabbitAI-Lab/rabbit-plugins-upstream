---
slug: "agentvibes-voice-skill-free"
name: "agentvibes-voice-skill-free"
version: "1.0.0"
displayName: "AgentVibes TTS LITE"
summary: "基础TTS语音合成,支持声音切换、预览、语速控制"
license: "MIT"
description: |-
  AgentVibes TTS 语音合成基础客户端（免费版）。集成 Piper TTS 单一 Provider,
  支持声音切换、列出、预览、采样、语速控制等基础能力。免费离线、无需账号（Piper 声音文件需下载）.
  适用于 AI Agent 基础语音播报、简单内容配音场景.
tags:
  - 研发工具
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# AgentVibes TTS LITE

AgentVibes 基础版,基于 Piper TTS 提供文本转语音能力。免费、离线、无需账号（Piper 声音文件需从 HuggingFace 下载）.
**范围外**（本技能不做）: macOS Say / Windows SAPI / Soprano 多 Provider 切换、个性风格、语音效果、背景音乐、语言学习模式、翻译播放（需升级付费版）.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AgentVibes TTS LITE处理的输入数据或指令 |
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
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### Provider
免费版仅支持 Piper TTS:

| Provider | 平台 | 成本 | 声音数量 |
|------:|------:|------:|------:|
| **Piper TTS** | 全平台 | 免费、离线 | 914+,30+ 语言 |

> **升级提示**: macOS Say / Windows SAPI / Soprano 等多 Provider 切换仅在 agentvibes-voi

**处理**: 解析Provider的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Provider的处理结果,包含执行状态码、结果数据和执行日志.
**输入**: 用户提供Provider所需的指令和必要参数.
### 声音命令

**输入**: 用户提供声音命令所需的指令和必要参数.
**处理**: 解析声音命令的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回声音命令的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`声音命令`的配置文档进行参数调优
### 切换声音
```bash
/agent-vibes:switch en_US-amy-medium
/agent-vibes:switch en_GB-alan-medium
/agent-vibes:switch fr_FR-siwis-medium
```

**输入**: 用户提供切换声音所需的指令和必要参数.
**处理**: 解析切换声音的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回切换声音的处理结果,包含执行状态码、结果数据和执行日志.
### 列出声音
```bash
/agent-vibes:list                    # 列出全部声音
/
# ...
**输入**: 用户提供声音命令相关的配置参数、输入数据和处理选项.
**处理**: 解析语音指令文本,匹配命令模式,执行对应的语音处理操作.
**输出**: 返回声音命令的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### 语速控制（0.5x - 3.0x）
# ...
```bash
/agent-vibes:set-speed 1.0             # 正常
/agent-vibes:set-speed 1.5             # 加速 50%
/agent-vibes:set-speed 0.8             # 减速
```
# ...
**输入**: 用户提供语速控制（0.5x - 3.0x）相关的配置参数、输入数据和处理选项.
**处理**: 解析语速控制（0.5x - 3.0x）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回语速控制（0.5x - 3.0x）的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### 默认声音（Piper TTS - 免费离线）
# ...
| 语言 | 推荐声音 |
|:---:|:---:|
| English (US) | en_US-lessac-medium · en_US-amy-medium · en_US-ryan-high |
| English (UK) | en_GB-alan-medium |
| French | fr_FR-siwis-medium |
| German | de_DE-thorsten-m
# ...
**输入**: 用户提供默认声音（Piper TTS - 免费离线）相关的配置参数、输入数据和处理选项.
**处理**: 解析默认声音（Piper TTS - 免费离线）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回默认声音（Piper TTS - 免费离线）的处理结果,包含执行状态码、结果数据和执行日志.
# ...
#
## Provider(补充)
# ...
免费版仅支持 Piper TTS:
# ...
| Provider(续)| 平台 | 成本 | 声音数量 |
|:-------------|-------------:|:-------------|:-------------|
| **Piper TTS** | 全平台 | 免费、离线 | 914+,30+ 语言 |
# ...
> **升级提示**: macOS Say / Windows SAPI / Soprano 等多 Provider 切换仅在 agentvibes-voice-skill 付费版中提供.
# ...
## 声音命令(补充)
# ...
### 切换声音(补充)
```bash
/agent-vibes:switch en_US-amy-medium
/agent-vibes:switch en_GB-alan-medium
/agent-vibes:switch fr_FR-siwis-medium
```
# ...
### 列出声音(补充)
```bash
/agent-vibes:list                    # 列出全部声音
/agent-vibes:list first 5            # 前 5 个
/agent-vibes:list last 3             # 后 3 个
```
# ...
### 预览声音
```bash
/agent-vibes:preview                 # 预览前 3 个
/agent-vibes:preview 5               # 预览前 5 个
```
# ...
### 单声音采样
```bash
/agent-vibes:sample en_US-ryan-high
```
# ...
### 当前声音
```bash
/agent-vibes:get                     # 显示当前声音
```
# ...
## 语速控制（0.5x - 3.0x）(补充)
```bash
/agent-vibes:set-speed 1.0             # 正常
/agent-vibes:set-speed 1.5             # 加速 50%
/agent-vibes:set-speed 0.8             # 减速
```
# ...
## 默认声音（Piper TTS - 免费离线）(补充)
# ...
| 语言(续)| 推荐声音 |
|---:|:---|
| English (US) | en_US-lessac-medium · en_US-amy-medium · en_US-ryan-high |
| English (UK) | en_GB-alan-medium |
| French | fr_FR-siwis-medium |
| German | de_DE-thorsten-medium |
| Spanish | es_ES-davefx-medium |
| Japanese | ja_JP-ayanami-medium |
| Chinese | zh_CN-huayan-x_low |
| Korean | ko_KR-kss-medium |
# ...
另有 900+ 声音覆盖 30+ 语言,均从 HuggingFace 下载,无需账号.
# ...
## 适用场景
# ...
| 场景 | 典型输入 | 输出内容 |
|:------:|--------|:-------|
| 声音切换与预览 | "切换到英语女声并预览" | 切换声音 + 播放采样 |
| 语速调整 | "把语速调到 1.5 倍" | 应用新语速 |
| 多语言声音选择 | "切换到日语声音" | 切换到对应语言声音 |
# ...
**不适用于**: 个性风格、语音效果、背景音乐、语言学习模式、多 Provider 切换（需升级付费版）
# ...
## 使用流程
# ...
### Step 1: 检查 Piper 可用性
```bash
/agent-vibes:provider list
```
# ...
### Step 2: 首次使用拉取声音
首次切换某声音时自动从 HuggingFace 下载,无需账号.
# ...
### Step 3: 选择并预览声音
```bash
/agent-vibes:list first 10
/agent-vibes:preview 5
/agent-vibes:sample en_US-amy-medium
```
# ...
### Step 4: 切换并调整语速
```bash
/agent-vibes:switch en_US-amy-medium
/agent-vibes:set-speed 1.0
```
# ...
**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
# ...
#
## 案例展示
# ...
### 案例1: 切换英语女声
**场景**: 用户需要将 AI Agent 的播报声音切换为英语女声
# ...
```bash
# 列出前 10 个声音
/agent-vibes:list first 10

# 预览前 5 个
/agent-vibes:preview 5

# 采样特定声音
/agent-vibes:sample en_US-amy-medium

# 切换到该声音
/agent-vibes:switch en_US-amy-medium
```
# ...
**输出**: 切换后的声音采样
# ...
**说明**: 建议先 `preview` 或 `sample` 验证声音效果再正式切换.
# ...
### 案例2: 调整语速
**场景**: 用户希望加快播报语速到 1.5 倍
# ...
```bash
# 查看当前配置
/agent-vibes:get

# 设置为 1.5 倍速
/agent-vibes:set-speed 1.5
```
# ...
**输出**: 应用新语速后的播报
# ...
**说明**: 语速范围 0.5x-3.0x,超出范围会被拒绝.
# ...
## 错误处理
# ...
# ...
| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|----|:--:|---:|----|
| piper_voice_not_downloaded | `voice file not found: en_US-amy-medium` | Piper 声音文件未下载 | 自动触发下载,或引导用户手动从 HuggingFace 拉取 |
| invalid_speed | `speed must be between 0.5 and 3.0` | set-speed 参数超出范围 | 检查网络连接和配置后重试,提示用户使用 0.5-3.0 之间的值 |
| voice_not_found | `voice 'xyz' not found` | 声音名称不存在 | 检查网络连接和配置后重试,引导用户 `list` 查看可用声音 |
| provider_unavailable | `piper not installed` | Piper TTS 引擎未安装 | 自动触发安装,或引导用户手动安装 |
| network_error | `failed to download voice file` | 网络不可达或 HuggingFace 访问失败 | 检查网络连接和配置后重试,或引导用户使用代理 |
# ...
## 常见问题
# ...
### Q1: AgentVibes 真的免费且离线吗?
A: Piper TTS 本地离线运行,声音文件从 HuggingFace 下载（无需账号）后本地缓存。仅首次下载声音文件需要网络.
# ...
### Q2: 如何添加新的 Piper 声音?
A: Piper 声音文件托管在 HuggingFace 的 rhasspy/piper-voices 仓库。首次切换到某声音时会自动下载。如需手动添加,将 `.onnx` 与 `.onnx.json` 文件放入 Piper 声音目录即可.
# ...
### Q3: 免费版和付费版有什么区别?
A: 免费版（LITE）仅支持 Piper TTS 单 Provider,提供声音切换、列出、预览、采样、语速控制基础能力。付费版（agentvibes-voice-skill）额外提供:
- macOS Say / Windows SAPI / Soprano 多 Provider 切换
- 个性风格（sarcastic/dramatic 等）
- 语音效果（reverb/echo/pitch/eq）
- 背景音乐
- 语言学习双语播报与翻译播放
- Verbosity 控制与 Mute/Replay
- 3 个完整案例（vs 免费版 2 个基础案例）
- 8 种错误处理（vs 免费版 5 种）
# ...
### Q4: 支持哪些语言?
A: Piper TTS 支持 30+ 语言、914+ 声音,包括英语、法语、德语、西班牙语、日语、中文、韩语等主流语言。通过 `list` 命令查看全部可用声音.
# ...
## 已知限制
# ...
1. **单 Provider**: 仅支持 Piper TTS,不支持 macOS Say / Windows SAPI / Soprano（需升级付费版）
2. **基础能力**: 不支持个性风格、语音效果、背景音乐、语言学习模式（需升级付费版）
3. **Piper 需下载声音文件**: 首次使用某声音需从 HuggingFace 下载
4. **语速范围 0.5-3.0**: 超出范围会被拒绝
5. **无 Replay**: 不支持回放历史音频（需升级付费版）
# ...
---
# ...
> **想要多 Provider 切换、个性风格、背景音乐、语言学习模式?** 升级到 agentvibes-voice-skill 付费版解锁全部高级能力.
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    "result": "AgentVibes TTS LITE处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "agentvibes-voice-skill"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
# ...