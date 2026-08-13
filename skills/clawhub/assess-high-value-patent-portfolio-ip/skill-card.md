## Description:

Rank a user-defined PatSnap patent candidate universe with an auditable 30/30/20/20 model based on simple-family forward citations, simple-family size, core-inventor concentration, and verified legal-event activity; select a documented 10-15% screening portfolio and generate traceable English HTML, JSON, and optional Word outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, R&D leaders, counsel, and developers use this skill to triage a reviewed PatSnap query result, rank candidates with a transparent evidence model, and prepare a traceable screening package. It supports prioritization and review preparation, not monetary valuation, enforceability, validity, freedom-to-operate, standards-essentiality, or investment conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PatSnap queries, patent universes, and generated reports may contain sensitive portfolio or business-review information.

Mitigation: Keep generated JSON, HTML, and DOCX reports private when the query or candidate universe is sensitive, and avoid placing PatSnap credentials in queries, command arguments, logs, screenshots, or reports.

Risk: Screening scores can be misread as patent value, validity, enforceability, freedom-to-operate, standards-essentiality, or investment advice.

Mitigation: Use the outputs for triage and review preparation only, preserve the stated limitations, and have an IP professional review the query scope, evidence gaps, event meaning, scoring interpretation, and selected narratives before relying on results.

Risk: Missing, failed, or not-run endpoint evidence can make a selected portfolio look more certain than the underlying data supports.

Mitigation: Preserve endpoint states, checkpoint errors, data gaps, and missing-data policy notes in the trace and reports; do not convert failures into factual zeros or conclude absence when required checks did not complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/assess-high-value-patent-portfolio-ip)
- [High-Value Patent Portfolio Screening Standard](artifact/references/screening-standard.md)
- [PatSnap Connect REST base URL](https://connect.patsnap.com)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Global Core Patents MCP server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated JSON, HTML, and optional DOCX report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a reviewed PatSnap query and PatSnap API credential; required outputs include an HTML report, JSON trace, selected-record JSON, and restartable checkpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
