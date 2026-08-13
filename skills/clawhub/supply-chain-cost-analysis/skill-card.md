## Description:

餐饮供应链成本分析报告生成。适用于供应商成本对比、成本卡数据分析、品类成本趋势追踪、异常检测与降本建议。触发词：成本分析、成本卡、供应商对比、供应商评估、成本对比、成本差异、降本分析、成本报告

This skill is ready for commercial/non-commercial use.

## Publisher:

[lwh111-qh](https://clawhub.ai/user/lwh111-qh)

### License/Terms of Use:

MIT-0

## Use Case:

External restaurant procurement and operations teams use this skill to turn supplier, cost card, category, logistics, and trend data into Chinese-language supply-chain cost analysis reports with variance breakdowns, anomaly flags, and cost-reduction recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic cost-analysis phrases may activate a specialized restaurant supply-chain reporting workflow.

Mitigation: Use the skill when the user intends restaurant procurement or supplier-cost analysis, and clarify scope when the request could mean a different domain.

Risk: Supplier or procurement recommendations can be misleading when source data lacks required fields, time periods, or consistent units.

Mitigation: Validate input fields, mark missing or anomalous data, state the analysis period, and avoid filling unsupported gaps.

## Reference(s):

- [餐饮供应链行业规则参考](references/domain-rules.md)
- [ClawHub skill page](https://clawhub.ai/lwh111-qh/skills/supply-chain-cost-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, analysis, guidance]

**Output Format:** [Markdown report with tables, findings, anomaly flags, and prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language output; analysis should cite time periods, currency units, standards used for anomaly flags, and risks for recommended cost-reduction actions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
