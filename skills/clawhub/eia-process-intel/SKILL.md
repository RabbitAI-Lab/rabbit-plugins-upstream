---
name: eia-process-intel
slug: eia-process-intel
displayName: EIA Process Intelligence
summary: 从环评报告提取企业真实产线的结构化事实，审查数字背后的监管博弈，推断工艺路线与设备选型，沉淀为可生长的三元组 ledger。Extract structured production-line facts from environmental impact assessment (EIA) reports, audit numbers for regulatory gaming, infer process routes and equipment selection, and accumulate a growing triple-store ledger.
license: MIT
description: 'Investigation workflow that turns Chinese EIA reports (环境影响评价报告/报告表/公示) into investment due-diligence intelligence: structured extraction (product scheme, per-step process flow, equipment list, material balance), adversarial field-credibility grading (EIA numbers are regulatory-gaming artifacts, not facts), physics-based cross-validation (low-risk fields as trust anchors to back-calculate capacity/yield/emissions), a per-industry process→equipment mapping knowledge base, and an append-only triple ledger with full provenance. 从环评报告提取企业真实产线的结构化事实，审查数字背后的企业与监管博弈，按字段博弈分级做交叉验证与反算（产能/良率/排放），以工序→设备映射库推断设备选型档次，并将结果沉淀为带来源、可生长的三元组 ledger。 Use when analyzing a company''s EIA filing, inferring real production lines and equipment selection, verifying capacity/yield claims, auditing EIA numbers for distortion, or building a process/equipment knowledge ledger. 触发场景：一级市场尽调、产能真实性核验、设备选型推断、物料平衡良率倒推、环评数字博弈审查、工艺路线判定 / Triggers: EIA report analysis, environmental impact assessment, capacity verification, equipment selection inference, material balance, yield back-calculation, regulatory gaming audit, process route identification.'
version: 0.1.3
agent_created: true
---

# 环评工艺情报（EIA Process Intelligence）

> **English** — This skill turns Chinese EIA filings (环境影响评价报告 / 报告表 / 公示) into investment due-diligence intelligence: structured extraction of product schemes, per-step process flows, equipment lists and material balances; adversarial field-credibility grading (EIA numbers are regulatory-gaming artifacts, not facts); physics-based cross-validation using low-risk fields as trust anchors; process→equipment mapping inference; and an append-only triple ledger with full provenance. Worked example: a fictionalized IR-detector case under `examples/`. **Full English documentation lives in [`en/SKILL.md`](en/SKILL.md)** (workflow, references, and a worked example mirrored).

定位：从环评报告提取企业真实产线的结构化事实，审查数字背后的监管博弈，推断工艺路线与设备选型，并将结果沉淀为可生长的三元组 ledger。

方法核心：环评通常不披露分环节良率，用物料平衡（关键投入如衬底 vs 芯片产出）反算端到端良率区间，并逐工序定位瓶颈——完整演示见 `examples/format-demo-ir-detector.md`（虚构案例）。

## 设计原则（优先级高于一切具体步骤）

1. **查询先行**：所有提取与推断只为"必须回答的 7 个问题"服务。新增实体/关系/字段前，必须有至少一条真实失败查询作依据（见 references/ledger-schema.md）。
2. **环评数字不是事实**：环评是企业在监管博弈下的申报口径。数字入 ledger 前必须过两道关——利益审查（影响审批分级/总量指标/监测频次/防护距离中的哪项、往哪个方向虚）与物理交叉验证（低风险字段反算高风险字段）。
3. **口径纪律**：每条事实带 source（文件名+页码+原文摘录）与披露日期；【披露】与【推断】严格分离；反算输出永远是带口径的区间，不是点值。
4. **一套词表**：工序→设备映射库即本体词汇层（设备类别别名归一），映射库与 ledger 共用同一份设备类别词表，一个资产不分两处。

## 必须回答的 7 个问题

| # | 问题 | 主要依据 |
|---|------|---------|
| 1 | 实际产能与建设节奏（对照融资口径） | 产品方案、建设分期、批复信息 |
| 2 | 工艺路线判定 | 工序序列 + 物料 + 污染物三面证据 |
| 3 | 设备选型档次（国别/世代/密度） | 设备清单、型号、数量与产能配比 |
| 4 | 良率与单耗倒推，定位瓶颈工序 | 物料平衡 |
| 5 | 污染特征反推工艺存在性 | 危化品/危废/特气清单 |
| 6 | 环评口径 vs 公司口径冲突证伪 | 全部字段 vs BP/访谈/公告 |
| 7 | 数字可信度分级与反算 | references/field-credibility.md |

