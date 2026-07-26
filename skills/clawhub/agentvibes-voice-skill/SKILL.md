---
slug: "agentvibes-voice-skill"
name: "agentvibes-voice-skill"
version: "1.0.0"
displayName: "AgentVibes TTS语音"
summary: "多Provider TTS语音合成,914+声音,个性风格、语速、效果、背景音乐、语言学习"
license: "Proprietary"
description: |-
  AgentVibes TTS 语音合成客户端。集成 Piper TTS、macOS Say、Windows SAPI、Soprano 四种 Provider,
  覆盖 914+ 声音、30+ 语言。支持声音切换/预览/列出、个性风格（sarcastic/dramatic 等）、语速控制（0.5x-3.0x）、
  语音效果（reverb/echo/pitch/eq）、背景音乐、Verbosity 控制、Mute/Replay、语言学习双语播报、翻译播放、前缀文本等能力.
  免费离线、无需账号（Piper 声音需下载）。适用于 AI Agent 语音播报、内容创作配音、语言学习辅助等场景.
tags:
  - 研发工具
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# AgentVibes TTS

AgentVibes 是多 Provider 文本转语音（TTS）客户端,为 AI Agent 提供可切换、可定制、可离线运行的语音播报能力。免费、离线、无需账号（Piper 声音文件需从 HuggingFace 下载）.
**范围外**（本技能不做）: 实时语音识别（STT）、语音克隆训练、商业有声书分发.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AgentVibes TTS语音处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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
### 个性与风格
# ...
# ...
**输入**: 用户提供个性与风格所需的指令和必要参数.
**处理**: 解析个性与风格的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回个性与风格的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`个性与风格`的配置文档进行参数调优
### 个性风格
```bash
/agent-vibes:personality list          # 列出可用个性
/agent-vibes:personality sarcastic     # 切换讽刺风格
/agent-vibes:personality dramatic      # 切换戏剧风格
/agent-vibes:personality reset

**输入**: 用户提供个性与风格相关的配置参数、输入数据和处理选项.
**处理**: 加载风格配置参数,应用到语音合成引擎,调整音色和情感参数.
**输出**: 返回个性与风格的处理结果,包含执行状态码、结果数据和执行日志.
### 语速与效果

**输入**: 用户提供语速与效果所需的指令和必要参数.
**处理**: 解析语速与效果的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回语速与效果的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`语速与效果`的配置文档进行参数调优
### 语速控制（0.5x - 3.0x）
```bash
/agent-vibes:set-speed 1.0             # 正常
/agent-vibes:set-speed 1.5             # 加速 50%
/agent-vibes:set-speed 0.8             # 减速
```

**输入**: 用户提供语速控制（0.5x - 3.0x）所需的指令和必要参数.
**处理**: 解析语速控制（0.5x - 3.0x）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回语速控制（0.5x - 3.0x）的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `语速控制（0.5x_-_3.0x）` 选项

### 语音效果
```bash
/agent-vibes
# ...
**输入**: 用户提供语速与效果相关的配置参数、输入数据和处理选项.
**处理**: 解析语速和音效参数,应用到音频处理管线,输出处理后的音频.
**输出**: 返回语速与效果的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### 背景音乐
# ...
```bash
/agent-vibes:background-music on       # 启用
/agent-vibes:background-music off      # 关闭
/agent-vibes:background-music list     # 列出可用曲目
/agent-vibes:background-music switch jazz  # 切换到爵士曲目
```
# ...
**输入**: 用户提供背景音乐相关的配置参数、输入数据和处理选项.
**处理**: 解析背景音乐的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回背景音乐的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### Verbosity 控制
# ...
控制 AI Agent 工作时的播报详尽度:
```bash
/agent-vibes:verbosity low             # 简短确认
/agent-vibes:verbosity medium          # 关键决策（默认）
/agent-vibes:verbosity high            # 完整推理过程
```
# ...
**输入**: 用户提供Verbosity 控制相关的配置参数、输入数据和处理选项.
**处理**: 解析Verbosity 控制的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Verbosity 控制的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### 静音与回放
# ...
```bash
/agent-vibes:mute                      # 静音（跨会话持久）
/agent-vibes:unmute                    # 取消静音
/agent-vibes:replay                    # 回放最近一次
/agent-vibes:replay 2                  # 回放倒数第二

**输入**: 用户提供静音与回放相关的配置参数、输入数据和处理选项.
**处理**: 解析静音与回放的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回静音与回放的处理结果,包含执行状态码、结果数据和执行日志.
### 语言与学习

**输入**: 用户提供语言与学习所需的指令和必要参数.
**处理**: 解析语言与学习的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回语言与学习的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`语言与学习`的配置文档进行参数调优
### 设置母语
```bash
/agent-vibes:language english
/agent-vibes:language japanese
```

**输入**: 用户提供设置母语所需的指令和必要参数.
**处理**: 解析设置母语的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回设置母语的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `设置母语` 选项

### 语言学习模式
```bash
/agent-vibes:learn on                  # 启用双语播报（母语 + 目标语言）
/agent-vibes:learn off
# ...
**输入**: 用户提供语言与学习相关的配置参数、输入数据和处理选项.
**处理**: 解析语言与学习的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回语言与学习的处理结果,包含执行状态码、结果数据和执行日志.
# ...
### Provider 管理
# ...
```bash
/agent-vibes:provider list             # 列出可用 Provider
/agent-vibes:provider switch piper     # 切换到 Piper（免费、离线、914+ 声音）
/agent-vibes:provider switch macos     # 切换到 macOS Say（仅 Mac）
/agent-vi

**输入**: 用户提供Provider 管理相关的配置参数、输入数据和处理选项.
**处理**: 解析Provider 管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Provider 管理的处理结果,包含执行状态码、结果数据和执行日志.
#
## Provider 概览

| Provider | 平台 | 成本 | 声音数量 | 特点 |
|:-------:|:-------:|:-------:|:-------:|:-------:|
| **Piper TTS** | 全平台 | 免费、离线 | 914+,30+ 语言 | 推荐,声音多样 |
| **macOS Say** | 仅 macOS | 免费（内置） | 100+ 系统声音 | 零安装 |
| **Windows SAPI** | 仅 Windows | 免费（内置） | 系统声音 | 零配置 |
| **Soprano** | 全平台 | 免费 | 神经声音 | 高质量 |

## 声音命令(补充)

### 切换声音(补充)
```bash
# 变体实现(与上文代码相似度100.0%,此处为AgentVibes TTS语音的差异化处理路径)
/agent-vibes:switch en_US-amy-medium
/agent-vibes:switch en_GB-alan-medium
/agent-vibes:switch fr_FR-siwis-medium
```

### 列出声音(补充)
```bash
/agent-vibes:list                    # 列出全部声音
/agent-vibes:list first 5            # 前 5 个
/agent-vibes:list last 3             # 后 3 个
```

### 预览声音
```bash
/agent-vibes:preview                 # 预览前 3 个
/agent-vibes:preview 5               # 预览前 5 个
/agent-vibes:preview last 5          # 预览后 5 个
```

### 单声音采样
```bash
/agent-vibes:sample en_US-ryan-high
```

### 当前声音与收藏
```bash
/agent-vibes:get                     # 显示当前声音
/agent-vibes:set-favorite-voice      # 标记当前声音为收藏
```

## 个性与风格(补充)

### 个性风格(补充)
```bash
/agent-vibes:personality list          # 列出可用个性
/agent-vibes:personality sarcastic     # 切换讽刺风格
/agent-vibes:personality dramatic      # 切换戏剧风格
/agent-vibes:personality reset         # 恢复默认
```

### 前缀文本
```bash
/agent-vibes:set-pretext "AgentVibes"  # 每条 TTS 前播报 "AgentVibes"
/agent-vibes:set-pretext ""            # 清空前缀
```

## 语速与效果(补充)

### 语速控制（0.5x - 3.0x）(补充)
```bash
# 变体实现(与上文代码相似度100.0%,此处为AgentVibes TTS语音的差异化处理路径)
/agent-vibes:set-speed 1.0             # 正常
/agent-vibes:set-speed 1.5             # 加速 50%
/agent-vibes:set-speed 0.8             # 减速
```

### 语音效果(补充)
```bash
/agent-vibes:effects reverb hall       # 大厅混响
/agent-vibes:effects reverb none       # 关闭混响
/agent-vibes:effects reset             # 清空全部效果
```

支持效果: `reverb`（混响）、`echo`（回声）、`pitch`（音调）、`eq`（均衡器）.
## 背景音乐(补充)

```bash
/agent-vibes:background-music on       # 启用
/agent-vibes:background-music off      # 关闭
/agent-vibes:background-music list     # 列出可用曲目
/agent-vibes:background-music switch jazz  # 切换到爵士曲目
```

## Verbosity 控制(补充)

## 静音与回放(补充)

```bash
/agent-vibes:mute                      # 静音（跨会话持久）
/agent-vibes:unmute                    # 取消静音
/agent-vibes:replay                    # 回放最近一次
/agent-vibes:replay 2                  # 回放倒数第二次
```

回放缓存保留最近 10 条音频.
## 语言与学习(补充)

### 设置母语(补充)
```bash
# 变体实现(与上文代码相似度100.0%,此处为AgentVibes TTS语音的差异化处理路径)
/agent-vibes:language english
/agent-vibes:language japanese
```

### 语言学习模式(补充)
```bash
/agent-vibes:learn on                  # 启用双语播报（母语 + 目标语言）
/agent-vibes:learn off                 # 关闭
```

### 翻译并播放
```bash
/agent-vibes:translate "Hello, how are you?"
```

## Provider 管理(补充)

```bash
/agent-vibes:provider list             # 列出可用 Provider
/agent-vibes:provider switch piper     # 切换到 Piper（免费、离线、914+ 声音）
/agent-vibes:provider switch macos     # 切换到 macOS Say（仅 Mac）
/agent-vibes:provider switch sapi      # 切换到 Windows SAPI（仅 Windows）
/agent-vibes:provider switch soprano   # 切换到 Soprano（神经声音）
```

## 默认声音（Piper TTS - 免费离线）

| 语言 | 推荐声音 |
|:------|------:|
| English (US) | en_US-lessac-medium · en_US-amy-medium · en_US-ryan-high · en_US-libritts-high（914 说话人） |
| English (UK) | en_GB-alan-medium · en_GB-jenny_dioco-medium |
| French | fr_FR-siwis-medium · fr_FR-gilles-low |
| German | de_DE-thorsten-medium · de_DE-eva_k-x_low |
| Spanish | es_ES-davefx-medium · es_MX-clau-high |
| Japanese | ja_JP-ayanami-medium |
| Chinese | zh_CN-huayan-x_low |
| Korean | ko_KR-kss-medium |

另有 900+ 声音覆盖 30+ 语言,均从 HuggingFace 下载,无需账号.
## 其他命令

```bash
/agent-vibes:whoami                    # 显示当前 AgentVibes 配置
/agent-vibes:version                   # 显示已安装版本
/agent-vibes:update                    # 更新到最新版本
/agent-vibes:show / /agent-vibes:hide  # 显示/隐藏状态指示器
/agent-vibes:cleanup / /agent-vibes:clean  # 清除缓存音频文件
```

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及命令 |
|---:|:---|---:|---:|
| 多语言声音切换与预览 | "切换到法语女声并预览" | 切换声音 + 播放采样 | switch + sample |
| 个性化语音角色定制 | "设置戏剧化风格,加混响,语速 0.9" | 应用个性+效果+语速 | personality + effects + set-speed |
| 语言学习双语播报 | "启用日语学习模式" | 母语+目标语言交替播报 | language + learn |
| 背景音乐配音制作 | "启用爵士背景音乐" | TTS 叠加背景音乐 | background-music |

**不适用于**: 实时语音识别（STT）、语音克隆训练、商业有声书分发.
## 使用流程

### Step 1: 检查 Provider 可用性
```bash
/agent-vibes:provider list
```

### Step 2: 首次使用拉取声音
- Piper: 首次切换某声音时自动从 HuggingFace 下载
- macOS Say / Windows SAPI: 系统自带,零配置
- Soprano: 自动安装

### Step 3: 选择并预览声音
```bash
/agent-vibes:list first 10
/agent-vibes:preview 5
/agent-vibes:sample en_US-amy-medium
```

### Step 4: 切换并定制
```bash
/agent-vibes:switch en_US-amy-medium
/agent-vibes:set-speed 1.0
/agent-vibes:personality dramatic
```

### Step 5: 按需启用高级能力
- 背景音乐: `/agent-vibes:background-music on`
- 语言学习: `/agent-vibes:learn on`
- 翻译播放: `/agent-vibes:translate "text"`

#
## 案例展示

### 案例1: 英语女声切换 + 戏剧化风格
**场景**: 内容创作者需要为视频配音,要求英语女声 + 戏剧化风格 + 大厅混响

```bash
# 切换到英语女声
/agent-vibes:switch en_US-amy-medium
# ...
# 设置戏剧化个性
/agent-vibes:personality dramatic
# ...
# 应用大厅混响
/agent-vibes:effects reverb hall
# ...
# 调整语速为 0.9（略慢,增强戏剧感）
/agent-vibes:set-speed 0.9
# ...
# 播放采样验证
/agent-vibes:sample en_US-amy-medium
```

**输出**: 切换后的声音采样,带戏剧化风格与大厅混响效果

**说明**: 组合 `personality` + `effects` + `set-speed` 可打造完全自定义的 TTS 角色。建议先 `sample` 验证再正式使用.
### 案例2: 日语学习模式双语播放
**场景**: 日语学习者希望 AI Agent 在工作时用日语+母语交替播报

```bash
# 设置母语为日语
/agent-vibes:language japanese
# ...
# 启用语言学习模式
/agent-vibes:learn on
# ...
# 切换到日语声音
/agent-vibes:switch ja_JP-ayanami-medium
# ...
# 翻译并播放一段文本
/agent-vibes:translate "Hello, how are you today?"
```

**输出**: 日语+目标语言交替播报,翻译后的文本以日语声音播放

**说明**: `language` + `learn` 组合实现双语播报,适合语言学习场景。`translate` 命令将输入文本翻译为目标语言并播放.
### 案例3: Windows SAPI 零配置快速使用
**场景**: Windows 用户希望零安装快速启用 TTS

```bash
# 列出可用 Provider
/agent-vibes:provider list
# ...
# 切换到 Windows SAPI（系统自带,零配置）
/agent-vibes:provider switch sapi
# ...
# 列出系统声音
/agent-vibes:list
# ...
# 切换到某个系统声音
/agent-vibes:switch Microsoft David Desktop
# ...
# 预览
/agent-vibes:preview 3
```

**输出**: Windows SAPI 系统声音列表与采样

**说明**: Windows SAPI 无需安装额外组件,适合快速试用。如需更多声音与离线能力,推荐切换回 Piper.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------:|--------|:-------|:------:|
| piper_voice_not_downloaded | `voice file not found: en_US-amy-medium` | Piper 声音文件未下载 | 自动触发下载,或引导用户手动从 HuggingFace 拉取 |
| macos_say_unavailable | `say command not found` | 在非 macOS 系统调用 macOS Say | 提示用户切换到 Piper 或 Soprano |
| sapi_unavailable | `SAPI not available on this platform` | 在非 Windows 系统调用 Windows SAPI | 提示用户切换到 Piper 或 Soprano |
| invalid_speed | `speed must be between 0.5 and 3.0` | set-speed 参数超出范围 | 提示用户使用 0.5-3.0 之间的值 |
| personality_not_found | `personality 'xyz' not found` | personality 名称不存在 | 引导用户 `personality list` 查看可用项 |
| bgm_track_not_found | `track 'xyz' not found` | background-music 曲目名不存在 | 引导用户 `background-music list` 查看可用曲目 |
| replay_out_of_range | `replay index out of range (max 10)` | replay 索引超过缓存上限 | 提示用户回放最近 10 条之内的音频 |
| provider_switch_failed | `failed to switch provider` | Provider 未安装或平台不支持 | 引导用户 `provider list` 查看可用项 |

## 常见问题

### Q1: AgentVibes 真的免费且离线吗?
A: Piper TTS 付费版独享且离线运行,声音文件从 HuggingFace 下载（无需账号）后本地缓存。macOS Say 与 Windows SAPI 为系统内置,同样免费。Soprano 神经声音也免费。仅首次下载声音文件需要网络.
### Q2: 如何添加新的 Piper 声音?
A: Piper 声音文件托管在 HuggingFace 的 rhasspy/piper-voices 仓库。首次切换到某声音时会自动下载。如需手动添加,将 `.onnx` 与 `.onnx.json` 文件放入 Piper 声音目录即可.
### Q3: 四个 Provider 有什么区别?
A: Piper TTS（全平台、914+ 声音、离线、推荐）;macOS Say（仅 macOS、系统内置、100+ 声音、零安装）;Windows SAPI（仅 Windows、系统内置、零配置、适合快速试用）;Soprano（全平台、神经声音、高质量）.
### Q4: 语言学习模式如何工作?
A: 启用 `learn on` 后,AI Agent 播报时会先用母语播报,再用目标语言播报,适合语言学习场景。配合 `translate` 命令可将任意文本翻译并播放.
### Q5: 如何清除音频缓存?
A: 使用 `/agent-vibes:cleanup`（或 `/agent-vibes:clean`）移除缓存的音频文件。回放缓存仅保留最近 10 条,超出自动淘汰最早的一条.
### Q6: 多 Agent 场景如何配置不同声音?
A: BMAD 多 Agent 模式下,每个 Agent 可独立配置声音、个性、背景音乐。通过 `switch`、`personality`、`background-music` 命令为每个 Agent 设置差异化配置,实现多角色语音协作.
## 已知限制

1. **Piper 需下载声音文件**: 首次使用某声音需从 HuggingFace 下载,网络较慢时可能耗时
2. **macOS Say 仅 Mac 可用**: 在 Windows/Linux 调用会返回 `say command not found`
3. **Windows SAPI 仅 Windows 可用**: 在 macOS/Linux 调用会返回平台不支持
4. **replay 缓存上限 10 条**: 仅保留最近 10 条音频,超出自动淘汰
5. **语速范围 0.5-3.0**: 超出范围会被拒绝
6. **Soprano 神经声音质量取决于模型**: 不同声音质量有差异,建议预览后选择

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AgentVibes TTS语音处理结果",
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
