## Description:

Fetch Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, macroeconomics, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Chinese market quotes, financial statements, valuations, announcements, research, fund and index data, macro indicators, sector data, and structured datasets for analysis or export. It is not intended for direct trading advice, automated order execution, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The InvestToday CLI can store an API key locally during initialization.

Mitigation: Install and initialize only in approved environments, protect local configuration files, and avoid entering credentials on shared or untrusted machines.

Risk: The one-shot initialization example can enable auto-update behavior that may modify the CLI or installed skills.

Mitigation: Use auto-update only when intentional and review updates before relying on the skill in controlled workflows.

Risk: Financial examples and returned data may be incomplete, unavailable, or unsuitable as investment advice.

Mitigation: Treat examples as reference documentation, disclose missing data or access limits, and require human review for investment decisions.

Risk: Queries may send portfolio, client, or research text to the InvestToday API.

Mitigation: Do not submit confidential data unless an approved data-handling policy permits it.

## Reference(s):

- [InvestToday Finance Data on ClawHub](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API Reference Index](artifact/docs/references-index.en.md)
- [Chinese API Reference Index](artifact/docs/references-index.md)
- [English Skill Usage Guide](artifact/SKILL_EN.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and structured financial-data query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and the @investoday/investoday-api package; data access may depend on network availability, permissions, local CLI configuration, and API coverage.]

## Skill Version(s):

1.8.59 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
