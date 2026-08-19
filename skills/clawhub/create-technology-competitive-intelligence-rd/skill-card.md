## Description:

Creates an evidence-led technology competitive-intelligence report for a defined company, technology, market, and review period.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D, strategy, product, and IP teams use this skill to produce management-grade competitive-intelligence briefings for a defined focal organization, technology scope, geography, time window, competitor set, and decision context. It supports competitor tiering, patent and technology comparisons, customer or partner mapping, event monitoring, threat assessment, and evidence-backed recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain sensitive business analysis, source research, or confidential input data.

Mitigation: Keep input JSON and output HTML in an appropriate workspace, and review sharing boundaries before distribution.

Risk: Competitive-intelligence conclusions can be misleading if patent counts, market values, assumptions, or recommendations are treated as legal, valuation, or primary customer-research advice.

Mitigation: Require reviewed evidence, visible assumptions, dated citations, disclosed calculation methods, and qualified counsel or specialists for legal, FTO, valuation, or customer-research decisions.

Risk: Public evidence and optional connector results may be incomplete, stale, or require analyst interpretation.

Mitigation: Record evidence cutoff dates, access dates, source links or identifiers, review status, and confidence levels; label unsupported items as not established from reviewed evidence.

## Reference(s):

- [V12 HTML report template](references/template_v12.html)
- [V11 HTML report template](references/template_v11.html)
- [V8 HTML report template](references/template_v8.html)
- [PatSnap Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, html, shell commands, configuration, guidance]

**Output Format:** [Self-contained HTML report plus concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local renderer expects reviewed UTF-8 JSON with required report fields and writes an .html output file.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
