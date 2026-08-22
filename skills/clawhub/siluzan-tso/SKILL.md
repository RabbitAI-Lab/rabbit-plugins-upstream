---
name: siluzan-tso
description: 丝路赞 TSO 广告平台（Google/Bing/Yandex/TikTok/Kwai/MetaAd），凡涉及丝路赞/TSO、投广告、出价预算、广告账户管理，或需要做行业分析/市场分析/行业分析报告（含「写一份 XX 行业报告」「电商/制造/医疗等行业报告」「市场调查/战略市场/KA 市场报告」「竞品/GTM/市场格局/行业趋势」等，无论是否提及丝路赞/广告/客户）须加载本 skill。【§零·最高优先】网址/域名/官网+诊断/检测/监测/评估/体检/报告/符合投放要求/能不能投（含「网络诊断」混说）→P8 website-diagnosis collect（禁纯WebFetch/肉眼看页），禁止P9/P1/W3、禁止A/B/C/D追问；细则见 intent-routing.md §零。【§零·B·次高优先】未命中§零时，行业/市场分析报告类话术→必走P9 market-analysis collect+render出HTML，禁止纯WebSearch/WebFetch在对话里写Markdown/HTML当终稿、禁止改走P8/P1/P4/W5/google-analysis；细则见 references/core/intent-routing.md §零·B。【§零·C·关键词规划】Google Ads/谷歌广告拓词、关键词规划/推荐、Keyword Planner、长尾关键词、月搜索量/搜索量、竞争度、核心词/种子词扩词（含「阅读网址/文章/页面后针对核心词出带搜索量词表」，无论是否提及丝路赞/TSO/账户）→必走W5 keyword -k … --google-only --json-out，禁止WebSearch/WebFetch编造搜索量当终稿；细则见 references/core/intent-routing.md §零·C。【报告/诊断消歧】其余报告类话术禁止默认某一CLI——行业/市场/战略/行业分析报告→P9 market-analysis（必走collect+render，禁止纯WebSearch代替）；Google账户ID+健康诊断→P1 google-ads-diagnosis；账户ID+周期/月度→P4；Meta/TikTok/Bing周期→P4/P4-FB；多账户对比→P3/P5；OKKI周报→P6；Google询盘→P7；官网+明确要搜索广告方案/campaign JSON→W3；仅要词表+搜索量/竞争度→W5；平台优化报告列表/推送→W7；对象仍不清→Read intent-routing.md。【账户】列表/余额/消耗/激活账单（W1）、多账户余额预警 balance-scan（P2）、多户消耗汇总 accounts-digest（P3）、六大媒体开户与进度（W2）、分享/解绑/MCC/BC/BM/权限（W9）。【投放】Google **仅支持搜索广告（Search）与 PMax**（不支持展示广告 Display）；搜索系列方案与 campaign-validate/create（W3）、系列/组/广告/关键词 CRUD/拒审、PMax 创建与素材、AI智投草稿 batch（W4）、拓词 keyword -k（W5）、AI广告优化 optimize（W6）、优化合规 SOP。【财务】充值/钱包、转账记录、发票/开票/抬头（W8）；写操作审计与 restore。【运营】智能预警 forewarning 创建/启停/记录（W10）、TikTok/Meta 线索 clue（W11）、日周巡检（W12）、宿主编排/投放自控/异常监控（hosted-automation）。【其他】RAG 知识库检索、Meta/Facebook 周期与诊断 HTML、Google/Meta 周期 Excel、多账户 google-analysis-batch。
license: MIT
compatibility: 需要 Node.js 18+、已安装 siluzan-tso-cli，通过 send-login-code + login 或 config set 完成鉴权
metadata:
  requires: nodejs,siluzan-tso-cli
allowed-tools: Bash(siluzan-tso:*) Read Write
---
<!-- AUTO-GENERATED from SKILL.md.tmpl — edit .tmpl or snippets/, then: node scripts/gen-skill-docs.mjs -->

# Siluzan TSO Skill

本文件只做 **任务路由**：意图 → **唯一**工作流 → 按需 Read 子文档（参数与步骤不在此重复）。

- 分析 / 报告 → `references/core/playbooks.md`（P1–P9）
- 操作 / 管理 → `references/core/workflows.md`（W1–W12）
- 命令参数 → 路由表「必读文档」
- 通用纪律与沟通 → `references/core/agent-conventions.md`

