## Description:

Snipe Polymarket opportunities from your own signal sources. Monitors RSS feeds with Trading Agent-grade safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to monitor configured RSS feeds, match signals to Polymarket markets, review safeguards, and optionally execute capped trades through the Simmer SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted RSS feed content can influence automated trading decisions.

Mitigation: Configure only trusted feeds, use keywords and explicit market IDs, inspect matched articles, and start with scan-only or dry-run mode.

Risk: Live mode can place real on-chain trades that cannot be recalled.

Mitigation: Keep --live disabled until the strategy is reviewed, use low trade limits, cap position size, and confirm wallet configuration before funding live runs.

Risk: Default trading parameters are not validated as a profitable strategy.

Mitigation: Run paper mode for an extended period, raise confidence thresholds when appropriate, and scale only after independent performance review.

Risk: Some fast-resolving markets may resolve before monitoring can exit a position.

Mitigation: Avoid short-deadline markets when possible and rely on conservative position sizing as the primary control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-signal-sniper)
- [Publisher profile](https://clawhub.ai/user/simmer)
- [Simmer API](https://api.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard)
- [Polymarket V2 migration guide](https://docs.simmer.markets/v2-migration)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit JSON status summaries when running in managed automation mode.]

## Skill Version(s):

1.5.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
