## Description:

Mirror positions from top Polymarket traders. Polling mode (free) for portfolio-style copying, Reactor mode (Pro) for event-driven real-time mirroring via Simmer's on-chain signal infrastructure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect, simulate, and optionally mirror Polymarket positions from selected trader wallets using polling or real-time Reactor mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute live financial trades unexpectedly.

Mitigation: Review the behavior before installation, start with $SIM or --venue sim, and use a low-balance dedicated wallet before allowing live trading.

Risk: Reactor mode can perform live automated trades.

Mitigation: Avoid Reactor mode unless you explicitly accept live automated trading and have configured conservative caps.

Risk: Simulated signals can route to Polymarket when that is not intended.

Mitigation: Set COPYTRADING_FORCE_SIMMER_VENUE=true when simulated signals should remain on the Simmer venue.

Risk: WALLET_PRIVATE_KEY provides full trading authority.

Mitigation: Treat WALLET_PRIVATE_KEY as a sensitive secret and prefer a dedicated wallet with limited funds.

Risk: Dependency drift can change runtime behavior.

Mitigation: Prefer pinned dependency versions when installing the Simmer SDK and related packages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-copytrading)
- [Simmer API](https://api.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Simmer V2 migration guide](https://docs.simmer.markets/v2-migration)
- [Predicting.top trader leaderboard](https://predicting.top)
- [AlphaWhale trader tools](https://alphawhale.trade)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, environment configuration, and concise trading-status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can place live trades when run with --live or Reactor mode; dry-run and simulated-venue flows are available for testing.]

## Skill Version(s):

1.12.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
