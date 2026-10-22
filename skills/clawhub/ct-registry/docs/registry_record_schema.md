# ct-registry Normalized Record Schema（契约文档）

**version 1.0.0 · 2026-10-14**（随 ct-registry v0.14.0 引入）

> 本文档是 ct-registry `normalize.py` 产出的统一记录（normalized record）与消费方
> （`ct-pipeline/scripts/competitor_discovery.py`、`export_xlsx.py` Master/原始明细
> 表、`registry_rules.py` / `cross_source_diff.py` / `outcome_pattern_stats.py` /
> `mesh_normalize.py`）之间的**显式数据契约**。背景：此前 pipeline 侧用
> `.get()` 软取值、无契约文档，字段一旦改名会**静默变空**（同 ct-base
> coze_io_contract §2.3 节点 schema 红线的同类教训）。消费方与本表冲突时，
> **先改代码对齐本表，再提版本升级**，不得单方面漂移。

## 1. 记录形态

- 顶层：JSON 数组（也兼容 `{"records": [...]}` 包装）。
- 元素：一个统一记录 = 一个注册条目（aggregate.py 去重桥接**之前**的形态）。
- 字段三类：**核心**（所有源路径尽力提供）、**源限**（仅部分源路径提供）、
  **扩展**（可选，v0.14.0 新增键一律视为可选，消费方用 `.get()` 容错）。

## 2. 字段定义

| 字段 | 类型 | 类别 | 说明 |
|---|---|---|---|
| `source` | str | 核心 | 来源码：`CTGOV` / `CDE` / `EUCTR` / `ISRCTN` / `CHICTR` / `DRKS` / `ICTRP` |
| `registry_id` | str\|null | 核心 | 各源自有登记号（NCT…/CTR…/20xx-xxxxxx-xx/ISRCTN…/ChiCTR…/DRKS…/WHO 主 ID） |
| `title` | str\|null | 核心 | 试验标题（brief title 优先） |
| `status` | str\|null | 源限 | 招募状态（原文，未翻译） |
| `phase` | str\|null | 源限 | 归一化分期（`PHASE 3` 风格，见 normalize.py `_phase` 家族） |
| `conditions` | list[str] | 源限 | 适应症/疾病列表（自由文本，未做概念归一；概念级见 mesh_normalize） |
| `interventions` | list[str] | 源限 | 干预措施列表 |
| `sponsor` | str\|null | 源限 | 主申办方 |
| `countries` | list[str] | 源限 | 实施/招募国家（去重） |
| `start_date` | str\|null | 源限 | `YYYY[-MM[-DD]]` |
| `primary_completion_date` | str\|null | 源限 | 同上 |
| `enrollment` | int\|null | 源限 | 目标/实际样本量（int） |
| `drug` | str\|null | 源限 | 首要药物（pipeline 兼容键，interventions[0] 语义） |
| `url` | str\|null | 核心 | 详情页链接 |
| `documents` | list | 扩展 | `[{title,type,url}]`（EU CTR PDF 由 fetch_eu_ctr_docs 填充） |
| `raw` | str\|obj | 扩展 | 原始记录（WHO/ChiCTR 路径为 JSON 字符串，供桥接扫描） |
| `study_type` | str\|null | 扩展(v0.14.0) | `INTERVENTIONAL` / `OBSERVATIONAL`（CT.gov 提取；其余源多为 null） |
| `primary_outcome` | str\|null | 扩展(v0.14.0) | 主要终点 measure 文本（多值 `; ` 连接） |
| `eligibility_sex` | str\|null | 扩展(v0.14.0) | 仅 CTGOV：`ALL`/`MALE`/`FEMALE` |
| `eligibility_min_age` / `eligibility_max_age` | str\|null | 扩展(v0.14.0) | 仅 CTGOV：如 `18 Years` |
| `last_update_posted` / `results_first_posted` / `status_last_known` | str\|null | 扩展 | 仅 CTGOV（供 stale_check / registry_rules） |
| `source_limited_fields` | list[str] | 契约键(v0.14.0) | **本源提取路径无法提供的字段名列表**（见 §3）。缺键按 `[]` 处理 |

## 3. `source_limited_fields` 语义（空值契约）

空字段有两种语义，Excel Master 表据此区分渲染：

| 渲染 | 语义 | 判定 |
|---|---|---|
| `N/A*` | 该源提取路径**不提供**该字段（结构性缺失，非数据问题） | 字段名 ∈ `source_limited_fields` |
| `—` | 该源**本应提供**但本次未检索到 | 其余空值 |

各路径当前登记（normalize.py v0.14.0）：

| 源路径 | source_limited_fields |
|---|---|
| CTGOV | `[]`（全提供；v0.14.0 起补齐 primary_outcome/study_type/eligibility_*） |
| CDE | 键可缺省（视同 `[]`） |
| EUCTR | `enrollment, primary_outcome, study_type` |
| ISRCTN | `enrollment, start_date, primary_completion_date, primary_outcome, study_type` |
| CHICTR（浏览器列表 shape） | `status, phase, conditions, interventions, sponsor, start_date, primary_completion_date, enrollment, primary_outcome, study_type`（detail shape 可缓解） |
| DRKS | `primary_outcome, study_type` |
| ICTRP | 键可缺省（视同 `[]`；detail shape 字段最全） |

## 4. 各源字段可用性矩阵（Master 12 列视角）

| Master 列 | CTGOV | CDE | EUCTR | ISRCTN | CHICTR | DRKS | ICTRP |
|---|---|---|---|---|---|---|---|
| registry_id | ● | ● | ● | ● | ● | ● | ● |
| title | ● | ● | ● | ● | ● | ● | ● |
| conditions | ● | ● | ● | ● | ○ | ● | ● |
| study_type | ● | ○ | N/A* | N/A* | N/A* | N/A* | ● |
| phase | ● | ● | ● | ● | N/A* | ● | ● |
| enrollment | ● | ● | N/A* | N/A* | N/A* | ● | ● |
| status | ● | ● | ● | ● | N/A* | ● | ● |
| sponsor | ● | ● | ● | ● | N/A* | ● | ● |
| countries | ● | ○ | ● | ● | ● | ● | ● |
| start_date | ● | ● | ● | N/A* | N/A* | ● | ● |
| primary_outcome | ●(v0.14.0) | ● | N/A* | N/A* | N/A* | N/A* | ● |
| url | ● | ● | ● | ● | ● | ● | ● |

● 提供 · ○ 部分提供 · N/A* 登记于 source_limited_fields

## 5. 消费方义务

1. **一律 `.get()` 容错 + 对照本表**；发现契约漂移 → 报缺陷（adapters/bug_report.py），不得静默兜底。
2. 空值渲染遵循 §3；分析层（统计/规则）跳过 `N/A*` 字段，不得计为「缺数据」。
3. 消费方引用本表时锁定版本号；本表升版须在 ct-registry CHANGELOG 记录并向 ct-base 回写经验。
