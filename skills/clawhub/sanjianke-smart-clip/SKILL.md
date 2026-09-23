---
name: smart-clip
slug: sanjianke-smart-clip
displayName: 三剪客 · 智能剪辑
description: "智能剪辑应用，支持模板查询、真人口播混剪、素材混剪和新闻体视频制作。支持 模板列表、模板详情、真人口播混剪、素材混剪、新闻体视频。使用时需要你自己的 api.a7w.cn API Key。遇到问题可加技术微信 9872659。"
version: 1.0.3
summary: "「智能剪辑」的完整调用封装：5 个接口的官方文档、参数表与一个零依赖客户端。需要自带 api.a7w.cn 的 API Key，调用按点数计费。遇到问题可加技术微信 9872659。"
license: MIT
tags:
  - 三剪客
  - 设计多媒体
  - 批量混剪
  - 短剧二创
---

# 智能剪辑

智能剪辑应用，支持模板查询、真人口播混剪、素材混剪和新闻体视频制作。

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
python3 scripts/client.py schema smart_clip

# 3. 调用（示例）
python3 scripts/client.py call smart_clip template --json '{}'
```

> **没有 Key？** 见 `references/getting-started.md`——注册、充值、取 Key 的完整步骤。也可以直接去 [算力集市](https://api.a7w.cn/) 注册。

## 接口一览

| 接口 | 名称 | 模式 | 计费 | 说明 |
|---|---|---|---|---|
| `template` | 模板列表 | 同步 | 免费（查询类接口） | 查询智能剪辑模板列表。 |
| `template_detail` | 模板详情 | 同步 | 免费（查询类接口） | 按模板 ID 获取模板结构详情。 |
| `realman_broadcast` | 真人口播混剪 | 异步（需轮询） | 免费（查询类接口） | 提交真人口播混剪视频制作任务。 |
| `broadcast_mixcut` | 素材混剪 | 异步（需轮询） | 免费（查询类接口） | 提交素材混剪视频制作任务，仅支持音频或素材输入链路。 |
| `news_mixcut` | 新闻体视频 | 异步（需轮询） | 免费（查询类接口） | 提交新闻体视频制作任务。 |

## 接口详情

### `template` · 模板列表

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`GET /api/v1/apps/smart_clip/template`

查询智能剪辑模板列表。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `sid` | string | 否 | 分页游标，当有值时代表存在下一页，继续查询下一页时需传入该值 |
| `scene` | enum | 是 | 可选值：realMan / oralMixCutting / newsMixCutting；模板使用场景：真人口播 realMan（提交接口 realman_broadcast）、素材混剪 oralMixCutting（提交接口 broadcast_mixcut）、新闻体视频 newsMixCutting（提交接口 news_m…（示例：realMan） |
| `sortBy` | enum | 否 | 可选值：desc / asc；排序方式，desc：按上架时间倒序排序，asc：按上架时间正序排序（示例：desc） |
| `pageSize` | integer | 否 | 每页大小（示例：10） |
| `searchKey` | enum | 否 | 可选值：name / id；搜索字段（示例：name） |
| `searchValue` | string | 否 | 搜索值（示例：口播） |

完整文档（含请求/响应示例）：[`references/api-template.md`](references/api-template.md)

### `template_detail` · 模板详情

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`GET /api/v1/apps/smart_clip/template_detail`

按模板 ID 获取模板结构详情。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `id` | string | 是 | 模板id（示例：67b7ee802b2beb0030cdeaaf） |

完整文档（含请求/响应示例）：[`references/api-template_detail.md`](references/api-template_detail.md)

### `realman_broadcast` · 真人口播混剪

**模式**：异步（提交后轮询任务） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/smart_clip/realman_broadcast`

提交真人口播混剪视频制作任务。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | 否 | 标题（示例：聊AI行业） |
| `styleId` | string | 是 | 视频模板id（示例：68aebb91b8619ed6f4168f40） |
| `language` | string | 否 | 特指视频中（videoUrl）对应的语种，音频驱动时需要传音频中内容的语种，语种参考ASR支持的语种（示例：zh-CN） |
| `subtitle` | array | 否 | 字幕信息（兼容subtitles字段），该字段专用于填充语音识别（ASR）后的结果，如果您未预先进行语音识别（ASR），请忽略该字段。 |
| `videoUrl` | string | 是 | 视频url（示例：https://example.com/a.mp4） |
| `materials` | array | 否 | 素材，素材格式要求详见产品介绍-功能介绍 |
| `packRules` | object | 否 | 包装规则：仅用于控制标题、素材、字幕等是否参与模版的效果包装，无特殊要求不建议设置。 |
| `callbackUrl` | string | 否 | 结果通知回调地址（示例：https://example.com/hook） |
| `processRules` | object | 否 | 处理规则 |
| `structLayers` | array | 否 | 需要修改的图层数据 |
| `introduceCard` | object | 否 | 身份栏信息，含义详见常见问题库 |
| `materialSoundSwitch` | boolean | 否 | 当素材为视频时原声开关 |

