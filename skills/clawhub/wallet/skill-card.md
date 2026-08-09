## Description:

Rustok Agentic Wallet is a self-custody Ethereum agent wallet that runs locally as an MCP-over-stdio container for wallet context, DeFi positions, transaction previews, on-chain sends, and message signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a local Ethereum wallet for reading balances and positions, previewing transactions, and submitting wallet actions under the user's chosen approval posture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent access to a real self-custody Ethereum wallet with high-impact money-moving capability.

Mitigation: Install only when comfortable with agent wallet access, fund the wallet with limited amounts, preview transactions before execution, and use capability narrowing such as read-only or preview-only where possible.

Risk: Autonomous mode can allow unattended spending after the user confirms that posture.

Mitigation: Keep autonomous mode disabled unless unattended spending is intentionally accepted and understood.

Risk: Seed phrases, approval PINs, and keyring passwords can be exposed if setup or approval flows run through an agent session.

Mitigation: Run wallet initialization and the approval console only in the user's own terminal, prefer Podman secrets over Docker password-file fallback, and never paste seed or PIN values into agent chat.

## Reference(s):

- [Rustok ClawHub Skill Page](https://clawhub.ai/rustok/skills/wallet)
- [Rustok MCP Repository](https://github.com/rustok-org/mcp)
- [Rustok Caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)
- [Rustok Install Guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include transaction preview summaries, wallet-status explanations, capability errors, and setup commands for Podman or Docker.]

## Skill Version(s):

0.9.2 (source: server release evidence, claw.json, and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
