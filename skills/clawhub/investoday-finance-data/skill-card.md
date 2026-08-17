## Description:

Fetches Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomics, and more than 200 API interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve, compare, and export structured Chinese market data for investment research, financial analysis, and data preparation. It is not intended for direct buy or sell advice, automated trading, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI initialization can store an API key or expose secrets when keys are passed directly on the command line.

Mitigation: Prefer interactive initialization or environment variables for secrets, and avoid including API keys in command history or shared logs.

Risk: Auto-update and skip-verify options can permit local scheduled updates or bypass checks for the installed CLI and skill files.

Mitigation: Do not use --auto-update or --skip-verify unless the operator intentionally accepts that update behavior and has reviewed the package source.

Risk: Scores, ratings, forecasts, and buy or sell signal fields may be mistaken for financial advice.

Mitigation: Treat retrieved data as research material only and avoid using the skill for direct trading advice, automated trading, or order execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API reference index](docs/references-index.en.md)
- [API reference index](docs/references-index.md)
- [Basic data reference](references/基础数据.md)
- [Market data reference](references/市场数据.md)
- [Announcement data reference](references/公告.md)
- [Bond data reference](references/债券.md)
- [Futures data reference](references/期货.md)
- [Spot data reference](references/现货.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on network access, local CLI initialization, API permissions, and endpoint-specific query parameters.]

## Skill Version(s):

1.8.74 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
