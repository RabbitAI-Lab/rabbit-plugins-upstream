## Description: <br>
Self-custody Ethereum agent wallet. Runs entirely on the user's machine as one Docker image (MCP over stdio); private keys never leave it. Read wallet context, balances and DeFi positions (Aave v3, ERC-4626); preview, execute and sign. The user assumes all risk for funds on the agent wallet - there are no hard-coded spending limits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[temrjan](https://clawhub.ai/user/temrjan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to a local self-custody Ethereum wallet for reading wallet context, balances, and DeFi positions, previewing and executing ETH sends, and signing messages. It is intended for users who understand the risk of giving an agent access to real funds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move real Ethereum funds and sign wallet messages. <br>
Mitigation: Fund the wallet conservatively, preview every send before execution, and require explicit user approval for transactions and signatures. <br>
Risk: A compromised keyring password, recovery phrase, or Docker volume can expose wallet funds. <br>
Mitigation: Keep the recovery phrase offline, store the keyring password only in a private 0600 env-file, and never place secrets in MCP configuration or shell history. <br>
Risk: A network-exposed wallet gateway can broaden access to wallet operations. <br>
Mitigation: Use the default stdio setup when possible; if network exposure is required, use strong authentication and isolation. <br>
Risk: Full wallet capabilities allow both read and execution actions by default. <br>
Mitigation: Use restricted capabilities such as read_wallet for read-only sessions when transaction execution is not needed. <br>


## Reference(s): <br>
- [Rustok MCP GitHub repository](https://github.com/rustok-org/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/temrjan/skills/rustok-wallet) <br>
- [Publisher profile](https://clawhub.ai/user/temrjan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces MCP wallet guidance and command/configuration examples; wallet tool responses may include balances, previews, risk levels, transaction hashes, and signatures.] <br>

## Skill Version(s): <br>
0.4.5 (source: frontmatter, claw.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
