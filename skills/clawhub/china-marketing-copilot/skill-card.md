## Description: <br>
把中国3C新品营销从“想创意”推进到“能执行、早避雷、能复盘”的策略技能包。适用于手机、电脑、耳机、穿戴和智能家居；用于上市打法、信息屋、传播创意、社媒文案、KOL渠道、竞品洞察、评论区压力测试、负面预警、上线判断和战情复盘。个人购买选型、维修排障和通用新闻摘要不触发。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killsnake01](https://clawhub.ai/user/killsnake01) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External marketing, product, social content, KOL, and startup teams use this skill to plan China-market 3C product launches, review messaging, generate campaign and channel guidance, analyze competitor pressure, and detect early negative signals. It supports marketing decisions with evidence labels and templates, but does not replace legal, advertising compliance, or product safety review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad routing and implicit invocation can pull unrelated requests into the marketing workflow. <br>
Mitigation: Confirm the user is asking for China-market 3C marketing work before applying the skill, especially for purchase advice, repairs, or general news summaries. <br>
Risk: Data-import workflows may process comments, reviews, specifications, or other user-provided files that include private or scraped platform content. <br>
Mitigation: Confirm which files will be processed and avoid using private customer data or scraped platform content unless the user has the right to use it. <br>
Risk: Price, ranking, share, new-product specifications, platform heat, and recent KOL reputation are high-volatility fields. <br>
Mitigation: Use current external verification when available, or label those claims as [待验证] before relying on them for formal launch or channel decisions. <br>
Risk: Launch-readiness recommendations can be mistaken for formal compliance or product safety approval. <br>
Mitigation: Keep final legal, advertising compliance, and product safety decisions with the responsible human reviewers. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/killsnake01/skills/china-marketing-copilot) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Agent Router](artifact/docs/agent-router.md) <br>
- [Data Index and Freshness Rules](artifact/docs/data-index.md) <br>
- [Runtime Capabilities](artifact/docs/runtime-capabilities.json) <br>
- [Evidence Freshness Gate](artifact/docs/templates/evidence-freshness-gate.md) <br>
- [Execution Readiness Gate](artifact/docs/templates/execution-readiness-gate.md) <br>
- [Negative Early Warning Library](artifact/docs/ecosystem/negative-early-warning.md) <br>
- [Output Quality Rubric](artifact/docs/evals/output-quality-rubric.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese-language Markdown with structured tables, evidence labels, optional JSON schemas, and optional Python command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Marks unverified timely claims as [待验证] and inferred claims as [推测] when evidence is incomplete.] <br>

## Skill Version(s): <br>
1.4.31 (source: server release metadata and artifact/VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
