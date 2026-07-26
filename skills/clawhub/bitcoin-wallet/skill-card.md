## Description: <br>
Self-custodial Bitcoin and Lightning wallet for AI agents that can check balances, receive payments, prepare sends, execute confirmed sends, and manage wallet operations through Breez SDK Spark. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robertclarkson](https://clawhub.ai/user/robertclarkson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate a self-custodial Bitcoin and Lightning wallet, including checking balances, generating payment requests, preparing sends with fees, and sending only after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent authority over a self-custodial Bitcoin wallet with real funds. <br>
Mitigation: Use testnet or a low-balance wallet first, and manually verify every recipient, amount, network, and fee before approving a send. <br>
Risk: The skill exposes wallet recovery data through the wallet backup workflow when explicitly requested. <br>
Mitigation: Do not request or display the mnemonic in chat unless disclosure is intentional and the environment is trusted. <br>
Risk: Installation depends on mutable external wallet code. <br>
Mitigation: Review or pin the external BreezClaw repository before running npm install. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robertclarkson/skills/bitcoin-wallet) <br>
- [Breez SDK](https://breez.technology/sdk/) <br>
- [BreezClaw repository](https://github.com/onesandzeros-nz/BreezClaw) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration, and wallet operation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the BreezClaw plugin and a Breez API key; wallet sends follow a two-step prepare and explicit-confirmation flow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
