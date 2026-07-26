---
name: dinzeeagent
description: "Cross-border e-commerce data agent. The user triggers a data source with an at-source marker such as @sif, or installs independent Dinzee business skills from the skill registry. The agent discovers available data sources and tools at runtime, calls them through the Dinzee gateway, and handles unified authentication and per-call billing. Upstream MCP endpoints and credentials are never exposed."
---

# DinzeeAgent — 跨境电商数据 Agent

DinzeeAgent 让你用 `@<数据源>` 触发第三方电商数据能力，也支持从 Dinzee skill 仓库安装独立业务 skill。看到触发标记后，**你（agent）自行编排**调用该数据源的多个 MCP 工具，完成用户的调研/分析任务，最后汇总成结论。

所有 Dinzee 付费数据调用经由 **Dinzee Gateway**（`https://gateway.dinzee.ai/`）：网关负责鉴权、调用真实上游、记录 provider/tool 用量明细；本地业务 skill 带 `skill_slug + skill_run_id` 编排多次 MCP 调用后，最后通过 `/v1/skill-runs/finalize` 按本次 skill 总点数一次性结算。上游地址与凭证对调用方完全隐藏，本地 skill 不保存、不读取、不暴露第三方上游密钥。

例外：用户自带账号的官方外部 MCP（例如 Sellersprite / 卖家精灵）不走 Dinzee Gateway，不扣 Dinzee 点数，也不能使用 Dinzee 平台共享 key。遇到这类需求时，优先调用用户本地已经配置好的官方 MCP；如果未配置，提示用户用自己的官方 key 配置。见 `references/seller-sprite.md`。

核心执行原则：

```text
Hermes / OpenClaw / Codex 本地只负责执行 skill playbook。
所有 Dinzee 付费数据源调用必须进入 Dinzee Gateway 的 /v1/mcp/calls。用户自带官方 MCP（如 Sellersprite）直接走用户本地 MCP，不走网关。
Dinzee Gateway 负责鉴权、调用真实上游、记录明细，并在 skill finalize 时按 `skill_slug` 汇总扣费。
本地 skill 不保存、不暴露上游数据源密钥。
不要调用 server-skill-run 执行本地业务 workflow。
*_run 永远只做完成标记，不作为数据源扣费。
失败时返回 request_id，便于后台查账。
```

**有哪些数据源、每个数据源有哪些工具，都由网关运行时决定（随时新增），本文档不写死。** 每次任务先用 `providers` / `list-tools` 实时发现（见下文「工具发现」）。

## 内置业务能力

DinzeeAgent 是总入口和数据网关客户端。当前包不内置执行型 task skill，也不随包注册 server-skill manifest。业务 skill 需要从 Dinzee skill 仓库单独安装/更新。

### 数据网关工具

- `@sif` 及其他已开放 Dinzee 数据源：通过 `providers` / `list-tools` 实时发现当前可用工具，按用户 token 计费调用。
- `@sellersprite` / `@卖家精灵`：不走 Dinzee Gateway。要求用户自行配置官方 Sellersprite MCP，并直接调用用户本地 MCP；Dinzee 不扣点、不代理、不保存 key。

## Setup

1. 取得用户接入 token（`sut_` 开头，由 ai_web 签发，每个用户独立）。
2. 配置 token（二选一）：
     （写入 `~/.dinzee/credentials.json`，权限 0600，重启不丢）
3. （可选）覆盖网关地址：`export DINZEE_GATEWAY_BASE=https://gateway.dinzee.ai/`
4. 自检：`python3 <skill>/scripts/dinzee.py status` 与 `python3 <skill>/scripts/dinzee.py providers`，确认 token 有效并看到当前可用的数据源。

## 装 / 更新数据 skill（安装不扣费）

DinzeeAgent 既是数据网关客户端，也是 **skill 交付客户端**——用户可以通过它把我们的数据 skill 装进 agent、或更新到新版。安装/更新只交付包，不扣费；真实扣费发生在本地业务 skill 的付费数据调用时，通过 Gateway 按 `provider/tool` 成功调用次数计费，失败由 Gateway 自动退款。

当用户说「**@dinzeeagent 安装 <skill>**」「**@dinzeeagent 更新 skill**」「更新一下技能」之类时：

1. **看有哪些可装的 skill 及价格**：
   ```bash
   python3 <skill>/scripts/dinzee.py skills
   ```
   列出每个 skill 的 slug、最新版本、单价（`N点/次` 或 `免费`）。
