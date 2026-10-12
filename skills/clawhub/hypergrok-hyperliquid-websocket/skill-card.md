## Description:

Provides read-only Hyperliquid WebSocket monitoring guidance and Python, TypeScript, and raw JSON examples for live market data and account activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-desk operators use this skill to monitor live Hyperliquid prices, books, fills, and order updates and to receive alerts without polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A background watcher may persist raw account trading activity in local logs without a retention policy.

Mitigation: Restrict log permissions, decide which account data to record, and rotate or delete logs on a defined schedule.

Risk: A persistent watcher may continue running or silently stop reporting after a connection failure.

Mitigation: Document how to stop the watcher and remove saved logs; monitor its heartbeat and reconcile account activity after gaps.

## Reference(s):

- [HyperGrok Hyperliquid Websocket on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-websocket)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Python, TypeScript, JSON, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only monitoring; examples default to testnet.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
