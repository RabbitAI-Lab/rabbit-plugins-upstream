## Description:

Build an evidence-backed competitive patent landscape for a defined industry, technology, competitor set, geography, and time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Executives, strategy teams, product leaders, competitive-intelligence analysts, and IP teams use this skill to scope and produce evidence-backed competitive patent landscape reports across industries, technologies, competitors, geographies, and time windows. It supports competitor technology-bet analysis, geographic filing-strategy comparison, representative patent review, and opportunity-hypothesis framing, but not infringement clearance or freedom-to-operate opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the patent landscape report as legal clearance or freedom-to-operate advice.

Mitigation: Use the report for research support only, preserve the skill's no-infringement-clearance boundary, and route legal conclusions to qualified counsel.

Risk: Patent conclusions may be distorted by stale cut-off dates, capped samples, unresolved assignee relationships, family deduplication choices, or missing legal-status context.

Mitigation: Review the generated report for evidence quality, retrieval dates, scope, denominators, sampling labels, entity resolution, counting unit, and dated legal status before sharing.

Risk: Client-sensitive or confidential information may be sent through configured PatSnap MCP tools or included in reports.

Mitigation: Use only information approved for the configured tools, keep API keys out of reports and logs, and review output for client-sensitive content before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/map-competitive-patent-landscape-ip)
- [Competitive patent landscape report template](references/REPORT_TEMPLATE.md)
- [Competitive patent landscape search strategy](references/SEARCH_STRATEGY.md)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Analysis, Guidance, Configuration]

**Output Format:** [Markdown guidance and a complete HTML patent landscape report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should state scope, retrieval date, counting unit, date basis, denominators, sampling limits, citations, legal-status dates, and confidence for strategic interpretations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
