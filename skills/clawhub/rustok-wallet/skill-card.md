## Description: <br>
Self-custody Ethereum agent wallet that runs locally as a Docker-based MCP server for reading wallet context, balances, DeFi positions, transaction previews, and message signing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[temrjan](https://clawhub.ai/user/temrjan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to a local self-custody Ethereum wallet for wallet inspection, balance and DeFi position review, transaction previews, and approved signing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real funds when configured with signing capability. <br>
Mitigation: Use small balances, restrict capabilities to read-only unless signing is needed, and verify each transaction preview before approval. <br>
Risk: The recovery phrase, keyring password, and wallet environment file protect access to the wallet. <br>
Mitigation: Back up the recovery phrase offline, keep secrets out of MCP configuration and shell history, and store the env file with private file permissions. <br>
Risk: The package relies on an external proprietary Docker image tagged latest. <br>
Mitigation: Install only when an agent-accessible self-custody wallet is intended, and review the image source and operational trust assumptions before use. <br>


## Reference(s): <br>
- [Rustok MCP homepage](https://github.com/rustok-org/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/temrjan/skills/rustok-wallet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker, a local wallet volume, RPC URL configuration, and explicit user review before signing actions.] <br>

## Skill Version(s): <br>
0.4.4 (source: frontmatter, claw.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
