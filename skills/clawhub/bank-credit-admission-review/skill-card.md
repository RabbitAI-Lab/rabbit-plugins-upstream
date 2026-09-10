## Description:

为银行授信审批和风险管理人员提供企业授信准入初审、红线快筛、四维风险分析、同业基准对比、流贷需求测算和结构化报告输出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriskinhaha](https://clawhub.ai/user/chriskinhaha)

### License/Terms of Use:

MIT-0

## Use Case:

Bank credit review, approval, and risk-management teams use this skill to triage enterprise credit-admission requests, screen hard negative criteria, compare borrowers with industry benchmarks, and produce a traceable preliminary review report. It is an advisory aid and does not replace formal credit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports high-impact lending judgments and may influence credit-admission decisions.

Mitigation: Use it only as an advisory aid in a controlled banking or credit-review workspace, with qualified human review before any lending action.

Risk: The workflow can rely on external data connectors and public-source fallbacks for financial, corporate, judicial, and market data.

Mitigation: Confirm connector approval for the customer data involved, label source reliability, cross-check material figures, and treat missing or stale data as a review gap.

Risk: The artifact includes rule-library and benchmark-database update behavior that can persist new rules or data.

Mitigation: Require user approval before persistent rule or database updates and keep update records reviewable.

Risk: Some soft-risk factors may touch sensitive family, social reputation, social-circle, or regional-culture attributes.

Mitigation: Do not use those factors as decision variables unless the applicable compliance policy explicitly permits and audits them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chriskinhaha/skills/bank-credit-admission-review)
- [「一般负面情况」认定标准细则](references/negative_criteria.md)
- [四维分析框架明细](references/analysis_framework.md)
- [多源信息检索 · 数据分析 · 结果审核（增强层）](references/data_retrieval_augmentation.md)
- [行业基准库（同行业上市公司平均水平 —— 尺度判断）](references/industry_benchmark.md)
- [流动资金贷款需求测算 与 刚性负债情况分析 — 方法论](references/loan_demand_analysis.md)
- [准入标准建议与风控要点建议 — 写法框架](references/admission_standards_control.md)
- [风险评级矩阵与评分卡](references/risk_rating.md)
- [信息来源可靠性分级与缺口标注规范](references/source_reliability.md)
- [授信准入初审报告 — 模板](references/report_template.md)
- [「一般负面情况」快筛报告模板](references/screening_report_template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown reports with tables, optional JSON from deterministic scripts, and shell commands for local calculations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory credit-review materials that require human review before use in lending decisions.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
