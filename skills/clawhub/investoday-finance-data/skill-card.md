## Description:

Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, macroeconomics, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to find and call InvestToday finance-data endpoints for Chinese market quotes, company fundamentals, fund data, announcements, research reports, macro indicators, sector data, and structured data export. It is not intended for trading execution, direct buy or sell advice, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI stores an API key in local configuration.

Mitigation: Initialize only in a trusted environment, protect the local configuration as a secret, and rotate the key if exposure is suspected.

Risk: Financial queries are sent to InvestToday services over the network.

Mitigation: Avoid submitting confidential or trading-sensitive inputs unless the service and data-handling terms are approved for the use case.

Risk: Background auto-updates can change the CLI or installed skills after setup.

Mitigation: Run initialization with auto-update disabled unless scheduled updates are intentionally approved, and review updates before enabling them.

Risk: Returned financial data or summaries may be mistaken for investment advice.

Mitigation: Use outputs as research data only and require qualified review before making investment or trading decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API Reference Index](docs/references-index.en.md)
- [API Reference Index](docs/references-index.md)
- [Base Data Reference](references/基础数据.md)
- [Market Data Reference](references/市场数据.md)
- [Announcements Reference](references/公告.md)
- [Research Corpus Reference](references/大模型语料.md)
- [Bonds Reference](references/债券.md)
- [Futures Reference](references/期货.md)
- [Spot Quotes Reference](references/现货.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the @investoday/investoday-api package, network access, and initialized local CLI configuration.]

## Skill Version(s):

1.8.79 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
