## Description:

Fetch Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomics, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Chinese market quotes, company fundamentals, fund and index data, announcements, research reports, macro indicators, and structured datasets for financial research. It is not intended for direct trading advice, automated order execution, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI may require a financial-data API key, network access, and local credential storage.

Mitigation: Prefer interactive initialization or an environment variable over putting API keys in commands, and review local configuration before use.

Risk: The documented initialization command includes optional auto-update and skip-verification flags.

Mitigation: Avoid --skip-verify and disable auto-update unless scheduled CLI and skill updates are intentional.

Risk: Financial outputs may be mistaken for investment advice or over-interpreted when data is unavailable.

Mitigation: Treat outputs as research data, avoid direct buy or sell recommendations, and state data, permission, network, or time-range limitations when applicable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API Reference Index](artifact/docs/references-index.en.md)
- [Chinese API Reference Index](artifact/docs/references-index.md)
- [Skill Usage Guide](artifact/SKILL_EN.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline CLI commands and summarized financial data results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on Node.js 18+, the @investoday/investoday-api package, network access, local CLI configuration, and data-provider permissions.]

## Skill Version(s):

1.8.75 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
