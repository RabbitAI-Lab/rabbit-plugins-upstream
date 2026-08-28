## Description:

Process Avanza CSV exports, calculate TWRR/Modified Dietz returns, and track portfolio performance. Use when importing stock transactions, calculating investment returns, or managing portfolio data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to import Avanza investment CSV exports, track portfolio accounts and holdings, update market prices, and calculate investment performance and risk metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can reset, delete, or rebuild local financial records.

Mitigation: Keep database backups and use `delete-tx --dry-run` before deleting transactions; reserve `reset --hard` and virtual account deletion for intentional cleanup.

Risk: Market-data, risk, or beta updates may contact external services and disclose asset names or tickers.

Mitigation: Use `--update-prices never` when external price requests are not desired, and review `--risk` or `--beta` usage before running those reports.

Risk: Unpinned dependency installation can make results less reproducible.

Mitigation: Pin and review the `requests` dependency before installing the skill in a managed or commercial environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/patello/skills/avanza-investment-tracker)
- [Workflows](references/workflows.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI/configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose commands that import, update, reset, or delete local portfolio records; review commands before execution.]

## Skill Version(s):

2.13.0 (source: ClawHub release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
