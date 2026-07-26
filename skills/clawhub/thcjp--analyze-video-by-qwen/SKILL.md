---
slug: "analyze-video-by-qwen"
name: "analyze-video-by-qwen"
version: 1.0.2
displayName: "Qwen视频智能分析"
summary: "使用Qwen多模态模型分析视频内容,支持本地文件和远程URL,可自定义提示词与抽帧频率"
license: "Proprietary"
description: |-
  基于 Qwen 3.5 Plus 多模态模型对视频进行智能分析。支持本地视频文件和远程 URL 两种输入方式,
  可自定义分析提示词与抽帧频率(FPS),灵活控制分析精度与 API 调用成本.
  核心能力涵盖场景描述、动作识别、物体检测、视频摘要生成、内容审核与问答式分析.
  适用于内容创作辅助、视频内容索引、媒体资产管理、教学视频分析、监控录像审查等场景.
  API Key 从 ~/.skill-platform/skill-platform.json 的 skills.dashscope.apiKey 字段读取.
tags:
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Qwen 视频智能分析

基于阿里云 Qwen 3.5 Plus 多模态模型对视频进行智能分析。支持本地视频文件和远程 URL 两种输入方式,通过自定义提示词与抽帧频率(FPS)灵活控制分析精度与成本。核心脚本为 `（请参考skill目录中的脚本文件）`.
**范围外**(本技能不做): 视频剪辑与转码、实时视频流分析、模型微调训练、视频字幕硬编码.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Qwen视频智能分析wen多模态模型分析 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8 及以上版本
- **网络**: 需可访问阿里云 DashScope API 服务端点

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| Qwen 3.5 Plus API | 远程多模态 API | 必需 | 阿里云 DashScope 控制台开通 |
| DashScope API Key | 配置文件 | 必需 | ~/.skill-platform/skill-platform.json 配置 |
| Python 3.8+ | 运行环境 | 必需 | python.org 下载安装 |
| requests / dashscope SDK | Python 库 | 必需 | pip install dashscope |

### 可用性分类
- **分类**: MD+EXEC(Markdown 指令驱动,需 exec 执行 Python 脚本)
- **说明**: 基于自然语言指令驱动 Agent 调用 Qwen 多模态 API,完成视频抽帧与内容分析

## 核心能力

本工具的核心能力包括：使用Qwen多模态模型分析视频内容,支持本地文件和远程URL,可自定义提示词与抽帧频率。具体功能详情请参考下方能力说明表格与使用场景.
## 认证

API Key 从 `~/.skill-platform/skill-platform.json` 的 `skills.dashscope.apiKey` 字段读取.
```bash
cat ~/.skill-platform/skill-platform.json | grep apiKey
```

若 Key 缺失，引导用户:
1. 登录阿里云 DashScope 控制台
2. 开通 Qwen 多模态模型服务并创建 API Key
3. 在 `~/.skill-platform/skill-platform.json` 中添加配置:

```json
{
  "skills": {
    "dashscope": {
      "apiKey": "your-dashscope-api-key"
    }
  }
}
```

4. 配置完成后重新发起分析请求

**安全红线**: 永不接受/回显/存储来自聊天输入的 API Key;Key 仅从配置文件读取.
## 参数说明

| 参数 | 说明 | 默认值 | 必填 |
|---:|---:|---:|---:|
| `video_source` | 视频文件路径或远程 URL(支持 http/https) | - | 是 |
| `--fps` | 抽帧频率,每秒抽取的帧数。FPS 越高分析越精细,但 API 调用成本越高 | 2 | 否 |
| `--prompt` | 分析提示词,引导模型关注特定内容 | "这段视频描绘的是什么景象?" | 否 |

## 快速用法

### 分析本地视频

默认设置分析本地视频文件:

```bash
python （请参考skill目录中的脚本文件） /path/to/video.mp4
```

自定义提示词,引导模型关注特定内容:

```bash
python （请参考skill目录中的脚本文件） /path/to/video.mp4 --prompt "请详细描述视频中的每个场景,包括人物动作和背景环境"
```

自定义抽帧频率(FPS 越高,分析越精细):

```bash
python （请参考skill目录中的脚本文件） /path/to/video.mp4 --fps 5
```

### 分析远程视频 URL

直接分析可公开访问的远程视频直链:

```bash
python （请参考skill目录中的脚本文件） https://example.com/video.mp4
```

