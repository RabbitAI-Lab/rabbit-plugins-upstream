## Description:

Generates enterprise carbon credit rating reports by extracting fields from customer materials, confirming industry parameters, calculating scores, and producing a formal Word report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise carbon-rating analysts use this skill to extract and confirm rating data from customer materials, identify blocking missing fields, calculate carbon credit scores, and generate a formal Word report with required disclosures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input materials and generated DOCX or JSON outputs may contain sensitive enterprise business records.

Mitigation: Install and use the skill only when local processing of enterprise carbon-rating materials is intended, and handle all inputs and generated outputs as sensitive records.

Risk: Incorrect or incomplete extracted fields can lead to misleading scores or a non-gradable result.

Mitigation: Review the extracted fields, missing-data table, industry parameters, and prior-score reuse before approving scoring or report generation.

Risk: Missing key rating fields can block scoring or trigger a no-rating outcome.

Mitigation: Require confirmation of enterprise identity fields and explicitly disclose uncollected or unresolved key fields rather than substituting zeroes, industry averages, or defaults.

## Reference(s):

- [Extraction Dictionary](references/extraction_dictionary.md)
- [Model Rules](references/model_rules.md)
- [Report Generation](references/report_generation.md)
- [Enterprise Carbon Credit Rating Report Template](assets/企业碳资信评级报告模板_v0.1.docx)
- [Enterprise Carbon Credit Scoring Rules Workbook](assets/企业碳资信评分规则配置表_v0.1.xlsx)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/enterprise-carbon-credit-rating)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown status summaries, JSON scoring inputs and results, shell commands, and generated DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces formal Word reports and optional intermediate JSON audit files after extracted fields and industry parameters are confirmed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
