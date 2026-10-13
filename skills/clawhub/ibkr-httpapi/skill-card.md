## Description:

Helps agents use a user-deployed Interactive Brokers HTTP API to retrieve market and account data, run technical analysis, and manage orders with explicit confirmation for account-changing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders with an existing ibkr-httpapi deployment use the skill to inspect Interactive Brokers market data, positions, and orders, run technical analysis, and request confirmed trading actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order placement, cancellation, and option exercise can affect a real brokerage account.

Mitigation: Prefer paper trading while testing; before each account-changing action, show the account, base URL, symbol, side, quantity, order type, and price and require explicit confirmation.

Risk: An exposed service without an API token can allow unauthorized access and trading.

Mitigation: Set a strong API_TOKEN before network exposure and keep the service on localhost or behind strong authentication.

Risk: A mistaken or untrusted API endpoint can receive account data or trading instructions.

Mitigation: Use only an ibkr-httpapi endpoint the user operates or trusts, and verify the target base URL and account before approving a trading action.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/ibkr-httpapi)
- [ibkr-httpapi project documentation](https://github.com/psyb0t/ibkr-httpapi)
- [Setup and configuration](references/setup.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with curl and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results and proposed trading actions; account-changing requests require explicit per-action confirmation.]

## Skill Version(s):

0.5.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
