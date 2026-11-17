## Description:

Guides agents to use the OKX CLI for crypto news aggregation, coin sentiment analysis, sentiment trends, and macro-economic calendar queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[numpy0001](https://clawhub.ai/user/numpy0001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer crypto market-intelligence questions with OKX CLI commands for news, sentiment, and economic-calendar data. It supports market briefings, coin sentiment checks, source-filtered news, and macro impact analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live OKX credentials may be exposed or used unsafely when configuring or invoking the CLI.

Mitigation: Use a safer credential setup path where available, avoid pasting real API secrets into command-line examples, and install only when comfortable with a global OKX CLI.

Risk: Some workflows may read private account balances or positions.

Mitigation: Run account-data workflows only when the user explicitly intends to share that account information.

## Reference(s):

- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)
- [OKX](https://www.okx.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and optional JSON-producing CLI invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a global OKX CLI installation, live OKX credentials, rate-limited economic calendar calls, and cross-skill market or portfolio commands for some workflows.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
