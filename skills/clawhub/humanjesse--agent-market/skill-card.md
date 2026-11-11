## Description:

Interact with the AgentMarket protocol on Base Sepolia to create, trade, provide liquidity, and resolve USDC-settled YES/NO prediction markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[humanjesse](https://clawhub.ai/user/humanjesse)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to inspect AgentMarket prediction markets, create YES/NO markets, trade positions, provide or remove liquidity, and participate in oracle resolution on Base Sepolia.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit wallet-signed transactions for market creation, trading, liquidity, claims, oracle proposals, disputes, resets, and arbitration.

Mitigation: Use only a dedicated Base Sepolia wallet with limited test funds and manually confirm each write action before execution.

Risk: Buy, sell, and add-liquidity actions use zero as the minimum received amount, which weakens trade-safety controls.

Mitigation: Review market price, expected output, fees, and slippage before using these actions; avoid unattended automation for trading or liquidity changes.

Risk: The skill requires a wallet private key to be configured for write actions.

Mitigation: Never use a reused or production private key; rotate credentials if exposed and keep only limited test funds in the configured wallet.

Risk: Arbitrator automation can finalize disputed outcomes or reset oracle state without separate judgment.

Mitigation: Require a human approval step before arbitrator actions, especially if adding periodic checks to HEARTBEAT.md.

## Reference(s):

- [Agent Market on ClawHub](https://clawhub.ai/humanjesse/skills/agent-market)
- [AgentMarket source code and docs](https://github.com/humanjesse/AgentMarket)
- [Base Sepolia RPC endpoint](https://sepolia.base.org)
- [Base Sepolia faucet](https://www.coinbase.com/faucets/base-sepolia-faucet)
- [Circle faucet](https://faucet.circle.com/)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Markdown-facing text, JSON strings for market lists and checks, and transaction hashes for write actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools query Base Sepolia market state; write tools may submit wallet-signed transactions when a wallet private key is configured.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
