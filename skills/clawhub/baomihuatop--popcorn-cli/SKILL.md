---
name: popcorn-cli
description: popcorn-cli 是爆米花系统（Popcorn）的官方 CLI，按任务类型分组组织命令，面向脚本、自动化与 Agent 场景。需要生图、生视频、上传资源或管理文件夹时使用本工具：查询当前租户可用模型、异步提交任务、按会话/任务 ID 查询最终结果、上传与检索资源、按类型查询/创建文件夹。需要确认登录凭据是否可用、绑定 API Key、登出，或查看本地 CLI 版本时，也可直接使用本 CLI。注意：API Key 会保存在本机配置文件中，任务参数、提示词和生成配置会发送到远程 Popcorn 后端；不要在共享机器、日志、提示词或任务参数中暴露敏感信息。
version: 0.2.0
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

popcorn-cli 是爆米花（Popcorn）官方命令行客户端，提供生图、生视频或管理文件夹的能力，popcorn-cli 按任务类型分组组织命令，面向脚本化、自动化和 Agent 场景。核心链路是 **查模型 → 提交任务 → 轮询结果**，此外覆盖资源上传 / 查询、文件夹管理与登录凭据管理。

## 安全与隐私约束

- **API Key 属于本机明文凭据**：`config set-key` / `auth bind` 会把 API Key 写入 `~/.popcorn-cli/config.json`（目录权限 `0700`、文件权限 `0600`）。不要提交到 Git、写入日志或截图，也不要共享给其他用户；在共享工作站、CI、Agent 运行环境中应限制该文件的访问权限。若怀疑泄露，立即在爆米花后台吊销并重新生成。
- **任务参数会离开本机**：`models`、`submit`、`task list`、`resource`、`folder` 都会调用远程 Popcorn 后端，`submit --params` 中的提示词与生成参数、`session_id` 等会随请求发送。不要把密码、密钥、个人隐私、未授权的客户资料或其他机密内容放进任务参数。
- **输出按敏感数据对待**：`task_id`、`session_id`、`folder id`、`result` URL 与错误信息可能携带业务上下文或资源地址，不要写入公开日志、公开 issue、聊天记录或可被无关人员读取的构建产物。

## 概念

- **会话（session）**：一次业务上下文，`session_id` 由调用方生成（如一次剧本推进、一次 Agent 会话）。同一 session 下可提交多个任务，便于统一追踪。
- **任务（task）**：一次具体的生成请求。`submit` 是异步接口，提交后只返回 `task_id`，须再用 `task list` 按 `task_id` / `session_id` 查询状态与结果。
- **模型（model）**：每个任务类型下有多个可用模型，各自带使用限制（时长、分辨率等）。模型清单与 API Key 所属租户绑定，只返回当前租户已开通且启用中的模型。
- **文件夹（folder）**：按用途分为两类**互不影响**的目录树，归属于当前 API Key 对应的用户。创建时可挂到同类型父目录下，查询返回扁平列表。

  | 对用户说法 | `--type` 参数 | 用途 |
  |------------|---------------|------|
  | AI 生成产物 | `cli_generate` | 归档生图 / 生视频等生成结果 |
  | 上传资源 | `cli_upload` | 整理上传的参考图、素材等 |

  两类目录**互斥**：`image/video submit -f` 只能挂 `cli_generate`；`resource upload -f` 只能挂 `cli_upload`。

## 使用前检查（仅会话首次）

**只在本次 Agent 会话第一次用到 popcorn-cli 时执行一次**，后续轮次直接执行业务命令，不要重复检查。

```bash
popcorn-cli --version
```

预期输出（退出码 `0`，版本号以实际为准）：

```
0.2.0
```

