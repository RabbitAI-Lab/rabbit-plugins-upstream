## Description:

Fetches China-market financial data and investment-research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, macroeconomics, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to locate InvestToday API endpoints and fetch structured China-market financial data for research, comparison, export, and downstream analysis. It should not be used for trading execution, direct buy/sell advice, or conclusions that require inventing missing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can store an API key locally.

Mitigation: Treat API keys as secrets, avoid sharing them in prompts or logs, and prefer initialization flows that do not expose credentials in reusable shell history.

Risk: The documented auto-update and skip-verify setup example can allow local CLI or installed skill changes outside the immediate query task.

Mitigation: Prefer `investoday-api init` or `investoday-api init --api-key <key> --no-auto-update`; use auto-update only when the deployment owner intentionally accepts that behavior.

Risk: Financial data and investment-signal outputs can be incomplete, delayed, permission-limited, or misleading if treated as advice.

Mitigation: Use outputs for informational research, verify important results against primary sources, and avoid direct trading or portfolio decisions based solely on this skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [Reference Index](docs/references-index.en.md)
- [Chinese Reference Index](docs/references-index.md)
- [Basic Data](references/基础数据.md)
- [Market Data](references/市场数据.md)
- [A-share, Shanghai, Shenzhen, and Beijing Data](references/沪深京数据/基础信息/证券资料.md)
- [Fund Overview](references/基金/基金资料/基金概况.md)
- [Bond Data](references/债券.md)
- [Domestic Macroeconomic Data](references/宏观经济/国内宏观.md)
- [Research Reports](references/研报/基础数据.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, @investoday/investoday-api, network access, and configured API credentials for data queries.]

## Skill Version(s):

1.8.76 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
