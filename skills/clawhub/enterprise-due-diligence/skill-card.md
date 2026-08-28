## Description:

企业尽调-分析生成 helps an agent research a target company across legal, financial, and business dimensions, combine public data with user-provided documents, and generate structured due-diligence reports and checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[merlinbeard000](https://clawhub.ai/user/merlinbeard000)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, investors, and business teams use this skill to perform company background research, investment due diligence, merger and acquisition screening, supplier checks, and IPO pre-assessment. It supports a lightweight public-information screen and a fuller due-diligence workflow that benefits from user-provided financial reports, contracts, screenshots, and other source documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can involve confidential company materials, financial records, contracts, screenshots, and other sensitive inputs.

Mitigation: Provide only documents needed for the due-diligence task, redact irrelevant personal or confidential details, and keep generated reports local unless sharing is explicitly required.

Risk: External data connectors and API tokens may expose account or query access if enabled without review.

Mitigation: Confirm Qichacha, Tianyancha, Qixin, or other API tokens and MCP connector settings before enabling them, and use least-privilege credentials where available.

Risk: Due-diligence outputs may affect commercial decisions and can contain incomplete or unverified public-source findings.

Mitigation: Treat the report as research support rather than investment advice, preserve source notes and timestamps, and verify high-risk or marked fields against official records and first-party documents.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/merlinbeard000/skills/enterprise-due-diligence)
- [Checklist Template](references/checklist_template.md)
- [Data Quality Rules](references/data_quality.md)
- [MCP Connectors](references/mcp_connectors.md)
- [Report Template](references/report_template.md)
- [Risk Classification](references/risk_classification.md)
- [Qichacha Open API](https://open.api.qichacha.com)
- [Tianyancha MCP Endpoint](https://mcp.tianyancha.com/v1)
- [Qixin MCP Endpoint](https://mcp.qixin.com/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown instructions, JSON company data, and local .docx Word reports and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports lightweight and standard report templates; generated reports include source tracking, verification labels, and P0/P1/P2 risk classification.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