| 情况 | 处理 |
|------|------|
| 命令不存在或执行报错 | CLI 未安装。引导用户执行 `npm install -g @baomihuatop/popcorn-cli`（需要 Node.js ≥ 18），安装完成后重试 |
| 版本低于 `0.2.0` | 不支持 `auth` 命令。引导升级：`npm install -g @baomihuatop/popcorn-cli@latest` |
| 版本号与本 Skill 的 `version` 字段不一致 | **不要**因此中止任务。以实际安装的 CLI 为准，必要时提醒用户文档与行为可能存在偏差 |

不要因为版本号不同就拒绝执行任务，也不要把版本检查变成每轮对话的固定动作。

## 能力概览

下表中 `<image|video>` 表示同一命令在两类任务下签名一致，实际执行时替换为 `image` 或 `video`。

| 分组 | 命令 | 用途 |
|------|------|------|
| `image` / `video` | `popcorn-cli <image\|video> models` | 查询当前租户可用模型（提交任务前先查） |
| | `popcorn-cli <image\|video> models --detail <MODEL_ID>` | 查看单个模型的完整入参规范与调用建议 |
| | `popcorn-cli <image\|video> submit -n <NAME> -d <DESCRIPTION> -p <JSON> [-s <SESSION_ID>] [-f <FOLDER_ID>]` | 提交生成任务，异步返回 `task_id` |
| `task` | `popcorn-cli task list -s <SESSION_ID>` | 查询某会话下的所有任务 |
| | `popcorn-cli task list -t <TASK_ID>` | 查询单个任务（含 `status` / `result`） |
| `resource` | `popcorn-cli resource upload <FILE> -n <NAME> -d <DESCRIPTION> [-f <FOLDER_ID>]` | 上传图片、视频或音频；类型由后端按扩展名推断 |
| | `popcorn-cli resource list [--name] [--created-from] [--created-to] [--page] [--page-size]` | 查询上传资源，支持名称模糊、时间范围与分页 |
| `folder` | `popcorn-cli folder list -t <TYPE>` | 查询某一类文件夹列表 |
| | `popcorn-cli folder create -n <NAME> -t <TYPE> [-p <PARENT_ID>]` | 创建文件夹，可挂到同类型父目录下 |
| `auth` | `popcorn-cli auth status` | 检查本地凭据是否可用；不可用时退出码 `3`（无法判定时为 `1`） |
| | `popcorn-cli auth bind --api-key <API_KEY>` | 使用 API Key 绑定登录，等同于 `config set-key` |
| | `popcorn-cli auth logout` | 清除本地凭据（含配置文件中的 API Key），幂等 |
| `config` | `popcorn-cli config show` | 查看当前生效的配置 |
| | `popcorn-cli config set-key <API_KEY>` | 设置 API Key（等同于 `auth bind`） |
| | `popcorn-cli config set-url <BASE_URL>` | 设置后端服务地址 |
| — | `popcorn-cli --version` | 查看本地已安装的版本号 |

补充说明：

- `task list` 是获取 `submit` 异步结果的**唯一入口**。
- `folder` 的 `--type` 取值与用户说法的对照见上文「概念 → 文件夹」。
- 不确定参数时用 `popcorn-cli <group> [<action>] --help` 自查。

## 交互约定

面向用户交流时遵守（命令行仍使用真实参数值）：

1. **先确认文件夹类型，再查询 / 创建**
   用户说「查一下文件夹」「帮我建个文件夹」但未说明用途时，**不要默认类型**，先用自然语言确认是「AI 生成产物」还是「上传资源」，确认后再执行 `folder list` / `folder create`。

2. **答复用自然语言，少甩字段原值**
   CLI JSON 里的枚举、状态、ID 是给程序用的，回复用户时翻译成可读说法：

   | 原值 | 面向用户说法 |
   |------|--------------|
   | `cli_generate` / `cli_upload` | 「AI 生成产物目录」/「上传资源目录」 |
   | `queued` / `running` / `succeed` / `failed` | 「排队中」/「执行中」/「已成功」/「失败」 |
   | `task_type: image` / `video` | 「生图任务」/「生视频任务」 |

   介绍目录时说名称与用途（如「上传资源下的「角色参考」」），`id` 只在内部保留供后续操作用；报错时说明「发生了什么、用户可以怎么做」，不要只贴字段名。

