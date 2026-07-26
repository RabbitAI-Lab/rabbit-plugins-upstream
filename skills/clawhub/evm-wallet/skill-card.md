## Description: <br>
Self-sovereign EVM wallet for AI agents that can create a local wallet, check balances, send ETH or ERC20 tokens, swap tokens, and interact with smart contracts across Base, Ethereum, Polygon, Arbitrum, and Optimism. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[surfer77](https://clawhub.ai/user/surfer77) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill when they want an agent-managed EVM wallet for balance checks, token transfers, swaps, and contract interactions while retaining local key custody. It is intended for workflows where the user manually confirms value-moving actions before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install unpinned remote code that later controls wallet behavior. <br>
Mitigation: Review or pin the GitHub code before use, and rerun review before accepting updates. <br>
Risk: The skill stores a private key locally and can move real crypto funds. <br>
Mitigation: Keep only small amounts in the wallet, protect ~/.evm-wallet.json, and never expose or share the private key. <br>
Risk: Transfers, swaps, and contract writes can send funds to the wrong recipient, chain, token, amount, or contract. <br>
Mitigation: Manually verify every recipient, chain, token, amount, gas estimate, swap quote, and contract write before confirming execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/surfer77/skills/evm-wallet) <br>
- [Project homepage](https://github.com/surfer77/evm-wallet-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require node and git, operate from the installed skill directory, and may create or use ~/.evm-wallet.json for local private-key storage.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
