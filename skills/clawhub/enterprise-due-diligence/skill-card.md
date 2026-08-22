## Description:

Generates structured Word due diligence reports and checklists for enterprise legal, financial, and business review using public company data and user-provided documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[merlinbeard000](https://clawhub.ai/user/merlinbeard000)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external analysts, and deal teams use this skill to prepare pre-investment, M&A, partner, supplier, and IPO-readiness due diligence outputs. It helps collect public company information, integrate user-supplied documents, classify P0/P1/P2 risks, and generate structured report and checklist files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process confidential contracts, financials, personal data, or regulated business information supplied by the user.

Mitigation: Use only documents you are authorized to process, avoid unnecessary sensitive uploads, and confirm where the agent and model environment send or store inputs.

Risk: The skill may contact public company-data sources or configured external data connectors while gathering due diligence evidence.

Mitigation: Review the configured sources and API credentials before use, and disclose external-source use in reports where appropriate.

Risk: Broad trigger phrases could activate the skill in contexts where a full due diligence workflow was not intended.

Mitigation: Narrow trigger phrases or require explicit user confirmation before running data collection and report generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/merlinbeard000/skills/enterprise-due-diligence)
- [Report template](references/report_template.md)
- [Checklist template](references/checklist_template.md)
- [Risk classification](references/risk_classification.md)
- [Data quality guidance](references/data_quality.md)
- [MCP connectors](references/mcp_connectors.md)
- [Qichacha open API](https://open.api.qichacha.com)
- [Tianyancha MCP endpoint](https://mcp.tianyancha.com/v1)
- [Qixin MCP endpoint](https://mcp.qixin.com/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands plus generated JSON and Word .docx report and checklist files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports a default lightweight 5-chapter report template and a standard 7-chapter investment or M&A due diligence template.]

## Skill Version(s):

v1.0.0 (source: server release metadata and target metadata; frontmatter 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