## 认证与凭据

### 凭据模型

只有一种凭据来源：`~/.popcorn-cli/config.json` 中的 `apiKey` 字段，请求时通过 `X-API-Key` 请求头传给后端。

- 发起请求时**不接受**在命令行显式传入 API Key，统一从本地配置读取。
- 只有绑定凭据时（`auth bind --api-key`）允许显式传入，该值仅用于写入本地配置文件，不参与请求。
- 该文件的存储安全约束见上文「安全与隐私约束」。

配置字段：

| 字段 | 说明 |
|------|------|
| `apiKey` | API Key，请求时通过 `X-API-Key` 头传给后端 |
| `baseUrl` | 后端服务地址，默认 `https://baomihua.top` |

> **当前版本没有 SSO 登录流程**，也没有 `auth login` / `update --check` 等命令。不要向用户承诺这类能力，也不要把它们写进给用户的建议里。

### 不要主动巡检凭据状态

**不要在每个会话开头或每轮对话前调用 `auth status`。** 所有业务命令（`models` / `submit` / `task list` / `resource` / `folder`）在凭据缺失或失效时会直接报错，按需处理即可。

只有两种情况才执行 `auth status`：

1. 业务命令返回了认证类错误（见下节识别规则）；
2. 用户主动询问「是否已登录 / 凭据还有效吗」。

### 识别认证错误：两种输出形态

认证错误在不同来源下形态不同，**判断依据不要混用**：

| 来源 | 输出位置 | 形态 | 退出码 |
|------|----------|------|--------|
| 业务命令（`models` / `submit` / `task list` / `resource` / `folder`） | stderr | 纯文本，如 `未配置 API Key。请先运行 ...` 或 `请求失败（HTTP 401）：API Key 无效` | `1` |
| `auth status` | stdout | 结构化 JSON，含 `authenticated` 与 `error.code` | `3`（无法判定时为 `1`） |

**识别规则**：业务命令报错中出现 `未配置 API Key` 或 `HTTP 401` → 属于凭据问题，按下一小节的决策表处理；其他报错（参数非法、任务 ID 不存在、模型未找到等）按业务错误处理，**不要误判为认证问题**，更不要因此重新绑定凭据。

### `auth status` — 检查凭据状态

```bash
popcorn-cli auth status
```

- 凭据有效：退出码 `0`，输出 `authenticated: true`、`method`、`api_key_masked`、`base_url`、`config_path`、`verified_at`。
- 凭据不可用：退出码 `3`（无法判定时为 `1`），输出 `authenticated: false` 与结构化 `error` 对象；**输出到 stdout**，可直接解析。

按 `error.code` 选择动作：

| `error.code` | 含义 | 动作 |
|--------------|------|------|
| `AUTH_NO_CREDENTIALS` | 本地没有凭据 | 向用户索取 API Key → 执行 `auth bind` → 重试此前失败的业务命令 |
| `AUTH_CREDENTIALS_INVALID` | 凭据被服务端拒绝（HTTP 401/403，`server_code` 为后端错误码） | 提示用户确认 API Key 是否已吊销 / 过期，重新生成后 `auth bind` 重新绑定 |
| `AUTH_CHECK_FAILED` | 网络或服务异常，无法判定（`http_status` 为 `0` 表示请求未送达） | **不要重新绑定**（凭据本身可能没问题）。提示用户检查网络，或用 `config show` 确认 `baseUrl` 是否正确，稍后重试 |

`error.hint` 字段已包含面向用户的处理建议，转述即可（不要照抄字段名，也不要把 `error.code` 原文甩给用户）。

### `auth bind` — 使用 API Key 绑定登录

