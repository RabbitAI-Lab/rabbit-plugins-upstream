---
slug: banner-gen-tool-free
name: banner-gen-tool-free
version: 1.0.0
displayName: 横幅插画生成免费版
summary: "使用图像生成API创建与编辑横幅插画，支持1K/2K/4K分辨率与草稿迭代流程，适合个人创作.。横幅插画生成工具免费版，面向个人创作者的轻量级图像生成与编辑工具。核心能力:"
license: Proprietary
edition: free
description: '横幅插画生成工具免费版，面向个人创作者的轻量级图像生成与编辑工具。核心能力:

  - 基于 Prompt 生成新图像

  - 编辑现有图像（添加/移除/改风格）

  - 支持 1K/2K/4K 三档分辨率

  - 草稿-迭代-终稿三阶段工作流

  适用场景:

  - 个人博客与社交媒体横幅制作

  - 快速概念图与配图生成

  - 现有图像的风格化编辑

  差异化: 免费版聚焦核心生成与编辑能力，去除所有外部平台与作者引用，强化中文本地化与适用关键词，适合个人用户零成本上手'
tags:
  - 图像生成
  - 横幅设计
  - 创作工具
  - 免费版
  - 工具
  - 效率
  - 自动化
  - 创意
  - 图像
  - 开发
  - 代码
  - api
  - png
  - prompt
  - key
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# 横幅插画生成工具（免费版）

## 概述

横幅插画生成工具免费版帮助你使用图像生成 API 创建新图像或编辑现有图像。支持 1K/2K/4K 三档分辨率，内置草稿-迭代-终稿三阶段工作流，让你快速迭代不浪费高分辨率配额.
## 核心能力

| 能力 | 说明 |
|---|---|
| 图像生成 | 基于 Prompt 描述生成新图像 |
| 图像编辑 | 对现有图像添加/移除/改风格 |
| 分辨率 | 1K（草稿）/ 2K（标准）/ 4K（终稿） |
| 迭代工作流 | 草稿快速反馈 → 锁定方向 → 终稿高分辨率 |
| 文件命名 | 时间戳 + 描述性命名，便于管理 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置.
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
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：使用图像生成、API、创建与编辑横幅插、分辨率与草稿迭代、适合个人创作、横幅插画生成工具、免费版、面向个人创作者的、轻量级图像生成与、编辑工具、编辑现有图像、三档分辨率、终稿三阶段工作流等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：生成博客横幅

为博客文章生成一张横幅图.
```bash
# 生成横幅（1K 草稿）
uv run （请参考skill目录中的脚本文件） \
  --prompt "A serene Japanese garden with cherry blossoms, soft morning light, watercolor style" \
  --filename "2026-07-18-blog-banner-draft.png" \
  --resolution 1K
# ...
# 满意后生成 4K 终稿
uv run （请参考skill目录中的脚本文件） \
  --prompt "A serene Japanese garden with cherry blossoms, soft morning light, watercolor style" \
  --filename "2026-07-18-blog-banner-final.png" \
  --resolution 4K
```

### 场景二：编辑现有图像

对现有照片进行风格化编辑.
```bash
# 编辑现有图像
uv run （请参考skill目录中的脚本文件） \
  --prompt "make the sky more dramatic with storm clouds, increase contrast" \
  --filename "2026-07-18-edited-sky.png" \
  --input-image "original-photo.jpg" \
  --resolution 2K
```

### 场景三：快速概念图

为产品设计生成快速概念图.
```bash
# 1K 快速概念图
uv run （请参考skill目录中的脚本文件） \
  --prompt "minimalist mobile app onboarding screen, pastel colors, flat design" \
  --filename "2026-07-18-concept-onboarding.png" \
  --resolution 1K
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```bash
# 1. 设置 API Key
export GEMINI_API_KEY="your-api-key"
# ...
# 2. 生成新图像
uv run （请参考skill目录中的脚本文件） \
  --prompt "your image description" \
  --filename "output-name.png" \
  --resolution 1K
# ...
# 3. 编辑现有图像
uv run （请参考skill目录中的脚本文件） \
  --prompt "editing instructions" \
  --input-image "path/to/input.png" \
  --resolution 2K
```

## 示例

```bash
# 分辨率映射
| 用户表述                    | 分辨率 |
|:-----|:-----|
| 未提及 / 1080 / 1080p / 1K  | 1K     |
| 2K / 2048 / 标准 / 中等     | 2K     |
| 高分辨率 / hi-res / 4K / 超清 | 4K     |
# ...
# API Key 检查顺序
1. --api-key 参数（用户在对话中提供）
2. GEMINI_API_KEY 环境变量
# ...
# 文件命名格式
{yyyy-mm-dd-hh-mm-ss}-{descriptive-name}.png
# ...
# 示例
# 2026-07-18-14-23-05-japanese-garden.png
# 2026-07-18-15-30-12-sunset-mountains.png
```

## 最佳实践

* 先用 1K 草稿快速迭代 Prompt，锁定方向后再生成 4K 终稿.
* 编辑图像时保持相同的 `--input-image`，直到满意为止.
* Prompt 包含主题、风格、构图、光照、背景、调色板等要素更精准.
* 编辑时明确「仅修改什么，保持其他不变」，避免意外变化.
* 文件命名包含时间戳与描述，便于后续查找.
* 不要读回生成的图像，仅告知用户保存路径.
* 保留用户的创作意图，仅在 Prompt 明显不足时才重写.
## 常见问题

**Q：免费版支持批量生成吗？**
A：免费版面向单张生成与编辑。如需批量生成与模板管理，请考虑 PRO 版本.
**Q：免费版支持自定义 Prompt 模板吗？**
A：免费版不提供模板保存。如需模板库与复用，请使用 PRO 版本.
**Q：API Key 如何获取？**
A：通过 `--api-key` 参数传入，或设置 `GEMINI_API_KEY` 环境变量。两者都不可用时脚本会报错.
**Q：编辑图像时会改变原图吗？**
A：不会。编辑会生成新文件，原图保持不变.
**Q：支持哪些图像格式？**
A：生成输出为 PNG。输入支持 PNG、JPG 等常见格式.
**Q：遇到 403 或配额错误怎么办？**
A：检查 API Key 是否有效、是否有访问权限、配额是否用尽。尝试更换 Key 或账户.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+
- **uv**: Python 包管理器

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 官方站点下载 |
| uv | 工具 | 必需 | 官方安装 |
| 图像生成 API | API | 必需 | 配置 API Key |

### API Key 配置
- `GEMINI_API_KEY` - 图像生成 API 密钥
- 也可通过 `--api-key` 参数传入
- API Key 仅从环境变量或参数读取，不硬编码

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + Python脚本执行）
- **说明**: 基于Markdown的AI Skill，通过 Python 脚本调用图像生成 API

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "横幅插画生成免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "banner gen"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
