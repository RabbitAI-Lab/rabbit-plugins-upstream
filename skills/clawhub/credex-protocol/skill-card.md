## Description: <br>
Access unsecured credit lines for AI agents on the Arc Network using the Credex Protocol for borrowing USDC, repaying debt, providing liquidity, and managing cross-chain USDC via Circle Bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capgoblin](https://clawhub.ai/user/capgoblin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to run Credex borrower and liquidity-provider workflows on Arc Network, including status checks, borrowing, repayment, deposits, withdrawals, and USDC bridging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a raw wallet private key for DeFi transaction signing, creating exposure to irreversible financial actions. <br>
Mitigation: Use a dedicated low-value or testnet wallet and manually approve each borrow, repay, approval, deposit, withdrawal, or bridge operation before execution. <br>
Risk: Misconfigured pool contracts, RPC endpoints, or agent service URLs can direct actions to unintended services or contracts. <br>
Mitigation: Verify CREDEX_POOL_ADDRESS, RPC_URL, and CREDEX_AGENT_URL against trusted release information before running commands. <br>
Risk: Borrowing, repayment, liquidity, and bridge operations can change wallet balances or debt positions. <br>
Mitigation: Check status, balances, available credit, pool liquidity, and transaction amounts before submitting any write command. <br>


## Reference(s): <br>
- [Credex Protocol Contract Reference](references/contracts.md) <br>
- [Credex Protocol ClawHub Skill Page](https://clawhub.ai/capgoblin/skills/credex-protocol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [JSON command output with markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may submit on-chain transactions and return transaction hashes, balances, debt, credit, bridge status, or error objects.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; package.json is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
