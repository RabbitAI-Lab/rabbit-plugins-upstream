## Description: <br>
$1 USDC entry. Pick 20 predictions. All 20 coins flip at once each round. Match the first 14 to win the entire jackpot. Live on Solana devnet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maurodelazeri](https://clawhub.ai/user/maurodelazeri) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use THE FLIP to query a Solana devnet coin-flip game, enter 20 H/T predictions with devnet USDC, trigger rounds, inspect tickets, and claim winnings when eligible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Transaction commands can use a local Solana wallet key and interact with a live devnet program. <br>
Mitigation: Use a fresh devnet-only wallet and never use a wallet that holds real funds or controls production programs. <br>
Risk: Operator fee withdrawal and game closure paths are present alongside normal gameplay commands. <br>
Mitigation: Review demo commands before running them and separate player workflows from authority-only operator actions. <br>
Risk: Setup instructions include remote installation and dependency installation steps. <br>
Mitigation: Prefer pinned dependencies and safer manual installation steps over blindly running remote install scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maurodelazeri/skills/the-flip) <br>
- [ClawHub metadata homepage](https://github.com/maurodelazeri/the-flip-publish) <br>
- [THE FLIP dashboard and API](https://the-flip.vercel.app) <br>
- [Solana devnet program](https://explorer.solana.com/address/7rSMKhD3ve2NcR4qdYK5xcbMHfGtEjTgoKCS5Mgx9ECX?cluster=devnet) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a devnet-only Solana wallet for transaction commands.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
