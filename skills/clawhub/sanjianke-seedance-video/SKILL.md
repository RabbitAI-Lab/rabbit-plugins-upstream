---
name: seedance-video
slug: sanjianke-seedance-video
displayName: 三剪客 · Seedance 2.0
description: "基于火山方舟 Seedance 2.0 的多模态视频生成应用。支持文本/图片/视频/音频任意组合输入，可输出 480p/720p/1080p 分辨率、4~15 秒时长的视频，并可选生成同步音频。按 token 计费，按分辨率和是否含视频输入分档。支持 创建素材资产组合、上传素材、获取素材详情、更新素材、删除素材、查询任务、创建任务。使用时需要你自己的 api.a7w.cn API Key。遇到问题可加技术微信 9872659。"
version: 1.0.3
summary: "「Seedance 2.0」的完整调用封装：7 个接口的官方文档、参数表与一个零依赖客户端。需要自带 api.a7w.cn 的 API Key，调用按点数计费。遇到问题可加技术微信 9872659。"
license: MIT
tags:
  - 三剪客
  - 设计多媒体
  - 视频生成
  - 图生视频
---

# Seedance 2.0

基于火山方舟 Seedance 2.0 的多模态视频生成应用。支持文本/图片/视频/音频任意组合输入，可输出 480p/720p/1080p 分辨率、4~15 秒时长的视频，并可选生成同步音频。按 token 计费，按分辨率和是否含视频输入分档。

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
python3 scripts/client.py schema seedance

# 3. 调用（示例）
python3 scripts/client.py call seedance createGroup --json '{}'
```

> **没有 Key？** 见 `references/getting-started.md`——注册、充值、取 Key 的完整步骤。也可以直接去 [算力集市](https://api.a7w.cn/) 注册。

## 接口一览

| 接口 | 名称 | 模式 | 计费 | 说明 |
|---|---|---|---|---|
| `createGroup` | 创建素材资产组合 | 同步 | 免费（查询类接口） | 创建 Asset Group（素材资产组合），上传素材前需先创建分组。 |
| `createAsset` | 上传素材 | 同步 | 免费（查询类接口） | 将公网可访问的素材文件上传到指定 Asset Group。支持图像 / 视频 / 音频。 |
| `getAsset` | 获取素材详情 | 同步 | 免费（查询类接口） | 查询素材信息，包括状态（Active / Processing / Failed）、URL、所属分组等。 |
| `updateAsset` | 更新素材 | 同步 | 免费（查询类接口） | 更新素材的名称等元数据。 |
| `deleteAsset` | 删除素材 | 同步 | 免费（查询类接口） | 删除指定素材；删除后无法在创建任务中再以 asset:// 形式引用。 |
| `query` | 查询任务 | 同步 | 免费（查询类接口） | 按服务任务 ID 查询 Seedance 任务状态（平台服务） |
| `create` | 创建任务 | 异步（需轮询） | 免费（查询类接口） | 提交 Seedance 2.0 视频生成任务。支持文生/图生/视频编辑/延长/多模态参考等场景。 |

## 接口详情

### `createGroup` · 创建素材资产组合

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/seedance/createGroup`

创建 Asset Group（素材资产组合），上传素材前需先创建分组。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `Name` | string | 是 | Asset Group 名称，上限 64 字符（示例：demo-group） |
| `GroupType` | string | 否 | 分组类型；AIGC 表示虚拟人像分组（示例：AIGC） |
| `Description` | string | 否 | 分组描述，上限 300 字符 |
| `ProjectName` | string | 否 | 项目名称，默认 default；非默认项目需填写正确名称 |

完整文档（含请求/响应示例）：[`references/api-createGroup.md`](references/api-createGroup.md)

### `createAsset` · 上传素材

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/seedance/createAsset`

将公网可访问的素材文件上传到指定 Asset Group。支持图像 / 视频 / 音频。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `URL` | string | 是 | 素材公网可访问 URL；将由上游拉取并入库（示例：https://your-domain.com/uploads/image.png） |
| `Name` | string | 否 | 素材名称，上限 64 字符 |
| `GroupId` | string | 是 | Asset 所属的 Asset Group Id（来自 createGroup 返回的 Result.Id）（示例：group-20260402173639-97brg） |
| `AssetType` | string | 是 | 素材类型：Image / Video / Audio（示例：Image） |
| `ProjectName` | string | 否 | 项目名称，默认 default |

完整文档（含请求/响应示例）：[`references/api-createAsset.md`](references/api-createAsset.md)

### `getAsset` · 获取素材详情

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/seedance/getAsset`

