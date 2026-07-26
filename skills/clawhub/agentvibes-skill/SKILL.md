---
slug: "agentvibes-skill"
name: "agentvibes-skill"
version: 1.0.1
displayName: "AgentVibes语音合成-专业版"
summary: "企业级TTS工具,支持神经声音、多角色协同、批量导出、背景音乐与音效,适配商业内容生产。"
license: "Proprietary"
edition: "pro"
description: |-
  AgentVibes语音合成专业版,面向企业团队与专业内容生产者的高级文本转语音工具。核心能力:
  - 神经声音引擎(Soprano),提供更自然的语音质量
  - 多角色协同播报,适合对话与剧本场景
  - 批量音频导出,支持 WAV/MP3 格式
  - 高级音效(混响、回声、变调、EQ)
  - 背景音乐库与自定义曲目导入

  适用场景:
  - 有声书与播客批量制作
  - 企业培训视频多语种配音
  - 游戏角色对话语音生成
  - 客服系统 IVR 语音批量生产

  差异化:专业版在免费版基础上扩展神经声音、多角色协同、批量导出与...
tags:
  - Creative
  - 语音合成
  - 企业版
  - 商业内容
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# AgentVibes语音合成-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| AgentVibes语音合成-专业版批量导出 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-----|:-----|:-----|:-----|
| 声音切换 | 是 | 是 | 914+ 离线声音 |
| 神经声音引擎 | 否 | 是 | Soprano 高质量合成 |
| 多角色协同 | 否 | 是 | 对话剧本多声音 |
| 批量音频导出 | 否 | 是 | WAV/MP3 批量产出 |
| 高级音效 | 限制 | 是 | 混响/回声/变调/EQ |
| 背景音乐库 | 限制 | 是 | 完整库 + 自定义导入 |
| 个性风格 | 基础 | 高级 | 自定义风格编辑 |
| API 调用 | 否 | 是 | 程序化集成 |
| 技术支持 | 社区 | 专属 | 工单响应 |
### 能力项

针对能力项,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力项相关的配置参数、输入数据和处理选项.
**输出**: 返回能力项的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力项`的配置文档进行参数调优
### 声音切换

针对声音切换,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供声音切换相关的配置参数、输入数据和处理选项.
**输出**: 返回声音切换的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`声音切换`的配置文档进行参数调优
### 神经声音引擎

针对神经声音引擎,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供神经声音引擎相关的配置参数、输入数据和处理选项.
**输出**: 返回神经声音引擎的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`神经声音引擎`的配置文档进行参数调优
#
## 适用场景

### 场景一:有声书批量制作

出版社需将一批文本章节转化为有声书,使用神经声音引擎与批量导出功能.
```bash
# 切换到神经声音引擎
/agent-vibes:provider switch soprano
# ...
# 设置播报风格为戏剧化
/agent-vibes:personality dramatic
# ...
# 批量导出章节音频(脚本调用)
python （请参考skill目录中的脚本文件） \
  --input ./chapters/ \
  --output ./audio/ \
  --voice soprano-zh-female-1 \
  --format mp3 \
  --speed 1.0
```

### 场景二:多角色对话配音

游戏开发商需要为角色对话生成多声音配音,使用多角色协同功能.
```bash
# 定义角色声音映射
/agent-vibes:role-add protagonist soprano-zh-male-1
/agent-vibes:role-add 旁白 soprano-zh-female-2
/agent-vibes:role-add villain soprano-zh-male-3
# ...
# 执行对话剧本播报
/agent-vibes:dialogue （请参考skill目录中的脚本文件） \
  --output game_voices.mp3
# ...
# 添加背景音乐与音效
/agent-vibes:background-music switch epic_theme
/agent-vibes:effects reverb hall
```

### 场景三:企业 IVR 语音批量生产

客服系统需要批量生成多语种 IVR 提示音,使用批量导出能力.
```bash
# 批量生成多语种 IVR 语音
python （请参考skill目录中的脚本文件） \
  --config ivr_prompts.json \
  --languages zh,en,ja,ko \
  --output ./ivr_audio/ \
  --format wav \
  --sample-rate 8000
