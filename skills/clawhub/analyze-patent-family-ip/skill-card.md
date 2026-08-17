## Description:

Analyze a patent family from a patent identifier or PatSnap patent URL by defining the family scope, reconstructing priority and procedural relationships, comparing technical disclosures and claim focus, mapping themes, and generating a source-traceable offline HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP counsel, portfolio teams, R&D groups, competitive-intelligence teams, and due-diligence teams use this skill to map patent-family structure, compare members, trace priority and procedural relationships, and produce a source-traceable offline report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects access to PatSnap patent MCP connectors and may depend on account-scoped patent data permissions.

Mitigation: Install it only for patent-family research workflows and review PatSnap account and connector permissions separately before use.

Risk: Patent-family analysis can be mistaken for legal, validity, enforceability, FTO, or commercial-strategy advice.

Mitigation: Keep conclusions bounded to source-traceable evidence, preserve unavailable-evidence labels, and route legal interpretations to qualified patent or counsel review.

Risk: Reports include user-supplied and patent-database text that must remain safe to view in a local browser.

Mitigation: Use the bundled local renderer, which escapes untrusted text, allowlists HTTP and HTTPS links, avoids remote dependencies, and writes only the requested HTML output.

## Reference(s):

- [Patent Briefing MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Advanced Patent Search MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Global Core Patent Database MCP Server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/analyze-patent-family-ip)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown workflow guidance, normalized JSON contract, and self-contained HTML report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is designed for offline review, preserves source locators, and explicitly labels unavailable evidence and analytical inferences.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