查询素材信息，包括状态（Active / Processing / Failed）、URL、所属分组等。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `Id` | string | 是 | Asset Id（来自 createAsset 返回的 Result.Id）（示例：asset-20260402224305-54j64） |
| `ProjectName` | string | 否 | 项目名称，默认 default |

完整文档（含请求/响应示例）：[`references/api-getAsset.md`](references/api-getAsset.md)

### `updateAsset` · 更新素材

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/seedance/updateAsset`

更新素材的名称等元数据。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `Id` | string | 是 | Asset Id（示例：asset-20260402224305-54j64） |
| `Name` | string | 否 | 新的素材名称，上限 64 字符 |
| `ProjectName` | string | 否 | 项目名称，默认 default |

完整文档（含请求/响应示例）：[`references/api-updateAsset.md`](references/api-updateAsset.md)

### `deleteAsset` · 删除素材

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/seedance/deleteAsset`

删除指定素材；删除后无法在创建任务中再以 asset:// 形式引用。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `Id` | string | 是 | Asset Id（示例：asset-20260402224305-54j64） |
| `ProjectName` | string | 否 | 项目名称，默认 default |

完整文档（含请求/响应示例）：[`references/api-deleteAsset.md`](references/api-deleteAsset.md)

### `query` · 查询任务

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`GET /api/v1/apps/seedance/query`

按服务任务 ID 查询 Seedance 任务状态（平台服务）

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `task_id` | string | 是 | 上游返回的任务 ID（与创建接口响应 data.id 一致）。也可使用查询参数 id。（示例：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx） |

完整文档（含请求/响应示例）：[`references/api-query.md`](references/api-query.md)

### `create` · 创建任务

**模式**：异步（提交后轮询任务） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/seedance/create`

提交 Seedance 2.0 视频生成任务。支持文生/图生/视频编辑/延长/多模态参考等场景。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `seed` | integer | 否 | 随机种子，可复现结果（若上游支持） |
| `draft` | boolean | 否 | 是否草稿模式（若上游支持） |
| `model` | string | 是 | 公开模型名称。请从模型名称与使用场景表中选择一个名称。（示例：seedance-2-text-2-video） |
| `ratio` | string | 否 | 画面宽高比。adaptive 表示由模型根据输入自动选择（示例：16:9） |
| `tools` | array | 否 | 可选工具（仅文生视频支持 web_search 联网搜索）（示例：[{'type': 'web_search'}]） |
| `frames` | integer | 否 | 帧数相关参数（若上游支持） |
| `content` | array | 是 | 多模态输入列表：支持 文本 + 图片 + 视频 + 音频 的任意组合。图片最多 9 张、视频最多 3 个、音频最多 3 段，且不可单独传音频。含 video_url 时按「含视频输入」档位计费。（示例：[{'text': '一只金毛犬在海边奔跑，夕阳西下', 'type': 'text'}]） |
| `duration` | integer | 否 | 生成视频时长（秒）。取值 4~15，或 -1 由模型自动决定（示例：5） |
| `watermark` | boolean | 否 | 是否在视频右下角添加水印（示例：） |
| `resolution` | string | 否 | 输出分辨率（示例：720p） |
| `callback_url` | string | 否 | 异步任务完成/失败时的回调地址（示例：https://your-domain.com/webhook/seedance） |
| `camera_fixed` | boolean | 否 | 是否固定机位（若上游支持） |
| `service_tier` | string | 否 | 服务档位（若上游支持） |
| `generate_audio` | boolean | 否 | 是否生成与画面同步的音频（示例：1） |

完整文档（含请求/响应示例）：[`references/api-create.md`](references/api-create.md)

## 关于异步任务

标记为「异步」的接口是**任务制**：提交后返回 `task_id`，需要轮询到完成。
`client.py call` 默认**自动轮询到结束**再返回，你也可以手动控制：

```bash
# 只提交，不等结果
python3 scripts/client.py call seedance <api> --json '{...}' --no-wait

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
| `Invalid.Params` | 参数不合法 | 用 `schema seedance` 核对参数与必填项 |
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
| `references/api-createGroup.md` | `createGroup` 的官方文档 |
| `references/api-createAsset.md` | `createAsset` 的官方文档 |
| `references/api-getAsset.md` | `getAsset` 的官方文档 |
| `references/api-updateAsset.md` | `updateAsset` 的官方文档 |
| `references/api-deleteAsset.md` | `deleteAsset` 的官方文档 |
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
