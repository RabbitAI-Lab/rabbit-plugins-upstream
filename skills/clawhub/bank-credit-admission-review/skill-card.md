## Description:

为银行授信审批和风险管理人员提供企业客户授信准入初审、一般负面情况红线快筛、四维信用风险分析、同业基准比对和结构化报告生成支持。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chriskinhaha](https://clawhub.ai/user/chriskinhaha)

### License/Terms of Use:

MIT-0

## Use Case:

Bank credit approval, underwriting, and risk management reviewers use this skill to screen enterprise borrowers against defined red-line criteria and draft evidence-traceable admission review reports. It supports quick negative-list screening and fuller credit admission analysis with risk ratings, data-gap labeling, benchmark comparison, and follow-up due-diligence requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Borrower identifiers, credit reports, internal underwriting notes, or non-public documents may be exposed when external search or data services are used.

Mitigation: Use the skill only under an approved data-handling policy, and do not send non-public borrower information to Neodata, WebSearch, or other external services unless that policy allows it.

Risk: Benchmark database updates and rule or case-log persistence can retain customer-derived facts or internal credit judgments.

Mitigation: Require explicit user confirmation before updating the benchmark database or appending to persistent rule, checklist, or case-log files.

Risk: Credit review outputs may be incomplete, stale, or misleading if source data is missing or inconsistent.

Mitigation: Treat generated reports as decision support only; require a qualified human reviewer to validate sources, resolve data gaps, and make the formal credit approval decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chriskinhaha/skills/bank-credit-admission-review)
- [Negative criteria](references/negative_criteria.md)
- [Data mapping](references/data_mapping.md)
- [Analysis framework](references/analysis_framework.md)
- [Data retrieval augmentation](references/data_retrieval_augmentation.md)
- [Industry benchmark](references/industry_benchmark.md)
- [Loan demand analysis](references/loan_demand_analysis.md)
- [Admission standards control](references/admission_standards_control.md)
- [Risk rating](references/risk_rating.md)
- [Source reliability](references/source_reliability.md)
- [Screening report template](references/screening_report_template.md)
- [Admission review report template](references/report_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown reports with tables, plus optional JSON or Markdown outputs from bundled calculation scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports a quick screening report and a fuller admission review report; outputs are advisory and require human credit approval review.]

## Skill Version(s):

1.4.0 (source: server release evidence, created 2026-09-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
