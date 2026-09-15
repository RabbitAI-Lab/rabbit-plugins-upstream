## Description:

Provides OKX Smart Money analytics for leaderboard traders, trader profiles, open and closed positions, trade history, aggregated long/short signals, and signal trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and trading-focused users use this skill to query OKX smart-money leaderboards, inspect trader performance and histories, and summarize current or historical consensus signals. It is intended for analytics and guidance around read-only OKX data, not for placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a globally installed external OKX npm CLI.

Mitigation: Install and run it only in environments where the @okx_ai/okx-trade-cli package and pinned release version are trusted.

Risk: Credential profile checks may expose sensitive authentication or profile details if command output is shared.

Mitigation: Use least-privilege OKX credentials, avoid withdrawal or unnecessary trading permissions, confirm secret redaction before agent use, and do not paste raw authentication output into chat or logs.

Risk: Smart-money signal commands exclude coin-margined exposure, which can understate a trader's position picture.

Mitigation: Cross-check trader-level position data when a complete exposure view is needed, especially for BTC or ETH analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-smartmoney)
- [OKX homepage](https://www.okx.com)
- [Smart Money Workflows](artifact/references/workflows.md)
- [Trader Commands Reference](artifact/references/trader-commands.md)
- [Signal Commands Reference](artifact/references/signal-commands.md)
- [Templates and Formatting Reference](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown tables and concise guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should request JSON output and present read-only analytics in the user's language.]

## Skill Version(s):

1.4.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
