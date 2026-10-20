## Description:

Guides agents using a user-operated Interactive Brokers HTTP bridge to retrieve market and account data, run technical analysis, and submit or cancel orders with explicit per-action confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers with an existing ibkr-httpapi deployment use this skill to inspect brokerage data and prepare explicitly approved account actions through the bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order placement, option exercise, and cancellation can affect a real brokerage account, including canceling every open order.

Mitigation: Start with a paper account and require explicit confirmation of the base URL, account, instrument, side, quantity, price, and affected orders before each mutating action.

Risk: An unauthenticated or publicly reachable bridge could expose account data and trading controls.

Mitigation: Set a strong API token and bind the bridge to localhost or protect it with strong access controls; never expose an unauthenticated instance.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/ibkr-httpapi)
- [Setup guide](references/setup.md)
- [ib_async library](https://github.com/ib-api-reloaded/ib_async)
- [wickworks indicators](https://github.com/psyb0t/docker-wickworks#available-indicators)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with curl and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running ibkr-httpapi bridge and the IBKR_HTTPAPI_URL setting; Docker and curl are listed as prerequisites.]

## Skill Version(s):

0.5.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
