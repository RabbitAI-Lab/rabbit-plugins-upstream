## Description:

面向银行风险条线的授信准入审查能力，支持一般负面情况红线快筛、完整准入初审、流动资金贷款需求测算、刚性负债分析和行业基准比对。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriskinhaha](https://clawhub.ai/user/chriskinhaha)

### License/Terms of Use:

MIT-0

## Use Case:

Bank credit officers, risk managers, and approval support teams use this skill to prepare evidence-traced admission screening and preliminary credit review reports for enterprise borrowers. It helps identify hard-stop negative criteria, quantify working-capital loan need, assess rigid debt pressure, compare peers, and list follow-up due diligence conditions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: External Neodata or WebSearch lookups may expose nonpublic customer files, borrower identifiers, or deal context.

Mitigation: Require explicit approval before external lookups, redact confidential inputs where possible, and prefer approved internal or customer-provided sources for sensitive credit matters.

Risk: Case logs, accumulated rules, and the local benchmark database can persist sensitive or case-derived information across future reviews.

Mitigation: Treat the skill directory as sensitive, review persisted files before sharing or reinstalling the skill, and remove confidential case data according to bank data-retention policy.

Risk: The skill can produce credit-risk guidance that may be incomplete or misleading if source data is missing, stale, or inconsistent.

Mitigation: Use the report as review support only, require human credit-approval review, preserve source labels and data-gap notes, and verify key financial metrics against authoritative documents.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chriskinhaha/skills/bank-credit-admission-review)
- [一般负面情况认定标准细则](references/negative_criteria.md)
- [授信准入初审报告模板](references/report_template.md)
- [一般负面情况快筛报告模板](references/screening_report_template.md)
- [四维分析框架明细](references/analysis_framework.md)
- [多源信息检索、数据分析与结果审核](references/data_retrieval_augmentation.md)
- [信息来源可靠性分级与缺口标注规范](references/source_reliability.md)
- [风险评级矩阵与评分卡](references/risk_rating.md)
- [准入标准建议与风控要点建议](references/admission_standards_control.md)
- [流动资金贷款需求测算与刚性负债情况分析](references/loan_demand_analysis.md)
- [行业基准库](references/industry_benchmark.md)
- [规则库和检查清单沉淀](references/rules_library.md)
- [案例与口径争议沉淀库](references/case_log.md)
- [财数数金融数据检索](https://www.codebuddy.cn/v2/tool/financedata)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with optional JSON outputs and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese banking review prose; source-labeled findings; deterministic helper-script outputs for red-line screening, working-capital loan sizing, rigid debt analysis, and industry benchmark comparison.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
