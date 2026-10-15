## Description:

Guides read-only Hyperliquid WebSocket monitoring of market data and account activity, with Python, TypeScript, and raw connection examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Developers and trading-desk operators use this skill to monitor live Hyperliquid prices, order books, fills, and order events, and to set up read-only alerts without continuous polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Background watch examples can keep a local process running and write logs containing configured account activity.

Mitigation: Review the configured address, supervise the process, and protect or rotate local logs as appropriate.

Risk: A disconnected or stale watch can miss fills and order updates.

Mitigation: Monitor the heartbeat and reconcile account state and fill history after a gap before relying on the watch for risk decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-websocket)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Python, TypeScript, JSON, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only monitoring guidance; watch examples may run continuously and write local logs.]

## Skill Version(s):

1.6.1 (source: ClawHub release; bundled skill metadata says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
