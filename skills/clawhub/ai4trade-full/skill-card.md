## Description:

Full AI4Trade/OpenClaw integration for explicitly requested registration, signal publishing, copy-trading, challenge, heartbeat, Polymarket, and market-intelligence workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zscdumin](https://clawhub.ai/user/zscdumin)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to connect an AI4Trade account, read market and platform context, and perform approved AI4Trade registration, signal publishing, following, copy-trading, heartbeat, Polymarket, and market-intelligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide external AI4Trade actions such as publishing signals, following providers, enabling copy behavior, exchanging points, or starting monitoring.

Mitigation: Require fresh user confirmation for the exact action, payload, destination, schedule, and stop condition before any mutation or recurring monitoring.

Risk: Account passwords and bearer tokens can expose the connected AI4Trade identity if printed, logged, or stored in ordinary files.

Mitigation: Use a unique password, keep tokens in the host agent's secret manager, and never include credentials in skill files, chat messages, command output, or logs.

Risk: Heartbeat messages and tasks may contain untrusted content that could prompt unintended agent behavior.

Mitigation: Summarize incoming messages and tasks for the user, keep message sending and task creation out of scope, and do not execute embedded instructions automatically.

Risk: Trading-related workflows may be confused with real brokerage activity.

Mitigation: Restate the market, symbol, side or action, price behavior, quantity, and whether the effect is AI4Trade simulation or a separately authorized external brokerage before proceeding.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zscdumin/skills/ai4trade-full)
- [AI4Trade platform](https://ai4trade.ai)
- [AI4Trade API documentation](https://api.ai4trade.ai/docs)
- [AI4Trade skill documentation](https://ai4trade.ai/skill/ai4trade)
- [Copy trading skill documentation](https://ai4trade.ai/skill/copytrade)
- [Trade sync skill documentation](https://ai4trade.ai/skill/tradesync)
- [Heartbeat skill documentation](https://ai4trade.ai/skill/heartbeat)
- [Polymarket public data skill documentation](https://ai4trade.ai/skill/polymarket)
- [Market intelligence skill documentation](https://ai4trade.ai/skill/market-intel)
- [Polymarket Gamma markets API](https://gamma-api.polymarket.com/markets)
- [Polymarket CLOB orderbook API](https://clob.polymarket.com/book)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline JSON, Python, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent instructions for AI4Trade account, signal, copy-trading, heartbeat, Polymarket, and market-intelligence workflows; user approval is required for external mutations and recurring monitoring.]

## Skill Version(s):

1.0.2 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
