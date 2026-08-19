## Description:

Combines oncology literature, epidemiology, clinical guidance, pharmaceutical intelligence, and clinical trial information to generate precision oncology reports about cancer biology and treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life-science, pharmaceutical R&D, and business development users can use this skill to investigate cancer mechanisms, standards of care, clinical trial activity, epidemiology, unmet medical needs, and commercial viability for oncology indications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive biomedical or regulated queries may be sent to PatSnap MCP services or web search.

Mitigation: Use only organization-approved data flows and avoid entering patient-identifying, confidential, or regulated information unless that use is approved.

Risk: The skill requires API-key-based access to PatSnap LifeScience MCP services.

Mitigation: Configure credentials using approved secret-handling practices and confirm MCP connectivity before use.

## Reference(s):

- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/precision-oncology)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with setup guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires approved PatSnap LifeScience MCP service access for its primary retrieval workflow.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
