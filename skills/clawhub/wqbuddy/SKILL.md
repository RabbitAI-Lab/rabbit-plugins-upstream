---
name: wq-buddy
description: "Provides CLI tools (`wq`) and a specialized Alpha Miner sub-agent for WorldQuant BRAIN, with v1.1.3 evolve-engine. Use for backtesting, searching BRAIN data fields, analyzing field characteristics, browsing datasets, syncing alphas, checking IS checks (auto-saves to DB), and submitting alphas. …"
metadata:
  openclaw:
    emoji: "📊"
    requires:
      bins: ["wq"]
      config:
        - path: "~/.wq-buddy/config.json"
          access: "read-write"
          purpose: "存储BRAIN平台登录凭据、默认回测参数和 LLM 配置。平台仅支持Cookie会话认证，不支持OAuth/API Key。Token缓存4小时自动刷新。"
        - path: "~/.openclaw/openclaw.json"
          access: "read-write"
          purpose: "添加插件路径并重启Gateway"
      filesystem:
        - path: "~/.wq-buddy/alpha_workbench.db"
          access: "read-write"
          purpose: "存储Alpha回测结果、字段分析、L0诊断结果（alpha_diagnosis表）"
        - path: "~/.wq-buddy/.wq_token.json"
          access: "read-write"
          purpose: "缓存BRAIN平台登录会话Token（有效期4小时），自动刷新"
      credentials:
        - name: "BRAIN账号"
          type: "username_password"
          storage: "file"
          path: "~/.wq-buddy/config.json"
          purpose: "WorldQuant BRAIN平台登录凭据"
          note: "平台不支持OAuth/API Key，仅支持Cookie会话认证"
      install:
        - id: npm
          kind: node
          package: "wq-buddy"
          label: "Install via npm"
        - id: clawhub
          kind: clawhub
          slug: wq-buddy
          label: "Install via ClawHub"
---

# WQBuddy v1.1.3 — WorldQuant BRAIN 工具与 Alpha Miner Agent

**项目仓库**: <https://github.com/sebrinass/wq-buddy>
**npm**: <https://www.npmjs.com/package/wq-buddy>

v1.1.2 修复：sync 状态映射/时间戳修正、L2/L3 失败自动重试、evolve_errors 反馈 Agent、update-status 支持 alpha_id。

***

## 一、安装

**第 1 步：安装 npm 包**

```bash
npm install -g wq-buddy
```

**第 2 步：创建配置文件** `~/.wq-buddy/config.json`

```json
{
  "version": "v1.1.3",
  "credentials": {
    "username": "你的BRAIN账号",
    "password": "你的BRAIN密码"
  },
  "default_settings": {
    "instrument_type": "EQUITY",
    "region": "USA",
    "universe": "TOP3000",
    "delay": 1,
    "decay": 0,
    "neutralization": "INDUSTRY",
    "truncation": 0.08,
    "pasteurization": "ON",
    "unit_handling": "VERIFY",
    "nan_handling": "OFF",
    "language": "FASTEXPR"
  },
  "database": { "type": "sqlite", "path": "alpha_workbench.db" },
  "batch_settings": { "sleep_between_requests": 10, "max_retries": 3, "timeout_seconds": 300 },
  "llm": {
    "provider": "openai",
    "model": "gpt-4o",
    "apiKey": "<YOUR_OPENAI_API_KEY>",
    "baseURL": "https://api.openai.com/v1",
    "maxTokens": 2000,
    "temperature": 0.3
  },
  "embedding": {
    "enabled": false,
    "base_url": "https://api.openai.com/v1",
    "api_key": "<YOUR_OPENAI_API_KEY>",
    "model": "text-embedding-3-small",
    "timeout_ms": 90000,
    "cache_ttl_ms": 1800000,
    "cache_size": 500,
    "rrf_k": 60
  }
}
```

- `llm`（可选）：provider 支持 openai/deepseek/anthropic/ollama，不配置时 evolve-engine 降级为纯规则诊断（L0 + 质量门独立运行，不依赖 LLM）
- `embedding`（可选）：用于经验匹配语义检索 + Alpha 向量空间。需兼容 OpenAI `/v1/embeddings` 接口（Ollama/Jina/OpenAI 等均可），不配置时自动降级为纯程序模式（向量空间不启用）

**第 3 步：设置文件权限（保护密码）**

```bash
chmod 600 ~/.wq-buddy/config.json
```

> config.json 包含明文密码，必须设置权限为仅用户可读写。

**第 4 步：注册运行时**

OpenClaw：在 `~/.openclaw/openclaw.json` 的 `plugins.load.paths` 中添加 npm 全局安装路径（通常为 `~/.npm-global/lib/node_modules/wq-buddy`），然后重启 Gateway：

```bash
openclaw gateway restart
```

Hermes：无插件加载机制，通过 terminal 工具直接调用 `wq` CLI（所有 18 个命令原生可用）。Hermes 只自动加载工作目录下的 `AGENTS.md`，需将 npm 包内的 `agent/AGENTS.md` symlink 到工作目录：

