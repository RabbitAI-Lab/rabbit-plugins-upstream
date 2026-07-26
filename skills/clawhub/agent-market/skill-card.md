## Description: <br>
Interact with the AgentMarket protocol on Base Sepolia to create, trade, provide liquidity, and resolve USDC-settled YES/NO prediction markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[humanjesse](https://clawhub.ai/user/humanjesse) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to inspect AgentMarket prediction markets and submit Base Sepolia transactions for market creation, YES/NO trading, liquidity management, oracle resolution, disputes, arbitration, and emergency withdrawal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit wallet-signed testnet transactions for trades, liquidity changes, bonds, disputes, arbitration, resets, and emergency withdrawals. <br>
Mitigation: Use a dedicated Base Sepolia test wallet with little or no valuable funds and require manual review before transaction-submitting actions. <br>
Risk: Incorrect contract or market addresses can route actions to the wrong on-chain target. <br>
Mitigation: Verify the factory, USDC, market, AMM, and oracle addresses before executing actions. <br>
Risk: Prediction market, liquidity, and oracle actions can create financial or operational loss even on test networks. <br>
Mitigation: Review market questions, deadlines, amounts, oracle state, dispute windows, arbitrator identity, and bond requirements before acting. <br>
Risk: The skill requires a wallet private key in the runtime environment. <br>
Mitigation: Keep the private key scoped to a low-value test wallet and avoid reusing production credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/humanjesse/skills/agent-market) <br>
- [Source code and docs declared by artifact](https://github.com/humanjesse/AgentMarket) <br>
- [Base Sepolia faucet](https://www.coinbase.com/faucets/base-sepolia-faucet) <br>
- [Circle testnet faucet](https://faucet.circle.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Text or JSON responses from TypeScript tool calls, including transaction hashes and market or oracle status.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can submit wallet-signed Base Sepolia transactions when wallet and RPC environment variables are configured.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
