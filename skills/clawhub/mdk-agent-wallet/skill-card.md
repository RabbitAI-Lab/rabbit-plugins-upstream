## Description: <br>
Self-custodial Bitcoin Lightning wallet for AI agents that can send and receive bitcoin payments, check balances, generate invoices, and manage wallet operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[satbot-mdk](https://clawhub.ai/user/satbot-mdk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent users use this skill to give an AI agent a self-custodial Bitcoin Lightning wallet for agent-to-agent payments, invoices, balance checks, and wallet management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a funded self-custodial Bitcoin Lightning wallet and initiate payments. <br>
Mitigation: Use a small, task-limited balance and require explicit human approval for every send or payment action. <br>
Risk: The wallet mnemonic is stored at ~/.mdk-wallet/config.json and controls real funds. <br>
Mitigation: Back up the mnemonic, restrict file permissions, and protect or remove the config file when the wallet is not needed. <br>
Risk: The skill installs and runs an npm wallet package with a local daemon and outbound Lightning connections. <br>
Mitigation: Inspect the @moneydevkit/agent-wallet package and source before use, pin the package version for production, and confirm the daemon/network behavior is expected. <br>


## Reference(s): <br>
- [MoneyDevKit agent-wallet documentation](https://docs.moneydevkit.com/agent-wallet) <br>
- [@moneydevkit/agent-wallet npm package](https://www.npmjs.com/package/@moneydevkit/agent-wallet) <br>
- [Repository URL declared by the skill](https://github.com/moneydevkit/mdk-checkout) <br>
- [ClawHub skill page](https://clawhub.ai/satbot-mdk/skills/mdk-agent-wallet) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with bash commands; wallet CLI responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npx; wallet config, mnemonic, and payment history persist under ~/.mdk-wallet/.] <br>

## Skill Version(s): <br>
0.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
