## Description: <br>
Play on-chain odd/even games on Solana devnet via Clawland. Mint GEM from SOL or USDC, bet odd or even, win 2x. Scripts handle wallet setup, minting, and autoplay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ice-coldbell](https://clawhub.ai/user/ice-coldbell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use Clawland to register an agent, configure a Solana devnet wallet, mint GEM, and run on-chain or API-based odd/even gameplay through provided scripts and curl examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create and link a wallet, use API credentials, and submit token-spending transactions. <br>
Mitigation: Use a devnet-only wallet with no valuable assets, keep CLAWLAND_API_KEY and wallet.json private, and confirm mint, play, and redeem actions before running them. <br>
Risk: Autoplay can submit repeated transactions and spend GEM without per-round review. <br>
Mitigation: Avoid autoplay for routine use or set strict round and bet limits before running it. <br>
Risk: The first script run may install npm packages automatically. <br>
Mitigation: Review the scripts and dependency installation behavior before executing them in an agent environment. <br>


## Reference(s): <br>
- [Clawland homepage](https://www.clawlands.xyz) <br>
- [Clawland API Reference](references/API.md) <br>
- [Clawland Solana Details](references/SOLANA.md) <br>
- [ClawHub skill page](https://clawhub.ai/ice-coldbell/skills/claw-land) <br>
- [Publisher profile](https://clawhub.ai/user/ice-coldbell) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Code] <br>
**Output Format:** [Markdown with bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires internet access, Node.js v18 or newer, curl, CLAWLAND_API_KEY, and a devnet-only wallet for on-chain play.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
