## Description:

Provides read-only Hyperliquid funding screens, spot-hedgeability checks, and settled-print history through free or paid market-data calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thearkoftech](https://clawhub.ai/user/thearkoftech)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and analysts use this skill to screen Hyperliquid funding opportunities and inspect historical funding prints before making their own decisions; it does not execute trades or hold funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid market-data calls can spend USDC through an external MCP/x402 service.

Mitigation: Approve each route and exact amount, validate the payment challenge, and use a low-balance wallet with a cumulative budget.

Risk: Remote requests could expose wallet secrets or unrelated confidential data.

Mitigation: Never send private keys, trading capital, or unrelated confidential context to the service.

Risk: Funding rates are not realized returns, and current live-position and legacy deposit claims conflict with verification.

Mitigation: Treat returns and operator status as unverified; do not send funds or execute trades based on this screen alone.

## Reference(s):

- [Carry Intel release on ClawHub](https://clawhub.ai/thearkoftech/skills/carry-intel)
- [Carry Intel MCP service](https://devbox.tail873466.ts.net:10000/mcp)
- [Carry Console MCP App](https://devbox.tail873466.ts.net:10000/mcp/carry-console)
- [Historical rate reports (not verified returns)](https://github.com/TheArkofTech/hl-carry-public)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Market-data summaries and structured funding-screen results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free sample and paid read-only calls; requires curl and node for the documented workflow.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
