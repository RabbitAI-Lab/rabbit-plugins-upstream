## Description:

Helps agents create, adjust, stop, and monitor OKX Grid, DCA Martingale, and Smart Portfolio trading bots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers use this skill to manage OKX trading bots, inspect performance, and explore recommended portfolio settings and backtests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live trading profile can move real funds through bot creation, closure, or rebalancing.

Mitigation: Prefer demo mode first, verify the selected profile, and require explicit confirmation before live create, stop, close-position, or instant-rebalance actions.

Risk: Reducing margin on a live contract bot can increase liquidation risk.

Mitigation: Confirm the active bot, profile, and margin change with the user before reducing margin.

Risk: Trading credentials could be exposed if supplied in chat.

Mitigation: Never request credentials in chat; direct users to the CLI credential setup flow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-cex-bot)
- [OKX](https://www.okx.com)
- [Grid bot commands](artifact/references/grid-commands.md)
- [DCA bot commands](artifact/references/dca-commands.md)
- [Smart Portfolio commands](artifact/references/smart-portfolio-commands.md)
- [Cross-skill workflows](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and trading-bot status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses identify live or demo mode; CLI results can be requested as JSON.]

## Skill Version(s):

1.4.9 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
