# 原文证据切片：cloudbase-2.32.4

> 关键原文摘录，供亮点条目溯源。来源：`<本地参考目录>/cloudbase-2.32.4`。

---

## 1. activation-map.yaml — 结构化场景路由契约（A-074 / A-076 / A-077 / A-078）

```yaml
- id: web-auth
  label: Web login / registration / auth UI
  priority: 100
  signals:
  - CloudBase Web 登录
  - Web 注册
  - auth login page
  - publishable key
  - 短信登录
  firstRead: auth-tool-cloudbase
  thenRead:
  - auth-web-cloudbase
  - web-development
  beforeAction:
  - 先检查并开启所需登录方式，再写前端代码。
  - 优先通过 `queryAppAuth` / `manageAppAuth` 获取 publishable key。
  doNotUse:
  - cloud-functions
  - http-api-cloudbase
  mustCheckBeforeAction:
  - Provider status and publishable key
  commonMistakes:
  - 把 Web 登录实现成云函数认证逻辑。
  - 未开启 provider 就直接生成登录 UI。
```

**每个场景都含**：`priority / signals / firstRead / thenRead / beforeAction / doNotUse / mustCheckBeforeAction / commonMistakes`——比"意图→动作"两列表多出负向路由、动作前检查、常见错误三个维度。SKILL.md 顶部路由表标注 `<!-- DO NOT EDIT: auto-generated from references/activation-map.yaml -->`。

---

## 2. 顶层路由表（A-074 的自动生成产物 + 负向路由列）

| Scenario | Read first | Then read | **Do NOT route to first** | **Must check before action** |
|----------|------------|-----------|------------------------|--------------------------|
| CloudBase PostgreSQL / PG | `postgresql-development-cloudbase` | ... | `relational-database-mcp-cloudbase`, `cloudbase-document-database-web-sdk` | PG schema, usernamePassword login, backend/RLS permission model |

---

## 3. tooling-fallback.md 决策树（A-07A）

```text
1. Probe MCP in THIS session
2. MCP tools usable now?
   ├── YES → Prefer MCP (inspect schemas, then call). Skip CLI for the same action.
   └── NO  → Continue below (do not spin on missing tools)
3. Is MCP configured?  NO → Install/configure MCP now, tell user a restart
     will unlock MCP next session, THEN use CLI for this session.
4. CLI path for this session ... tcb login → confirm envId → tcb env use <envId>
5. After the user restarts the session → Re-probe MCP; switch back to MCP-first.
```

**硬规则**（节选）：
- **Do not loop** — after 1–2 failed MCP probes, fall back; do not retry MCP setup 5+ times.
- **No silent npm assumption** — if npm/npx is missing, surface the Node install path before retrying.
- **Do not recommend `tcb deploy`** — always open the matching domain skill and follow its commands.

---

## 4. cloudbase-code-review — 双轨规则库 + 规则边界（A-083 / A-103）

**双层机制**：

| Layer | Method | What it catches |
|-------|--------|-----------------|
| **Lint** | 正则（`node cloudbase-lint.mjs`） | 确定性错误（错 API 调用、缺配置、模式不匹配） |
| **LLM review** | 读每条规则 "LLM 检查" 节，语义审查 | 路由守卫逻辑、RLS 完整性、架构级问题 |

**规则统一格式**：
```markdown
# RULE-ID Rule Name
- **Module**: auth / postgresql / storage / ...
- **Severity**: error | warning
- **Stage**: code-generation | deployment | config

## 正则检查 (Lint)    ← 给确定性脚本
## LLM 检查           ← 给语义审查
## 修复指引           ← 怎么修
```

**Rule boundary（规则边界纪律）**：
> "Do not promote a single failed run or case-specific workaround into a hard rule. A rule should be backed by stable SDK/API documentation, repeated failures, or deterministic runtime behavior. Case-specific observations belong in attribution reports; only broadly applicable constraints should enter RULES_INDEX or the lint checklist."

---

## 5. minimal-web-baas-demo — 能力嗅探顺序 + BaaS-first（A-023 / A-053）

```text
0. Connector pre-enabled (or shortest Trust path)
1. Template warmup // parallel with credential wait   ← 等待期并行预热
2. envQuery(action="info")                            ← 嗅探 env
3. Lock ONE DB plane (NoSQL | PG | MySQL)             ← no mid-flight thrash
4. MCP schema + minimal permissions
5. Browser @cloudbase/js-sdk CRUD
6. Local preview (list + add)
7. Cloud functions ← skip (count = 0) unless secrets/cron/rules-cannot-express
```

**Cloud functions are forbidden by default**：`Todo/Notes/Chat/Kanban → zero cloud functions`。创建云函数**唯一条件**：(a) 逻辑安全规则/RLS 表达不了 **且** (b) 需要服务端密钥 或 定时/后台任务。

---

## 6. spec-workflow — EARS 验收标准（A-043）

```text
EARS pattern: While <optional precondition>, when <optional trigger>,
the <system name> shall <system response>

Example: When the user submits the form, the booking system shall
validate required fields before creating the record.
```

**三阶段**：requirements.md（问题/范围/用户故事/EARS 验收标准）→ design.md（架构/技术选型/数据模型）→ tasks.md（可执行任务，每条回链需求）→ **逐阶段用户确认后才进下一阶段**。

---

## 7. 三层横切协议（A-079）

`references/cloudbase-platform/references/protocols/`：
- `change-safety-protocol.md` — 任何代码/配置变更前必读
- `deployment-gate.md` — 部署/发布/自定义域名/CloudRun 前必过检查
- `sensitive-runtime-data-protection.md` — 禁止 echo `x-cloudbase-context` / 完整 `req.headers` / `process.env`

路由器统一声明："Making code or configuration changes without first following the Change Safety Protocol" 列为 common mistake。
