## Description:

Provides target intelligence reports covering target details, drugs, pipelines, druggability, and indications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External life-science researchers, drug intelligence analysts, and developers use this skill to generate target intelligence reports from PatSnap LifeScience MCP services. It supports questions about target biology, drug pipelines, clinical progress, patents, druggability, indications, and competitive landscapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to PatSnap MCP services using a PatSnap API key.

Mitigation: Avoid exposing real API keys in shared terminals, logs, screenshots, or recordings, and rotate the key if exposure is suspected.

Risk: The setup process adds MCP service configuration to the agent environment.

Mitigation: Review the added MCP configuration before use and remove it when the PatSnap integration is no longer needed.

## Reference(s):

- [Target Intelligence on ClawHub](https://clawhub.ai/yuanzhian-patsnap/skills/target-intelligence)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with setup guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires connected PatSnap LifeScience MCP services before answering user queries.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
