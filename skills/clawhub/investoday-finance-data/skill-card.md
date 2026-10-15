## Description:

Helps agents retrieve and interpret Chinese-market financial data covering stocks, funds, indices, company financials, announcements, research, and macroeconomic indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to retrieve and compare China-market quotes, fund data, financial statements, disclosures, research reports, and macroeconomic series for investment research and data export. It does not execute trades or provide personal buy-or-sell advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote API use may require an API key stored in local CLI configuration.

Mitigation: Install only if the remote service and local credential storage are acceptable; protect the API key.

Risk: Free-form entity recognition may transmit sensitive personal, account, or proprietary text.

Mitigation: Do not send sensitive text to the entity-recognition endpoint.

Risk: Inconsistent reference examples or unavailable data may lead to misleading investment analysis.

Mitigation: Confirm important endpoint semantics and results, disclose missing data, and treat outputs as research rather than personal financial advice.

## Reference(s):

- [InvestToday Finance Data on ClawHub](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API reference index](artifact/docs/references-index.en.md)
- [Chinese API reference index](artifact/docs/references-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Structured financial data]

**Output Format:** [Markdown summaries, data tables, and CLI query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on remote API availability, access permissions, and data coverage.]

## Skill Version(s):

1.8.96 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
