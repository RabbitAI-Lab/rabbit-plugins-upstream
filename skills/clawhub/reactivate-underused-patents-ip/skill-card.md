## Description:

Assess underused patent assets and build evidence-backed activation options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent and IP portfolio teams, business owners, and authorized advisors use this skill to review a defined patent and related-intangible-asset population, cluster assets into evidence-backed activation options, evaluate transaction-readiness gates, research candidate counterparties, and prepare management-facing action plans. It supports screening and decision preparation for internal reuse, maintenance review, licensing, assignment, collaboration, portfolio cleanup, and related diligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use authorized internal patent, IP, business, contract, or transaction records that are confidential or access-controlled.

Mitigation: Install and run it only for users authorized to analyze the relevant portfolio, and set confidentiality, external-disclosure, and source-access boundaries before use.

Risk: Outputs could be mistaken for legal advice, formal valuation, buyer interest, outreach approval, or a final maintenance, abandonment, licensing, assignment, pledge, or transaction decision.

Mitigation: Treat outputs as decision support and require the relevant owner, counsel, valuation or finance, tax, regulatory, technical, and business approval gates before acting.

Risk: Missing internal records, unavailable source dependencies, or model-derived scores could lead to unsupported conclusions about use, value, demand, transaction readiness, or counterparties.

Mitigation: Preserve unknowns, record source provenance and evidence levels, separate database or model signals from verified facts, and avoid final claims without authoritative evidence.

## Reference(s):

- [MCP and Evidence Boundaries](references/mcp-boundaries.md)
- [Deliverable Specification](references/output-spec.md)
- [Example Requests](references/example-prompts.md)
- [PatSnap Patent Monetization and Valuation MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-monetize)
- [PatSnap Advanced Patent Search MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Global Core Patent Database MCP Server](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [PatSnap Patent Briefing MCP Server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Guidance]

**Output Format:** [Markdown guidance with optional self-contained HTML, PDF, DOCX, XLSX, or PPTX deliverables when requested and authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision support only; outputs require appropriate owner, legal, valuation, finance, tax, regulatory, technical, and business review before final action.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