完整文档（含请求/响应示例）：[`references/api-realman_broadcast.md`](references/api-realman_broadcast.md)

### `broadcast_mixcut` · 素材混剪

**模式**：异步（提交后轮询任务） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/smart_clip/broadcast_mixcut`

提交素材混剪视频制作任务，仅支持音频或素材输入链路。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | 否 | 标题（示例：聊AI行业） |
| `content` | string | 否 | 文本，与audioUrl字段二选一，选择文本，则speakerId为必须；当前应用不支持该定制声音分支 |
| `styleId` | string | 是 | 视频模板ID（示例：68aebb91b8619ed6f4168f40） |
| `audioUrl` | string | 否 | 音频URL，与content字段二选一；当前应用仅支持 audioUrl 或素材输入链路（示例：https://example.com/a.mp3） |
| `language` | string | 否 | 语种，特指音频（audioUrl）对应的语种，语种参考ASR支持的语种（示例：zh-CN） |
| `subtitle` | array | 否 | 字幕信息（兼容subtitles字段），该字段专用于填充语音识别（ASR）后的结果，如果您未预先进行语音识别（ASR），请忽略该字段。 |
| `materials` | array | 是 | 素材 |
| `packRules` | object | 否 | 包装规则：仅用于控制标题、素材、字幕等是否参与模版的效果包装，无特殊要求不建议设置。 |
| `speakerId` | string | 否 | 音色ID；当前应用不支持 content + speakerId 定制声音分支 |
| `callbackUrl` | string | 否 | 结果通知回调地址（示例：https://example.com/hook） |
| `processRules` | object | 否 | 处理规则 |
| `speakerExtra` | object | 否 | 音色扩展参数，传speakerId时有效；当前应用不支持 content + speakerId 定制声音分支 |
| `structLayers` | array | 否 | 需要修改的图层数据 |
| `introduceCard` | object | 否 | 身份栏信息，含义详见常见问题库 |

完整文档（含请求/响应示例）：[`references/api-broadcast_mixcut.md`](references/api-broadcast_mixcut.md)

### `news_mixcut` · 新闻体视频

**模式**：异步（提交后轮询任务） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/smart_clip/news_mixcut`

提交新闻体视频制作任务。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | 是 | 标题（示例：聊AI行业） |
| `styleId` | string | 是 | 视频模板ID（示例：68aebb91b8619ed6f4168f40） |
| `materials` | array | 是 | 素材 |
| `packRules` | object | 否 | 包装规则：仅用于控制标题、素材、字幕等是否参与模版的效果包装，无特殊要求不建议设置。 |
| `callbackUrl` | string | 否 | 结果通知回调地址（示例：https://example.com/hook） |
| `processRules` | object | 否 | 处理规则 |
| `structLayers` | array | 否 | 需要修改的图层数据 |
| `introduceCard` | object | 否 | 身份栏信息，含义详见常见问题库 |

完整文档（含请求/响应示例）：[`references/api-news_mixcut.md`](references/api-news_mixcut.md)

## 关于异步任务

标记为「异步」的接口是**任务制**：提交后返回 `task_id`，需要轮询到完成。
`client.py call` 默认**自动轮询到结束**再返回，你也可以手动控制：

```bash
# 只提交，不等结果
python3 scripts/client.py call smart_clip <api> --json '{...}' --no-wait

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
| `Invalid.Params` | 参数不合法 | 用 `schema smart_clip` 核对参数与必填项 |
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
| `references/api-template.md` | `template` 的官方文档 |
| `references/api-template_detail.md` | `template_detail` 的官方文档 |
| `references/api-realman_broadcast.md` | `realman_broadcast` 的官方文档 |
| `references/api-broadcast_mixcut.md` | `broadcast_mixcut` 的官方文档 |
| `references/api-news_mixcut.md` | `news_mixcut` 的官方文档 |
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