# ...
# 应用统一音效标准化
/agent-vibes:effects eq normalize
```

## 使用流程

### 优秀步:启用专业版功能

```bash
# 设置专业版模式
export AGENTVIBES_EDITION="pro"
export AGENTVIBES_LICENSE="your_license_key"
# ...
# 验证授权
/agent-vibes:version
```

### 第二步:切换到神经声音引擎

```bash
# 查看 Soprano 神经声音
/agent-vibes:provider switch soprano
/agent-vibes:list soprano
# ...
# 切换到高质量神经声音
/agent-vibes:switch soprano-zh-female-1
```

### 第三步:批量生产音频

```bash
# 批量导出
python （请参考skill目录中的脚本文件） \
  --input texts/ \
  --output audio/ \
  --voice soprano-zh-female-1 \
  --format mp3
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | agentvibes-skill处理的内容输入 |,  |
| content | string | 否 | agentvibes-skill处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    result: "skill 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 18+ 或 Python 3.9+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Soprano 引擎 | 神经TTS | 专业版必需 | 随 License 提供 |
| Piper TTS | 离线TTS | 推荐 | 自动下载 |
| ffmpeg | 音频处理 | 必需 | 包管理器安装 |
| sox | 音效处理 | 推荐 | 包管理器安装 |
| Python 3.9+ | 脚本运行 | 必需 | 官方安装 |

### API Key 配置
- **环境变量名**: `AGENTVIBES_LICENSE`(企业版授权)
- **附加变量**: `AGENTVIBES_EDITION=pro`
- **获取方式**: 通过企业服务渠道申请,支持浮动授权
- **安全建议**: 使用密钥管理服务存储 License,避免明文写入脚本或镜像

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持神经声音、批量导出、多角色协同等企业级语音生产场景

## 案例展示

专业版完整配置:

```bash
# 环境变量
AGENTVIBES_EDITION=pro
AGENTVIBES_LICENSE=your_license
AGENTVIBES_DEFAULT_ENGINE=soprano
AGENTVIBES_DEFAULT_FORMAT=mp3
AGENTVIBES_SAMPLE_RATE=44100
# ...
# 高级音效参数
/agent-vibes:effects reverb hall      # 大厅混响
/agent-vibes:effects reverb room      # 房间混响
/agent-vibes:effects echo 0.3         # 回声(延迟秒)
/agent-vibes:effects pitch -2         # 变调(半音)
/agent-vibes:effects eq bass+3        # 低频增强
/agent-vibes:effects eq normalize     # 标准化
# ...
# 背景音乐控制
/agent-vibes:background-music on
/agent-vibes:background-music switch jazz
/agent-vibes:background-music volume 0.3
```

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有命令,迁移时仅需设置 `AGENTVIBES_EDITION=pro` 并配置 License.
### Q2:神经声音与离线声音的区别?
A:神经声音(Soprano)使用神经网络合成,自然度更高但需在线或较高算力;离线声音(Piper)本地运行,速度更快但表现力稍弱。建议按场景选择.
### Q3:批量导出支持哪些格式?
A:支持 WAV(无损)、MP3(压缩)、OGG(流媒体)三种格式,可指定采样率(8000/16000/22050/44100/48000 Hz).
### Q4:多角色对话如何定义?
A:通过 `role-add` 命令建立角色名与声音的映射,然后在剧本文件中用 `[角色名]` 标记对话行,批量生成时自动分配声音.
### Q5:License 如何管理?
A:License 绑定企业账号,支持浮动授权(同时在线数受限)。通过环境变量 `AGENTVIBES_LICENSE` 配置,支持离线激活.
### Q6:能否自定义声音模型?
A:专业版支持导入自定义微调声音模型(需符合 Soprano 模型规范),联系企业服务获取技术文档.
## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

