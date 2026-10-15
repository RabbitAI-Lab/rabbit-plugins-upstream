---
name: popcorn-cli
description: popcorn-cli 是爆米花系统（Popcorn）的官方 CLI。需要生图、生视频或管理文件夹时即可使用本工具：通过本地 API Key 查询可用模型、异步提交任务、按会话/任务 ID 查询最终结果，以及按类型查询/创建文件夹。注意：API Key 会保存在本机配置文件中，任务参数、提示词和生成配置会发送到远程 Popcorn 后端；不要在共享机器、日志、提示词或任务参数中暴露敏感信息。
version: 0.1.3
metadata:
  openclaw:
    requires:
      bins:
        - popcorn-cli
      config:
        - ~/.popcorn-cli/config.json
    install:
      - kind: node
        package: "@baomihuatop/popcorn-cli"
        bins:
          - popcorn-cli
    skillKey: popcorn-cli
    emoji: "🎬"
    homepage: https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html
---

# popcorn-cli

**popcorn-cli 是爆米花（Popcorn）的命令行客户端；需要生图、生视频或管理文件夹时，直接使用本 CLI 即可完成模型查询、任务提交、结果查询与文件夹管理。** 按任务类型分组组织命令，面向脚本化、自动化和 Agent 场景。

## 安全与隐私提示

- **API Key 本地存储**：`popcorn-cli config set-key` 会把 API Key 保存到 `~/.popcorn-cli/config.json`。该配置文件属于本机明文凭据存储，请不要提交到 Git、复制到日志、截图或共享给其他用户；在共享工作站、CI、Agent 运行环境中应限制 home 目录和配置文件访问权限。
- **远程传输**：执行 `models`、`submit`、`task list`、`folder list`、`folder create` 时，CLI 会调用远程 Popcorn 后端服务。`submit --params` 中的提示词、媒体生成参数、业务上下文、会话 ID 等会随请求发送到 Popcorn 后端；不要把密码、密钥、个人隐私、未授权客户资料或其他机密内容放入任务参数。
- **输出处理**：命令返回的 `task_id`、`session_id`、`folder id`、`result` URL 和错误信息可能包含业务上下文或资源地址。请按敏感数据处理，不要无意写入公开日志、公开 issue、聊天记录或可被无关人员读取的构建产物。

## 概念

- **会话（session）**：一次业务上下文，`session_id` 由调用方生成（例如一次剧本推进、一次 Agent 会话）。同一 session 下可提交多个任务，便于统一追踪。
- **任务（task）**：一次具体的生成请求。`submit` 为异步接口，提交后立刻返回 `task_id`（不含最终结果）；须再用 `task list` 按 `task_id` / `session_id` 查询状态与结果。
- **模型（model）**：每个任务类型下有多个可用模型，模型自带使用限制（时长、分辨率等）。可用模型清单与 API Key 所属租户绑定，仅返回当前租户开通且启用中的模型。提交任务前建议先用 `<group> models` 查询目标场景的可用模型。
- **文件夹（folder）**：按业务用途分为两类独立目录树，归属到当前 API Key 对应的用户。创建时可挂到同类型父目录下；查询返回扁平列表。
  - **AI 生成产物目录**（命令参数 `cli_generate`）：用来归档生图 / 生视频等 CLI 生成结果；`image/video submit -f` 只能挂这类目录。
  - **上传资源目录**（命令参数 `cli_upload`）：用来整理用户上传的参考图、素材等资源；不能作为生图/生视频的归属目录。

## Agent 行为约定

面向用户交流时遵守以下约定（命令行仍使用真实参数值）：

1. **先确认文件夹类型，再查询 / 创建**  
   用户说「查一下文件夹」「帮我建个文件夹」但未说明用途时，**不要默认类型，先用自然语言确认**：
   - 「AI 生成产物」：归档生图、生视频结果
   - 「上传资源」：整理上传的参考图、素材等  
   确认后再执行 `folder list` / `folder create`，并把对应类型映射为 `cli_generate` / `cli_upload`。

