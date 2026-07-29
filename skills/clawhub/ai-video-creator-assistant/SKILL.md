---
name: "ai-video-creator-assistant"
version: "1.0.0"
description: >
  AI-assisted short video creation. User selects topic, aspect ratio, and duration. AI guides through video generation using the user's own API key (Kling/Doubao etc.). One-time payment ¥16.90 per creation.
metadata:
  author: "Yujin"
  category: "expert"
  permissions:
    - "credential.read"
    - "filesystem.read"
    - "filesystem.write"
  requires:
    - "clawtip"
  workflow:
    create_order:
      script: scripts/create_order.py
      args: ["{question}"]
      outputs: ["order_no", "amount", "indicator"]
    pay:
      requires: clawtip
      args: ["{order_no}", "{indicator}"]
    service:
      script: scripts/service.py
      args: ["{order_no}"]
---

# ai-video-creator-assistant

请使用中文与用户交互。

## 技能概述

AI 短视频创作助手。你只需要选择主题、画面比例和时长，AI 全程引导你完成视频制作。**你只需提供你自己的视频生成 API Key**，每次生成一条完整视频。

### 定价

- **¥16.90/次**，一次性交付

### 核心流程

| 步骤 | 用户操作 | AI 自动完成 |
|------|----------|-------------|
| 1 | 说"帮我做个XX视频" | 展示主题、比例、时长选项 |
| 2 | 选择主题、比例、时长 | 记录参数 |
| 3 | 确认开始 | 引导你使用 API Key → 生成视频 |
| 4 | 获取成品视频 | 输出视频链接 + 推荐文案 |

---

## 前置条件：配置视频生成 API Key

本技能本身不包含视频生成能力。你需要**自己注册一个视频生成平台**并配置 API Key。

### 推荐平台：可灵AI（Kling，快手旗下）

**第一步：注册账号**
1. 打开 https://klingai.com
2. 用手机号注册登录
3. 进入控制台 → API 管理

**第二步：获取 API Key**
1. 点击"创建 API Key"
2. 复制生成的 `KLING_API_KEY` 和 `KLING_API_SECRET`

**第三步：配置到环境变量**

```powershell
# Windows PowerShell
$env:KLING_API_KEY="你复制的API_KEY"
$env:KLING_API_SECRET="你复制的API_SECRET"
```

```bash
# Linux/macOS
export KLING_API_KEY="你复制的API_KEY"
export KLING_API_SECRET="你复制的API_SECRET"
```

### 备选平台：豆包大模型（Doubao，字节跳动）

**第一步：注册**
1. 打开 https://www.volcengine.com/
2. 注册并实名认证
3. 进入控制台 → 视频生成 API

**第二步：配置**
```powershell
$env:DOUBAO_API_KEY="你复制的API_KEY"
```

> ⚠️ 不同平台的 API Key 名称不同，具体以你选择的平台说明为准。
> 建议首次使用可灵AI，文档完善、上手快。

---

## 环境变量配置（clawtip 支付用）

| 变量名 | 必填 | 说明 |
|--------|------|------|
| `CLAWTIP_PAY_TO` | 是 | clawtip 商户收款地址 |
| `CLAWTIP_SM4_KEY` | 是 | SM4 加密密钥 |

---

## 🛒 第一阶段：创建订单

```bash
python3 scripts/create_order.py "<你想做的视频描述>"
```

**成功：** `ORDER_NO=... AMOUNT=... INDICATOR=...`
**失败：** `Order creation failed: <详情>` → 终止。

---

## 💳 第二阶段：支付处理

```bash
npx --yes @clawtip/clawtip-sandbox-cli@1.0.0 pay -o <ORDER_NO> -i <INDICATOR> -v 1.0.12
```

生产环境调用 **clawtip** 钱包：`{"orderNo": "<ORDER_NO>", "indicator": "<INDICATOR>"}`

---

## 🚀 第三阶段：视频创作

```bash
python3 scripts/service.py "<order_no>"
```

成功后 AI 在对话中引导你完成完整的视频创作流程。

---

## 主题预设库

| # | 主题 | 描述 |
|---|------|------|
| 1 | 🐶 狗狗做饭 | 泰迪穿围裙做川菜 |
| 2 | 🐱 猫咪对话 | 方言对话搞笑 |
| 3 | 🐕 萌宠日常 | 小狗拆家片段 |
| 4 | 🐾 宠物变装 | 动物穿衣服走秀 |
| 5 | 🎨 自定义 | 你描述，AI 辅助生成 |

---

## 数据处理说明

### 本地存储
| 文件 | 路径 | 内容 |
|------|------|------|
| 订单文件 | `~/.openclaw/skills/orders/{indicator}/{order_no}.json` | 支付验证字段 |

### 远程传输
本技能自身不发起远程 HTTP 请求。视频由用户配置的 API Key 对应的平台生成，数据传输由用户与该平台之间直接完成，本技能不介入。

### 绝不收集或传输
视频内容、用户 API Key、平台账号凭据。

---

## 版本历史

| Version | Date | Notes |
|:--------|:-----|:------|
| 1.0.0 | 2026-07-28 | Initial release: guided short video creation with user-provided API Key |
