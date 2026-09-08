## Description:

Buy, hold, rebalance and sell a basket of Coinbase tokenized US stocks (NVDA, AAPL, META, GOOGL) on Base from $1 through the free Liquid Agent API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leftychris13](https://clawhub.ai/user/leftychris13)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to guide Base-mainnet tokenized stock basket actions, including vault discovery, buy, rebalance, redeem, send, and optional paid signal or publish calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad investing requests may lead to irreversible on-chain financial transactions.

Mitigation: Confirm the exact product, USD amount, wallet, transaction target, and Base-mainnet network before any signing or broadcast.

Risk: Sell, send, rebalance, gas sponsorship, publish, and paid x402 signal calls can move funds, change positions, or incur charges.

Mitigation: Require explicit user approval for each of those actions before invoking the API or submitting a transaction.

Risk: Portfolio signals could be mistaken for investment advice.

Mitigation: Present signals as aggregated data only and avoid framing them as personalized financial advice.

## Reference(s):

- [Liquid Agent API](https://api.liquidagent.ai)
- [Liquid Agent Guide](https://api.liquidagent.ai/v1/guide)
- [Liquid Agent OpenAPI Spec](https://api.liquidagent.ai/openapi.json)
- [Liquid Agent llms.txt](https://api.liquidagent.ai/llms.txt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP API requests and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl; API write operations return unsigned Base-mainnet transaction payloads for local wallet signing.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
