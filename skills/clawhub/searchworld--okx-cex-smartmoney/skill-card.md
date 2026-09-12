## Description:

Guides agents through read-only OKX Smart Money analytics for leaderboard traders, trader positions and history, and aggregated long/short signal trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query OKX Smart Money leaderboard and signal data through the OKX CLI, compare top traders, inspect positions and realized history, and summarize results in Markdown tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated profile checks can expose local OKX API-key profile details to the agent context.

Mitigation: Prefer OAuth or a least-privilege OKX API profile with withdrawals disabled and IP restrictions, and never paste credentials into chat.

Risk: Smart Money signal commands exclude coin-margined contracts, which can understate a trader's exposure in aggregated signals.

Mitigation: Cross-check a trader's full position book with trader-positions when signal output appears incomplete.

Risk: The skill uses live-only leaderboard data and does not support demo mode.

Mitigation: Treat outputs as live-market analytics and avoid presenting them as simulated or test data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/searchworld/skills/okx-cex-smartmoney)
- [OKX Homepage](https://www.okx.com)
- [Signal Commands Reference](artifact/references/signal-commands.md)
- [Trader Commands Reference](artifact/references/trader-commands.md)
- [Smart Money Workflows](artifact/references/workflows.md)
- [Templates and Formatting Reference](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only OKX CLI commands are expected to run with --json; trader and signal results are summarized for the user.]

## Skill Version(s):

1.4.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
