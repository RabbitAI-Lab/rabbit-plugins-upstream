---
slug: "analyze-video-by-qwen-free"
name: "analyze-video-by-qwen-free"
version: "1.0.0"
displayName: "Qwen视频分析LITE"
summary: "Qwen多模态模型视频分析基础版,支持本地视频文件场景描述与内容理解"
license: "MIT"
description: |-
  Qwen 视频智能分析基础客户端(免费版)。基于 Qwen 3.5 Plus 多模态模型对本地视频文件进行内容分析,
  支持场景描述与基础内容理解。使用默认抽帧频率与默认提示词,适合快速概览视频内容.
  API Key 从 ~/.skill-platform/skill-platform.json 的 skills.dashscope.apiKey 字段读取.
  适用于个人创作者快速理解视频内容、学习试用多模态分析能力.
tags:
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Qwen 视频分析 LITE

Qwen 视频智能分析基础版,基于 Qwen 3.5 Plus 多模态模型对本地视频文件进行内容分析。仅支持本地文件输入与默认分析参数.
**范围外**(本技能不做): 远程 URL 在线分析、自定义抽帧频率(FPS)、自定义分析提示词、高精度动作识别、内容审核(需升级付费版).
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Qwen视频分析LITE处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

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
| dashscope SDK | Python 库 | 必需 | pip install dashscope |

### 可用性分类
- **分类**: MD+EXEC(Markdown 指令驱动,需 exec 执行 Python 脚本)
- **说明**: 基于自然语言指令驱动 Agent 调用 Qwen 多模态 API,完成基础视频分析

## 核心能力

本工具的核心能力包括：Qwen多模态模型视频分析基础版,支持本地视频文件场景描述与内容理解。具体功能详情请参考下方能力说明表格与使用场景.
## 认证

API Key 从 `~/.skill-platform/skill-platform.json` 的 `skills.dashscope.apiKey` 字段读取.
```bash
cat ~/.skill-platform/skill-platform.json | grep apiKey
```

若 Key 缺失,引导用户:
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
## 基础用法

使用默认参数分析本地视频文件(FPS=2,默认提示词"这段视频描绘的是什么景象?"):

```bash
python （请参考skill目录中的脚本文件） /path/to/video.mp4
```

脚本将分析结果输出到 stdout,Agent 应将结果整理后返回给用户.
> **升级提示**: 自定义提示词、自定义抽帧频率(FPS)、远程 URL 在线分析等高级能力仅在 analyze-video-by-qwen 付费版中提供.
## 适用场景

| 场景 | 典型输入 | 输出内容 |
|---:|---:|---:|
| 本地视频内容概览 | "分析这个视频里发生了什么" | 场景描述与内容摘要 |
| 短视频快速理解 | "看看这段视频讲了什么" | 视频内容描述 |

**不适用于**: 远程 URL 分析、高精度动作识别、内容审核、自定义提示词分析(需升级付费版)

## 使用流程

### Step 1: 校验 API Key 配置
```bash
cat ~/.skill-platform/skill-platform.json | grep apiKey
```
若返回为空或文件不存在,按照认证章节引导用户配置.
### Step 2: 确认视频文件
确认本地视频文件路径存在且为支持的视频格式(mp4/avi/mov/mkv/webm 等).
### Step 3: 执行分析
```bash
python （请参考skill目录中的脚本文件） /path/to/video.mp4
```
使用默认 FPS=2 和默认提示词进行分析,结果输出到 stdout.
#
## 案例展示

### 案例一： 本地视频内容概览
**场景**: 用户需要快速了解一段本地视频的内容

```bash
python （请参考skill目录中的脚本文件） /path/to/video.mp4
```

**输出**: 模型返回视频场景描述,概括视频主要内容

**说明**: 使用默认参数(FPS=2,默认提示词),适合快速概览短视频内容。FPS=2 在每秒抽取 2 帧,平衡分析速度与内容覆盖度.
### 案例二： 产品演示视频理解
**场景**: 创作者需要理解一段产品演示视频的内容概要

```bash
python （请参考skill目录中的脚本文件） /path/to/product-demo.mp4
```

**输出**: 模型返回视频内容描述,涵盖产品展示场景与主要功能

**说明**: 默认提示词"这段视频描绘的是什么景象?"适合通用场景理解。如需聚焦产品特点的定制化分析,需升级付费版使用自定义提示词功能.
## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| api_key_missing | `apiKey not found in config` | 配置文件中未找到 DashScope API Key | 引导用户按照认证章节配置 ~/.skill-platform/skill-platform.json |
| file_not_found | `FileNotFoundError: video.mp4` | 本地视频文件路径不存在 | 确认文件路径正确,检查文件是否存在 |
| unsupported_format | `Unsupported video format` | 视频格式不被支持 | 转换为 mp4/avi/mov/mkv/webm 等常见格式后检查网络连接和配置后重试 |
| api_rate_limited | `429 Too Many Requests` | 短时间内 API 调用过多 | 等待 60 秒后检查网络连接和配置后重试 |
| network_timeout | `Connection timed out` | 网络不稳定或 DashScope 服务不可达 | 检查网络连接和配置后重试,确认可访问阿里云服务后检查网络连接和配置后重试 |

## 常见问题

### Q1: 如何配置 DashScope API Key?
A: 在 `~/.skill-platform/skill-platform.json` 文件中添加 `skills.dashscope.apiKey` 字段。首先登录阿里云 DashScope 控制台开通 Qwen 多模态模型服务并创建 API Key,然后将 Key 写入配置文件.
### Q2: 支持哪些视频格式?
A: 支持 mp4、avi、mov、mkv、webm 等常见视频格式。本地文件路径可以是绝对路径或相对路径。免费版仅支持本地文件,不支持远程 URL(需升级付费版).
### Q3: 免费版和付费版有什么区别?
A: 免费版(LITE)支持本地视频文件的默认参数分析(FPS=2,默认提示词)。付费版(analyze-video-by-qwen)额外提供:
- 远程 URL 在线视频分析
- 自定义抽帧频率(--fps 参数,1-5 可调)
- 自定义分析提示词(--prompt 参数)
- 高精度动作识别与内容审核
- 3 个完整案例(vs 免费版 2 个基础案例)
- 8 种错误处理(vs 免费版 5 种)

### Q4: 分析结果不够详细怎么办?
A: 免费版使用默认提示词"这段视频描绘的是什么景象?",提供通用场景描述。如需针对特定维度(产品特点、动作细节、违规内容等)的定制化分析,需升级付费版使用自定义提示词功能.
## 已知限制

1. **仅支持本地文件**: 不支持远程 URL 在线分析(需升级付费版)
2. **固定 FPS=2**: 不支持自定义抽帧频率(需升级付费版)
3. **固定默认提示词**: 不支持自定义分析提示词(需升级付费版)
4. **需 DashScope API Key**: 必须配置阿里云 DashScope API Key
5. **分析质量取决于模型能力**: 复杂场景识别准确度受限于 Qwen 3.5 Plus 模型能力

---

> **想要远程 URL 分析、自定义提示词与抽帧频率?** 升级到 [analyze-video-by-qwen 付费版](#) 解锁全部高级能力.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Qwen视频分析LITE处理结果",
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
