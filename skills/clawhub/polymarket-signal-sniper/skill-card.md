## Description:

Snipe Polymarket opportunities from your own signal sources. Monitors RSS feeds with Trading Agent-grade safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor configured RSS feeds, match news signals to Polymarket markets, review safeguard context, and optionally execute small prediction-market trades through the Simmer SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that non-live modes still invoke an account redemption method.

Mitigation: Review the redemption path before installation with real funds, keep live trading disabled during evaluation, and require explicit opt-in before relying on dry-run or scan-only as non-mutating modes.

Risk: RSS fetching has weak network scoping.

Mitigation: Configure only trusted RSS feed URLs and review feed sources before enabling automated recurring scans.

Risk: Automated on-chain trading can create irreversible losses from strategy errors, stale signals, market changes, or misconfiguration.

Mitigation: Use paper mode first, run with a dedicated low-balance account, set conservative position limits, and check market resolution criteria and safeguard warnings before live execution.

Risk: Wallet private keys may be needed for external-wallet live trading.

Mitigation: Avoid putting private keys in chat or shell history; use environment secrets and prefer a dedicated wallet with limited funds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-signal-sniper)
- [Simmer API](https://api.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Polymarket V2 migration guide](https://docs.simmer.markets/v2-migration)
- [Disclaimer](DISCLAIMER.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON status output for managed automation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query RSS feeds and Simmer APIs; live mode can submit trades when explicitly enabled and credentials are configured.]

## Skill Version(s):

1.5.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
