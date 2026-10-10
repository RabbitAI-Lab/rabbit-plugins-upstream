## Description:

Guides read-only market and account monitoring with desk briefings, scheduled checks, and alerts for changing or unavailable data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Traders and desk operators use this skill to request sourced account and market briefings, schedule read-only checks, and receive alerts when conditions change or data becomes unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stale or interrupted market feeds can make a missed condition look like an all-clear.

Mitigation: Set a freshness limit for each watch; alert on failed, missing, or stale reads and record the last good update.

Risk: Account monitoring or alerts could be sent to an unintended destination, or mistaken for authorization to trade.

Mitigation: Confirm the account source, alert destination, schedule, and log location before enabling watches; keep watches read-only and require a separate approval process for trades.

## Reference(s):

- [HyperGrok Desk Monitoring on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-monitoring)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown briefings, alerts, and monitoring guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source and UTC timestamps, data-freshness checks, and read-only watch boundaries]

## Skill Version(s):

1.5.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
