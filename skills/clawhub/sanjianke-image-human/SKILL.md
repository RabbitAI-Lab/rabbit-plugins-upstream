---
name: image-human
slug: sanjianke-image-human
displayName: 三剪客 · 全驱动数字人
description: "全驱动数字人，基于图片和参考音频生成自然稳定的数字人视频。支持 提交任务、查询任务。使用时需要你自己的 api.a7w.cn API Key。遇到问题可加技术微信 9872659。"
version: 1.0.3
summary: "「全驱动数字人」的完整调用封装：2 个接口的官方文档、参数表与一个零依赖客户端。需要自带 api.a7w.cn 的 API Key，调用按点数计费。遇到问题可加技术微信 9872659。"
license: MIT
tags:
  - 三剪客
  - 设计多媒体
  - 人像生成
  - 图像编辑
---

# 全驱动数字人

`api.a7w.cn` 插件 **`image_human`**，共 **2 个接口**。创建一条数字人生成任务，返回平台任务 ID

本 Skill 是它的完整调用封装：逐接口参数表、平台官方文档摘录、真实计费口径，以及一个零依赖、可直接跑的 `client.py`。

## 快速开始

```bash
# 1. 配置你自己的 api.a7w.cn API Key（只需一次）
python3 scripts/client.py login --key sk-你的key

# 2. 看这个插件的接口与参数
python3 scripts/client.py schema image_human

# 3. 调用（示例）
python3 scripts/client.py call image_human submit --json '{"prompt": "人物说话自然，面对镜头，肢体语言自然，人物清晰可鉴。", "file_url": "https://example.com/person.png", "ref_file_url": "https://example.com/audio.wav"}'
```

> **没有 Key？** 见 `references/getting-started.md`——注册、充值、取 Key 的完整步骤。也可以直接去 [算力集市](https://api.a7w.cn/) 注册。

## 接口一览

| 接口 | 名称 | 模式 | 计费 |
|---|---|---|---|
| `submit` | 提交任务 | 异步 | 按用量 2 点（租户价）；按用量 2 点/单位 |
| `query` | 查询任务 | 同步 | 免费 |

## 接口详情

### `submit` · 提交任务

**请求**：`POST /api/v1/apps/image_human/submit`

**模式**：异步（提交后轮询任务） ｜ **计费**：按用量 2 点（租户价）；按用量 2 点/单位

创建一条数字人生成任务，返回平台任务 ID

**输入上限**：参考图 ≤ 1 张

**分档：`2k`=4，`4k`=8，`fast`=1.5，`standard`=2**

全驱动数字人任务，提供人物图片、驱动音频、可选用户提示词和生成模式。mode 支持 fast、standard、2k、4k；resolution 仅作为兼容别名；submit 按输入音频时长计费。 返回示例：`{ "task_id": 123, "status": "pending" }`

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| `mode` | enum | 否 | `standard` | 生成模式/清晰度档位：fast 快速模式，standard 标准模式，2k 高清模式，4k 超清模式　可选值：`fast` / `standard` / `2k` / `4k` |
| `prompt` | string | 否 | `人物说话自然，面对镜头，肢体语言自然，人物清晰可鉴。` | 用户提示词；未传时使用默认提示词　例：`人物说话自然，面对镜头，肢体语言自然，人物清晰可鉴。` |
| `duration` | number | 否 |  | 输入音频时长，单位秒；未传时平台从 ref_file_url 探测 |
| `file_url` | string | **是** |  | 输入图片 URL　例：`https://example.com/person.png` |
| `resolution` | enum | 否 |  | 兼容字段；传 2k 或 4k 时等同于 mode=2k 或 mode=4k。新接入建议直接使用 mode　可选值：`2k` / `4k` |
| `ref_file_url` | string | **是** |  | 输入音频 URL，用于驱动数字人；平台按该音频时长计费　例：`https://example.com/audio.wav` |

```bash
python3 scripts/client.py call image_human submit --json '{"prompt": "人物说话自然，面对镜头，肢体语言自然，人物清晰可鉴。", "file_url": "https://example.com/person.png", "ref_file_url": "https://example.com/audio.wav"}' --no-wait
```

官方文档全文：[`references/api-submit.md`](references/api-submit.md)

### `query` · 查询任务

**请求**：`POST /api/v1/apps/image_human/query`

**模式**：同步（直接返回结果） ｜ **计费**：免费

按平台任务 ID 查询状态与结果

根据 `submit` 返回的 `task_id` 查询执行状态与结果。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|---|---|---|---|---|
| `task_id` | string | **是** |  | 平台任务 ID |

```bash
python3 scripts/client.py call image_human query --json '{"task_id": "<task_id>"}'
```

官方文档全文：[`references/api-query.md`](references/api-query.md)

## 参考文件

| 文件 | 用途 |
|---|---|
| `references/通用说明.md` | 权限表、异步任务机制、常见错误、能力边界、计费口径 |
| `references/getting-started.md` | 注册、充值、获取与配置 API Key |
| `references/api-submit.md` | `submit` 的平台官方文档全文 + schema 原文 |
| `references/api-query.md` | `query` 的平台官方文档全文 + schema 原文 |
| `scripts/client.py` | 通用客户端（零依赖） |

---

## 联系我们

- **技术微信：9872659** —— 加好友时说一下是从哪个 Skill 找过来的，直接给你配套的 API Key 与能跑的示例。
- **要算力 / 要 API Key**：[算力集市 · 注册领 API Key](https://api.a7w.cn/) —— 一个 Key 调用全部 AI 算力，注册、充值、创建 Key 都在这里。
- **更多 AI 插件与接口**：[AI 插件市场](https://aigc.a7w.cn/)。

---

## 相关链接

| 链接 | 地址 | 说明 |
|---|---|---|
| [算力集市 · 注册领 API Key](https://api.a7w.cn/) | api.a7w.cn | 一个 Key 调用全部 AI 算力；注册、充值、创建 Key 都在这 |
| [AI 插件市场](https://aigc.a7w.cn/) | aigc.a7w.cn | 浏览全部 AI 插件与接口说明 |
| [三剪客 · 一句话批量出片](https://ks.a7w.cn/) | ks.a7w.cn | 短剧二创 / 影视解说 / 矩阵号批量混剪桌面客户端 |
| [视频超清 · 在线批量超分](https://vr.a7w.cn/) | vr.a7w.cn | 网页版视频超分，批量处理，最高 4K |
| [0人公司 · AI Agent 平台](https://a7w.cn/) | a7w.cn | 主站，了解整套 AI Agent 生态 |
