## Description: <br>
The Flip Publish helps agents operate and inspect a Solana devnet coin-flip game where players enter with 1 USDC, submit 14 heads-or-tails predictions, and claim the jackpot if all predictions match. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maurodelazeri](https://clawhub.ai/user/maurodelazeri) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to query game state, enter a devnet USDC coin-flip game, check tickets, execute flips, and claim or administer on-chain outcomes through Node and Solana commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read wallet keypair files and sign devnet transactions for enter, claim, withdraw-fees, and close-game-v1 operations. <br>
Mitigation: Use only a dedicated Solana devnet wallet, keep keypair files private, and review each transaction before approving commands. <br>
Risk: The setup instructions include a curl-piped Solana installer command. <br>
Mitigation: Verify the Solana installer source and contents before running the installation command. <br>
Risk: The security verdict is suspicious because value-moving and admin operations have incomplete warnings. <br>
Mitigation: Treat the release as requiring human review before installation or operation, and avoid mainnet or valuable wallets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/maurodelazeri/skills/the-flip-publish) <br>
- [Source Repository](https://github.com/maurodelazeri/the-flip-publish) <br>
- [Game Dashboard](https://the-flip.vercel.app) <br>
- [Solana Devnet Program](https://explorer.solana.com/address/7rSMKhD3ve2NcR4qdYK5xcbMHfGtEjTgoKCS5Mgx9ECX?cluster=devnet) <br>
- [Game State API](https://the-flip.vercel.app/api/game) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and Solana devnet wallet context; transaction commands may sign devnet value-moving or admin operations.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
