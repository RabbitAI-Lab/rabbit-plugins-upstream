# 免费生图生视频（free-media-gen）

## 简介（中文）

**free-media-gen** 是一个统一的免费文生图 / 文生视频入口。它直接调用你已在 WorkBuddy「自定义模型」中配置好的第三方**免费**模型——Agnes、商汤 SenseNova、硅基流动 Kolors——来生成图片与视频，**刻意绕过内置的混元 ImageGen**，因此产出**不带 "Workbuddy" 水印**，用哪个后端完全由你决定。

核心特性：

- **免费优先**：只聚合实测可用的免费模型（Agnes 图+视频、商汤 U1.5 Lite / U1 Fast 图、Kolors 图）；Gemini 图像因免费配额为 0 已标记不可用。
- **无水印**：全部走自带 Python 脚本直连第三方端点，不经混元，不出平台水印。
- **密钥复用**：媒体模型复用 `models.json` 中已有的平台密钥，不重复保存明文。
- **开箱即用**：运行时自动解析配置根 / 工作区根，无硬编码绝对路径，任何用户安装即用。
- **首装引导**：未检测到可用密钥时，输出 4 家免费平台申请地址，而非空跑报错。
- **按需审计**：一级命令可触发模型清单审计，输出带日期的 Markdown 报告。

### 快速开始

```
打开免费生媒体                       # 一级命令：列出可用模型并选择
用 Agnes 生图 一只赛博朋克风格的猫      # 二级命令：直接执行
用 Agnes 生视频 从航母上看海上日出      # 支持 720P 横版视频
```

### 适用对象

面向 WorkBuddy 的「自定义模型」注册表（`models.json`）设计。若你在其他 OpenClaw 客户端使用，
将各平台 API 密钥以相同结构写入 `~/.workbuddy/models.json`（含 `id` / `url` / `apiKey`）即可复用。

---

## Introduction (English)

**free-media-gen** is a unified, free text-to-image / text-to-video entry point. It calls the
**free** third-party models you already configured in WorkBuddy's custom-models registry
(`models.json`) — Agnes, SenseNova (Shanghai AI Laboratory / SenseTime), and SiliconFlow Kolors —
to generate images and video. It **deliberately bypasses the built-in Hunyuan ImageGen**, so outputs
carry **no "Workbuddy" watermark**; you choose the backend.

Key features:

- **Free-first**: aggregates only verified-free models (Agnes image+video, SenseNova U1.5 Lite / U1 Fast image, Kolors image). Gemini image is flagged unavailable (free quota measured at 0).
- **No watermark**: all generation runs through bundled Python scripts that call third-party endpoints directly — no Hunyuan, no platform watermark.
- **Key reuse**: media models reuse the platform keys already present in `models.json`; no duplicate plaintext secrets.
- **Portable**: resolves config / workspace roots at runtime; no hardcoded absolute paths, works for any user out of the box.
- **First-run guidance**: when no usable key is detected, prints application links for 4 free platforms instead of failing silently.
- **On-demand audit**: the top-level command can trigger a model-list audit that writes a dated Markdown report.

### Quick start

```
打开免费生媒体                       # top-level: list available models and choose
用 Agnes 生图 一只赛博朋克风格的猫      # sub-command: run immediately
用 Agnes 生视频 从航母上看海上日出      # 720P landscape video supported
```

### Who it is for

Designed for WorkBuddy's custom-models registry (`models.json`). On other OpenClaw clients, write
each platform's API key into `~/.workbuddy/models.json` using the same shape (`id` / `url` / `apiKey`)
and the whole flow is reusable.

---

## 元数据 / Metadata

- **Slug**: `free-media-gen`
- **Version**: `1.0.0`
- **License**: MIT
- **Runtime**: Python 3 (standard library only, no third-party install)
- **Category**: productivity
- **Tags**: #workbuddy #free-media-gen #image-generation #text-to-video #free-api
- **Supported OS**: windows / macos / linux
