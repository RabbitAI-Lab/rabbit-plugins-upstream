## Description:

Fetches China-market financial data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomic data, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial researchers use this skill to find InvestToday API endpoints, run CLI queries, and retrieve structured China-market data for research, comparison, export, or backtesting preparation. It is not intended for direct trading advice, automated order execution, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow documents a one-shot initialization command that combines an API key with auto-update and skip-verify flags.

Mitigation: Prefer interactive initialization or a secret-store workflow, avoid pasting real API keys into shell commands or chat, and do not use auto-update or skip-verify unless reviewed.

Risk: The skill depends on the third-party @investoday/investoday-api package and network access to retrieve market data.

Mitigation: Install only when the package and data source are trusted, and review package updates before deployment.

Risk: Returned financial data may be misread as investment advice or used beyond the available data scope.

Mitigation: Treat responses as research input, verify important outputs against source endpoint documentation, and clearly state when data is missing, restricted, or unavailable.

Risk: Security evidence notes that some examples appear inconsistent or contaminated.

Mitigation: Double-check endpoint documentation and parameters before relying on example commands in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API reference index](docs/references-index.en.md)
- [Source provenance unavailable](evidence.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and concise data-query guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the @investoday/investoday-api package, network access, and appropriate API credentials or local CLI configuration.]

## Skill Version(s):

1.8.83 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
