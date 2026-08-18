## Description:

Supports Chinese disease research reports by combining academic literature, epidemiology, clinical guidance, drug intelligence, clinical trials, patents, and commercial dynamics with PatSnap Life Science MCP data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life science, pharmaceutical R&D, and business development users use this skill to investigate disease mechanisms, epidemiology, standards of care, clinical pipelines, patents, and market opportunities. It is oriented toward Chinese-language disease investigation workflows that depend on PatSnap Life Science MCP data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disease research queries and related context are sent through the PatSnap MCP service.

Mitigation: Use the skill only when PatSnap is an approved service for the data being queried, and avoid sending confidential or regulated information unless that use is authorized.

Risk: The setup flow uses an API key in an MCP configuration command.

Mitigation: Store and rotate the API key according to local secret-handling policy, and avoid committing or sharing commands that contain live credentials.

Risk: The skill depends on PatSnap MCP availability and performs a connectivity check before answering.

Mitigation: Confirm the required MCP service is connected before use, and stop troubleshooting repeated tool failures until credentials and connectivity are verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/disease-investigation-zhcn)
- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with structured sections and concise setup guidance that may include shell command blocks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured PatSnap Pharma Intelligence MCP service; web search is used only after MCP database retrieval is insufficient or when recency is required.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
