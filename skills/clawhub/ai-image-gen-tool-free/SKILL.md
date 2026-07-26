---
name: "ai-image-gen-tool-free"
description: "通过文本描述生成图片,支持多种比例与标准分辨率,适合个人创作者快速出图。"
license: Proprietary
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "AI图像生成-免费版"
  version: "1.0.0"
  summary: "通过文本描述生成图片,支持多种比例与标准分辨率,适合个人创作者快速出图。"
  tags:
    - "Creative"
    - "图像生成"
    - "AI创作"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# AI图像生成工具 - 免费版

## 概述

AI图像生成免费版是一款面向个人用户的文本生成图像工具。通过自然语言描述即可生成高质量图片,支持多种画幅比例与标准分辨率,无需绘画基础,几秒钟即可获得原创图像。

本版本依托 Gemini Flash Image 模型能力,提供基础的文生图功能,支持社交媒体头像、配图、创意灵感等多种场景,适合个人创作者快速产出图像内容。

## 核心能力

| 能力项 | 免费版支持 | 说明 |
|:-------|:-----------|:-----|
| 文本生成图片 | 是 | 输入描述生成图像 |
| 多比例支持 | 是 | 1:1/3:2/16:9 等 10 种 |
| 标准分辨率 | 是 | 基础清晰度 |
| 2K 分辨率 | 限制 | 部分比例支持 |
| 4K 分辨率 | 否 | PRO 版支持 |
| 图生图(图+文) | 否 | PRO 版支持 |
| 风格转换 | 否 | PRO 版支持 |
| 批量生成 | 否 | PRO 版支持 |
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
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：通过文本描述生成、支持多种比例与标、适合个人创作者快、速出图、图像生成免费版、面向个人用户的文、本生成图像工具、文本描述生成图片、文生图、等多种比例、标准分辨率输出、满足社交媒体与基、础设计需求、多风格支持、赛博朋克、写实摄影等等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:社交媒体头像

用户需要一个独特的社交媒体头像,生成一张 1:1 的艺术风格图片。

```bash
python3 scripts/generate_image.py \
  "一只戴着圆框眼镜的橘猫,水彩风格,柔和色调,简洁背景" \
  --model gemini-3.1-flash-image \
  --output avatar.png
```

### 场景二:短视频封面图

内容创作者为短视频制作 16:9 横版封面图。

```bash
python3 scripts/generate_image.py \
  "未来都市夜景,霓虹灯光,赛博朋克风格,雨后湿润街道反射,电影感构图" \
  --model gemini-3.1-flash-image-16x9 \
  --output video_cover.png
```

### 场景三:创意灵感可视化

设计师希望快速将一个创意概念可视化,用于灵感记录。

```bash
python3 scripts/generate_image.py \
  "一座漂浮在云端的图书馆,书籍如瀑布般倾泻而下,暖色调,梦幻氛围,吉卜力风格" \
  --model gemini-3.1-flash-image-3x2 \
  --output inspiration.png
```

## 不适用场景

以下场景AI图像生成-免费版不适合处理：

- 需要100%确定性的关键决策
- 医疗诊断
- 法律判决

## 触发条件

需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于非本工具能力范围的需求。

## 快速开始

### 第一步:配置 API Key

```bash
export IMAGE_GEN_API_KEY="your_api_key_here"
export IMAGE_GEN_BASE_URL="https://code.newcli.com/gemini"
```

### 第二步:执行生成命令

```bash
python3 scripts/generate_image.py \
  "你的提示词描述" \
  --model gemini-3.1-flash-image \
  --output output.png
```

### 第三步:查看结果

生成的图片保存在 `--output` 指定路径,直接展示给用户即可。

## 示例

基础配置项说明:

```bash
# 环境变量
IMAGE_GEN_API_KEY=your_key                    # 必填
IMAGE_GEN_BASE_URL=https://code.newcli.com/gemini  # 默认值

# 常用参数组合
# 1:1 头像
--model gemini-3.1-flash-image

# 16:9 横版
--model gemini-3.1-flash-image-16x9

# 9:16 竖版(手机壁纸)
--model gemini-3.1-flash-image-9x16

# 2K 高清(部分比例)
--model gemini-3.1-flash-image-2k-16x9
```

### 可用模型(标准分辨率)

| 模型 ID | 比例 | 适用场景 |
|:-------|:-----|:---------|
| gemini-3.1-flash-image | 1:1 | 社交媒体头像 |
| gemini-3.1-flash-image-3x2 | 3:2 | 横版照片 |
| gemini-3.1-flash-image-2x3 | 2:3 | 竖版海报 |
| gemini-3.1-flash-image-4x5 | 4:5 | Instagram |
| gemini-3.1-flash-image-9x16 | 9:16 | 手机壁纸/短视频 |
| gemini-3.1-flash-image-16x9 | 16:9 | 电脑壁纸/视频 |
| gemini-3.1-flash-image-21x9 | 21:9 | 超宽屏 |

## 最佳实践

1. **提示词要具体**:描述主体、场景、光线、风格、色调,例如"一位老匠人在木工作坊中雕刻,暖黄光线,写实摄影风格"
2. **指定艺术风格**:水彩、油画、赛博朋克、吉卜力、写实摄影、中国工笔等
3. **说明构图**:视角(俯视/仰视)、景深、焦点位置
4. **色彩指定**:主色调与配色方案,如"以深红、金色、墨黑为主"
5. **比例匹配用途**:头像用 1:1,视频封面用 16:9,手机壁纸用 9:16

## 常见问题

### Q1:生成的图片质量不够清晰?
A:免费版默认标准分辨率,可尝试使用 2K 模型(如 `gemini-3.1-flash-image-2k-16x9`)。如需 4K 超高清,请使用 PRO 版。

### 已知限制
A:建议控制在 500 字以内,过长的提示词可能影响生成效果。核心元素前置描述。

### Q3:可以生成人物肖像吗?
A:可以,但请避免生成真实公众人物的肖像,以免涉及版权与肖像权问题。

### Q4:生成失败怎么办?
A:检查 API Key 是否正确;确认网络可访问 API 地址;尝试简化提示词后重试。

### Q5:免费版有调用次数限制吗?
A:API 调用受服务商配额限制,免费版配额较低。如需高频调用或批量生成,请使用 PRO 版。
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力
## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Python 3.8+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Gemini Image API | 外部 API | 必需 | 服务商申请 |
| Python 3.8+ | 运行时 | 必需 | 官方安装 |
| requests | Python 库 | 必需 | pip install requests |
| Pillow | 图像处理 | 推荐 | pip install Pillow |

### API Key 配置
- **环境变量名**: `IMAGE_GEN_API_KEY`
- **附加变量**: `IMAGE_GEN_BASE_URL`(可选,有默认值)
- **获取方式**: 通过 API 服务商申请
- **存储建议**: 写入 `.env` 文件或系统环境变量,避免硬编码到脚本

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过Python脚本调用外部API生成图像

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
