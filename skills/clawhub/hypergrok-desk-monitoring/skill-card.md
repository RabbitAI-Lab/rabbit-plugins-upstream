## Description:

HyperGrok Desk Monitoring helps agents prepare read-only trading-desk briefs, account watches, market checks, and alerts without placing or changing trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-desk operators use this skill to ask an agent for market and account briefings, scheduled checks, and read-only watch guidance between trades. The skill is intended for monitoring and alerting, not trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watches may read sensitive account and market data and write local logs or briefs.

Mitigation: Confirm data sources, alert destinations, routine schedules, and log locations before enabling watches.

Risk: Monitoring alerts could be mistaken for trade instructions.

Mitigation: Keep alerts limited to sourced facts, thresholds, UTC timestamps, and proposal identifiers; route any action through the desk proposal lifecycle.

Risk: Too many or too-frequent watches can hit rate limits and reduce monitoring reliability.

Mitigation: Use a small number of supervised watches, prefer WebSocket subscriptions where appropriate, and keep polling intervals within the documented 5-15 second range.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-monitoring)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code paths, tables, and example brief text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only monitoring guidance; no exchange order placement or account changes.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