```bash
popcorn-cli auth bind --api-key <API_KEY>
```

用于凭据缺失或失效时。效果等同于 `popcorn-cli config set-key <API_KEY>`，写入同一配置文件，**不会**校验 API Key 是否有效 —— 可用性由后续业务命令或 `auth status` 体现。

- API Key 必须由用户提供。**不要编造、猜测或复用其他账号的 Key**；用户手上没有时，引导其到爆米花后台创建后再回来绑定。
- 绑定结果中只返回脱敏后的 `api_key_masked`。**不要把用户提供的明文 API Key 回显、写入文件或放进任何任务参数**。
- 绑定成功后，若用户原本正在执行某个业务命令，直接重试该命令即可，不必额外插一步 `auth status`。

### `auth logout` — 登出

```bash
popcorn-cli auth logout
```

清除本地凭据（配置文件中的 `apiKey`，以及可能存在的独立凭据文件），保留 `baseUrl` 等其他配置。幂等：无凭据时同样退出码 `0`，`cleared` 为空数组。登出后所有需要认证的命令立即不可用。

**只在用户明确要求登出或切换账号时执行。** 不要把它当作「清除报错」的手段 —— 尤其不要用 `logout` 再 `bind` 的方式反复试探凭据状态（`bind` 不校验有效性，来回操作解决不了问题，还会让用户丢失原本可用的凭据）。

### 认证相关禁止事项

- ❌ 不要主动巡检 `auth status` —— 业务命令会自己报错，按需排查即可
- ❌ 不要在凭据有效时重复 `auth bind` —— 会覆盖当前可用的 API Key
- ❌ 不要在 `AUTH_CHECK_FAILED` 时反复 `auth bind` —— 网络问题绑定解决不了
- ❌ 不要对同一个认证错误反复重试业务命令；同一失败原因最多重试 1 次
- ❌ 不要输出、记录或回显用户的明文 API Key
- ❌ 不要向用户承诺 SSO 登录、`auth login`、`update --check` 等本 CLI 不存在的命令

## 命令详情

`<image|video>` 的含义同上文「能力概览」。

### `models` — 查询模型

查询某任务类型下当前租户可用的模型（仅返回当前 API Key 所属租户 + 场景匹配 + 启用中 + 非历史版本）。提交任务前应先调用本命令。

```bash
popcorn-cli <image|video> models
popcorn-cli <image|video> models --detail <MODEL_ID>
```

默认返回模型清单、完整 `model_limit`、计费配置、公共调用建议和 `params_schema`：

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

`--detail <MODEL_ID>` 返回单个模型的完整信息（含完整入参规范与调用建议）。

`params_schema` 是 JSON Schema 风格的描述，说明 `submit --params` 可用的字段、类型与默认值。

### `submit` — 提交任务

**异步接口**：仅负责入队，立即返回 `task_id`，**不等待生成完成，也不包含最终结果**；拿到 `task_id` 后须用 `task list` 轮询，待 `status` 为终态再读 `result` / `error_message`。

预计耗时（任务已开始执行时的参考值；若处于 `queued` 排队中还需额外等待）：生图约 **1–2 分钟**，生视频约 **4–10 分钟**。请据此设置轮询间隔与超时，避免过早判定失败。

