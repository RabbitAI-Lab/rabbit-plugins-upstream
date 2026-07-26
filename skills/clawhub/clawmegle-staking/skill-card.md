## Description: <br>
Stake $CLAWMEGLE tokens to earn dual rewards (ETH + CLAWMEGLE) from Clanker LP fees and manage staking positions through Bankr API or direct wallet transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tedkaczynski-the-bot](https://clawhub.ai/user/tedkaczynski-the-bot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent developers use this skill to manage CLAWMEGLE staking positions on Base, including staking, checking balances and rewards, claiming rewards, unstaking, and depositing rewards when authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit live blockchain transactions for staking, claiming, unstaking, and reward deposits. <br>
Mitigation: Use a dedicated low-balance wallet and independently verify the Base chain, contract address, token address, transaction value, and calldata before approval. <br>
Risk: Credential handling relies on Bankr API keys or raw private keys for transaction-capable workflows. <br>
Mitigation: Protect or rotate the Bankr API key, prefer Bankr or other scoped wallet infrastructure, and avoid raw private keys when possible. <br>
Risk: Heartbeat automation and reward deposit flows can trigger recurring or value-bearing transactions. <br>
Mitigation: Do not enable automation or reward deposits unless explicit human approval rules exist for every transaction type and threshold. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tedkaczynski-the-bot/skills/clawmegle-staking) <br>
- [Clawmegle homepage](https://clawmegle.xyz) <br>
- [Contract ABI & Examples](references/contract.md) <br>
- [Bankr Transaction Format](references/bankr-format.md) <br>
- [Contract on Basescan](https://basescan.org/address/0x56e687aE55c892cd66018779c416066bc2F5fCf4) <br>
- [CLAWMEGLE Token on Basescan](https://basescan.org/token/0x94fa5D6774eaC21a391Aced58086CCE241d3507c) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and transaction parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces command guidance for Bankr API or direct wallet flows; some commands can submit live Base-chain transactions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
