## Description: <br>
Rustok Wallet TUI gives agents a local self-custody Ethereum wallet for reading balances and DeFi positions, previewing transactions, signing messages, and parking on-chain sends for separate human console approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rustok](https://clawhub.ai/user/rustok) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect a local Ethereum wallet, review balances and DeFi positions, preview transactions, and request human-approved on-chain execution. It is intended for self-custody workflows where the user accepts financial risk and keeps secrets outside the agent chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can participate in workflows involving a self-custody wallet and real funds. <br>
Mitigation: Use it only when comfortable with agent-mediated wallet access, keep funds limited to the risk you accept, and review transaction previews before approval. <br>
Risk: Seed phrases, PINs, and keyring passwords can leak if entered through the agent chat or an agent-visible shell. <br>
Mitigation: Run wallet initialization and approval console steps only in a separate user-controlled terminal, and prefer Podman secrets or file-based secret mounts for keyring passwords. <br>
Risk: Plaintext message signing is not separately approved in the console. <br>
Mitigation: Treat message signing as an active signing capability and restrict sessions to read-only capabilities when signing or transaction execution is not needed. <br>
Risk: An agent with shell or container access may reach sensitive wallet surfaces outside the intended chat flow. <br>
Mitigation: Do not grant untrusted agents shell or docker exec access to the wallet container, and use capability restrictions such as read_wallet for lower-risk sessions. <br>


## Reference(s): <br>
- [Rustok MCP repository](https://github.com/rustok-org/mcp) <br>
- [Rustok installation guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce wallet status summaries, transaction previews, execution polling guidance, and setup instructions; on-chain sends require separate user approval.] <br>

## Skill Version(s): <br>
0.8.3 (source: SKILL.md frontmatter, claw.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
