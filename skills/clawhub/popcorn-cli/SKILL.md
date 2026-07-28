---
name: popcorn-cli
description: popcorn-cli 是 Popcorn 的命令行客户端，通过本地配置的 API Key 调用 Popcorn 后端服务：按任务类型（生图、生视频等）提交任务、查询某类型下的可用模型（含使用限制与入参 schema）、按会话 ID 或任务 ID 查询任务状态。当需要在终端、脚本或自动化流程中触发 Popcorn 后端能力、查询任务状态或查看可用模型信息时使用此 skill。
version: 0.1.0
metadata:
  openclaw:
    requires:
      bins:
        - popcorn-cli
      config:
        - ~/.popcorn-cli/config.json
    install:
      - kind: node
        package: "@zongzi1993/popcorn-cli"
        bins:
          - popcorn-cli
    skillKey: popcorn-cli
    emoji: "🎬"
    homepage: https://mangaforge-qa-1255521909.cos.ap-shanghai.myqcloud.com/docs/popcorn-cli/popcorn-cli-installation-guide.html
---

# popcorn-cli

爆米花系统(popcorn-cli)的命令行客户端，按任务类型分组组织命令，面向脚本化、自动化和 Agent 场景。

## 概念

- **会话（session）**：一次业务上下文，`session_id` 由调用方生成（例如一次剧本推进、一次 Agent 会话）。同一 session 下可提交多个任务，便于统一追踪。
- **任务（task）**：一次具体的生成请求。提交后由后端返回 `task_id`，可用它查询单个任务状态。
- **模型（model）**：每个任务类型下有多个可用模型，模型自带使用限制（时长、分辨率等）。可用模型清单与 API Key 所属租户绑定，仅返回当前租户开通且启用中的模型。提交任务前建议先用 `<group> models` 查询目标场景的可用模型。

## 能力概览

**任务提交 / 模型查询**（按任务类型两级分组，当前均为 mock 实现，接口签名一致）：

| 任务类型 | 提交任务 | 查询模型 |
|----------|----------|----------|
| 生图 | `popcorn-cli image submit` | `popcorn-cli image models` |
| 生视频 | `popcorn-cli video submit` | `popcorn-cli video models` |

所有 `submit` / `models` 子命令的参数与返回结构在各任务类型间完全一致，见下文「命令详情」小节。

**任务查询**（跨任务类型统一入口）：

| 命令 | 说明 |
|------|------|
| `popcorn-cli task list --sid <id>` | 查询某会话下的所有任务 |
| `popcorn-cli task list --tid <id>` | 查询单个任务 |

**配置管理**：

| 命令 | 说明 |
|------|------|
| `popcorn-cli config show` | 查看当前生效的配置 |
| `popcorn-cli config set-key <apiKey>` | 设置 API Key |

## 认证与配置

CLI 不接受在命令行显式传入 API Key，统一从本地配置读取。

**配置文件位置**：`~/.popcorn-cli/config.json`

**配置字段**：

| 字段 | 说明 |
|------|------|
| `apiKey` | API Key，请求时通过 `X-API-Key` 头传给后端 |

## 命令详情

### 提交任务：`image submit` / `video submit`

两类任务的 `submit` 子命令签名一致，仅调用不同后端接口。

```bash
popcorn-cli <image|video> submit -p <JSON> [-s <SESSION_ID>]
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `--params` | `-p` | 是 | 任务参数，必须是 JSON 对象字符串 |
| `--sid` | `-s` | 否 | 会话 ID，用于将同一会话下的任务关联；不传则该任务不归属任何会话 |

使用示例：

```bash
popcorn-cli image submit -p '<按 params_schema 构造的 JSON>'
popcorn-cli video submit -p '<按 params_schema 构造的 JSON>' -s <SESSION_ID>
```

`-p` 的字段结构由后端 `params_schema` 决定，同场景所有模型共用。使用前请先执行 `popcorn-cli <group> models` 查询当前租户可用的模型清单与 `params_schema`，再选定 `model_id` 并据 schema 构造 `--params`。

### 查询模型：`image models` / `video models`

查询某任务类型下当前租户可用的模型（仅返回当前 API Key 所属租户 + 场景匹配 + 启用中 + 非历史版本）。

```bash
popcorn-cli <image|video> models
```

无参数。返回结构：

```jsonc
{
  "type": "image",
  "total": 2,
  "models": [
    {
      "model_id":    "...",   // 模型唯一标识
      "name":        "...",   // 展示名
      "description": "...",   // 简介
      "model_limit": { ... }  // 单模型使用限制（不同模型可能不同）
    }
  ],
  "params_schema": { ... }    // 该场景 submit 时 --params 的字段结构（同场景所有模型共用）
}
```

`params_schema` 是 JSON Schema 风格描述，说明 `submit --params` 可用的字段、类型、默认值。同一场景（image / video）下所有模型共用一份。

**推荐流程**：先 `<group> models` 查看当前租户可用模型清单和 `params_schema`，据此选定 `model_id`，再结合 `params_schema` 的必填 / 可选字段构造 `submit` 的 `--params`。

### `task list` — 查询任务

```bash
popcorn-cli task list -s <SESSION_ID>
popcorn-cli task list -t <TASK_ID>
```

| 参数 | 缩写 | 必填 | 说明 |
|------|------|------|------|
| `--sid` | `-s` | 二选一 | 按会话 ID 查询该会话下的所有任务 |
| `--tid` | `-t` | 二选一 | 按任务 ID 查询单个任务 |

`--sid` 与 `--tid` 必须提供其中之一。

## 使用场景示例

- **CI/自动化脚本**：按 session 提交批量任务并轮询状态
- **Agent 编排**：Agent 用同一 `session_id` 提交生图 / 生视频任务，之后统一 `task list --sid` 查询整个会话的所有任务

## 帮助信息

```bash
popcorn-cli --help
popcorn-cli <group> --help          # 如 popcorn-cli image --help / popcorn-cli task --help
popcorn-cli <group> <action> --help
```