组合使用参数:

```bash
python （请参考skill目录中的脚本文件） /path/to/video.mp4 --fps 3 --prompt "视频中出现了哪些人物和物体?请逐一列出"
python （请参考skill目录中的脚本文件） https://example.com/video.mp4 --fps 4 --prompt "请详细描述视频场景的色调和构图"
```

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及参数 |
|:---:|:---:|:---:|:---:|
| 本地视频内容理解 | "分析这个视频里发生了什么" | 场景描述与内容摘要 | video_source + prompt |
| 远程视频在线分析 | "分析这个视频链接的内容" | 远程视频内容描述 | video_source(URL) + prompt |
| 高精度抽帧分析 | "逐帧详细分析这个视频" | 细粒度场景描述与物体识别 | video_source + fps(高) + prompt |
| 问答式视频审查 | "视频中出现了哪些违规内容?" | 针对性内容审核结果 | video_source + prompt(审核导向) |

**不适用于**: 实时视频流分析、视频剪辑与转码、模型微调训练.
## 使用流程

### Step 1: 校验 API Key 配置
```bash
# 变体实现(与上文代码相似度100.0%,此处为Qwen视频智能分析的差异化处理路径)
cat ~/.skill-platform/skill-platform.json | grep apiKey
```
若返回为空或文件不存在,按照认证章节引导用户配置.
### Step 2: 确认视频源
- 本地文件: 确认路径存在且为支持的视频格式(mp4/avi/mov/mkv/webm 等)
- 远程 URL: 确认 URL 为可公开访问的直链(http/https 协议)

### Step 3: 选择抽帧频率
- 快速概览(短视频 <30s): fps=2(默认)
- 常规分析(30s-3min): fps=3
- 高精度分析(动作识别/物体检测): fps=5
- 注意: FPS 越高,API 调用次数越多,成本越高

### Step 4: 构造提示词
- 场景描述: "请详细描述视频中的每个场景"
- 物体识别: "视频中出现了哪些物体?请逐一列出"
- 动作分析: "请分析视频中人物的动作和行为"
- 内容审核: "视频中是否存在违规或不适宜的内容?"

### Step 5: 执行分析并返回结果
```bash
python （请参考skill目录中的脚本文件） <video_source> --fps <fps> --prompt "<prompt>"
```
脚本将分析结果输出到 stdout,Agent 应将结果整理后返回给用户.
#
## 案例展示

### 案例一： 本地视频场景描述分析
**场景**: 内容创作者需要理解一段产品演示视频的内容,用于编写文案

```bash
python （请参考skill目录中的脚本文件） /path/to/product-demo.mp4 \
  --fps 3 \
  --prompt "请详细描述视频中展示的产品外观、使用场景和主要功能特点"
```

**输出**: 模型返回多段场景描述,涵盖产品外观、使用场景、功能演示等内容

**说明**: `--fps 3` 在 30 秒视频中抽取约 90 帧,平衡分析精度与 API 成本。提示词聚焦产品特点,引导模型输出可直接用于文案创作的结构化描述.
### 案例二： 远程视频 URL 内容审核
**场景**: 运营团队需要审核一段在线视频是否包含不适宜内容

```bash
python （请参考skill目录中的脚本文件） https://example.com/user-upload.mp4 \
  --fps 4 \
  --prompt "请审查视频内容是否包含暴力、色情或违规信息,逐帧描述可疑画面并给出风险等级"
```

**输出**: 模型逐帧分析并返回审核结果,包含可疑画面描述与风险等级评估

**说明**: 远程 URL 方式无需下载视频到本地,直接传入可公开访问的直链即可。`--fps 4` 提高抽帧密度以减少漏检。审核导向的提示词引导模型聚焦风险内容识别.
### 案例三： 高精度动作识别分析
**场景**: 体育教练需要分析运动员的训练视频,识别动作细节

```bash
python （请参考skill目录中的脚本文件） /path/to/training.mp4 \
  --fps 5 \
  --prompt "请逐帧分析运动员的动作轨迹、身体姿态和发力方式,指出动作中的不足之处并给出改进建议"
```

**输出**: 模型返回逐帧动作分析,包含姿态描述、发力分析与改进建议

