## Description:

Research a product feature from current public sources, decompose it into technical dimensions, retrieve and review related patents, map each patent's disclosed evidence to those dimensions, rank relevance under a transparent rubric, and generate a self-contained interactive HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and IP researchers use this skill to turn a product-feature question into sourced product evidence, technical dimensions, related patent retrieval, evidence-backed patent-to-dimension mapping, relevance-ranked analysis, and an interactive HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product-feature descriptions and search terms may be sent to public web sources or PatSnap MCP services.

Mitigation: Confirm the research boundary and connector permissions before use, and avoid confidential product details unless that sharing is acceptable.

Risk: Patent-feature mappings can be mistaken for legal conclusions about implementation, ownership, infringement, validity, or freedom to operate.

Mitigation: Present mappings as technical correspondence only, preserve uncertainty, and require qualified IP review for legal conclusions.

Risk: Live patent connector schemas, retrieval caps, missing record links, or incomplete patent text can limit reproducibility and coverage.

Mitigation: Inspect active connector schemas, record operations, dates, parameters, record IDs, counts, caps, and limitations, and avoid completeness claims from limited result sets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/map-product-features-to-patents-ip)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Deep Patent Mining MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [PatSnap Global Core Patent Database MCP server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance and self-contained HTML report content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local interactive HTML report with embedded CSS and minimal filtering JavaScript; patent mappings remain evidence-backed and non-legal.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
