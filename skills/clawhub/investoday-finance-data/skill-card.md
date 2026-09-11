## Description:

Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomics, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query, export, and compare structured Chinese market data for research workflows. It is intended for data retrieval and analysis support, not direct buy/sell advice, automated trading, or order execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill wraps a third-party networked finance-data CLI and may transmit query text or financial research inputs to external services.

Mitigation: Install only after reviewing the third-party CLI and avoid submitting confidential account, portfolio, or personal data to free-text endpoints.

Risk: Setup examples include command-line API keys, automatic updates, and disabled verification flags.

Mitigation: Prefer interactive initialization, do not pass real API keys directly in shell commands, and avoid --skip-verify or --auto-update unless the updater has been separately validated.

Risk: Financial data outputs can be mistaken for investment advice or trading instructions.

Mitigation: Treat results as research data, state data-access or coverage limits, and do not use the skill for direct buy/sell advice, automated trading, or order execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API reference index](artifact/docs/references-index.en.md)
- [Chinese API reference index](artifact/docs/references-index.md)
- [Skill usage guide](artifact/SKILL_EN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and structured data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Node.js 18+, the @investoday/investoday-api package, network access, local CLI configuration, and API permissions.]

## Skill Version(s):

1.8.83 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
