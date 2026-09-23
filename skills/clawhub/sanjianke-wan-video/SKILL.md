---
name: wan-video
slug: sanjianke-wan-video
displayName: 三剪客 · Wan 视频生成
description: "Wan 模型族视频生成应用。版本通过 model 参数选择，支持文生视频、角色参考生视频与视频编辑。支持 查询视频任务、创建视频任务。使用时需要你自己的 api.a7w.cn API Key。遇到问题可加技术微信 9872659。"
version: 1.0.5
summary: "「Wan 视频生成」的完整调用封装：2 个接口的官方文档、参数表与一个零依赖客户端。需要自带 api.a7w.cn 的 API Key，调用按点数计费。遇到问题可加技术微信 9872659。"
license: MIT
tags:
  - 三剪客
  - 设计多媒体
  - 视频生成
  - 文生视频
---

# Wan 视频生成

Wan 模型族视频生成应用。版本通过 model 参数选择，支持文生视频、角色参考生视频与视频编辑。

## 权限与用途说明

| 能力 | 是否申请 | 用途 |
|---|---|---|
| 网络访问 | **申请** | 调用 `api.a7w.cn` 的插件接口（本 Skill 唯一的联网行为） |
| 读取文件 | 仅读取用户指定的输入文件（图片/音频/视频） | 作为接口的素材入参 |
| 写入文件 | 仅在传入 `--out` 时 | 保存接口返回的 JSON 结果 |
| 凭证 | 读取**使用者自己**提供的 API Key | 从 `~/.a7w/config.json` 或环境变量读取 |
| 子进程 / 后台常驻 | 不申请 | 脚本执行完即退出 |

**不内嵌任何密钥。** 脚本只把 Key 发往 `api.a7w.cn`，不发送到其他任何地址。

## 快速开始

```bash
# 1. 配置你自己的 api.a7w.cn API Key（只需一次）
python3 scripts/client.py login --key sk-你的key

# 2. 看这个插件的接口与参数
python3 scripts/client.py schema wan

# 3. 调用（示例）
python3 scripts/client.py call wan query --json '{}'
```

> **没有 Key？** 见 `references/getting-started.md`——注册、充值、取 Key 的完整步骤。也可以直接去 [算力集市](https://api.a7w.cn/) 注册。

## 接口一览

| 接口 | 名称 | 模式 | 计费 | 说明 |
|---|---|---|---|---|
| `query` | 查询视频任务 | 同步 | 免费（查询类接口） | 按平台 task_id 查询 Wan 任务状态与结果。 |
| `create` | 创建视频任务 | 异步（需轮询） | 免费（查询类接口） | 提交 Wan 视频生成任务。model 用于选择 Wan 版本与能力。 |

## 接口详情

### `query` · 查询视频任务

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`GET /api/v1/apps/wan/query`

按平台 task_id 查询 Wan 任务状态与结果。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `task_id` | string | 是 | 创建任务后返回的平台任务 ID。（示例：task_xxxxxxxxxxxx） |

完整文档（含请求/响应示例）：[`references/api-query.md`](references/api-query.md)

### `create` · 创建视频任务

**模式**：异步（提交后轮询任务） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/wan/create`

提交 Wan 视频生成任务。model 用于选择 Wan 版本与能力。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `seed` | integer | 否 | 随机种子，用于结果复现。范围：0-2147483647。 |
| `size` | string | 否 | 视频画幅比例。（示例：16:9） |
| `model` | string | 是 | Wan 模型版本。不同版本支持的素材输入略有差异。（示例：wan2.7） |
| `prompt` | string | 是 | 视频画面与运动描述。（示例：一辆复古跑车沿着海岸公路行驶，电影感光影） |
| `duration` | integer | 否 | 生成视频时长，单位秒。wan2.7、wan2.7-r2v 支持 2-15；wan2.7-videoedit 支持 2-10。（示例：5） |
| `metadata` | object | 否 | 附加业务信息。wan2.7-videoedit 可在 metadata.audio_setting 中选择音频处理方式。（示例：{'biz_id': 'order_1001', 'audio_setting': 'auto'}） |
| `audio_url` | string | 否 | 参考音频 URL。需要音频驱动生成时传入。（示例：https://example.com/audio.mp3） |
| `watermark` | boolean | 否 | 是否添加水印。（示例：） |
| `image_urls` | array | 否 | 参考图片 URL 列表。wan2.7 最多 2 张；wan2.7-videoedit 最多 4 张。（示例：['https://example.com/reference.png']） |
| `resolution` | string | 否 | 输出分辨率。（示例：720p） |
| `video_urls` | array | 否 | 视频素材地址列表，最多 1 段。wan2.7-videoedit 必填，并按含视频输入档计费。（示例：['https://example.com/input.mp4']） |
| `callback_url` | string | 否 | 任务完成或失败时由平台主动通知的 HTTPS 地址。（示例：https://your-domain.com/webhook/wan） |
| `prompt_extend` | boolean | 否 | 是否启用提示词扩展。（示例：） |
| `negative_prompt` | string | 否 | 不希望出现在画面中的内容。 |
| `image_with_roles` | array | 否 | 角色或参考图列表。wan2.7-r2v 必填，最多 2 张。（示例：[{'url': 'https://example.com/role.png', 'role': 'reference_image'}]） |

完整文档（含请求/响应示例）：[`references/api-create.md`](references/api-create.md)

## 关于异步任务

标记为「异步」的接口是**任务制**：提交后返回 `task_id`，需要轮询到完成。
`client.py call` 默认**自动轮询到结束**再返回，你也可以手动控制：

```bash
# 只提交，不等结果
python3 scripts/client.py call wan <api> --json '{...}' --no-wait

# 之后用 task_id 查状态
python3 scripts/client.py task <task_id>
```

异步任务在**提交时会预冻结点数**，任务完成后按实际用量结算。
**不要重复提交同一个任务**——每次提交都可能产生费用。

## 常见错误

| 返回 | 含义 | 处理 |
|---|---|---|
| HTTP 401 | Key 无效或过期 | 重新创建 Key 后 `login` |
| HTTP 402 / `code:402` | 点数不足 | 去算力中心充值；错误信息里有本次所需点数 |
| `Invalid.Params` | 参数不合法 | 用 `schema wan` 核对参数与必填项 |
| 任务 `status: failed` | 上游处理失败 | 看 `error.message`；换素材或稍后重试 |

## 能力边界

- **不提供 API Key**：Key 必须由使用者自己获取
- **不代付费用**：调用消耗的是使用者自己账号的点数
- **不保证可用性**：接口由第三方平台提供，可用性、限流与计费以站内为准
- **不替代内容合规审查**：生成内容的合规责任由使用者承担

## 参考文件

| 文件 | 用途 |
|---|---|
| `references/getting-started.md` | 注册、充值、获取与配置 API Key |
| `references/api-query.md` | `query` 的官方文档 |
| `references/api-create.md` | `create` 的官方文档 |
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
