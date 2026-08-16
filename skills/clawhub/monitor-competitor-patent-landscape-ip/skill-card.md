## Description:

Analyzes one competitor's patent portfolio architecture in a defined technology for monitoring and strategy reports while avoiding infringement or freedom-to-operate conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Corporate IP teams, R&D engineers, product leaders, and strategy analysts use this skill to examine a competitor's patent activity within a defined technology, identify technical concentration and filing behavior, select representative patent families, and produce evidence-backed R&D recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Competitor names, technology scope, search terms, and retrieved patent-analysis data may be sent to PatSnap MCP services.

Mitigation: Confirm the user is comfortable sharing that information with PatSnap services, honor confidentiality constraints, and keep API keys secret.

Risk: A generated patent landscape report could be mistaken for legal advice, infringement analysis, or freedom-to-operate clearance.

Mitigation: Present the report as research and strategy support only, and recommend qualified IP counsel or a separate FTO workflow when legal clearance is required.

Risk: Requested PDF output may fall back to HTML if PDF conversion is unavailable.

Mitigation: Choose report output paths intentionally and report the actual generated HTML or PDF path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/monitor-competitor-patent-landscape-ip)
- [Competitor patent landscape workflow guide](references/workflow_guide.md)
- [PatSnap Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with JSON analysis data and HTML or PDF report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report renderer escapes JSON-derived content, attempts PDF generation, and writes an HTML fallback when PDF conversion is unavailable.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
