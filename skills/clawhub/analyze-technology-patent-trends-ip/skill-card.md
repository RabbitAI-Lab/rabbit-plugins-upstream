## Description:

Convert an already retrieved, screened, and tagged patent dataset into an evidence-bounded competitive technology insight report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and IP strategy teams use this skill to turn prepared patent datasets into management-grade technology trend, competitor positioning, opportunity, and R&D/IP action reports. It is intended for decision support after retrieval, screening, and formal tagging have already established dataset scope and evidence boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent and business datasets may contain sensitive or restricted information.

Mitigation: Use only datasets approved for analysis and preserve the skill's evidence boundary, provenance, coverage, and missing-value disclosures in generated reports.

Risk: Connector URLs, API keys, or private access details could be exposed if included in input data or reports.

Mitigation: Keep credentials and private connection URLs outside report content and use only authorized PatSnap MCP connectors when live validation or enrichment is needed.

Risk: Generated strategic or IP recommendations could be mistaken for legal, market, freedom-to-operate, or product conclusions.

Mitigation: Review outputs as decision support, use bounded language, and route legal, FTO, market, and product claims to the appropriate expert review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/analyze-technology-patent-trends-ip)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Competitive technology insight white-paper framework](references/white-paper-framework.md)
- [HTML competitive technology insight report specification](references/html-report-template-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown reports or self-contained HTML reports, with evidence-bound tables, matrices, methods, limitations, and action recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve dataset provenance, counting rules, missingness, coverage, evidence strength, and limitations; generated reports must not expose API keys or private connector URLs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
