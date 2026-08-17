## Description:

Assesses underused patents and related intangible assets, clusters them into decision-ready packages, evaluates activation options, and creates evidence-backed portfolio activation deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized external users use this skill to review defined patent portfolios, identify underused or under-evidenced assets, compare internal reuse and transaction scenarios, and prepare evidence-backed activation plans. It is intended for screening and planning, with legal, valuation, finance, tax, regulatory, technical, and business decisions left to qualified reviewers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive patent, portfolio, and business records may be exposed to unauthorized audiences.

Mitigation: Install only for authorized reviewers, preserve confidentiality boundaries, and create external versions only after removing confidential technical detail, personal data, internal thresholds, and restricted-source content.

Risk: Screening outputs may be mistaken for legal advice, formal valuation, buyer interest, or authority to contact counterparties or abandon rights.

Mitigation: Label outputs as screening and planning materials, keep decisions behind explicit approval gates, and require qualified legal, valuation, finance, tax, regulatory, technical, and business review.

Risk: Incomplete internal records, connector limits, or model-derived scores can produce unsupported activation claims.

Mitigation: Record evidence levels, dates, sources, missing data, and diligence gates; preserve unknowns instead of converting them into conclusions.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/yuanzhian-patsnap/skills/reactivate-underused-patents-ip)
- [MCP and Evidence Boundaries](references/mcp-boundaries.md)
- [Deliverable Specification](references/output-spec.md)
- [Example Requests](references/example-prompts.md)
- [PatSnap Patent Monetization MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-monetize)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Global Core Patent Database MCP server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown, structured tables, and self-contained HTML reports when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PDF, DOCX, XLSX, or PPTX only when requested and verified; outputs retain evidence states, diligence gates, and review boundaries.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
