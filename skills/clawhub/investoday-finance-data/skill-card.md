## Description:

Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomics, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find and call InvestToday finance-data endpoints for market quotes, company fundamentals, fund and index data, announcements, research reports, macroeconomic data, and structured export for downstream analysis. It should support research workflows and should not be used for direct trading advice, order execution, or invented conclusions when data is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI requires network access and may need an API key, so secrets could be exposed if passed directly on the command line or stored carelessly.

Mitigation: Prefer interactive initialization or environment-based secret handling, avoid logging credentials, and review local CLI configuration after setup.

Risk: The documented --auto-update setup path can enable background updates that may change the CLI or installed skills after initial review.

Mitigation: Avoid --auto-update unless background updates are explicitly desired, and re-review the skill and CLI behavior after updates.

Risk: Financial ratings, target prices, trading signals, and sample data can be mistaken for investment advice.

Mitigation: Use outputs as informational research, avoid direct buy or sell recommendations, and direct users to qualified financial advice for investment decisions.

Risk: Endpoint results can be empty, restricted by permission, stale, or outside the requested time range.

Mitigation: State the query scope and data limitations clearly, and do not infer market conclusions from unavailable or incomplete data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API reference index](docs/references-index.en.md)
- [Base data references](references/基础数据.md)
- [A-share and Beijing market financial data references](references/沪深京数据/财务数据/三大报表当期数据.md)
- [Fund performance references](references/基金/基金业绩表现/净值数据.md)
- [Announcement references](references/公告.md)
- [Research report references](references/研报/基础数据.md)
- [Macroeconomic references](references/宏观经济/国内宏观.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and structured data returned by the InvestToday CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, network access, the @investoday/investoday-api package, and appropriate API credentials or local CLI configuration.]

## Skill Version(s):

1.8.71 (source: SKILL.md frontmatter and server release metadata, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
