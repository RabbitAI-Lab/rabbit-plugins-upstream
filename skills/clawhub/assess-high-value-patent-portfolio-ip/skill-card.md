## Description:

Rank a user-defined PatSnap patent candidate universe with an auditable 30/30/20/20 model based on simple-family forward citations, simple-family size, core-inventor concentration, and verified legal-event activity; select a documented 10-15% screening portfolio and generate traceable English HTML, JSON, and optional Word outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, IP analysts, R&D leaders, counsel, and developers use this skill to screen one reviewed PatSnap patent-query result, rank candidates with documented evidence, and prepare a traceable high-value patent portfolio review. It supports triage and prioritization, not monetary valuation, enforceability, validity, freedom-to-operate, standards-essentiality, or investment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PatSnap API credentials could be exposed if placed in query text, command arguments, logs, screenshots, repositories, or reports.

Mitigation: Keep the API key in PATSNAP_API_KEY or a reviewed PATSNAP_API_KEY_FILE and review generated artifacts for credential absence before sharing.

Risk: Patent-screening scores may be mistaken for monetary value, legal enforceability, validity, claim scope, market coverage, or investment merit.

Mitigation: Use the report as triage only, preserve evidence states, and require human review of query scope, missing data, legal events, and selected-record rationales.

Risk: Optional abstract-image fetching can make outbound HTTP(S) requests and may retrieve expiring or untrusted image URLs.

Mitigation: Leave image downloading disabled unless final_records.json came from the trusted pipeline and outbound image fetching is acceptable; use the built-in HTTP(S), redirect, content-type, and size checks.

Risk: A missing or failed endpoint result can be misread as factual zero or legal-event absence.

Mitigation: Retain missing, error, empty, and not_run states separately from scoring points and state when absence cannot be concluded.

## Reference(s):

- [High-Value Patent Portfolio Screening Standard](references/screening-standard.md)
- [Reference implementation README](scripts/README.md)
- [PatSnap Connect REST base URL](https://connect.patsnap.com)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Global Core Patents MCP server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/assess-high-value-patent-portfolio-ip)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated files, including static HTML, JSON trace data, stage checkpoints, and optional DOCX output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a reviewed PatSnap query and PatSnap credentials; preserves restartable checkpoints and evidence states.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
