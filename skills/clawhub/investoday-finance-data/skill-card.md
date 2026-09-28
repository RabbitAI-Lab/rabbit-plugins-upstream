## Description:

Helps agents retrieve and explain Chinese market quotes, company financials, funds, indices, announcements, research, and macroeconomic data through InvestToday APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and other users researching Chinese markets can retrieve and compare stock, fund, index, corporate, and macroeconomic data or export it for further analysis. The skill does not execute trades or provide personalized buy or sell advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed in shell history or local configuration.

Mitigation: Avoid placing keys directly in shell commands when possible and review where the CLI stores its configuration.

Risk: Ratings, forecasts, and market signals may be mistaken for personalized investment advice.

Mitigation: Treat outputs as research data, verify important figures, and do not use the skill for direct trading decisions.

Risk: The skill relies on an external InvestToday CLI and data service.

Mitigation: Install only if you trust the package and state clearly when network access, permissions, or coverage prevent a reliable answer.

## Reference(s):

- [InvestToday Finance Data release](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API reference index (English)](artifact/docs/references-index.en.md)
- [API reference index (Chinese)](artifact/docs/references-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data, Guidance]

**Output Format:** [Natural-language summaries and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on API access, data coverage, and requested time range.]

## Skill Version(s):

1.8.91 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
