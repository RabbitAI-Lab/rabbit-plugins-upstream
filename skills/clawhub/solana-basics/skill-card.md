## Description: <br>
Interact with Solana through Helius APIs to create and manage wallets, check SOL and token balances, send transactions, prepare Jupiter swaps, and monitor addresses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chattyclaw](https://clawhub.ai/user/chattyclaw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to manage Solana wallets, inspect balances and assets, send SOL or SPL tokens, and prepare Jupiter token swaps through Helius-backed Solana APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move Solana funds through sends and swaps. <br>
Mitigation: Use a test or low-value wallet, require manual approval for every send or swap, and independently verify addresses and amounts before signing. <br>
Risk: Wallet key storage safeguards are too weak for meaningful funds. <br>
Mitigation: Replace the wallet encryption approach before storing valuable assets and limit the skill's authority during review and deployment. <br>
Risk: Helius API keys or wallet activity could be exposed through logs or untrusted webhook endpoints. <br>
Mitigation: Avoid logging secrets or sensitive wallet activity and use trusted endpoints only. <br>


## Reference(s): <br>
- [Solana Skill on ClawHub](https://clawhub.ai/chattyclaw/skills/solana-basics) <br>
- [Publisher Profile](https://clawhub.ai/user/chattyclaw) <br>
- [Helius API Reference](references/helius-api.md) <br>
- [Jupiter Swap Integration](references/jupiter.md) <br>
- [Wallet Security Best Practices](references/security.md) <br>
- [Helius Dashboard Signup](https://dashboard.helius.dev/signup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TypeScript examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include transaction, wallet, API, and security guidance that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
