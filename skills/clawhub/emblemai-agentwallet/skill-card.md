## Description: <br>
Connect to EmblemVault and manage crypto wallets via Emblem AI - Agent Hustle across Solana, Ethereum, Base, BSC, Polygon, Hedera, and Bitcoin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[genecyber](https://clawhub.ai/user/genecyber) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to the Emblem Agent Wallet CLI for wallet address lookup, balance checks, portfolio review, token swaps, transfers, and other blockchain wallet interactions that require user-controlled credentials and approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent high-impact crypto wallet abilities, including transfers, swaps, signing, and DeFi actions. <br>
Mitigation: Use a dedicated wallet with limited funds and require explicit human review and approval before any transaction, signing, order placement, or DeFi operation. <br>
Risk: The EMBLEM_PASSWORD and files under ~/.emblemai can control wallet access. <br>
Mitigation: Protect EMBLEM_PASSWORD and ~/.emblemai, avoid logging credentials, prefer browser auth for interactive use, and secure any automation environment that stores credentials. <br>
Risk: The evidence says the noninteractive transaction-approval boundary is not fully demonstrated. <br>
Mitigation: Do not allow unattended agent-mode transfers, swaps, signing, or DeFi actions unless the approval behavior has been independently verified. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/genecyber/skills/emblemai-agentwallet) <br>
- [EmblemVault homepage](https://emblemvault.dev) <br>
- [npm package @emblemvault/agentwallet](https://www.npmjs.com/package/@emblemvault/agentwallet) <br>
- [Agent Hustle](https://agenthustle.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with CLI commands and wallet-operation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route requests through the emblemai CLI and return Hustle AI responses; complex wallet or trading queries may take up to two minutes.] <br>

## Skill Version(s): <br>
3.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
