## Description:

Mert Sniper scans near-expiry Polymarket markets, filters for strongly-skewed 60/40+ splits, and prepares bounded dry-run or live trades with documented limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and agent operators use this skill to scan near-expiry Polymarket markets, review bounded dry-run opportunities, and optionally execute live trades after configuring Simmer API and wallet credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mode can place real, irreversible orders and redeem positions using wallet credentials.

Mitigation: Test in dry-run or paper mode first, understand the --live behavior, and provide wallet credentials only after confirming the intended trade direction and limits.

Risk: Platform tunable defaults and ranges may not match the documented safeguards for position size, expiry window, and split threshold.

Mitigation: Review and adjust ClawHub tunables before running live so they align with the documented max bet, expiry window, minimum split, and trade-count limits.

Risk: Thin or unavailable order books can make near-expiry execution unreliable.

Mitigation: Keep safeguards enabled, retain the order-book depth gate, and skip markets when book data cannot be fetched or depth is below the configured minimum.

Risk: Default strategy parameters are not validated as a profitable trading edge.

Mitigation: Run extended paper-mode trials and use conservative sizing before increasing trade limits or enabling live execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-mert-sniper)
- [Publisher profile](https://clawhub.ai/user/simmer)
- [Strategy source thread](https://x.com/mert/status/2020216613279060433)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Simmer V2 migration guide](https://docs.simmer.markets/v2-migration)
- [Simmer API base](https://api.simmer.markets)
- [Polymarket CLOB API](https://clob.polymarket.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration values, and Python command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run is the default; live mode can place real Polymarket orders when --live and credentials are provided.]

## Skill Version(s):

1.3.5 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
