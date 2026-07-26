## Description: <br>
Solana wallet operations: create wallets, check balances, send SOL or SPL tokens, swap via Jupiter, and launch tokens on Pump.fun. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spendit-ai](https://clawhub.ai/user/spendit-ai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to manage Solana wallets, inspect balances, transfer SOL or SPL tokens, request and execute Jupiter swaps, and launch Pump.fun tokens from command-line scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent real Solana spending authority. <br>
Mitigation: Use only a new low-balance wallet, avoid valuable private keys, and manually verify every recipient, amount, token mint, swap route, fee, and network before broadcasting. <br>
Risk: Mainnet wallet actions, swaps, and token launches can be irreversible. <br>
Mitigation: Test on devnet first where supported and keep autonomous execution disabled until each transaction has been reviewed. <br>
Risk: Vanity-address token guidance could be mistaken for authenticity or endorsement. <br>
Mitigation: Do not use vanity addresses to imply legitimacy, endorsement, or safety. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/spendit-ai/skills/solana-skills) <br>
- [Jupiter Ultra API endpoint](https://api.jup.ag/ultra/v1) <br>
- [Jupiter API portal](https://portal.jup.ag/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with bash commands and command-line text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOLANA_PRIVATE_KEY for wallet operations and JUPITER_API_KEY for swaps; commands may broadcast Solana transactions.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
