## Description:

Converts a prepared, screened, and tagged patent dataset into an evidence-bounded competitive technology insight report covering technology routes, competitor positioning, taxonomy-function matrices, opportunities, trends, and R&D/IP actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, R&D strategy teams, and external users use this skill to turn validated tagged patent datasets into bounded competitive technology insight, including landscape summaries, technology-route analysis, competitor profiles, opportunity hypotheses, and next-step R&D/IP recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be mistaken for legal, investment, market, or product proof.

Mitigation: Treat outputs as decision-support analysis and route legal, investment, market, and product conclusions to qualified review.

Risk: Incomplete or unvalidated patent data can produce unsupported competitive claims.

Mitigation: Use a validated screened and tagged dataset or approved PatSnap MCP connectors; when inputs are incomplete, report readiness gaps instead of presenting an executed analysis.

Risk: Connector authorization or output location may be inappropriate for the task.

Mitigation: Review connector authorization and the approved output path before use, and keep API keys or private connection URLs out of generated reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/analyze-technology-patent-trends-ip)
- [Competitive technology insight white-paper framework](artifact/references/white-paper-framework.md)
- [HTML competitive technology insight report specification](artifact/references/html-report-template-spec.md)
- [PatSnap Advanced Patent Search MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Deep Patent Mining MCP marketplace](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [PatSnap Developer Center](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown report or self-contained HTML document]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a validated screened and tagged patent dataset, records explicit evidence boundaries, and omits unsupported analytical dimensions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