## 工作流

### Phase 0 获取文件（用户未提供时）

按序检索（沉淀自实践，欢迎补行）：
1. 全国建设项目环境影响评价信息公示平台；目标公司注册地/项目地的省、市、县三级生态环境局官网"环评受理/拟批准/审批决定"栏目
2. 全国排污许可证管理信息平台（许可证正本 + 年度执行报告）
3. 尚云环评云助手、环评爱好者论坛等存量文库（补历史版本）

检索式：公司全称、`项目名 环评报告表`、`项目名 环境影响报告书 受理` + 地市名。同一项目常有受理公示/拟批准公示/审批决定三个版本，受理版最全；报告表（短）与报告书（全）内容差异大，都拿。

### Phase 1 结构化提取

从 PDF 逐节提取为事实表（字段清单与博弈分级见 references/field-credibility.md）：

- 项目概况与批复信息：批复文号、审批时间、审批层级、环评编制单位、建设性质（新建/扩建/技改）
- 产品方案与产能：分产品、分规格、分建设期
- 工艺流程：逐工序转写，含产污环节标注；流程图逐节点转文字，注明"自流程图转录"
- 设备清单：名称/型号/数量/来源（自购/租赁/利旧）
- 原辅材料与危化品：名称/年用量/危化特性
- 物料平衡与水平衡：逐工序投入产出
- 污染源与治理设施：产污环节→污染物→治理措施→排放去向
- 建设期与投资额：分期节奏、总投资与环保投资

每行事实带 source。扫描件先 OCR；表格数据优先从表格原文转录，避免转述失真。

### Phase 2 博弈审查

加载 references/field-credibility.md：给每个数字字段标 `game_risk`（高/中高/中/中低/低）与失真方向（虚增/虚减/拆分）。对高风险字段过利益审查三问：影响哪项监管后果？哪个方向有利？有无压线特征？

发现的博弈痕迹（批小建大、化整为零、隐匿工序、试产名义量产等）单独成清单，并按 ledger 关系 `博弈痕迹` 落账——它同时是治理尽调证据。

### Phase 3 交叉验证

加载 references/cross-validation.md：用低风险信任锚（设备数量、厂房/排放口等物理信息）反算高风险字段（产能/物料/排放）；外部材料按可得性使用：排污许可执行报告、危废转移联单、环保处罚记录、招股书在建工程、招投标与海关数据。

每个字段标 `status`：`申报值` / `已交叉验证` / `与外部冲突`。冲突不改数字，冲突本身写进报告。

### Phase 4 推断

- **工艺路线**：工序序列、物料投入、污染物特征三面证据交叉定路线（例：T2SL vs VOx、单片式 vs 两片式封装、干法 vs 湿法），注明各证据面。
- **设备选型**：加载 references/mappings/<赛道>.md，按"工序→设备类别→档次信号→国别/代表厂商"推断。映射库没有的工序标【映射缺失】记入 backlog，禁止临场编造。
- **良率/单耗**：物料平衡反算端到端良率与瓶颈工序，输出区间 + 口径脚注（"环评口径自洽下的推算值"）。
- **CAPEX 强度**：设备数量×市场价格区间（外部报价佐证）→ 单位产能投资强度，对照融资额与产能承诺。

推断一律标【推断】，推理链写明：哪几条事实 → 什么规则 → 什么结论。

### Phase 5 产出报告

固定五段结构（Markdown）：
1. 结构化事实表（含 source / game_risk / status）
2. 环评口径 vs 公司口径对照表
3. 博弈痕迹清单
4. 推断摘要（工艺路线 / 设备选型 / 良率区间 / CAPEX 强度）
5. 访谈提问清单——环评里缺失、含糊、冲突的点逐条转为 DD 问题

### Phase 6 ledger 落账

按 references/ledger-schema.md 追加三元组。要点：
- 追加式 JSONL，一赛道一文件，存放在尽调项目工作区 `{项目目录}/eia-ledger/<赛道>.jsonl`；本 skill 目录不存业务数据
- 每条必带 source / game_risk / status / 披露日期 / 落账日期
- 本体答不了的问题记入同目录 `failed-queries.md`，等真实失败查询积累后再动 schema

## 映射库维护（references/mappings/）

- 一赛道一文件，行结构：环评信号（工序/污染物/危化品关键词）→ 设备类别（词表）→ 档次信号 → 国别代表厂商 → 判读依据
- 每次尽调结束补行；无据不写；不确定的标【待验证】并写明验证路径
- 设备类别名称变更 = 词表变更，须同步 references/ledger-schema.md 的词表节
