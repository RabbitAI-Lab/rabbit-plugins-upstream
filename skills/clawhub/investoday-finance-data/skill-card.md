## Description:

Helps agents retrieve Chinese-market financial data and investment research on stocks, funds, indices, company financials, announcements, reports, and macroeconomics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and other users can use this skill to look up and compare market quotes, fund performance, financial statements, research, and economic indicators for Chinese markets. It does not execute trades or provide personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Putting an API key directly into a setup command can expose it through shell history or process listings.

Mitigation: Prefer interactive setup or protected secret storage; avoid copying inline API-key examples.

Risk: The example setup command disables a verification check and the skill depends on an external package and service.

Mitigation: Install only if you trust the package and service; do not use --skip-verify without understanding the check it disables.

Risk: Inconsistent reference examples or incomplete market data can lead to misleading conclusions or financial decisions.

Mitigation: Independently verify results and coverage; treat outputs as research data, not financial advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API reference index](artifact/docs/references-index.en.md)
- [Chinese API reference index](artifact/docs/references-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with financial data summaries, optional tables, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live data requires Node.js 18+, the InvestToday package, service access, and local configuration.]

## Skill Version(s):

1.8.93 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
