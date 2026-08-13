## Description:

Orchestrates an evidence-backed patent-landscape workflow for product planning, R&D strategy, competitor intelligence, technology-route analysis, patent packages, portfolio planning, and self-contained HTML reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and IP, R&D, product, and strategy teams use this skill to scope, search, analyze, tag, and report patent landscapes with traceable evidence and a genuine human tagging handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects PatSnap MCP connectors and may be unable to complete search, briefing, mining, or patent-database stages when those connectors are unavailable.

Mitigation: Confirm connector availability and live operation schemas before execution; mark affected modules unavailable rather than simulating results.

Risk: Patent landscape work can involve confidential project terms, local CSV, JSON, and HTML artifacts, and client-specific patent identifiers.

Mitigation: Confirm confidentiality constraints and the preferred project path before creating artifacts, and keep generated files in the agreed workspace.

Risk: Patent status, asset, transaction, and legal-event data are signals that can be mistaken for legal conclusions.

Mitigation: Use the artifact's legal boundary: present dated signals and follow-up queues only, and route FTO, infringement, validity, ownership, enforceability, SEP, or transaction advice to qualified review.

Risk: The artifact instructs English output even when a user may prefer another language.

Mitigation: Confirm the requested output language at task start and disclose any English-only connector or artifact constraint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/create-patent-landscape-overview-ip)
- [PatSnap Skill Hub](https://open.patsnap.com/marketplace/skill-hub)
- [PatSnap MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Global Core Patent Database MCP server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [Query and Taxonomy Construction Methodology](references/query-and-taxonomy-methodology.md)
- [Patent Landscape HTML Report Blueprint](references/report-html-blueprint.md)
- [Scientific and Executive Visual Standard](references/report-visual-style.md)
- [Scenario: Industry Patent Landscape](references/scenario-industry-landscape.md)
- [Scenario: Technology Evolution](references/scenario-technology-evolution.md)
- [Scenario: Competitor Patent Profile](references/scenario-competitor-portrait.md)
- [Scenario: Technical Solution Deep Dive](references/scenario-solution-deep-dive.md)
- [Scenario: Curated Patent Package and Index](references/scenario-patent-package-and-index.md)
- [Scenario: Patent Asset and Risk Signals](references/scenario-asset-and-risk-signals.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured artifact specifications for JSON, CSV, and self-contained HTML deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local project artifacts such as search configuration, patent indexes, chart data, tagging files, report manifests, and offline HTML reports when the required data sources and human review steps are available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
