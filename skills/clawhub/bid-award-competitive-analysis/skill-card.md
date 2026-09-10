## Description:

Helps agents produce bid-award company intelligence and competitive-analysis reports covering awarded projects, amount trends, regional distribution, customer and supplier relationships, competitor overlap, public-risk findings, and optional HTML exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business analysts, procurement teams, and sales or competitive-intelligence teams use this skill to assess a company's public bid-award record, business footprint, customer ecosystem, and competitors. It supports single-company diligence reports and two-company competitive comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask to auto-register with the vendor service, collect a hashed MAC-derived device identifier after consent, and store an API key under ~/.zlbx/config.json.

Mitigation: Review the vendor API flow before installation, require explicit user consent before auto-registration, and prefer a user-supplied ZLBX_API_KEY when device-based trial registration is not desired.

Risk: The skill generates shareable reports and may include sk-bearing links that provide convenient access to company or bid pages.

Mitigation: Treat exported reports and sk-bearing links as sensitive, share them only with intended recipients, and avoid removing or altering returned URL parameters.

Risk: Bid-award data can be incomplete or stale, and competitive conclusions may be misleading if unsupported by returned evidence.

Mitigation: Use only API-returned amounts, counts, company names, and URLs; mark data gaps clearly; include data boundaries and source links in the report.

Risk: Public-risk and company-diligence language can create reputational risk if it states accusations as facts.

Mitigation: Use factual, source-linked wording for public-risk items, separate facts from interpretations, and avoid categorical claims about wrongdoing or reliability.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-award-competitive-analysis)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration guide](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)
- [HTML report renderer](artifact/scripts/render_report.py)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, HTML files]

**Output Format:** [Markdown reports in chat, JSON report data for rendering, and optional self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include cited bid/company records when available, generated HTML paths, data-boundary notes, and explicit cost estimates before paid queries.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
