## Description:

Fetches Chinese financial-market and investment-research data across A-shares, Hong Kong stocks, funds, ETFs, indices, financial statements, announcements, research reports, market data, and macroeconomic datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to find and call InvestToday data endpoints for Chinese equities, Hong Kong stocks, funds, indices, announcements, research reports, macro data, and structured data export. It supports research workflows and should not be used for direct buy or sell advice, automated trading, or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI initialization can store API credentials or expose them through shell history when keys are passed directly on the command line.

Mitigation: Prefer interactive investoday-api init or a secret-management workflow; avoid placing real API keys directly in shell commands.

Risk: Auto-update behavior can change the CLI or installed skills after setup.

Mitigation: Use --no-auto-update when persistence is not desired and check update state with investoday-api update status or investoday-api update disable.

Risk: Using --skip-verify can bypass verification during setup.

Mitigation: Avoid --skip-verify unless there is a documented reason and the package, endpoint, and configuration source have been reviewed.

Risk: Financial outputs, ratings, targets, and indicators may be mistaken for investment advice.

Mitigation: Treat all returned data and analysis as research information only; do not use the skill for direct buy or sell advice, automated trading, or order execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API Reference Index (English)](docs/references-index.en.md)
- [API Reference Index](docs/references-index.md)
- [Basic Data Reference](references/基础数据.md)
- [Market Data Reference](references/市场数据.md)
- [Announcements Reference](references/公告.md)
- [Macro Data Reference](references/宏观经济/国内宏观.md)
- [Fund Data Reference](references/基金/基金资料/基金概况.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured data returned by the InvestToday CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the @investoday/investoday-api package, network access, and local CLI initialization before data queries.]

## Skill Version(s):

1.8.62 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