> **加载**：按下方路由表 Read **一个**工作流卡片 + **一个**命令/报告 reference 后执行。写操作、报告交付、批量拉数、对用户写结论、或上下文被压缩时，再 Read `references/core/agent-conventions.md`（含 §十四沟通）。
>
> **报告 / 诊断 / 分析 / 拓词 / 转化成本·CPA·零询盘话术模糊**：先 Read `references/core/intent-routing.md`（含 **§零·D**：无 CRM 的转化巡检 → P3，不是 P7），再回路由表。数据任务一律 `--json-out` + 代码读盘（示例见 `references/core/tips.md`）。未指定格式时 P1/P4/P4-FB/P8/P9 默认 **HTML**；**P6/P7 默认多 Sheet `.xlsx`**（「表格形式」= xlsx，禁止 Markdown 表 / 手写 HTML 代替）。巡检类任务须交付摘要或显式失败原因。

---

## 基本使用

```bash
siluzan-tso -h
```

未安装 / 未登录 / 401 → Read `references/core/setup.md`。

**步骤**：① 报告类模糊 → Read `intent-routing.md` → ② 锁定下方**唯一**工作流行 → ③ Read 该行「必读文档」+ 工作流卡片 → ④ 按编号步骤执行；写操作前与用户确认；对用户写结论时 Read conventions §十四。**禁止** Read `report-templates/*.html`（由 CLI `render` 使用）。

---

## 即时规范

- `entityId`（UUID）≠ `mediaCustomerId`（`list-accounts` 的 `ma.mediaCustomerId`：Google/TikTok/Bing 多为数字；**Yandex=`porg-…`**；Meta 常带 `act_`）。`stats`/`balance`/`accounts-digest`/`ad *` 的 `-a` **只传 mediaCustomerId**；空结果或 verbose 打出 403 时**先核验 ID**，禁止把 UUID/`entityId` 传给 `-a`，也**禁止**据此直接 `reauth`。
- **Google CID 特殊性**：UI 常写 `123-456-7890`（带连字符），平台 `mediaCustomerId` 为纯数字 `1234567890`。CLI 会自动去连字符；**勿**把带横杠 403 误判为 OAuth 失效。优先用 `list-accounts` 的纯数字 ID。
- **禁止臆测授权过期**：见 403/`HTTP 403`/拉数失败/「可能 OAuth 失效」时，**禁止**口头推断授权过期或直接 `reauth`。须先核验 ID（及 Google 连字符）。**`account check-access` 仅支持 Google**（无 `-m`，禁止对 TikTok/Meta/Bing/Yandex/Kwai 调用）：Google 跑 `account check-access -a <mediaCustomerId>`，以 `accessible` / `reauth_required` / `no_permission` 为准；非 Google 看 `list-accounts` 的 `invalidOAuthToken`。仅当 `list-accounts` 输出含激活字段且可判定未激活时才跳过用其判断授权过期；细则见 `accounts-permissions.md`。
- **Google 广告命令名**：列表是 `ad campaigns`（不是 `ad-campaigns` / `campaign list`）；`balance`/`stats` 须带 `-m Google`；单国地域用 `ad geo search … --json-out`（或 `geo resolve`）。
- **Google 广告类型边界**：CLI/Skill **仅支持** Google **搜索广告（Search）** 与 **Performance Max（PMax）** 的方案、创建与精细管理；**不支持展示广告（Display）**（含自适应展示广告 RDA、独立 Display 系列）。用户要做展示广告时须明确告知不支持，可改推 Search / PMax；**禁止**用 `campaign-create` / `ad-create` 伪装创建 Display。
- **创建完成后交付（硬性）**：`ad batch diff` 的 stdout 含 `BEGIN_USER_DELIVERY_MARKDOWN`…`END_USER_DELIVERY_MARKDOWN`——**立刻**把中间全文原样发给用户（可先于补建）；禁止只摘要、禁止只说「创建成功/详情已交付/未发现缺失」、禁止等全部补建结束再交付。
- `list-accounts` 无余额/消耗；列全部用 `--page-size 999`。
- 多户余额用 `balance-scan`（P2），多户消耗用 `accounts-digest`（P3）；禁止外层 for-loop 逐户拉数。
- `stats` 的 `spend` = **区间合计**，不是日消耗。
- 行业/市场报告禁止纯 WebSearch 当终稿；须 P9 `market-analysis collect`+`render`。
- **禁止编造平台网址**：给用户 `*.siluzan.com` / `mysiluzan.com` 链接前，**必须**当轮 `config show` 取 `webUrl`，路径**只**用已 Read 文档中的相对路径表拼接；CLI 输出的授权 URL **原样粘贴**；文档未给路径则**不拼链接**。细则见 `agent-conventions.md`。