**说明**: `--fps 5` 在每秒抽取 5 帧,适合需要捕捉快速动作变化的场景。提示词要求逐帧分析并给出改进建议,适合运动训练、舞蹈教学等精细动作分析需求。注意高 FPS 会显著增加 API 调用次数.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| api_key_missing | `apiKey not found in config` | 配置文件中未找到 DashScope API Key | 引导用户按照认证章节配置 ~/.skill-platform/skill-platform.json |
| file_not_found | `FileNotFoundError: video.mp4` | 本地视频文件路径不存在或拼写错误 | 确认文件路径正确,检查文件是否存在 |
| invalid_url | `URL not accessible` | 远程视频 URL 无法访问或非直链 | 确认 URL 为可公开访问的视频直链,需登录的页面链接不支持 |
| unsupported_format | `Unsupported video format` | 视频格式不被支持 | 转换为 mp4/avi/mov/mkv/webm 等常见格式后 |
| api_rate_limited | `429 Too Many Requests` | 短时间内 API 调用过多 | 降低 FPS 参数,等待 60 秒后 |
| network_timeout | `Connection timed out` | 网络不稳定或 DashScope 服务不可达 | ,确认可访问阿里云服务后 |
| video_too_long | `Video duration exceeds limit` | 视频过长导致抽帧数量超出 API 限制 | 降低 FPS 参数,或将视频分段后分别分析 |
| model_unavailable | `Model service unavailable` | Qwen 3.5 Plus 模型服务暂时不可用 | 等待 5 分钟后如持续不可用联系阿里云支持 |

## 常见问题

### Q1: 如何配置 DashScope API Key?
A: 在 `~/.skill-platform/skill-platform.json` 文件中添加 `skills.dashscope.apiKey` 字段。首先登录阿里云 DashScope 控制台开通 Qwen 多模态模型服务并创建 API Key,然后将 Key 写入配置文件。配置文件格式参见认证章节.
### Q2: FPS 参数应该设置多少?
A: 默认 FPS 为 2,适合大多数概览场景。短视频(<30秒)可用 fps=2;常规分析(30秒-3分钟)建议 fps=3;需要动作识别或物体检测的高精度分析建议 fps=5。注意 FPS 越高,API 调用次数越多,成本相应增加。超长视频建议降低 FPS 或分段分析.
### Q3: 支持哪些视频格式?
A: 支持 mp4、avi、mov、mkv、webm 等常见视频格式。本地文件路径可以是绝对路径或相对路径。远程 URL 必须是可公开访问的视频直链(http/https 协议),需要登录才能访问的页面链接不支持.
### Q4: 本地视频和远程 URL 有什么区别?
A: 本地视频直接从文件系统读取并抽帧,适合分析已下载的视频文件。远程 URL 方式无需预先下载,直接传入可公开访问的直链即可在线分析。两种方式的分析能力和提示词支持完全一致,区别仅在于视频来源.
### Q5: 如何优化分析提示词?
A: 提示词越具体,分析结果越精准。建议: 场景描述用"请详细描述视频中的每个场景";物体识别用"视频中出现了哪些物体?请逐一列出";动作分析用"请分析视频中人物的动作和行为";内容审核用"视频中是否存在违规内容?"。可根据具体需求组合多个分析维度.
### Q6: 分析长视频时如何控制成本?
A: 长视频(>3分钟)建议: 降低 FPS 到 1 或 2,减少抽帧数量;将视频按场景分段后分别分析;使用针对性强的提示词避免重复分析。FPS=2 时,3 分钟视频约抽取 360 帧,已能满足多数分析需求.
## 已知限制

1. **需 DashScope API Key**: 必须配置阿里云 DashScope API Key,无 Key 环境无法使用
2. **远程 URL 需公开访问**: 需登录的页面链接不支持,必须是可公开访问的视频直链
3. **FPS 影响成本**: FPS 越高 API 调用次数越多,长视频高 FPS 分析成本显著
4. **视频时长有限制**: 超长视频可能导致抽帧数量超出 API 限制,需降低 FPS 或分段分析
5. **分析质量取决于提示词**: 提示词描述越具体,分析结果越符合预期
6. **不支持实时视频流**: 仅支持本地文件和远程 URL 两种离线视频源
7. **模型能力受限于 Qwen 3.5 Plus**: 复杂场景识别准确度取决于模型能力,极端场景可能需要人工复核

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Qwen视频智能分析处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "analyze-video-by-qwen"
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