2. **安装/更新某个 skill**（不扣费，只交付包）：
   ```bash
   python3 <skill>/scripts/dinzee.py skill-install <slug>
   ```
   交付成功后文件会写入 agent 的 skills 目录，openclaw 热加载即可使用。
3. **更新已装的全部内容 skill**：
   ```bash
   python3 <skill>/scripts/dinzee.py skill-update --all
   ```
   只拉取新版本包；安装/更新不扣费。

4. **同步 Dinzee 业务 skill 包**：
   ```bash
   python3 <skill>/scripts/dinzee.py sync-skills
   ```
   这会自动安装/更新当前由 Dinzee skill 仓库提供的业务 skill，用户不需要逐个记住子 skill 的 slug。

**注意**：
- 安装/更新不扣费；不要把包交付当成业务调用收费。
- `dinzeeagent` 自身是免费客户端，用 clawhub 安装/更新。
- 业务扣费发生在本地业务 skill 完成后的 `finalize-skill-run` 汇总结算上；单个 Gateway `provider/tool` 调用只记录用量。不要用 `server-skill-run` 或 `*_run` 作为本地业务 skill 的数据源扣费入口。

## 本地运行业务 skill

当用户要运行一个已经封装好的任务包，先通过 `skills` 查看可安装包，再通过 `skill-install <slug>` 或 `sync-skills` 安装到本地 Hermes/OpenClaw runtime。DinzeeAgent 本包不再内置具体执行任务；已安装的独立业务 skill 以其自身 `SKILL.md` 为准。

## 用户自带官方 MCP：Sellersprite / 卖家精灵

Sellersprite 是用户自费官方服务，不属于 Dinzee Gateway 计费数据源。处理 `@sellersprite`、`@卖家精灵`、卖家精灵关键词/市场/ASIN/评论/ABA 等需求时：

1. 不调用 `python3 <skill>/scripts/dinzee.py list-tools --provider sellersprite`，也不通过 `/v1/mcp/calls` 调 Sellersprite。
2. 检查用户当前 agent/client 是否已配置官方 Sellersprite MCP。
3. 如果已配置，直接调用用户本地 Sellersprite MCP 的 tools/list 和 tools/call。
5. 这类调用不扣 Dinzee 点数；额度消耗由用户自己的 Sellersprite 账号承担。

详细说明见 `references/seller-sprite.md`。

## 工具发现：动态，不要硬编码（核心）

**不要假设有哪些数据源、也不要背工具清单**——可用的数据源和工具由网关运行时决定，随时可能新增或下线。每次任务都先发现：

1. **看有哪些数据源**：`python3 <skill>/scripts/dinzee.py providers`
   返回当前网关已开放的 provider 列表。用户 `@xxx` 里的 `xxx` 必须在这个列表里，否则告诉用户该数据源暂未开放。
2. **看某数据源有哪些工具**：`python3 <skill>/scripts/dinzee.py list-tools --provider <source>`
   返回该 provider 全部已开放工具，**每个工具自带 `description`（官方用途说明）、`input_schema`（入参 schema）、`points_cost`（单价，null=免费）、`chargeable`**。
3. **据此自由编排**：读 `description` 理解每个工具能干什么、读 `input_schema` 知道怎么填参数，按任务需要挑工具、定顺序、多次调用，最后汇总。

这样你永远拿到的是网关上**当前真实可用**的工具及其官方说明——新接入的数据源/工具无需更新本文档即可使用。

## 触发与编排

当用户输入含 `@<source>`（例如「使用 @sif 帮我调研 B0CP9Z56SW」），你应当：

1. **理解任务**：用户想要什么结论（广告诊断 / 关键词机会 / 流量异常 / 销量趋势 / 综合调研 …）。
2. **发现工具**：`providers` 确认 `<source>` 可用 → `list-tools --provider <source>` 拿到该源全部工具及说明。
3. **自由编排**：从工具清单里挑合适的，按需多次调用。一般思路——
   - 综合调研一个对象：先用「结构/概览类」工具看全貌 → 再按需下钻「趋势类 / 明细类」工具 → 需要时用「诊断/分析类」工具。
   - 具体用哪些工具、什么顺序，**完全依据 `list-tools` 返回的 `description` 自己判断**，不要套用固定工具名。