2. **答复用自然语言，少甩字段原值**  
   CLI JSON 里的枚举、状态、ID 等是给程序用的；回复用户时请翻译成可读说法，例如：
   - `cli_generate` → 「AI 生成产物目录」；`cli_upload` → 「上传资源目录」
   - `succeed` / `failed` / `queued` / `running` → 「已成功」「失败」「排队中」「执行中」
   - `task_type: image|video` → 「生图任务」「生视频任务」
   - 介绍目录时优先说名称与用途（如「上传资源下的「角色参考」」），需要进一步操作时再在内部保留 `id`；不要把 `type=cli_upload`、`status=succeed` 这类原文直接甩给用户。
   - 报错时说明「发生了什么、用户可怎么做」，避免只贴原始错误字段名。

## 能力概览

**模型查询 / 任务提交**（按任务类型两级分组，接口签名一致）：

| 任务类型 | 查询模型 | 提交任务 |
|----------|----------|----------|
| 生图 | `popcorn-cli image models` | `popcorn-cli image submit` |
| 生视频 | `popcorn-cli video models` | `popcorn-cli video submit` |

所有 `models` / `submit` 子命令的参数与返回结构在各任务类型间完全一致，见下文「命令详情」小节。

**任务查询**（跨任务类型统一入口；用于获取 `submit` 异步任务的最终结果）：

| 命令 | 说明 |
|------|------|
| `popcorn-cli task list --sid <id>` | 查询某会话下的所有任务 |
| `popcorn-cli task list --tid <id>` | 查询单个任务（含 status / result） |

**资源查询 / 上传**：

| 命令 | 说明 |
|------|------|
| `popcorn-cli resource upload <file> --name <name> --description <description>` | 上传图片、视频或音频资源；可选 `--folder-id`；类型由后端推断 |
| `popcorn-cli resource list --name <keyword>` | 查询上传资源，支持名称模糊、上传时间范围与分页 |

**文件夹管理**（按用途分两类目录，互不影响）：

| 命令 | 说明 |
|------|------|
| `popcorn-cli folder list --type <type>` | 查询某一类文件夹列表 |
| `popcorn-cli folder create --name <name> --type <type>` | 创建文件夹；可用 `--parent-id` 挂到父目录 |

`--type` 与用户说法的对应关系（对用户用左侧说法，命令用右侧参数）：

| 对用户说法 | 命令参数 `--type` | 用途 |
|------------|-------------------|------|
| AI 生成产物 | `cli_generate` | 归档生图 / 生视频等生成结果 |
| 上传资源 | `cli_upload` | 整理上传参考图、素材等 |

用户未说明要哪一类时，先确认再执行命令（见上文「Agent 行为约定」）。

**配置管理**：

| 命令 | 说明 |
|------|------|
| `popcorn-cli config show` | 查看当前生效的配置 |
| `popcorn-cli config set-key <apiKey>` | 设置 API Key |

## 认证与配置

CLI 不接受在命令行显式传入 API Key，统一从本地配置读取。

**配置文件位置**：`~/.popcorn-cli/config.json`

**用户警告**：该配置文件会在本机保存 API Key，属于明文 secret 存储。请确保文件只对当前用户可读，不要把 `~/.popcorn-cli/config.json` 纳入备份共享、代码仓库、日志采集或公开工单。若怀疑 API Key 泄露，应立即在 Popcorn 后台吊销并重新生成。

**配置字段**：

| 字段 | 说明 |
|------|------|
| `apiKey` | API Key，请求时通过 `X-API-Key` 头传给后端 |

## 命令详情

### 查询模型：`image models` / `video models`

查询某任务类型下当前租户可用的模型（仅返回当前 API Key 所属租户 + 场景匹配 + 启用中 + 非历史版本）。提交任务前应先调用本命令。

```bash
popcorn-cli <image|video> models
popcorn-cli <image|video> models --detail <MODEL_ID>
```

`models` 默认返回模型清单、完整 `model_limit`、计费配置、公共调用建议和 `params_schema`。默认返回结构：

