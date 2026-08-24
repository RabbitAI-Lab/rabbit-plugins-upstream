## Description:

Analyze creator revenue streams (Stripe, PayPal, affiliate, sponsorships) to calculate true profitability per content piece, identify unprofitable segments, forecast cash flow gaps, and recommend high-margin content verticals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ncreighton](https://clawhub.ai/user/ncreighton)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, solopreneurs, and digital agencies use this skill to aggregate revenue sources, calculate true content profitability, identify unprofitable segments, forecast cash flow, and prepare automated financial health reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for live payment and business-service credentials, which could expose transaction or customer data if credentials are over-scoped or mishandled.

Mitigation: Use sandbox or read-only credentials where possible, store secrets only in a proper secret manager or environment configuration, and restrict token scopes before running financial analyses.

Risk: Automated reports can send sensitive financial or customer information to unintended Slack, Airtable, or Zapier destinations.

Mitigation: Verify every reporting destination before enabling automation and avoid sharing customer or transaction data unless that disclosure is intended.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain-text financial reports, alerts, recommendations, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include financial summaries, profitability rankings, cash-flow forecasts, and automated report setup guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
