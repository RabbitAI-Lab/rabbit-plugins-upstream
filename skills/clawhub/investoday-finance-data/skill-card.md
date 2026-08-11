## Description:

Fetches Chinese financial-market data across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomic datasets, and related market information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to locate InvestToday finance-data endpoints, run CLI data queries, and prepare structured Chinese market data for research, comparison, and analysis. It is not intended for direct trading advice, automated order execution, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup flags can enable background auto-updates that modify the CLI and installed skills.

Mitigation: Review initialization flags before installing; use --no-auto-update unless recurring updates are intended and avoid --skip-verify unless the verification tradeoff is acceptable.

Risk: Financial data outputs can be mistaken for personalized investment advice.

Mitigation: Treat outputs as research data, preserve the skill's restriction against direct buy or sell advice, and verify important conclusions against authoritative market sources.

Risk: Queries and returned data may include watchlists, fund codes, date ranges, or personal profile fields.

Mitigation: Minimize sensitive inputs, avoid unnecessary personal identifiers, and handle returned profile or portfolio-like fields as sensitive research data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English Skill Documentation](artifact/SKILL_EN.md)
- [API Reference Index](artifact/docs/references-index.en.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the @investoday/investoday-api package, network access, and any credentials needed by the InvestToday CLI.]

## Skill Version(s):

1.8.66 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
