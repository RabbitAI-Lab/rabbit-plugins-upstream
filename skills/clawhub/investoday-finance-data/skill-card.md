## Description:

Fetches Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, and macroeconomic datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:


## Use Case:

External users and developers can retrieve structured Chinese-market financial data for investment research, comparisons, and downstream analysis. The skill is not intended to provide direct buy/sell advice or execute trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented setup shortcut enables automatic software and skill updates, whose scope may not be clear to the user.

Mitigation: Initialize with --no-auto-update unless scheduled updates are intentional; inspect update status and disable automatic updates when needed.

Risk: The skill uses an API key and sends financial-data queries to the data provider.

Mitigation: Protect the API key and understand that query information is sent to the financial-data provider.

## Reference(s):

- [InvestToday Finance Data on ClawHub](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API Reference Index](docs/references-index.en.md)
- [Market Data Reference](references/市场数据.md)
- [Fundamentals Reference](references/基础数据.md)

## Skill Output:

**Output Type(s):** [Structured financial data, Text, Markdown]

**Output Format:** [Structured financial data with optional natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage and fields depend on the selected endpoint, instruments, query parameters, permissions, and data availability.]

## Skill Version(s):

1.8.98 (source: skill frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