```jsonc
{
  "type": "image",
  "total": 2,
  "models": [
    {
      "model_id":    "...",   // 模型唯一标识
      "name":        "...",   // 展示名
      "description": "...",   // 简介
      "model_limit": { ... },  // 单模型使用限制（不同模型可能不同）
      "price_config": { ... }, // 计费配置
      "has_model_usage_guidance": true // 是否有调用建议
    }
  ],
  "model_usage_guidance": "...", // 公共调用建议
  "params_schema": { ... }    // 该场景 submit 时 --params 的字段结构（同场景所有模型共用）
}
```

使用 `models --detail <MODEL_ID>` 查看单个模型完整信息（含完整 模型入参规范 和 调用建议）。

`params_schema` 是 JSON Schema 风格描述，说明 `submit --params` 可用的字段、类型、默认值。同一场景（image / video）下所有模型共用一份。

**推荐流程**：如果不清楚模型跟入参，先执行 `popcorn-cli <image|video> models` 查看当前租户可用模型清单并选定 `model_id`，再执行 `popcorn-cli <image|video> models --detail <MODEL_ID>` 查看该模型的完整入参规范和调用建议，最后据此构造 `submit` 的 `--params`。

### 提交任务：`image submit` / `video submit`

两类任务的 `submit` 子命令签名一致，仅调用不同后端接口。

> **异步接口**：`submit` 仅负责入队，立即返回 `task_id` 等受理信息，**不会等待生成完成，也不包含最终结果**。拿到 `task_id`（或传入的 `session_id`）后，须通过下方 `task list` 轮询任务状态，待 `status` 为终态后再读取 `result` / `error_message`。
>
> **预计耗时**（不排队、任务已开始执行时的参考时长；若处于 `queued` 排队中则还需额外等待）：
> - 生图（image）：约 **1–2 分钟**
> - 生视频（video）：约 **4–10 分钟**
>
> 轮询时请按上述时长设置合理间隔与超时，避免过早判定失败。

```bash
popcorn-cli <image|video> submit -n <NAME> -d <DESCRIPTION> -p <JSON> [-s <SESSION_ID>] [-f <FOLDER_ID>]
```

| 参数 | 缩写 | 必填 | 说明                                          |
|------|------|------|---------------------------------------------|
| `--name` | `-n` | 是 | 为要生成的产物起一个名称                       |
| `--description` | `-d` | 是 | 对目标产物添加描述,方便复用                   |
| `--params` | `-p` | 是 | 任务参数，必须是 JSON 对象字符串                         |
| `--sid` | `-s` | 否 | 会话 ID，用于将同一会话下的任务关联；不传则该任务不归属任何会话           |
| `--folder-id` | `-f` | 否 | 归属文件夹 ID；仅支持 `cli_generate` 目录。不传则归入默认（未归类） |

使用示例：

```bash
popcorn-cli image submit -n "主角图" -d "角色参考生成" -p '<按 params_schema 构造的 JSON>'
popcorn-cli video submit -n "主角视频" -d "镜头测试" -p '<按 params_schema 构造的 JSON>' -s <SESSION_ID>
popcorn-cli image submit -n "文件夹产物" -d "归档测试" -p '<按 params_schema 构造的 JSON>' -f 12
```

`-p` 的字段结构由后端 `params_schema` 决定，同场景所有模型共用。使用前请先执行 `popcorn-cli <image|video> models` 查询当前租户可用模型清单并选定 `model_id`，再执行 `popcorn-cli <image|video> models --detail <MODEL_ID>` 查看该模型的完整入参规范和调用建议，最后据此构造 `--params`。

指定文件夹时，请先确认用户要归档到「AI 生成产物」目录，再 `popcorn-cli folder list -t cli_generate` 获取目录 `id`。**生图/生视频只能挂到 AI 生成产物目录**（`cli_generate`）；上传资源目录（`cli_upload`）不可用于本接口。

返回结构（受理成功，任务已入队）：

