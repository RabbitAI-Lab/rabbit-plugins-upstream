## Description: <br>
Agent Credit lets an agent borrow from Aave via credit delegation, repay debt, and check health status across Aave V2/V3 deployments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaronjmars](https://clawhub.ai/user/aaronjmars) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to give a dedicated agent wallet limited Aave borrowing and repayment capability against a delegator's approved collateral. It is intended for workflows that need on-chain liquidity checks, borrow execution, repayment, and status reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can create real Aave debt against delegated collateral. <br>
Mitigation: Use small per-asset delegation limits, set conservative per-transaction caps, review each borrow or repay action, and revoke delegation when the agent does not need access. <br>
Risk: The configured agent wallet key can authorize on-chain borrow and repayment transactions. <br>
Mitigation: Use a dedicated low-balance agent wallet, avoid plaintext key storage where possible, restrict config file permissions, and never use the delegator's main wallet key. <br>
Risk: Borrowing or market movement can reduce the delegator health factor and create liquidation exposure. <br>
Mitigation: Test on testnet first, keep a conservative minimum health factor, monitor health factor externally, and abort borrowing when safety checks fail. <br>
Risk: A compromised or misdirected agent could borrow beyond the intended workflow. <br>
Mitigation: Keep delegation ceilings narrow, monitor active allowances and debt, and revoke stale delegation by setting each debt token allowance to zero. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaronjmars/skills/agent-credit) <br>
- [Safety Guidelines](safety.md) <br>
- [Aave Deployments Reference](deployments.md) <br>
- [Aave Contract Addresses](contracts.md) <br>
- [Aave V3 Developers Documentation](https://docs.aave.com/developers) <br>
- [Aave Credit Delegation Guide](https://docs.aave.com/developers/guides/credit-delegation) <br>
- [Aave DebtToken Reference](https://docs.aave.com/developers/tokens/debttoken) <br>
- [Aave Address Book](https://github.com/bgd-labs/aave-address-book) <br>
- [Foundry Book](https://book.getfoundry.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash scripts and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces shell-facing instructions and scripts that may perform on-chain read and write operations when configured with an agent wallet key.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
