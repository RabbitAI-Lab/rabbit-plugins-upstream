## Description: <br>
Create and manage agentic wallets with Privy for autonomous onchain transactions, wallet creation, policy management, and transaction execution on Ethereum, Solana, and other chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tedim52](https://clawhub.ai/user/tedim52) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to guide agents through Privy server wallet setup, policy creation, wallet management, and guarded transaction execution for autonomous onchain workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through operations that move real funds or sign value-bearing transactions. <br>
Mitigation: Use a dedicated Privy app with limited funds, start on testnets or low-value wallets, and require human review for any value-bearing transaction or signature. <br>
Risk: Compromised or exposed Privy credentials could allow unauthorized wallet operations. <br>
Mitigation: Keep PRIVY_APP_SECRET out of source control and chats; use environment variables or a secrets manager. <br>
Risk: Overly broad wallet policies could permit unintended transfers or contract interactions. <br>
Mitigation: Configure strict spending limits, chain restrictions, and allowlists before creating or using wallets. <br>
Risk: Prompt injection or external content could attempt to trigger unauthorized transactions or remove policy guardrails. <br>
Mitigation: Accept transaction requests only from direct user intent, validate recipient, amount, and chain, and require explicit confirmation before policy or rule deletion. <br>


## Reference(s): <br>
- [Security Guide](references/security.md) <br>
- [Privy Setup](references/setup.md) <br>
- [Wallets](references/wallets.md) <br>
- [Policies](references/policies.md) <br>
- [Transactions](references/transactions.md) <br>
- [Privy Server Wallets Guide](https://docs.privy.io/guide/server-wallets) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes user-confirmation checkpoints, policy constraints, and transaction validation guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