```bash
popcorn-cli <image|video> submit -n <NAME> -d <DESCRIPTION> -p <JSON> [-s <SESSION_ID>] [-f <FOLDER_ID>]
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `--name` | `-n` | 是 | 为要生成的产物起一个名称 |
| `--description` | `-d` | 是 | 对目标产物添加描述，方便复用 |
| `--params` | `-p` | 是 | 任务参数，**必须是 JSON 对象字符串** |
| `--sid` | `-s` | 否 | 会话 ID，用于关联同一会话下的任务；不传则该任务不归属任何会话 |
| `--folder-id` | `-f` | 否 | 归属文件夹 ID；**仅支持 `cli_generate` 目录**，不传则归入默认（未归类） |

`-p` 的字段结构由后端 `params_schema` 决定，同场景所有模型共用。构造流程：

1. `popcorn-cli <image|video> models` —— 查看当前租户可用模型，选定 `model_id`
2. `popcorn-cli <image|video> models --detail <MODEL_ID>` —— 查看该模型的完整入参规范与调用建议
3. 据此构造 `-p` 并提交

使用示例：

```bash
popcorn-cli image submit -n "主角图" -d "角色参考生成" -p '<按 params_schema 构造的 JSON>'
popcorn-cli video submit -n "主角视频" -d "镜头测试" -p '<按 params_schema 构造的 JSON>' -s <SESSION_ID>
popcorn-cli image submit -n "文件夹产物" -d "归档测试" -p '<按 params_schema 构造的 JSON>' -f 12
```

指定文件夹时，先确认用户要归档到「AI 生成产物」目录，再 `popcorn-cli folder list -t cli_generate` 获取目录 `id`。

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
| `--folder-id` | `-f` | 否 | 归属文件夹 ID；**仅支持 `cli_upload` 目录**，不传则不归属目录 |

使用示例：

```bash
popcorn-cli resource upload ./demo.png -n "demo image" -d "reference image"
popcorn-cli resource upload ./demo.mp4 -f 123 -n "demo video" -d "reference video"
```

指定文件夹时，先确认用户要整理到「上传资源」目录，再 `popcorn-cli folder list -t cli_upload` 获取目录 `id`。`--folder-id` 必须是正整数（不能为 0），并由后端校验当前用户对该目录的权限。

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

按类型查询当前用户下某一类文件夹的扁平列表。

**Agent 注意**：若用户未说明要查哪一类，先按「交互约定」确认类型，再带上对应 `--type` 执行；不要猜默认类型。

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

返回为扁平列表，可用 `id` / `parent_id` 自行组树；创建子目录前先 `folder list` 拿到目标父目录的 `id`。

### `folder create` — 创建文件夹

创建某一类文件夹，可选挂到同类型、同用户的父目录下。

**Agent 注意**：创建前必须明确类型（按「交互约定」确认），创建成功后用自然语言反馈，例如「已在上传资源下创建文件夹「主角」」，不要复述 JSON 字段。

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

约束：`parent_id` 必须存在，且与新建文件夹属于**同一类型、同一用户**；不能把不存在的目录 ID、其他类型目录或其他用户目录当作父目录。

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

## 典型流程/使用场景示例

**生图 / 生视频**

1. `popcorn-cli image models` 选定 `model_id`
2. `popcorn-cli image models --detail <MODEL_ID>` 查看入参规范
3. `popcorn-cli image submit -n ... -d ... -p '<JSON>' [-s <SESSION_ID>]` 拿到 `task_id`
4. `popcorn-cli task list -t <TASK_ID>` 轮询至终态，读 `result`

**上传素材并归档**

1. 与用户确认目录用途；`popcorn-cli folder list -t cli_upload` 取目标目录 `id`（目录不存在则先 `popcorn-cli folder create -t cli_upload`）
2. `popcorn-cli resource upload ./a.png -n ... -d ... -f <FOLDER_ID>`

**批量任务**

用同一 `session_id` 连续 `submit` 多个任务，再用 `popcorn-cli task list -s <SESSION_ID>` 一次性汇总状态。

**凭据排查**

业务命令报未授权 → `auth status` 区分「未绑定」与「凭据失效」→ 按决策表引导 `auth bind` 重新绑定 → 重试原命令。

## 帮助信息

```bash
popcorn-cli --help
popcorn-cli auth --help
popcorn-cli auth bind --help
popcorn-cli <group> --help          # 如 popcorn-cli image --help / popcorn-cli folder --help
popcorn-cli <group> <action> --help
```
