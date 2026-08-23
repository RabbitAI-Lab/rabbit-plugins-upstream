## Description:

基于公开企业信息渠道，为指定中国企业生成结构化 HTML 尽职调查报告，涵盖工商登记、股权结构、实际控制人、司法与经营风险、关联企业和综合评价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[spzhangsanfeng](https://clawhub.ai/user/spzhangsanfeng)

### License/Terms of Use:

MIT-0

## Use Case:

Business, legal, compliance, and investment users can use this skill to assemble a public-record due diligence report for a China-registered enterprise. The report is intended to organize source-backed facts, risk indicators, ownership information, and recommendations for human review.

### Deployment Geography for Use:

Global, for due diligence on China-registered enterprises and Chinese public-record sources.

## Known Risks and Mitigations:

Risk: The skill can compile detailed company and related-person risk profiles from public records.

Mitigation: Confirm the target company, avoid unnecessary related-person profiling, and check source terms plus legal and privacy obligations before generating or sharing a report.

Risk: The generated HTML report may contain sensitive business due-diligence conclusions.

Mitigation: Treat the report as a sensitive business document and review it before distribution.

## Reference(s):

- [Enterprise report data-source checklist](references/data-sources.md)
- [HTML report template](assets/report-template.html)
- [ClawHub skill page](https://clawhub.ai/spzhangsanfeng/skills/enterprise-report)

## Skill Output:

**Output Type(s):** [text, code, guidance]

**Output Format:** [Structured HTML report with narrative analysis, source notes, tables, and risk scoring]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the bundled HTML template and public-source checklist; generated reports should be reviewed before sharing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