```bash
ln -s $(npm root -g)/wq-buddy/agent/AGENTS.md ./AGENTS.md
```

> Hermes 不会自动加载 SOUL.md / SAFETY.md / TOOLS.md（OpenClaw 会按 SOUL → SAFETY → TOOLS 顺序加载）。需把这三个文件的关键内容合并进工作目录的 AGENTS.md，或在该 AGENTS.md 顶部加"启动必读"清单显式 Read。

***

## 二、CLI 命令清单（20 个命令）

入口 `wq` + 子命令。OpenClaw 和 Hermes 下均原生可用。

### 模式 A：CLI 直接调用（轻量任务）

适合单条回测、字段搜索、状态查询。不占额外上下文。

| 命令                           | 简写   | 用途                                                                                                                                     |
| ---------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `wq backtest "expr"`         | `bt` | 单条/批量回测，支持 `--file` `--concurrency 1-3` `--enable-duplicate-check` 以及 `--decay/--neutralization/--truncation/--region/--universe` 参数覆盖 |
| `wq search "kw"`             | `s`  | 搜索数据字段，支持 `--dataset` `--limit`                                                                                                        |
| `wq search-all "家族前缀"`     | `sa` | 全量搜索字段（突破 API 50 条限制），按前缀拆分逐批拉取合并去重，自动缓存本地                                                                                       |
| `wq analyze <field>`         | `a`  | 字段特性分析（6项测试）                                                                                                                           |
| `wq stats`                   | —    | 回测统计报告                                                                                                                                 |
| `wq export [alpha\|field]`   | —    | 导出 CSV                                                                                                                                 |
| `wq operators`               | `op` | 平台 API 获取运算符清单，支持 `--category`                                                                                                         |
| `wq datasets`                | `ds` | 浏览平台数据集，支持 `--category --region --universe`                                                                                            |
| `wq competitions`            | `cp` | 用户竞赛进度                                                                                                                                 |
| `wq check <alphaId>`         | `ck` | 提交前 IS Checks（含自相关性），自动回写 DB（checks/submit_status/reject_reason/is_self_correlation）                                               |
| `wq submit <alphaId> --yes`  | `sm` | 正式提交 Alpha（不可逆，需 `--yes`）                                                                                                              |
| `wq sync`                    | —    | 从平台同步全部 Alpha 到本地数据库（分页拉取+去重+自动诊断+L2/L3触发）                                                                                             |
| `wq correlations <alphaId>`  | `cr` | 查询 Alpha 相关性                                                                                                                           |
| `wq list`                    | `ls` | 列出本地/平台 Alpha，支持 `--status --limit --offset`                                                                                           |
| `wq user`                    | `ui` | 当前用户信息                                                                                                                                 |
| `wq update-status <id> <状态>` | `us` | 更新提交状态（未通过/待check/可提交/已提交/提交失败）                                                                                                        |
| `wq diagnose --alpha <id>`   | `dg` | 对指定 alpha 跑深度诊断（L0 规则 + L1 统计 + L2 聚类 + 单轮 LLM 归因 + 反模式检测），支持 `--expression` / `--no-llm` / `--json`                                   |
| `wq insights`                | `in` | 输出 evolve-engine 整体洞察报告（L1/L2/L3/衰减/审计/反模式），支持 `--section` / `--since` / `--json`                                                      |
| `wq field-stats <类型>`        | `fs` | 字段类型失败统计（最近50条该类型Alpha的失败分布+超额率），支持 `--json`                                                                                           |
| `wq help`                    | —    | 帮助                                                                                                                                     |

> L0 诊断在回测成功后也会自动触发，结果写入 `alpha_diagnosis` 表，并通过 `alphaResult.diagnosis_patterns` / `diagnosis_suggested_fix` 字段返回。回测返回值同时顺路捎带 evolve-engine 洞察摘要（`evolve_insights` / `l1_triggered` / `l2_triggered` / `l3_triggered` / `insights_as_of`，详见第四节）。`wq diagnose` 命令用于主动对历史 alpha 跑完整深度诊断（含 LLM 归因）。

### 模式 B：spawn Alpha Miner Agent（专业任务）

适合字段勘探、批量回测（≥5 条）、策略迭代、提交全流程。需要构建携带完整领域知识的专业 Agent。

**Agent 知识文件**（npm 包内 `agent/` 目录，spawn 时注入）：

1. **工作空间规则**：`agent/AGENTS.md` —— 启动顺序 SOUL → SAFETY → TOOLS → knowledge/wiki
2. **身份与价值观**：`agent/SOUL.md` —— Alpha Miner 是谁、挖矿6步标准流程
3. **安全红线**：`agent/SAFETY.md` —— 15 条安全红线
4. **工具清单**：`agent/TOOLS.md` —— 14 个工具速查 + 6 项字段测试 + 回测参数速查
5. **领域知识库**：`agent/knowledge/wiki/` —— 字段分析/策略模式/优化诊断/平台资源/术语表/研究技巧/面试指南七大知识域
6. **17 类想法模板**：`agent/knowledge/wiki/idea-templates/`

