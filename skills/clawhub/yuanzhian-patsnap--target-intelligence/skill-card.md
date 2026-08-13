## Description:

Provides target intelligence reports covering target details, drugs, pipelines, druggability, and indications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External life-science analysts and drug-development teams use this skill to produce target intelligence reports covering target biology, drug pipelines, clinical progress, patents, and competitive landscape from configured PatSnap LifeScience MCP services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target names and related biomedical research queries may be sent to PatSnap through the configured API key.

Mitigation: Use this skill only for intended PatSnap LifeScience MCP workflows and avoid submitting sensitive research queries unless PatSnap use is approved for that data.

Risk: The required PatSnap MCP configuration remains in Claude until removed.

Mitigation: Remove the configured MCP services when PatSnap access is no longer needed.

Risk: Reports depend on configured PatSnap LifeScience MCP services being connected and authorized.

Mitigation: Verify MCP connectivity before relying on the skill output, and resolve authentication or service errors before running target research.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/target-intelligence)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with setup commands and configuration guidance when PatSnap MCP services are not connected]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured PatSnap LifeScience MCP services and a PatSnap API key for data retrieval.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
