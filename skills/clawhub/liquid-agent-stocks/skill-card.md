## Description:

Helps agents guide users through buying, holding, rebalancing, selling, and transferring a Coinbase tokenized NVDA, AAPL, META, and GOOGL basket on Base through the Liquid Agent API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leftychris13](https://clawhub.ai/user/leftychris13)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare Liquid Agent API calls and wallet-signing steps for a self-custodied tokenized-stock vault on Base. It is intended for transaction preparation and portfolio operations, not general investment advice or traditional brokerage activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad stock-investing requests may be routed into irreversible on-chain transactions.

Mitigation: Require explicit user confirmation for buy, sell, rebalance, send, and paid x402 actions, including the amount, vault or recipient address, fees, and chain before signing or broadcasting.

Risk: Users may treat basket signals or transaction flows as general investment advice.

Mitigation: Keep responses scoped to Liquid Agent tokenized-stock vault operations and state that signals are aggregated data, not investment advice.

Risk: Wallet or chain mistakes can cause failed transactions or loss of funds.

Mitigation: Never request private keys or seed phrases; confirm Base mainnet, USDC amount formatting, ETH for gas, and transaction receipts before proceeding to the next step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leftychris13/skills/liquid-agent-stocks)
- [Liquid Agent API](https://api.liquidagent.ai)
- [Liquid Agent guide](https://api.liquidagent.ai/v1/guide)
- [Liquid Agent OpenAPI specification](https://api.liquidagent.ai/openapi.json)
- [Liquid Agent llms.txt](https://api.liquidagent.ai/llms.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown guidance with curl examples and JSON API request and response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl; prepares unsigned transaction payloads that the user signs with their own Base wallet.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
