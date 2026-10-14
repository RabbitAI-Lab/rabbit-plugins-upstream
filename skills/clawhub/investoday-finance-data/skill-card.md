## Description:

Helps agents retrieve and compare Chinese market quotes, company financials, funds, indices, announcements, research, and macroeconomic data through the InvestToday API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, researchers, and developers use this skill to look up Chinese equities, Hong Kong stocks, funds, market and company data, and to prepare structured financial data for comparison or further research. It does not provide trading execution or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI setup requires an API key and sends financial query parameters to the InvestToday service.

Mitigation: Install only if the CLI and service are trusted; use secure key handling and avoid placing real keys directly in shell commands.

Risk: Sensitive financial data examples and advisory-like analyses may be mistaken for suitable investment advice.

Mitigation: Treat outputs as research data, avoid direct trading recommendations, and apply appropriate care to sensitive information.

Risk: Inconsistent reference examples or schemas can produce misleading or incorrect results.

Mitigation: Check endpoint parameters and verify consequential findings against authoritative sources before acting on them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API reference index](docs/references-index.en.md)
- [Chinese API reference index](docs/references-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured financial data, Shell commands]

**Output Format:** [Natural-language summaries and CLI query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the InvestToday CLI, service access, and an API key; coverage and results depend on endpoint permissions.]

## Skill Version(s):

1.8.95 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
