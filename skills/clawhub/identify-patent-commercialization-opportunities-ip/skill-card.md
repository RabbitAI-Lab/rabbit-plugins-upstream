## Description:

Assess a narrowly defined technology opportunity through reproducible patent searches, full-scope metrics, representative patent evidence, transparent scoring, and an offline multi-page decision report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent analysts, product teams, and R&D teams use this skill to assess whether a specific technical route merits further R&D, licensing, partnering, portfolio review, or commercialization diligence. It structures PatSnap-backed patent searches, separates full-scope metrics from representative patent evidence, and produces a traceable decision report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes a local ten-file report package, which can create or replace files in the working output area.

Mitigation: Run the skill in a clean project or output directory when preserving existing files matters.

Risk: Patent research may involve confidential technology details that are sent through the configured PatSnap MCP services.

Mitigation: Use only an approved PatSnap/MCP setup for sensitive data, and avoid entering confidential details when that setup is not approved.

Risk: Patent evidence can support diligence but does not establish legal freedom to operate, valuation, market demand, profitability, or investment suitability.

Mitigation: Treat the report as a screening aid and route legal, market, valuation, and FTO conclusions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/identify-patent-commercialization-opportunities-ip)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Deep Patent Mining MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [PatSnap Global Core Patent Database MCP server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [Input scoping prompt](references/prompts/input_scoping_prompt.md)
- [Search strategy prompt](references/prompts/search_strategy_prompt.md)
- [Full-scope metrics prompt](references/prompts/full_scope_metrics_prompt.md)
- [Evidence mapping prompt](references/prompts/evidence_mapping_prompt.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance, files]

**Output Format:** [Offline report package containing HTML, JSON, CSV, and Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a ten-file local report package with index, patent register, subfield, evidence, methodology, metrics, representative record, README, and quality-check artifacts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
