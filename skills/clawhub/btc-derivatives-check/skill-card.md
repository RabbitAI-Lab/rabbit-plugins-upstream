## Description:

Before a Bitcoin trade, check the derivatives picture across exchanges - funding and basis, open interest, long/short positioning, recent liquidations and where the large order-book walls are. Live data from AgentReeve; free samples, live data per request over x402 (USDC on Base).

This skill is ready for commercial/non-commercial use.

## Publisher:

[shakeelamjid](https://clawhub.ai/user/shakeelamjid)

### License/Terms of Use:

MIT-0

## Use Case:

People assessing a possible Bitcoin trade can use this skill to review funding and basis, positioning, liquidations, and large order-book levels across exchanges. It summarizes market conditions without recommending trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rated the skill suspicious because it may make paid data requests costing up to $0.25 per task without asking first.

Mitigation: Require user approval before any paid request, verify the quoted recipient, Base network, and USDC asset, and keep the total at or below $0.25 unless the user approves more.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/shakeelamjid/agentreeve-skills/tree/main/btc-derivatives-check)
- [BTC Derivatives Check on ClawHub](https://clawhub.ai/shakeelamjid/skills/btc-derivatives-check)
- [AgentReeve BTC derivatives data](https://agentreeve.com/api/v1/btc/derivatives)
- [AgentReeve BTC positioning data](https://agentreeve.com/api/v1/btc/positioning?hours=24)
- [AgentReeve BTC liquidations data](https://agentreeve.com/api/v1/btc/liquidations?minutes=60)
- [AgentReeve BTC order-book walls data](https://agentreeve.com/api/v1/btc/walls?hours=24)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown market summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observational market data; no trade recommendations; reports errors or unavailable fresh data rather than estimating values.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
