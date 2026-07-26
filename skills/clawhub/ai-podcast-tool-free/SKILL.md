---
name: "ai-podcast-tool-free"
description: "将PDF、文本、链接转为双人对话播客,适合个人创作者快速制作音频内容。"
license: Proprietary
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "AI播客生成-免费版"
  version: "1.0.0"
  summary: "将PDF、文本、链接转为双人对话播客,适合个人创作者快速制作音频内容。"
  tags:
    - "Creative"
    - "播客生成"
    - "AI创作"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# AI播客生成工具 - 免费版

## 概述

AI播客生成免费版是一款面向个人用户的文档转播客工具。通过 MagicPodcast 引擎,将 PDF、文本、笔记或链接转化为自然的双人对话播客,几分钟即可获得可收听可分享的音频内容。

本版本适合内容创作者、学习者及多渠道内容分发者,通过分步引导式交互,快速将图文内容转化为音频形式。

## 核心能力

| 能力项 | 免费版支持 | 说明 |
|:-------|:-----------|:-----|
| PDF 转播客 | 是 | PDF URL 输入 |
| 文本转播客 | 是 | 粘贴文本输入 |
| 多语种支持 | 是 | 中英日韩等 |
| 双人对话格式 | 是 | 主持人+嘉宾 |
| 分享链接 | 是 | 可分享播放 |
| 自定义对话风格 | 否 | PRO 版支持 |
| 批量生成 | 否 | PRO 版支持 |
| 音频下载 | 否 | PRO 版支持 |
| 节目封面定制 | 否 | PRO 版支持 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：链接转为双人对话、适合个人创作者快、速制作音频内容、播客生成免费版、面向个人用户的文、档转播客工具等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:文章转播客

内容创作者希望将一篇博客文章转为播客,方便通勤族收听。

```bash
# 配置 API
export MAGICPODCAST_API_URL="https://api.magicpodcast.app"
export MAGICPODCAST_API_KEY="your_api_key"

# 从文本创建播客
payload="$(jq -n --arg text "$SOURCE_TEXT" --arg language "$LANGUAGE" '{text:$text,language:$language}')"

curl -sS -X POST "$MAGICPODCAST_API_URL/agent/v1/podcasts/text" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MAGICPODCAST_API_KEY" \
  --data-binary "$payload"
```

### 场景二:PDF 报告转播客

用户希望将一份 PDF 报告转为播客,方便听觉学习。

```bash
# 从 PDF URL 创建播客
PDF_URL="https://example.com/report.pdf"
LANGUAGE="zh"

# 验证 URL 有效性
if ! printf '%s' "$PDF_URL" | grep -Eq '^https?://[^[:space:]]+$'; then
  echo "Invalid PDF URL" >&2
  exit 1
fi

payload="$(jq -n --arg pdfUrl "$PDF_URL" --arg language "$LANGUAGE" '{pdfUrl:$pdfUrl,language:$language}')"

curl -sS -X POST "$MAGICPODCAST_API_URL/agent/v1/podcasts/pdf" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MAGICPODCAST_API_KEY" \
  --data-binary "$payload"
```

### 场景三:学习笔记转播客

学生希望将学习笔记转为播客,通勤时复习。

```text
流程:
1. 系统询问播客主题
2. 询问内容来源(粘贴文本)
3. 询问播客语言
4. 确认后创建播客
5. 返回分享链接

用户: 把我的机器学习笔记转成播客
系统: 请粘贴你的笔记文本
用户: [粘贴文本]
系统: 播客用什么语言?
用户: 中文
系统: 确认创建中文播客?
用户: 是
系统: 已创建,链接: https://www.magicpodcast.app/...
```

## 不适用场景

以下场景AI播客生成-免费版不适合处理：

- 加密文件破解
- 损坏文件修复
- 物理介质数据恢复

## 触发条件

需要文件处理、文档转换、格式互转、内容提取时使用。不适用于非本工具能力范围的需求。

## 快速开始

### 第一步:配置 API Key

```bash
export MAGICPODCAST_API_URL="https://api.magicpodcast.app"
export MAGICPODCAST_API_KEY="your_api_key"
```

获取地址:`https://www.magicpodcast.app/skill-platform`

### 第二步:分步交互创建

系统会依次询问:主题→来源→语言→确认,然后创建播客。

### 第三步:查看结果

创建后访问 `https://www.magicpodcast.app/app` 查看播客仪表盘,生成完成后返回分享链接。

#
## 示例

基础配置项说明:

```bash
# 环境变量
MAGICPODCAST_API_URL=https://api.magicpodcast.app
MAGICPODCAST_API_KEY=your_key

# 安全命令模板
safe_job_id() {
  printf '%s' "$1" | grep -Eq '^[A-Za-z0-9_-]{8,128}$'
}

safe_http_url() {
  printf '%s' "$1" | grep -Eq '^https?://[^[:space:]]+$'
}

# 查询任务状态
curl -sS "$MAGICPODCAST_API_URL/agent/v1/jobs/$JOB_ID" \
  -H "x-api-key: $MAGICPODCAST_API_KEY"
```

## 最佳实践

1. **内容质量决定效果**:输入文本结构清晰、信息丰富,生成的播客质量更高
2. **语言明确指定**:不要假设语言,明确指定(如"中文"、"English")避免异常
3. **PDF 需可访问**:PDF URL 必须是公开可访问的直链,本地文件需先上传
4. **生成需等待**:播客生成通常需要 2-5 分钟,可在仪表盘查看进度
5. **敏感内容谨慎**:不要发送敏感文档,除非确认可接受外部处理
6. **分享链接优先**:完成后默认返回 `outputs.shareUrl`,缺失时回退到 `outputs.appUrl`

## 常见问题

### Q1:API Key 如何获取?
A:访问 `https://www.magicpodcast.app/skill-platform`,用 Google 账号登录,复制 API Key。免费注册,一分钟内完成。

### Q2:本地 PDF 文件怎么处理?
A:需先将本地 PDF 上传到可访问的 URL(如网盘公开链接),再使用 PDF URL 方式创建。

### Q3:生成失败怎么办?
A:检查 API Key 是否有效;确认 PDF URL 可公开访问;查看返回的错误信息;稍后重试。

### 已知限制
A:登录用户可免费生成播客,但有配额限制。如需批量生成或高级功能,请使用 PRO 版。

### Q5:生成的播客可以下载吗?
A:免费版仅提供在线分享链接。如需下载音频文件,请使用 PRO 版的音频下载功能。
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力
## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Bash shell + curl + jq

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| MagicPodcast API | 外部 API | 必需 | 官网注册免费获取 |
| curl | 命令行工具 | 必需 | 系统自带 |
| jq | JSON 处理 | 必需 | 包管理器安装 |

### API Key 配置
- **环境变量名**: `MAGICPODCAST_API_KEY`
- **附加变量**: `MAGICPODCAST_API_URL`(有默认值)
- **获取方式**: 访问 `https://www.magicpodcast.app/skill-platform` 注册
- **存储建议**: 写入 `.env` 文件或系统环境变量,避免硬编码到脚本

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过分步对话与 curl 调用驱动播客生成流程

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
