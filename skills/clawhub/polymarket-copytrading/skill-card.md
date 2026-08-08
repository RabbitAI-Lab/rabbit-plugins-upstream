## Description:

Mirror positions from top Polymarket traders. Polling mode (free) for portfolio-style copying, Reactor mode (Pro) for event-driven real-time mirroring via Simmer's on-chain signal infrastructure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect and mirror selected Polymarket trader wallets, either through dry-run or paper-trading workflows or through live automated trading with configured caps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reactor mode can place automated live trades, and polling dry-run behavior does not apply to reactor execution.

Mitigation: Use paper trading or polling dry-run before enabling reactor, and configure conservative max size and daily cap values before running reactor cron or loop mode.

Risk: Live self-custody Polymarket trading may require a wallet private key in the environment.

Mitigation: Avoid setting WALLET_PRIVATE_KEY unless live self-custody trading is intended; prefer paper trading or managed-wallet workflows when validating the strategy.

Risk: Copying selected wallets can create financial losses from signal lag, market movement, wallet-selection errors, or misconfiguration.

Mitigation: Validate wallet choices in paper mode, keep per-position and per-run caps low at first, and review reported skipped trades, conflicts, and positions after each run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-copytrading)
- [Skill disclaimer](DISCLAIMER.md)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Simmer v2 migration guide](https://docs.simmer.markets/v2-migration)
- [predicting.top](https://predicting.top)
- [alphawhale.trade](https://alphawhale.trade)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger Simmer SDK/API calls and trading actions when the user runs the provided commands with live trading enabled.]

## Skill Version(s):

1.12.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
