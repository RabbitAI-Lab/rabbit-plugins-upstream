## Description: <br>
Self-custody Ethereum agent wallet that runs locally in Docker or Podman, keeps private keys on the user's machine, and lets an agent read wallet context, balances and DeFi positions, preview and execute sends, and sign plain messages or EIP-712 typed data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[temrjan](https://clawhub.ai/user/temrjan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use Rustok Wallet to give an agent a local self-custody Ethereum wallet for checking balances and positions, previewing transactions, executing ETH sends, and producing wallet signatures. It is intended for users who deliberately accept the operational risk of agent-controlled real funds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent can control a funded self-custody wallet and may move real funds when execution capabilities are enabled. <br>
Mitigation: Keep only limited funds in the wallet, prefer read-only or preview-only capabilities unless execution is needed, and require a fresh transaction preview before execution. <br>
Risk: Network exposure of the HTTP gateway can expand signing risk if API-key handling or access control is misconfigured. <br>
Mitigation: Keep the gateway loopback-only by default and expose it over a network only when the operator intentionally configures an API key and accepts the risk. <br>
Risk: Keyring password exposure can compromise access to the local wallet. <br>
Mitigation: Use Podman secrets or a 0600 password file, and do not place the keyring password inline in shell history or MCP configuration. <br>


## Reference(s): <br>
- [Rustok wallet homepage](https://github.com/rustok-org/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet setup, MCP configuration, capability guidance, transaction preview guidance, and operational cautions for self-custody use.] <br>

## Skill Version(s): <br>
0.5.0 (source: SKILL.md frontmatter, claw.json, evidence release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
