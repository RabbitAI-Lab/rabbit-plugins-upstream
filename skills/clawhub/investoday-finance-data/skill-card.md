## Description:

Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, and macroeconomic datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch Chinese market quotes, financial statements, valuation data, announcements, research reports, macroeconomic datasets, and structured exports for investment research and comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI initialization can store an API key, and passing real secrets directly on the command line can expose them through local command history or process inspection.

Mitigation: Prefer interactive initialization or an environment variable, and avoid placing real API keys directly in shell commands.

Risk: The auto-update option can enable a user-level scheduled task that later modifies the CLI or installed skills.

Mitigation: Enable auto-update only after accepting that behavior; otherwise keep auto-update disabled and review updates before use.

Risk: Returned market signals, research reports, and financial datasets can be stale, incomplete, permission-limited, or misread as investment advice.

Mitigation: Treat returned data as reference material, state data coverage and time-range limitations, and avoid direct buy or sell recommendations.

Risk: Network, permission, or service failures can prevent reliable data retrieval.

Mitigation: Stop inference that depends on unavailable data and report the limitation instead of filling gaps.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API Reference Index](docs/references-index.en.md)
- [Chinese API Reference Index](docs/references-index.md)
- [Market Data Reference](references/市场数据.md)
- [Basic Data Reference](references/基础数据.md)
- [Announcements Reference](references/公告.md)
- [Macro Economy Reference](references/宏观经济/国内宏观.md)
- [Funds Reference](references/基金/基金资料.md)
- [Index Quotes Reference](references/指数/基础行情.md)
- [Research Reports Reference](references/研报/基础数据.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration guidance]

**Output Format:** [Markdown responses with inline shell commands and structured financial-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the @investoday/investoday-api package, network access, and service credentials for protected data.]

## Skill Version(s):

1.8.80 (source: SKILL.md frontmatter and ClawHub release metadata, released 2026-09-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
