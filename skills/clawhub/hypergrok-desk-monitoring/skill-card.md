## Description:

Guides read-only trading-desk briefings, account and market checks, and scheduled price, funding, and risk alerts between trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk operators use this skill to request sourced market and account briefings, set up read-only watches, and receive alerts about price, funding, positions, or unavailable data. Watches report conditions but do not place or change orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent watch may monitor unintended markets or account data, or send alerts at unwanted times.

Mitigation: Confirm the market, account scope, schedule, alert destination, and stop condition before starting a watch.

Risk: Stale or failed market reads may be mistaken for a quiet market.

Mitigation: Set a freshness bound and report failed or stale reads as unavailable rather than as a condition that did not fire.

## Reference(s):

- [HyperGrok Desk Monitoring on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-monitoring)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown briefings, alerts, and watch setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Briefings and alerts identify data sources and UTC times; watches are read-only.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
