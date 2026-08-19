## Description:

Design and generate a configurable single-file enterprise patent-portfolio operations workspace with a dashboard, asset register, fee/deadline view, outside-counsel analytics, competitor monitoring, FTO workflow intake, patent-value screening, and novelty-search intake.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

In-house IP operations teams, patent portfolio managers, and R&D legal teams use this skill to create or refresh an authorized patent-portfolio workspace, including asset, fee/deadline, counsel, competitor, FTO, value-screening, and novelty-search views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized or confidential patent, invention, attorney work product, billing, credential, or personal data could be sent to an unapproved connector or service.

Mitigation: Confirm entity scope, confidentiality rules, approved data sources, and connector authorization before retrieving or using source data.

Risk: A generated static HTML workspace could be mistaken for a production system with secure persistence, notifications, payment handling, docketing writeback, or authenticated access.

Mitigation: Treat the HTML as a prototype or report unless a real approved backend is supplied, and keep backend-dependent actions disabled or clearly routed to approved workflows.

Risk: Patent status, fee/deadline, FTO, valuation, novelty, or competitor outputs could be interpreted as authoritative legal or operational conclusions without review.

Mitigation: Use official patent-office, docketing, authorized connector, and counsel-reviewed evidence, and preserve source, cutoff, limitation, and review metadata in the workspace.

## Reference(s):

- [Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Global Core Patent Database MCP server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with a self-contained HTML file specification and implementation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a portable HTML workspace prototype or report unless an approved backend is provided.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