---

## 路由表（意图 → 工作流 → 必读文档）

> 写操作 / 报告交付 / 批量拉数 / 对用户回复 → Read `agent-conventions.md`。找不到行 → 澄清或 Read `intent-routing.md`（勿整本加载 `references/README.md`）。

### 账户与财务

| 用户意图（关键词） | 工作流 | 必读文档 |
| ------------------ | ------ | -------- |
| 账户列表 / 有哪些 / 有多少 / 列出全部某媒体 | W1 | `references/accounts/accounts-list.md`（list-accounts） |
| 单户实时余额 | W1 | `references/accounts/accounts-balance-stats.md`（balance） |
| 多账户余额 / 续航不足预警 | **P2** | `references/accounts/accounts-balance-stats.md`（balance-scan） |
| 单户消耗 / 投放数据 | W1 / **P1** | `references/accounts/accounts-balance-stats.md`（stats） |
| 多账户消耗/对比汇总 / 转化成本·CPA·零转化巡检（无 CRM） | **P3** | `references/accounts/accounts-balance-stats.md`（accounts-digest）；消歧见 `intent-routing.md` **§零·D** |
| 激活/充值账单明细 | W1 | `references/accounts/accounts-list.md`（account-active-bills） |
| 开户（六大媒体）/ 开户进度 | W2 | `references/accounts/open-account-by-media.md`（**首次须列全必填项**；Google 加 `open-account-google-ui.md`） |
| 账户权限：分享/取消/解绑/重授权/MCC/BC/BM/关闭/提现/邮箱授权 | W9 | `references/accounts/accounts-permissions.md` |
| 充值 / 钱包 / 转账 / 发票 / 抬头 | W8 | `references/accounts/finance.md` |
| 审计 / 误操作恢复 | — | `references/accounts/write-audit-restore.md` |

### Google 广告投放

> **类型边界**：仅 **Search** + **PMax**；**不支持 Display（展示广告）**。详见 `references/google-ads/google-ads.md` Gotchas。

| 用户意图（关键词） | 工作流 | 必读文档 |
| ------------------ | ------ | -------- |
| 新建搜索系列 / 出投放方案 / Excel·表格方案 / 官网生成搜索广告 | **W3** | `references/google-ads/google-ads-campaign-plan.md`（§**仅出方案 vs 创建**）+ **`assets/campaign-create-template.json`**（先 Read）+ `assets/campaign-create-template.md` + `rules/google-ads-launch-plan-template.md`（JSON 后**写代码**投影完整审查稿）；有方案文件时加 `rules/google-ads-plan-source-fidelity.md`。**≠ P8 / ≠ P9 / ≠ W5**；**禁止**因缺账户阻塞出方案、**禁止**只交概览表 |
| 展示广告 / Display / 自适应展示广告（RDA） | — | **不支持**。向用户说明后改推 Search（W3）或 PMax（W3）；勿创建、勿假装已支持 |
| 广告系列/组/广告/关键词 **查询** / 拒审字段 | W3 | `references/google-ads/google-ads-read.md` |
| 广告系列/组/广告/关键词 **创建·编辑·启停** | W3 | `references/google-ads/google-ads-write.md` |
| PMax 系列 | W3 | **`assets/pmax-create-template.json`**（先 Read）+ `assets/pmax-create-template.md` + `rules/google-ads-pmax-launch-plan-template.md`（**写代码**投影完整审查稿）+ `references/google-ads/pmax-api.md` + `google-ads-write.md`（PMax 节） |
| AI 智投草稿 list/get/update/publish | W4 | `references/google-ads/google-ads-batch.md` |
| 拓词 / keyword / 关键词规划 / 月搜索量 / 竞争度 / Keyword Planner | **W5** | `references/analytics/keyword-planner-workflows.md`（**§零·C**；客户背景先 `references/analytics/rag.md`） |
| AI 广告优化记录 / 建议 | W6 | `references/operations/optimize.md` |
| 优化/合规 SOP | W3 / W6 | `references/google-ads/rules/README.md`（**仅读索引表** → 再 Read **一个**具体 `rules/*.md`） |

### 分析与报告

