## Description:

Smart Money analytics on OKX: leaderboard traders, position tracking, trade records, closed-position history, aggregated consensus signals, and signal history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to query OKX Smart Money leaderboard traders, trader positions, historical trades, closed-position records, and aggregated long/short consensus signals through authenticated read-only CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and authenticating the OKX CLI gives the agent access to persistent local OKX auth and profile state.

Mitigation: Use a dedicated least-privileged OKX profile or sub-account, and do not provide credentials or secrets in chat.

Risk: The installed OKX CLI is broader than this skill's documented read-only smart-money commands.

Mitigation: Limit use to the documented read-only smartmoney commands and avoid live trading permissions unless they are needed outside this skill.

Risk: The CLI installation includes a postinstall helper-binary download.

Mitigation: Review the package and installation source before installing in sensitive environments.

Risk: Smart-money signal outputs can omit coin-margined exposures and may understate some trader positions.

Mitigation: Cross-check a trader's full position book with trader-position commands when signal coverage materially affects a decision.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-smartmoney)
- [Trader Commands Reference](references/trader-commands.md)
- [Signal Commands Reference](references/signal-commands.md)
- [Smart Money Workflows](references/workflows.md)
- [Templates & Formatting Reference](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with CLI command examples and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON CLI responses as source data and presents summaries as human-readable Markdown tables.]

## Skill Version(s):

1.4.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