`{npm_global}` 路径通过 `npm root -g` 获取。

> **子 Agent 分流**：回测 ≥10 条时 OpenClaw 用 `sessions_spawn` 开子 Agent；Hermes 用 `delegate_task` 替代，需在 task 描述里显式指定读 `AGENTS.md`。子 Agent 严格按父 Agent 给的回测任务执行，不擅自改配置。

***

## 三、决策路由

```
用户请求 Alpha 相关任务
│
├─ 单条表达式回测 → CLI: wq backtest "expr"（返回结果含可执行改进建议，详见 [单条优化工作流](workflows/single-alpha-optimization.md)）
├─ 搜索一两个字段 → CLI: wq search "keyword"
├─ 快速查看统计 → CLI: wq stats
├─ 查运算符/数据集/竞赛清单 → CLI: wq operators / datasets / competitions
├─ 检查 Alpha 是否可提交 → CLI: wq check <id>
├─ 提交 Alpha → CLI: wq submit <id> --yes
├─ 同步平台 Alpha 到本地 → CLI: wq sync
├─ 同步提交状态 → CLI: wq update-status <id> <状态>
├─ 列出/查相关性/查用户 → CLI: wq list / correlations / user
├─ 导出 CSV → CLI: wq export
├─ 深度诊断某条 alpha → CLI: wq diagnose --alpha <id> [--no-llm] [--json]
├─ 仅对表达式跑反模式检测 → CLI: wq diagnose --expression "rank(close)" --no-llm

└─ 以下场景 → spawn Alpha Miner Agent：
   ├─ 批量回测（≥5 条表达式）
   ├─ 字段特性勘探（6 项分析）
   ├─ 优化诊断（Sharpe/Turnover/Fitness 不达标，看 L0 诊断建议 + `wq diagnose` 深度归因）
   ├─ 策略设计（从想法到可提交 Alpha 全流程，套用 17 类想法模板）
   └─ 提交全流程闭环（待check→可提交→已提交）
```

***

## 四、evolve-engine 操作指引

### 1. 回测后看什么

每条回测完自动诊断，返回值多了以下字段：

| 字段                                               | 含义                | 怎么用            |
| ------------------------------------------------ | ----------------- | -------------- |
| `diagnosis_patterns`                             | 命中的失败模式标签         | 看"哪里有问题"       |
| `diagnosis_suggested_fix`                        | 改进建议              | 按建议改表达式        |
| `evolve_insights`                                | 新增的 L1/L2/L3 洞察摘要 | 一眼看出"有没有新经验产出" |
| `l1_triggered` / `l2_triggered` / `l3_triggered` | 是否触发了统计/聚类/抽象     | 触发后应翻完整报告      |
| `insights_as_of`                                 | 摘要截止时间            | —              |

要查完整报告：`wq insights`

### 2. 检查时机矩阵

| 触发时机       | 该查什么                    | 命令                                          |
| ---------- | ----------------------- | ------------------------------------------- |
| 会话启动       | 最近失败模式 / 策略建议 / 衰减状态    | `wq insights`                               |
| 回测完想知根因    | L0 诊断 + LLM 归因 + 反模式    | `wq diagnose -a <id>`                       |
| 攒了一批失败想找规律 | L1 统计 + L2 聚类 + 反模式 Top | `wq insights --section l1` / `--section l2` |
| 怀疑知识过时     | decay 状态                | `wq insights --section decay`               |

> 顺路捎带字段解决"回测当下有没有新洞察"，检查时机矩阵解决"什么时候该主动翻完整报告"，两者互补。Hermes 下顺路捎带原生可用——`wq backtest` 的 stdout 即返回值，`--json` 模式更结构化，Agent 解析 stdout 即可拿到洞察摘要，无需额外适配。

***

## 五、Web UI

WQBuddy 自带本地 Web UI（http://localhost:9876），用于浏览 SQLite 数据。**仅供本地使用**。

启动：`npm run db-viewer`（源码）或全局安装后运行 `wq` 包内的 `dist/db-viewer/server.js`。

登录：与 CLI 凭证打通，任意一边登录后另一边自动免密。

***

## 六、知识库（wiki）

npm 包内 `agent/knowledge/wiki/` 目录，工具模式下可主动 Read 查阅：字段分析、策略模式、17类想法模板、优化诊断、质量门禁、平台资源、术语表/研究技巧/面试指南等。

> 以上知识库在 Agent 模式下由 Alpha Miner 自动加载和维护，工具模式下可按需 Read。
> 想要完整的领域知识加持、经验自动沉淀、批量回测子 Agent 分流？切到 Agent 模式（见第二节模式 B），让专业 Agent 替你跑完整闭环。
