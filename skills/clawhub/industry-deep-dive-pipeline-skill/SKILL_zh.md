---
name: industry-deep-dive-pipeline
description: 将单篇科技、AI、数据、云和企业软件产业选题推进到审核通过的正式 Markdown。采用 Prompt Chaining + Evaluator-Optimizer：固定主链保证可追踪，八角色会审后的修订循环保证质量。
description_zh: 产业深度文章全流程编排
description_en: Industry deep-dive pipeline
version: 1.0.0
disable: false
agent_created: true
---

# 产业深度文章全流程编排（Industry Deep-Dive Pipeline）

将单篇科技、AI、数据、云和企业软件产业选题推进到审核通过的正式 Markdown。采用 Prompt Chaining + Evaluator-Optimizer：固定主链保证可追踪，八角色会审后的修订循环保证质量。

## 何时使用

- 输入包含选题简报、事件、厂商案例、政策变化或研究材料，需要形成有判断、有证据、有边界的深度文章。
- 需要先查中文与英文同类内容，确认信息增量和表述撞车风险。
- 需要在正文前完成目标读者、核心判断、论证链、反方、结构、标题和风险策划。
- 需要事实表、原创性复核、会审记录和终稿复检形成完整证据包。

## 不适用

- 新闻快讯、摘要、产品说明书、技术教程或营销稿。
- 厂商大会全景报告；改用 `vendor-summit-report`。
- LinkedIn 单平台短观察；改用 `linkedin-industry-observation`。
- 微信排版、封面、摘要、关键词、社交物料、CMS/Notion 入库或发布；交给独立发布套件。
- 多篇系列的自动排期与批量生成。系列信息仅作单篇上下文。

## 必备输入

读取 `references/planning-schema.md`，建立 case bundle。至少确认：`topic`、`source_materials`、`target_reader`、`target_format`、`length_range`、`writing_profile`。可选：合集或系列关系、历史平台信号、必须处理的反方、本篇新增红线、时效窗口和用户已有假设。

## 工作流

### 步骤 1：[确定性] 输入诊断

1. 校验路径、URL、日期、目标格式和 writing profile。
2. 判断文章类型、时效等级、事实风险与敏感性。
3. 把用户已有判断标为待验证假设，不直接当成结论。
4. 复制 `templates/case-brief.template.md` 为 `00-case-brief.md`。
5. 运行 `python scripts/validate_case_bundle.py --case-dir <case-dir> --stage input --enforce`。输入门禁失败时停止，报告缺项。

### 步骤 2：[LLM] 事实表

1. 从材料提取数字、日期、公司、政策、产品状态、引述和因果声明。
2. 使用搜索发现来源，回到官网、财报、论文、监管原文或官方发布核验关键事实。
3. 高风险事实至少双源确认，或由一手权威源确认。
4. 记录原始日期、核验日期、状态、来源等级、可使用措辞和失效条件。
5. 复制 `templates/fact-table.template.md` 为 `01-fact-table.md`。
6. 按需读取 `references/evidence-and-originality.md`。

### 步骤 3：[LLM] 原创性与竞争复核

1. 拆出核心判断、分析框架和标志性表达。
2. 搜索中英文新闻覆盖、同主题分析和高度相似论证。
3. 区分公共观点、独立深化、可验证差异和表述撞车。
4. 主动查找直接反方、历史反例和证伪变量。
5. 输出 `02-originality-review.md`。以下情况停止：核心判断已被充分覆盖且无信息增量；论点依赖无法核实的事实；选题只能依靠夸大标题成立。

### 步骤 4：[LLM] 完整策划简报

1. 复制 `templates/planning-brief.template.md` 为 `03-planning-brief.md`。
2. 完成选题可行性、竞争程度、读者分层、核心判断、论证链、原创锚点、反方、标题、结构、收藏载体、风险和系列关系。
3. 只保留真正需要人做价值判断的待确认项。

### 门禁 A：[人工] 确认策划

暂停并确认：核心判断、标题方向、篇幅与取舍、争议处理、平台目标和系列关系。确认前禁止写正文。

### 步骤 5：[LLM] 起草

1. 只使用确认后的策划与事实表。
2. 判断先行，论据、反方和边界随后展开。
3. 禁止补入事实表中没有的新数字、日期、状态和强结论。
4. 禁止把任务背景、内部备注、发布信息和写作过程带入正文。
5. 输出 `04-draft.md`；只保留必要的图表占位。

### 步骤 6：[确定性] 机器门禁

运行 `python scripts/scan_draft_gates.py --draft <case-dir>/04-draft.md --facts <case-dir>/01-fact-table.md --profile <writing-profile.json> --output <case-dir>/05-machine-gate.json --enforce`。检查未登记数字、凭据、UUID、个人路径、元信息、对举句、营销词、口语缓冲和 profile 红线。失败时回到步骤 5 修订并重跑。

