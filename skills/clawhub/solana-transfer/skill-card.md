## Description: <br>
Send SOL or SPL tokens on the Solana blockchain from OpenClaw agents for payments, rewards, or on-chain settlement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vortitron](https://clawhub.ai/user/vortitron) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill when an OpenClaw agent needs to send native SOL or SPL token payments, rewards, or settlement transactions on Solana. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent direct ability to send real Solana funds without built-in approval, recipient allowlists, or spend limits. <br>
Mitigation: Use devnet first, configure a dedicated wallet with limited funds, restrict who can invoke the skill, and add human approval, recipient allowlists, and per-transfer and daily spending caps before mainnet use. <br>
Risk: The skill depends on a local Solana keypair file that controls the configured wallet. <br>
Mitigation: Never use a main wallet keypair, keep the keypair file secret, avoid committing or sharing it, and rotate the wallet if exposure is suspected. <br>


## Reference(s): <br>
- [Solana Transfer on ClawHub](https://clawhub.ai/vortitron/skills/solana-transfer) <br>


## Skill Output: <br>
**Output Type(s):** [json, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON transaction, balance, and address responses; JavaScript API calls; and Markdown usage guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Solana RPC endpoint and a dedicated keypair with funds for the selected network.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
