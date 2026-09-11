## Description:

Mirror positions from top Polymarket traders. Polling mode (free) for portfolio-style copying, Reactor mode (Pro) for event-driven real-time mirroring via Simmer's on-chain signal infrastructure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External traders and agents use this skill to inspect Polymarket whale positions, paper trade with Simmer, or execute capped copytrading runs. It supports portfolio-style polling and Pro Reactor mode for event-driven mirroring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically execute real-money trades and sells when run live.

Mitigation: Review carefully before installing, test with a dedicated low-balance wallet, and prefer --venue sim or COPYTRADING_FORCE_SIMMER_VENUE=true while validating behavior.

Risk: Default polling should be treated as sell-capable unless whale-exit handling is disabled.

Mitigation: Use --no-whale-exits when buy-only behavior is required, and review rebalance and exit settings before running with live funds.

Risk: Reactor cron can execute automatically and Reactor mode is documented as live execution.

Mitigation: Do not enable Reactor cron until the operator understands its automatic execution model, and use Simmer venue configuration for paper trading first.

Risk: Trading behavior depends on installed dependencies and SDK behavior.

Mitigation: Pin and review dependencies before using live funds, including the required simmer-sdk package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-copytrading)
- [Simmer publisher profile](https://clawhub.ai/user/simmer)
- [Simmer API](https://api.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Polymarket V2 migration guide](https://docs.simmer.markets/v2-migration)
- [predicting.top](https://predicting.top)
- [alphawhale.trade](https://alphawhale.trade)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown status summaries with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run dry-run simulations or live trading commands depending on user flags and venue configuration.]

## Skill Version(s):

1.12.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
