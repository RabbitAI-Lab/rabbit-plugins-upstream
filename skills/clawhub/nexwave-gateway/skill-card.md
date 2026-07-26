## Description: <br>
Unified crosschain USDC balance via Circle Gateway and Circle Programmable Wallets for depositing, checking balances, and transferring USDC across supported testnet chains without raw private keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[botmechanic](https://clawhub.ai/user/botmechanic) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to set up Circle Gateway workflows, inspect a unified USDC balance, deposit USDC, and run crosschain transfer scripts through Circle Programmable Wallets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create wallets and submit deposit or transfer transactions that move USDC on supported chains. <br>
Mitigation: Use testnet credentials first, restrict Circle API keys to the minimum needed permissions, and require explicit review of chain, amount, recipient, fees, and irreversibility before running fund-moving scripts. <br>
Risk: The security review verdict is suspicious because the skill lacks strong in-skill confirmation or risk controls for fund-moving operations. <br>
Mitigation: Do not allow unattended agent execution of deposit or transfer scripts; review the scripts and runtime output before each transaction. <br>


## Reference(s): <br>
- [Nexwave Gateway on ClawHub](https://clawhub.ai/botmechanic/skills/nexwave-gateway) <br>
- [Circle Gateway Docs](https://developers.circle.com/gateway) <br>
- [Circle Programmable Wallets](https://developers.circle.com/wallets) <br>
- [Gateway Quickstart](https://developers.circle.com/gateway/quickstarts/unified-balance-evm) <br>
- [Circle Wallet Skill](https://clawhub.ai/eltontay/circle-wallet) <br>
- [Arc Testnet Docs](https://docs.arc.network) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JavaScript and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Circle API credentials and Node.js dependencies; transaction scripts produce console output and blockchain transaction hashes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
