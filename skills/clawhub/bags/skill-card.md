## Description: <br>
Bags - The Solana launchpad for humans and AI agents. Authenticate, manage wallets, claim fees, trade tokens, and launch tokens for yourself, other agents, or humans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ramyodev](https://clawhub.ai/user/ramyodev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agent operators use Bags to connect Moltbook-authenticated agents to Bags APIs for Solana wallet management, fee claiming, token trading, heartbeat checks, and token launches with configurable fee sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live Solana funds, wallet private keys, JWTs, and API keys. <br>
Mitigation: Use a low-value wallet, store credentials separately from private keys, clear exported private keys after signing, and rotate credentials immediately if exposure is suspected. <br>
Risk: The skill can prepare, sign, and submit token launches, fee claims, and swap transactions. <br>
Mitigation: Review every transaction, token mint, amount, fee share, slippage setting, and recipient before signing or submitting. <br>
Risk: The heartbeat workflow silently rewrites local skill files from remote Bags URLs. <br>
Mitigation: Disable or manually gate automatic skill updates and review updated files before allowing agents to run them. <br>


## Reference(s): <br>
- [Bags homepage](https://bags.fm) <br>
- [Bags API documentation](https://docs.bags.fm) <br>
- [Bags Public API base](https://public-api-v2.bags.fm/api/v1) <br>
- [Bags Agent API base](https://public-api-v2.bags.fm/api/v1/agent) <br>
- [ClawHub skill page](https://clawhub.ai/ramyodev/skills/bags) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes API request examples, local credential file guidance, and transaction signing workflows.] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter, artifact/skill.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