| 用户意图（关键词） | 工作流 | 必读文档 |
| ------------------ | ------ | -------- |
| Google 广告账户诊断 / 健康检查（**含账户 ID**） | **P1** | `references/analytics/account-analytics.md` + `report-templates/google-ads-diagnosis.md`（可选对照 `report-templates/google-account-diagnosis-report.md`） |
| Google 账户周期 / 月度 / 季度报告（非 OKKI / 非询盘 / 非强调健康诊断） | **P4** | `report-templates/google-period-report.md` + `references/analytics/account-analytics.md`；Excel 加 `google-period-report-excel.md` |
| Meta/Facebook 周期或诊断 | **P4-FB** | `report-templates/meta-period-report.md` + `assets/meta-period-report-rules.md` + `references/analytics/facebook-analysis-guide.md` |
| TikTok / Bing 周期报告 | **P4** | `references/analytics/account-analytics.md` + 对应 `report-templates/*-period-report.md` |
| Yandex 账户分析 / 周期 / 月报 | **P4** | `report-templates/yandex-period-report.md` + `references/analytics/account-analytics.md`；Excel 加 `yandex-period-report-excel.md` |
| 账户级按日 Excel | **P4-DAILY** | `report-templates/stats-daily-excel.md` |
| 多账户 × 多维度批处理 | **P5** | `references/analytics/google-analysis-batch.md` + `references/analytics/account-analytics.md` |
| OKKI 周报 / 表格形式（OKKI） | **P6** | `report-templates/okki-weekly-google-client.md`（**必产 5 Sheet `.xlsx`**；「表格形式」= Excel） |
| Google 询盘分析（**须 CRM 询盘资料**；口语零询盘/CPA → **P3**） | **P7** | `report-templates/google-inquiry-analysis.md` + `references/analytics/geo-continents.json` |
| 网址/域名/官网 + 诊断·检测·监测·报告 / **是否符合广告投放要求** / 能不能投 | **P8** | `references/core/intent-routing.md` §零 + `references/analytics/website-diagnosis-guide.md` + `assets/website-diagnosis-rules.md`（**必** `website-diagnosis collect`；**≠ P9 ≠ W3**；禁纯 WebFetch） |
| 市场/行业分析报告 / 战略市场 / KA 市场报告 | **P9** | `references/analytics/market-analysis-guide.md` + `assets/market-analysis-rules.md`（须 collect+render；**≠ P8**） |
| TSO 平台优化报告：列表/生成/推送 | W7 | `references/analytics/reporting.md` |
| RAG 知识库检索 | W5 | `references/analytics/rag.md` |

### 工具与运营

| 用户意图（关键词） | 工作流 | 必读文档 |
| ------------------ | ------ | -------- |
| 智能预警：创建/查询/启停/触发记录 | W10 | `references/operations/forewarning.md` |
| TikTok / Meta 线索表单 | W11 | `references/operations/clue.md` |
| 日/周巡检 | W12 | `references/core/workflows.md`（W12）+ `references/accounts/accounts-balance-stats.md` |
| 超预算熔断 / 空耗熔断（全户 Google） | — | `references/operations/guard.md`（`guard budget-circuit` / `guard zero-conv`；禁止逐户 for-loop） |
| Bing 自动化巡检（封禁/拒审/超预算/空耗预警） | — | `references/operations/hosted-automation-bing.md`（只读告警，不能自动暂停/改价） |
| Yandex 自动化巡检（余额/CPA/日花费预警） | — | `references/operations/hosted-automation-yandex.md`（只读告警，不能自动改投放） |
| TikTok 自动化巡检（封禁/拒审/超预算/空耗预警） | — | `references/operations/hosted-automation-tiktok.md`（只读告警，不能自动暂停/改价） |
| 宿主编排 / 投放自控 / 异常监控 / 自动优化 | — | `references/operations/hosted-automation-user-catalog.md`（**仅当用户问自动化/巡检/熔断**；表内每行只 Read **一个** SOP；Google 熔断优先 guard.md；Bing/Yandex/TikTok 走上三行） |

---

## Subagent 自主委派（可选）

宿主具备 Task / subagent 时：复杂报告或批处理（**P5 / P6 / P7**）、预计 CLI 输出很长 → Read `references/core/subagent-orchestration.md`；handoff 在 `snippets/handoff-p{5,6,7}-*.md`。写操作确认、`--commit`、401/`resume` 与最终交付留在主 Agent。

---

## 职责划分

| 本 Skill + CLI | 宿主 / 外部调度 |
| -------------- | --------------- |
| 结构化拉数（`--json-out`）、写命令语义、金额/ID 口径 | 触发时机、IF 决策、触达（钉钉/飞书）、批处理限速；可选 subagent 并行 |
