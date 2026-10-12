## Description:

根据目标企业和技术方向生成可追溯专利公开号的竞争格局分析，并支持导出 Word 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

企业研发、知识产权及战略团队可分析指定企业在特定技术方向的专利竞争格局、对手动向和潜在风险，获取带依据的摘要或 Word 报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target company, technical area and supplied background materials are sent to PatentMax.

Mitigation: Share only materials approved for external processing; remove confidential details before submission.

Risk: Trial credentials are retained locally, and shared environments may use an unintended account or endpoint.

Mitigation: Set PATENTMAX_API_KEY deliberately, review or clear ~/.patentmax as needed, and avoid untrusted PATENTMAX_BASE_URL settings.

Risk: Creating a report can incur charges.

Mitigation: Show the cost and obtain explicit user approval before starting a report.

Risk: Incomplete patent coverage or lower-quality reports can lead to overconfident conclusions.

Mitigation: Disclose search scope and quality limitations; seek professional advice for infringement or validity decisions.

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/ip930/skills/company-patent-analysis)
- [PatentMax API 平台](https://api.ip930.com/features/api-platform)
- [使用流程](references/workflow.md)
- [背景素材指南](references/materials-guide.md)
- [常见问题](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, DOCX document]

**Output Format:** [Markdown analysis and optional downloadable Word report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source scope, patent publication numbers and report quality status when available.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