```jsonc
{
  "task_id":    "...",   // 任务唯一标识，用于后续 task list --tid 查询
  "session_id": "...",   // 传入的会话 ID；未传则为 null
  "task_type":  "image", // 任务类型：image / video
  "folder_id":  12,      // 归属文件夹 ID；未指定则为 null
  "created_at": "..."    // 任务创建时间（ISO 8601）
}
```

### `task list` — 查询任务

用于获取 `submit` 异步任务的最终状态与结果。提交成功后请用本命令轮询，不要假定 `submit` 返回里已有生成结果。

```bash
popcorn-cli task list -s <SESSION_ID>
popcorn-cli task list -t <TASK_ID>
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `--sid` | `-s` | 二选一 | 按会话 ID 查询该会话下的所有任务 |
| `--tid` | `-t` | 二选一 | 按任务 ID 查询单个任务 |

`--sid` 与 `--tid` 必须提供其中之一。

返回结构：

```jsonc
{
  "total": 1,
  "tasks": [
    {
      "task_id":       "...",      // 任务唯一标识
      "session_id":    "...",      // 会话 ID；未归属会话则为 null
      "task_type":     "image",    // 任务类型：image / video
      "created_at":    "...",      // 创建时间
      "finished_at":   "...",      // 完成时间；未完成时可能为空
      "status":        "succeed",  // 见下方状态说明
      "result":        "...",      // 成功时的结果（如资源 URL 等）；未完成或失败可能为空字符串
      "error_message": ""          // 失败时的错误信息；成功时通常为空字符串
    }
  ]
}
```

`status` 取值：

| 状态 | 说明 |
|------|------|
| `queued` | 已入队，等待执行 |
| `running` | 执行中 |
| `succeed` | 成功（终态，可读 `result`） |
| `failed` | 失败（终态，可读 `error_message`） |

### `resource upload` — 上传资源

上传本地图片、视频或音频资源到 Popcorn。`--name` / `--description` 必填；可指定归属的上传资源目录。**资源类型不由 CLI 指定**，一律由后端根据文件扩展名 / Content-Type 推断。

```bash
popcorn-cli resource upload <FILE> -n <NAME> -d <DESCRIPTION> [-f <FOLDER_ID>]
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `<file>` | - | 是 | 本地文件路径（位置参数） |
| `--name` | `-n` | 是 | 根据该资源内容命名，方便后续查询复用 |
| `--description` | `-d` | 是 | 根据该资源内容描述，方便了解资源详情 |
| `--folder-id` | `-f` | 否 | 归属文件夹 ID；仅支持 `cli_upload`（上传资源）目录。不传则不归属目录 |

使用示例：

```bash
popcorn-cli resource upload ./demo.png -n "demo image" -d "reference image"
popcorn-cli resource upload ./demo.mp4 -f 123 -n "demo video" -d "reference video"
```

指定文件夹时，请先确认用户要整理到「上传资源」目录，再 `popcorn-cli folder list -t cli_upload` 获取目录 `id`。**上传资源只能挂到上传资源目录**（`cli_upload`）；AI 生成产物目录（`cli_generate`）不可用于本接口。`--folder-id` 必须是正整数（不能为 0），并由后端校验当前用户对该目录的权限。

### `resource list` — 查询上传资源

查询当前 API Key 用户上传的资源，支持 name 模糊搜索、上传时间范围和分页。

