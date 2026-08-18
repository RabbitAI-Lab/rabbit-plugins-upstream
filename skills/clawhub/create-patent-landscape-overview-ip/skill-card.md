## Description:

Orchestrates an evidence-backed patent-landscape workflow for product planning, R&D strategy, competitor intelligence, technology-route analysis, recommended patent packages, portfolio planning, and self-contained HTML reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

IP, R&D, product, and strategy teams use this skill to scope patent landscape questions, search and de-noise patent sets, design taxonomies, coordinate human tagging, analyze evidence, and produce a traceable HTML decision report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent landscape outputs can be mistaken for legal opinions or definitive risk conclusions.

Mitigation: Frame legal, asset, validity, infringement, FTO, and risk items as dated research signals for qualified follow-up, not conclusions.

Risk: The workflow depends on access to PatSnap MCP connectors and may otherwise lack live patent data.

Mitigation: Confirm connector access before execution; when a required connector is unavailable, continue only with authorized user-supplied data or preparation work and mark affected modules unavailable.

Risk: Patent exports, business context, and human-tagging files may contain sensitive project information.

Mitigation: Store exported patent data, user-supplied context, and tagging files only in an approved project location with appropriate data-handling controls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/create-patent-landscape-overview-ip)
- [PatSnap Skill Hub](https://open.patsnap.com/marketplace/skill-hub)
- [PatSnap MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Global Core Patent Database MCP](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
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

**Output Type(s):** [Guidance, Text, Markdown, Code, Configuration, Files]

**Output Format:** [Markdown guidance plus structured JSON, CSV, and self-contained HTML artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires evidence traceability, user checkpoints, human tagging handoff, and approved PatSnap connector access for live patent data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
