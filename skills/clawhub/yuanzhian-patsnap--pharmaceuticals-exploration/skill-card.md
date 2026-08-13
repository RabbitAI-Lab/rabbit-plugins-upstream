## Description:

This skill helps agents answer drug-related questions by retrieving and summarizing patents, literature, database records, clinical trials, drug deals, and related life-science data through PatSnap MCP services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and life-science analysts use this skill to investigate specific drugs, targets, indications, clinical evidence, patent and literature records, safety signals, competitive landscapes, and licensing activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drug names, disease terms, targets, and related research questions may be sent to PatSnap MCP services and, when needed, web search providers.

Mitigation: Use the skill only for information your organization permits sharing with those services, and avoid confidential pipeline, unpublished research, or proprietary deal information unless approved.

Risk: The PatSnap API key used for MCP access could expose paid or sensitive service access if mishandled.

Mitigation: Protect API keys in MCP configuration and avoid placing real keys in shared prompts, reports, logs, or examples.

Risk: Pharmaceutical research summaries can be misleading if based only on search snippets or incomplete records.

Mitigation: Follow the skill's search-then-fetch pattern, cite supporting records in the report, and use web search only after MCP database retrieval is complete or when current information is explicitly needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/pharmaceuticals-exploration)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [Pharma Intelligence MCP server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Chemical Molecular MCP server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [Biology Modality MCP server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with numbered sections, citation summaries, tables when deals are available, and inline shell commands for MCP setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured PatSnap LifeScience MCP services; fallback web search is limited to cases where database retrieval is insufficient or current information is requested.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