```bash
popcorn-cli resource list [--name <KEYWORD>] [--created-from <DATETIME>] [--created-to <DATETIME>] [--page <PAGE>] [--page-size <PAGE_SIZE>]
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `--name` | `-n` | 否 | 按资源名称模糊搜索 |
| `--created-from` | - | 否 | 上传时间起（含），例如 `2026-08-01` 或 ISO 8601 时间 |
| `--created-to` | - | 否 | 上传时间止（含），例如 `2026-08-06` 或 ISO 8601 时间 |
| `--page` | - | 否 | 页码，默认 1 |
| `--page-size` | - | 否 | 每页条数，默认 20，最大 100 |

返回结构：

```jsonc
{
  "total": 1,
  "page": 1,
  "page_size": 20,
  "resources": [
    {
      "name": "demo image",
      "description": "reference image",
      "file_url": "https://...",
      "created_at": "2026-08-06T..."
    }
  ]
}
```

### `folder list` — 查询文件夹

按类型查询当前用户下某一类文件夹的扁平列表。两类目录是独立业务域，互不影响。

**Agent 注意**：若用户未说明要查哪一类，先用自然语言确认是「AI 生成产物」还是「上传资源」，再带上对应 `--type` 执行；不要猜默认类型。向用户汇报结果时，用「AI 生成产物 / 上传资源 + 文件夹名称」描述，不要直接输出 `cli_generate` / `cli_upload`。

```bash
popcorn-cli folder list -t <TYPE>
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `--type` | `-t` | 是 | `cli_generate`（AI 生成产物）或 `cli_upload`（上传资源） |

使用示例：

```bash
popcorn-cli folder list -t cli_generate   # 查 AI 生成产物目录
popcorn-cli folder list -t cli_upload     # 查上传资源目录
```

返回结构：

```jsonc
{
  "type": "cli_upload",
  "total": 2,
  "folders": [
    {
      "id": 12,
      "parent_id": null,       // 父目录 ID；根目录为 null
      "name": "角色参考",
      "type": "cli_upload",
      "user_id": "...",
      "api_key_id": 3,
      "created_at": "..."
    }
  ]
}
```

返回为扁平列表；可用 `id` / `parent_id` 自行组树。创建子目录前请先 `folder list` 拿到目标父目录的 `id`。向用户说明时可说：「上传资源下有「角色参考」」等，需要再建子目录时再使用对应 `id`。

### `folder create` — 创建文件夹

创建某一类文件夹。可选挂到同类型、同用户的父目录下。

**Agent 注意**：创建前必须明确类型。用户只说「建个叫某某的文件夹」时，先确认是「AI 生成产物」还是「上传资源」；确认后再执行。创建成功后用自然语言反馈，例如：「已在上传资源下创建文件夹「主角」」，而不是复述 JSON 字段。

```bash
popcorn-cli folder create -n <NAME> -t <TYPE> [-p <PARENT_ID>]
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `--name` | `-n` | 是 | 文件夹名称（最长 128） |
| `--type` | `-t` | 是 | `cli_generate`（AI 生成产物）或 `cli_upload`（上传资源） |
| `--parent-id` | `-p` | 否 | 父文件夹 ID；不传则为该类型下的根目录 |

使用示例：

```bash
popcorn-cli folder create -n "角色参考" -t cli_upload
popcorn-cli folder create -n "主角" -t cli_upload -p 12
popcorn-cli folder create -n "本周产物" -t cli_generate
```

约束：

- `parent_id` 必须存在，且与新建文件夹属于同一类型、同一用户
- 不能把不存在的目录 ID、其他类型目录或其他用户目录当作父目录

返回结构：

```jsonc
{
  "id": 13,
  "parent_id": 12,
  "name": "主角",
  "type": "cli_upload",
  "user_id": "...",
  "api_key_id": 3,
  "created_at": "..."
}
```

## 使用场景示例

- **CI/自动化脚本**：按 session 提交批量任务，再轮询 `task list` 直到终态
- **Agent 编排**：Agent 用同一 `session_id` 异步提交生图 / 生视频任务，之后统一 `task list --sid`（或 `--tid`）获取最终结果
- **资源归档**：先与用户确认目录用途。整理上传素材用 `folder create -t cli_upload`，再在 `resource upload -f <id>` 时传入目录 ID；归档生图/生视频用 `folder create -t cli_generate`，再在 `image/video submit -f <id>` 时传入目录 ID。回复用户时说「已创建上传资源目录 / AI 生成产物目录 …」，不要直接报 `cli_*` 参数名。

## 帮助信息

```bash
popcorn-cli --help
popcorn-cli <group> --help          # 如 popcorn-cli image --help / popcorn-cli folder --help
popcorn-cli <group> <action> --help
```
