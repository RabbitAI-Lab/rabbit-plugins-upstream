## Description:

Subscribe to live Hyperliquid data over WebSocket from the desk computer - mids, order book, trades, candles, best bid/offer, and per-account fills, order updates and events - with raw JSON, Python SDK and TypeScript examples, plus how to run a supervised watch that logs to a file and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading desk operators use this skill to monitor Hyperliquid WebSocket streams, configure read-only watch processes, log market and account events, and receive fill or order-update alerts without expensive polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local watch logs can contain trading activity, fills, order updates, timestamps, and account identifiers when account subscriptions are enabled.

Mitigation: Use restricted file permissions, rotate or delete old logs, and avoid logging account streams on shared machines unless that is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-websocket)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline Python, TypeScript, JSON, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only WebSocket monitoring guidance; examples may write local log files when a watch is configured.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
