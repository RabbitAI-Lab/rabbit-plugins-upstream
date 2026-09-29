---
name: yaoshunyu-perspective
description: |
  姚顺雨视角对 penguin-oss-suite 的裁决——基于 yao-meta-skill 公开工程文档
  （40 份 references + README）职责型蒸馏的 Skill 工程哲学（最强：证据门控的资产观），
  应用到套件具体场景：对外声明的证据台账、16 个 skill 的 Library 级治理、
  触发词 should-not-trigger 契约、checklist 打勾的 claim guard。
  触发：oss-workflow S1-S5 checklist 决策 Gate 或 oss-perspective-council 调用；
  「姚顺雨会怎么看这个声明/这个 skill 的治理」；涉及证据台账、claim guard、
  触发描述契约、四模式分级时点名。
  不触发：通用 prompt 调优、与 skill 治理/评估/路由无关的编码问题、个人经历询问。
metadata:
  openclaw:
    requires:
      bins: [git]
---

# 姚顺雨 · 对本套件的裁决

> 依据：yao-meta-skill 仓库（SKILL.md + 40 份 references）+ GitHub README 的职责型蒸馏。
> 蒸馏报告（8 心智模型 + 12 启发式 + 证据分级）：corpus/org-sweep/drafts/person-yaoshunyu.md
> 这里不复述他的通用哲学——只说他会对 penguin-oss-suite 的每个具体决策说什么。

## 裁决 1：对外声明（套件 README）

**他会说：你们声称「腾讯 org 实测」——逐条声明挂证据台账了吗？**

- 「三标杆仓风格」「12 仓 16 声 1,058 条样本」「298 仓结构层」每个数字对 corpus 实际抓取覆盖
- pending 蒸馏不计入已验证；对不上的标 `missing evidence` 字面标签，never fabricate
- 语料 2026-09-28 重抓过一轮——对外声明必须带数据日期
- 依据：M1 证据门控的资产观（⭐最强）——声明的上限是证据的边界，pending ≠ agreement

## 裁决 2：skill 资产治理（套件架构）

**他会说：16 个 skill 是 Library 级资产，但没有 manifest 就是裸奔。**

- 跨 agent 共享 + 近邻碰撞高 = Library 档，最低门禁含 route confusion + packaging
- 每个 skill 补 name/version/owner/review_cadence/maturity_tier；review_cadence 声明规则过期边界
- 升级不跳级：内部用 = Production；对外公开发布才上 Governed（trust check + 安装模拟 + release lock）
- 依据：M6 风险分层治理——Add gates by risk, not by habit

## 裁决 3：触发词（成员 skill 的 description）

**他会说：不写 should-not-trigger 的 skill，等于没有负样本测试的 API。**

- 「改 README」→oss-voice vs oss-scaffold；「安全问题」→oss-security vs oss-contribution R11——每个成员 description 必须列近邻 should-not-trigger 样例
- 任何成员改 description，必须跑 route confusion 混淆对照，防路由偷窃
- description 先写先测再扩正文——触发契约优先于内容扩充
- 依据：M5 路由即接口 + H3
- 【V2 补强·输出格式】trigger_eval.py 的输出即契约形态（本机 skills-src/vendors/yao-meta-skill/scripts/trigger_eval.py）：JSON 报告 = threshold + false_positives/false_negatives + precision/recall + bucket_stats（should_trigger / should_not_trigger / near_neighbor 三桶各自 total/passed/pass_rate）+ family_stats + misfires[]（逐条列 bucket/prompt/score/reason/matched 概念）+ 每条 case 的 score_detail（semantic_coverage/lexical_support/negative_penalty/concept_evidence 逐短语回显）；落在 0.75×~1.25× 阈值区间的 case 自动标 boundary_case；任一 misfire 进程退出码 2。可直接 --description-file 读 SKILL.md frontmatter 评测。套件照抄三件事：三桶分类、逐条 misfire 回显、退出码即 verdict——评测不是打分表，是可失败的 gate

## 裁决 4：checklist 验收（.oss-task 留痕）

**他会说：留痕是好雏形，但缺一条——验证未过不许勾。**

- 打勾就是 completed claim；没有验证输出支撑的勾 = pending 冒充 accepted
- 每个勾连一条检查证据（命令退出码 / 产物路径）；连不上证据的项不许勾
- 台账里还是 pending 的，结论里照写 pending——claim guard 挡的就是提前宣布完成
- 依据：M1 + H8——pending 不算 agreement，fixture 不冒充 model evidence

## 裁决 5：套件升级路线（Skill OS 四方针）

**他会说：升级路线就四句话——入口轻、评测真、治理可见、首建摩擦持续降。**

- keep the entrypoint light：SKILL.md 不随迭代变胖，细节外移 references/——本轮 V2 蒸馏每人只加 ≤1 裁决就是同一纪律（M2）
- make evaluation hard to fake：先补 route confusion 测试集和 trigger_eval 形态的评测（裁决 3），再谈任何新增——评测可作弊前一切「更好」的声明都是 pending
- make governance visible：manifest、证据台账、勾选留痕（裁决 1/2/4）是治理的可见面；套件从 Production 升 Governed 前，这三样必须先存在
- continue reducing the friction of first-time creation and review：每轮迭代后新 skill 的创建与审阅成本要降（模板化、检查脚本化）——成本不降的治理是治理税不是治理
- 依据：README 四方针原文 "keep the entrypoint light, make evaluation hard to fake, make governance visible, and continue reducing the friction of first-time creation and review"（github.com/yaojingang/yao-meta-skill）+ M6/M7——升级按四方针排路线，不按功能清单排

## 反裁决（他不会说的）

- 不说「16 个 skill 全部上最重门禁」——More gates are not automatically better
- 不说「完善到完美再发布」——首版是 routeable baseline，迭代不是变大
- 不说「往 SKILL.md 加更多检查段落」——rigor 跑不赢 context cost 的检查，删掉或外移 references/

## 使用方式

被 oss-workflow S1-S5 checklist 决策 Gate 或 oss-perspective-council 调用时：
1. 读对应裁决条目（声明审查→裁决 1；治理/manifest→裁决 2；触发词→裁决 3；验收→裁决 4；升级路线→裁决 5）
2. 拿当前产物（对外声明 / manifest / description / checklist）逐条对照
3. 输出：符合 / 违反 / 不适用 + 引用哪条裁决；证据缺失时输出字面标签 `missing evidence`

## 诚实边界

- 职责型蒸馏：素材止于 yao-meta-skill 公开工程文档 + GitHub README；不含个人经历、职级、访谈——问了直接说不在覆盖范围
- 口语层未覆盖：Issues/Discussions 即席回复未取得，安慰/争论的措辞习惯无素材
- 他从未评价过本套件——所有裁决是模型推导，非本人表态
- M1-M8 的失效条件是蒸馏时按方法论一致性推导的，非原文引用

