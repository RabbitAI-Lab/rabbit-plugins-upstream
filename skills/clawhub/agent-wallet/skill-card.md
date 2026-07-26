## Description: <br>
The agent's wallet. Use this skill to safely create a wallet the agent can use for transfers, swaps, and any EVM chain transaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[glitch003](https://clawhub.ai/user/glitch003) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to create and operate a smart-account EVM wallet for an agent. The agent can check balances, transfer or swap tokens, and send contract transactions within policies set by the wallet owner. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables agent-controlled crypto wallet actions, and the security summary notes that the default setup can allow unrestricted real fund movement until policies are configured. <br>
Mitigation: Use a testnet or tiny balances first, claim the wallet immediately, set strict address, token, function, and spending policies, require human approval for transactions, and keep the API key private. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/glitch003/skills/agent-wallet) <br>
- [Default Agent Wallet API and frontend](https://safeskill-production.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides wallet creation, API-key use, balance checks, transfers, swaps, arbitrary EVM transactions, and owner policy setup.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
