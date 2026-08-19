## Description:

Helps agents answer drug-related questions by searching and summarizing PatSnap life-science data, patents, literature, clinical trials, and licensing transaction documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and pharmaceutical analysts use this skill to investigate drugs, targets, indications, clinical trials, patents, literature, safety, competitive landscapes, and licensing deals through PatSnap life-science services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drug, disease, target, trial, patent, and deal queries may be sent to PatSnap MCP services.

Mitigation: Install only when PatSnap life-science services are intended for the workflow, and avoid submitting information that should not be shared with those services.

Risk: The setup flow uses a PatSnap API key for MCP server access.

Mitigation: Protect the API key like any other secret, avoid committing it to files or logs, and rotate it if exposure is suspected.

Risk: Pharmaceutical research answers can be incomplete or misleading if based on summaries or insufficient retrieval.

Mitigation: Follow the skill's search-then-fetch pattern, review cited source IDs and records, and have qualified personnel review outputs before using them for clinical, regulatory, or commercial decisions.

## Reference(s):

- [Pharmaceuticals Exploration Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/pharmaceuticals-exploration)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)
- [Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses numbered report sections, an abstract with core conclusions, citation summaries, and a mandatory conclusion section.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