4. **每个工具调一次 CLI**（同步、秒级返回单工具结果）：
   ```bash
   python3 <skill>/scripts/dinzee.py call <tool_name> --args '<json>'
   ```
5. **汇总**：把多次调用的 JSON 结果整合成一份给用户的结论（不要把原始 JSON 直接丢给用户）。

带 `skill_slug + skill_run_id` 的业务 skill 调用不会在单个工具阶段扣点；网关会记录每个成功工具的 `points_cost`。skill 结束后必须调用 `finalize-skill-run`，网关按本次 run 的成功工具总点数，以 `workflow_id=<skill_slug>` 一次性扣点并返回工具调用统计。

### 本地业务 skill 的计费闭环（必须）

业务 skill 运行时必须生成一个稳定的 `skill_run_id`，并在本次运行里的每个 Dinzee MCP 调用中传入 `skill_slug` 和 `skill_run_id`：

### 本地业务 skill 烟雾测试与版本校验

做安装后验证/烟雾测试时，优先遵循下面几条：

1. **安装版本以 `<skill_dir>/_meta.json` 为准**。某些 Dinzee skill 的 `SKILL.md` frontmatter 版本号可能滞后于实际安装版本；当用户指定测试 `@1.0.4` 这类版本时，先读 `_meta.json` 再下结论。
2. **`dinzee_skill_runner.py`、实际 Gateway 调用、`meter_skill_run.py` 必须共用同一个 `DINZEE_SKILL_RUN_ID`**。否则 finalize 容易报 `CLIENT_SKILL_RUN_EMPTY`。
3. **重复测试必须更换每次调用的 `idempotencyKey`**。同一工具、不同参数却复用旧 key，会触发 `409 IDEMPOTENCY_CONFLICT`。
4. **`report_hosting.upload_artifacts` 返回 `mode=local_artifact_placeholder` 时，只能证明 Gateway 调用链和 finalize 可用**，不能当作“公网报告托管功能已完整验证”。
5. **当用户要求“每个 skill 都要按同一结算标准来”时，以 `sif-amazon-ads-analysis@1.0.5` 为基准审计 3 个脚本位点**：
   - `scripts/meter_skill_run.py` 必须复用 `dinzee_wrapper.finalize_skill_run()`，不要自己裸调 finalize 接口。
   - `scripts/dinzee_skill_runner.py` 必须把 `skill_run_id` 写入 `<OUTPUT_DIR>/data/run_context.json`。
   - `scripts/dinzee_wrapper.py` 必须在 finalize 成功后，用服务端返回重写 `dinzee_billing_response.json` 与 `billing_summary.json`。
6. **不要把“finalize 成功”误判为“整个业务 skill 已完成可计费闭环”**。还要继续检查主业务数据调用是否真的经过 Dinzee Gateway；如果业务脚本仍直连外部 MCP 或硬编码第三方 key，finalize 可能成功但 `tool_usage` 为空或 0 点。
7. 当主业务数据必须走用户本地官方 MCP、但又需要 Dinzee 计费闭环时，采用“混合链路”模式：主分析保留在本地官方 MCP，下挂 1 个同 `DINZEE_SKILL_RUN_ID` 的 Dinzee 可计费补充步骤，再 finalize。已验证样例见 `references/mixed-chain-business-skills.md`。
8. 详细做法见 `references/dinzee-business-skill-smoke-tests.md` 与 `references/business-skill-finalize-standard.md`。

```bash
export DINZEE_SKILL_SLUG="<business-skill-slug>"
export DINZEE_SKILL_RUN_ID="run_$(date +%s)_$RANDOM"
python3 <skill>/scripts/dinzee.py call <tool_name> --provider <provider> --args '<json>'
```

或显式传参：

```bash
python3 <skill>/scripts/dinzee.py call <tool_name> \
  --provider <provider> \
  --skill-slug <business-skill-slug> \
  --skill-run-id <run_id> \
  --idempotency-key <stable-step-key> \
  --args '<json>'
```

每个工具成功后返回 `billing.chargeStatus=deferred`，表示已经记录用量、等待本次 skill 汇总结算。业务 skill 完成后必须调用：

```bash
python3 <skill>/scripts/dinzee.py finalize-skill-run \
  --skill-slug <business-skill-slug> \
  --skill-run-id <run_id> \
  --idempotency-key <stable-final-key>
```

finalize 返回 `total_points`、`points_charged`、`billing_ledger_id` 和 `tool_usage`。`tool_usage` 是本次 skill 的 provider/tool 明细；后台扣费只发生一次，`workflow_id=<skill_slug>`。