### 步骤 7：[LLM] 八角色会审

调用 `tech-content-review-panel`，复用 G1/G2、R1–R4、G3 和 T1。复制 `templates/review-record.template.md` 为 `06-review-record.md`，将意见分为必改、建议改、可选和张力项。

### 门禁 B：[人工] 解决真实张力

仅在出现传播与专业、深度与完读、风险与表达、系列一致与单篇独立等真实张力时暂停。事实错误、来源缺失、格式错误和明确红线由流程直接修正，不推给用户决定。

### 步骤 8：[LLM] 修订至定稿

1. 处理全部必改和建议改。
2. 按门禁 B 决策处理张力项。
3. 禁止接受会审中新出现且未经核验的事实。
4. 记录未采纳意见及理由，避免重复提出。
5. 输出 `07-final.md`。

### 步骤 9：[确定性 + LLM] 复检

1. 重核事实、时效和来源。
2. 对 `07-final.md` 重跑 `scan_draft_gates.py`。
3. 人工通读检查机器难以识别的 AI 腔、逻辑跳步和姿态越界。
4. 对照策划，确认判断、范围、标题和表格一致。
5. 输出 `08-final-check.md`。
6. 运行 `python scripts/validate_case_bundle.py --case-dir <case-dir> --stage final --enforce`。

### 步骤 10：[确定性] 打包交付

复制 `templates/final-package.template.md` 为交付说明。交付：`07-final.md`、事实表、原创性复核、确认后的策划、会审记录和终稿复检。

## 硬规则

1. 搜索用于发现，关键事实回到一手来源。
2. 用户假设必须经过验证，不因用户提出就视为事实。
3. 原创、首创、唯一等判断必须有检索证据和边界。
4. 门禁 A 未确认不得写正文。
5. 门禁 B 只处理真实价值张力，不把事实和格式问题交给用户。
6. 正文中的高风险数字、日期和状态必须出现在事实表。
7. 改稿后必须重跑机器门禁并人工通读。
8. 私有写作 profile 只按需读取，不复制进通用 Skill 或公开包。
9. 输出止于审核定稿和证据包；禁止生成或执行发布动作。
10. 任何工具失败执行重试与交叉验证；修复后必须重跑。

## 故障处理

| 场景 | 处理 |
|---|---|
| 输入材料缺失 | 停止，列缺项，不猜测内容 |
| 高风险事实无法确认 | 删除、降级或标记待核，禁止进入强判断 |
| 原创空间不足 | 停止写作，给出合并、换角度或放弃建议 |
| 门禁 A 未确认 | 保持任务进行中，不生成正文 |
| 机器门禁失败 | 修订对应问题并重跑，最多两轮后报告剩余阻塞 |
| 会审新增未经核验事实 | 拒绝纳入，回到事实表核验 |
| 门禁 B 未确认 | 保留张力项，暂停终稿修订 |
| 工具首次失败 | 同操作重试 1–2 次，再换工具交叉验证 |
| 最终验证失败 | 不标完成，不生成发布物料 |

## 输出格式

```
<case-dir>/
├── 00-case-brief.md
├── 01-fact-table.md
├── 02-originality-review.md
├── 03-planning-brief.md
├── 04-draft.md
├── 05-machine-gate.json
├── 06-review-record.md
├── 07-final.md
├── 08-final-check.md
└── FINAL-PACKAGE.md
```

## 参考

- `references/planning-schema.md`：输入、策划和 case bundle 字段。
- `references/evidence-and-originality.md`：来源分级、事实状态和原创性判断。
- `references/writing-profile-interface.md`：私有写作 profile 接口。
- `references/replay-evaluation.md`：Fireworks、Kimi 和欧洲 AI 回放标准。

## 易错点

- 公司案例写成公司介绍，产业判断退到次要位置。
- 原创性复核只搜同标题，遗漏同论证不同表述。
- 会审后改稿未复扫，重新引入红线和事实错误。
- 把摘要、关键词、标签、封面提示词或发布备注混入正文。
- 系列上下文变成跨篇自指，导致单篇无法独立成立。
- 为减少打断跳过门禁 A，最终围绕错误判断写完整篇文章。

## 核查清单

- [ ] 必填输入齐全，case bundle 通过 input 校验。
- [ ] 高风险事实可追溯率 100%。
- [ ] 原创性复核覆盖中英文同类内容、反方和证伪变量。
- [ ] 门禁 A 有明确确认记录。
- [ ] 初稿机器门禁通过后才进入会审。
- [ ] 门禁 B 只包含真实张力项。
- [ ] 终稿重跑机器扫描并完成人工通读。
- [ ] 凭据与私有标识 P0=0。
- [ ] 输出不包含发布物料或外部动作。
- [ ] case bundle 通过 final 校验。
