## Description: <br>
Self-custody Ethereum agent wallet that runs locally as an MCP-over-stdio container, keeps private keys in a local volume, reads wallet context, balances and DeFi positions, previews transactions, executes console-gated on-chain sends, and signs plaintext messages without console approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rustok](https://clawhub.ai/user/rustok) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to a local self-custody Ethereum wallet for balance and DeFi position reads, transaction previews, human-approved on-chain transactions, and plaintext message signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects an agent workflow to a real self-custody crypto wallet with broad wallet authority and no hard-coded spending limits. <br>
Mitigation: Only fund the wallet with amounts the user is willing to expose to the agent workflow, restrict RUSTOK_MCP_CAPABILITIES where possible, and preview transaction details before any execution request. <br>
Risk: The installer uses a remote shell download path and should be reviewed before execution. <br>
Mitigation: Prefer the documented download-inspect-run path and review the installer before running it. <br>
Risk: Plaintext message signing is not separately approved in the console. <br>
Mitigation: Treat sign_message as unprotected and avoid connecting the wallet to agents the user would not trust to sign messages. <br>
Risk: Secrets, seed phrases, PINs, and console approval can leak if run through an agent-visible shell. <br>
Mitigation: Run init and approval console steps only in a separate user-controlled terminal, use Podman secrets or Docker password files, and never place keyring passwords in MCP config or shell history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rustok/skills/rustok-wallet-tui) <br>
- [Rustok MCP repository](https://github.com/rustok-org/mcp) <br>
- [Rustok install guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md) <br>
- [Rustok installer script](https://raw.githubusercontent.com/rustok-org/mcp/wallet-tui-v0.8.2/scripts/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration snippets, and wallet-operation instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP wallet tool usage for wallet context, balances, positions, transaction preview, transaction execution status, and message signing.] <br>

## Skill Version(s): <br>
0.8.2 (source: server release metadata, SKILL.md frontmatter, claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