## CLI 速查

```bash
# 列出当前已开放的数据源（不扣点）
python3 <skill>/scripts/dinzee.py providers

# 列出某数据源的全部工具，带 description / input_schema / points_cost（不扣点）
python3 <skill>/scripts/dinzee.py list-tools --provider <source>

# 查看单个工具是否可用 / 是否扣点
python3 <skill>/scripts/dinzee.py describe <tool>

# 调用工具（JSON 入参；可用 --skill-slug / --skill-run-id 写入账单维度）
python3 <skill>/scripts/dinzee.py call <tool> --args '<json>'

# 大入参从 stdin 读（heredoc）
python3 <skill>/scripts/dinzee.py call <tool> --stdin <<'EOF'
{"asin": "B0CP9Z56SW", "marketplace": "US"}
EOF

# 原始 JSON 输出（便于你程序化解析后再汇总）
python3 <skill>/scripts/dinzee.py --format json call <tool> --args '{...}'

# 耗时较长的工具可调大超时（秒）
python3 <skill>/scripts/dinzee.py call <tool> --timeout 300 --args '{...}'

# token 状态
python3 <skill>/scripts/dinzee.py status

# 一键安装/更新 Dinzee 官方业务 skill 包
python3 <skill>/scripts/dinzee.py sync-skills
```

## 错误处理

| HTTP | code | 含义 / 处理 |
|---:|---|---|
| 401 | `USER_INTEGRATION_TOKEN_REQUIRED` | 没传 token；CLI 会自动带，通常是 token 没配，跑 `status` 检查 |
| 401 | `USER_INTEGRATION_TOKEN_INVALID` | token 错或过期，让用户重新取一个 |
| 402 | `INSUFFICIENT_POINTS` | 用户积分不足，提示充值 |
| 403 | `MCP_PROVIDER_NOT_ALLOWLISTED` / `MCP_TOOL_NOT_ALLOWLISTED` | provider/tool 名拼错，或该数据源/工具未在网关开放——用 `providers` / `list-tools` 确认当前可用 |
| 409 | `IDEMPOTENCY_CONFLICT` | 同 idempotencyKey 配了不同参数；CLI 默认随机 key，一般不会遇到 |
| 503 | `MCP_PROVIDER_UNAVAILABLE` | 上游不可达/鉴权失败，网关已记熔断 |
| 503 | `MCP_PROVIDER_CIRCUIT_OPEN` | 上游连续失败触发熔断，等几十秒重试 |

调用失败时读 error 详情，按上表调整或重试；不要把原始报错直接丢给用户，转述成可理解的提示。

## Examples

> 下列示例只示范**工作流程**，`<...>` 处的工具名/参数一律以 `list-tools` 的实时返回为准，不要照抄占位名。

### Example 1：综合调研一个 ASIN（典型 @<source> 编排）

用户：「使用 @sif 帮我调研 B0CP9Z56SW」。你应当：

```bash
# 1) 发现该源的工具
python3 <skill>/scripts/dinzee.py list-tools --provider sif
# 2) 读 description 选工具：先调「广告/流量结构概览」类工具看全貌
python3 <skill>/scripts/dinzee.py call <结构概览工具> --args '{"asin":"B0CP9Z56SW","marketplace":"US"}'
# 3) 按需下钻「趋势 / 关键词 / 明细」类工具
python3 <skill>/scripts/dinzee.py call <趋势或关键词工具> --args '{"asin":"B0CP9Z56SW","marketplace":"US"}'
# 4) 如怀疑异常，再调「诊断/分析」类工具
```
然后把多份结果整合成一份「结构 + 流量来源 + 关键词机会」的调研结论给用户。

### Example 2：关键词研究

```bash
python3 <skill>/scripts/dinzee.py list-tools --provider <source>
python3 <skill>/scripts/dinzee.py --format json call <关键词需求工具> --args '{"keyword":"wireless earbuds"}'
python3 <skill>/scripts/dinzee.py --format json call <关键词竞争工具> --args '{"keyword":"wireless earbuds"}'
```
对比需求强度与竞争程度，给出选词建议。

### Example 3：耗时较长的诊断类工具

```bash
python3 <skill>/scripts/dinzee.py call <诊断分析工具> --timeout 300 \
  --args '{"asin":"B0XXXXXXXX","marketplace":"US"}'
```
