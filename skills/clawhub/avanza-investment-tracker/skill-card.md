## Description:

Process Avanza CSV exports, calculate TWRR/Modified Dietz returns, and track portfolio performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT

## Use Case:

Developers and finance-focused users use this skill to import Avanza transaction exports, maintain a local portfolio database, calculate investment returns, inspect holdings, and generate portfolio statistics or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio data is stored in a local SQLite database, and generated backup files can contain sensitive financial information.

Mitigation: Store the database and .bak files outside source control and restrict access to the local data directory.

Risk: Default price updates can send asset names and currency pairs to Avanza; risk metrics can send benchmark ticker and date range to Riksbanken or Yahoo Finance.

Mitigation: Use --update-prices never for offline operation and avoid --risk or --beta unless those external market-data calls are acceptable.

Risk: Destructive commands can permanently delete transactions or rebuild derived portfolio data.

Mitigation: Back up the database first, use dry-run options where available, and avoid broad selectors until the target rows are verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patello/skills/avanza-investment-tracker)
- [Workflows](references/workflows.md)
- [Troubleshooting](references/troubleshooting.md)
- [Avanza market data endpoint](https://www.avanza.se)
- [Riksbanken API](https://api.riksbank.se)
- [Yahoo Finance query endpoint](https://query1.finance.yahoo.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI commands produce tables or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or write a user-specified SQLite database and can use optional network calls for market data unless disabled.]

## Skill Version(s):

2.14.1 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
