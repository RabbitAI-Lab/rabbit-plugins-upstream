## Description: <br>
Participate in Bread Protocol - a meme coin launchpad for AI agents on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrissorrell](https://clawhub.ai/user/chrissorrell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to understand Bread Protocol participation on Base, including proposing tokens, backing proposals, claiming tokens, and claiming refunds. It provides workflow guidance, contract addresses, and code-oriented transaction examples for agent-assisted participation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides real wallet approvals and Base mainnet transactions that could spend ETH, BREAD, or create lasting token allowances. <br>
Mitigation: Use a dedicated low-balance wallet, require manual signing, verify chain ID 8453, contract addresses, approval amounts, ETH values, gas costs, and revoke allowances when finished. <br>
Risk: Private keys or main-wallet credentials could be exposed if pasted into an agent workflow. <br>
Mitigation: Do not paste a main-wallet private key into an agent; prefer wallet flows that keep signing outside the agent. <br>
Risk: Incorrect proposal IDs, contract addresses, or expected outcomes could lead to failed transactions or asset loss. <br>
Mitigation: Independently verify getbread.fun, proposal IDs, contract addresses, fees, refund rules, and claim status before submitting any transaction. <br>


## Reference(s): <br>
- [Bread Protocol Website](https://getbread.fun) <br>
- [Contract Reference](references/contracts.md) <br>
- [Workflows](references/workflows.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/chrissorrell/skills/bread-protocal) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown with JavaScript code blocks and contract parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Base mainnet contract addresses, transaction examples, approval guidance, and workflow checks.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
