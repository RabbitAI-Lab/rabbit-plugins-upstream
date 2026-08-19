## Description:

Rustok Agentic Wallet is a self-custody Ethereum wallet skill that lets an agent read wallet state, preview transactions, and request console-gated on-chain sends while keys stay local.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect an agent to a local Ethereum wallet for balance and DeFi position awareness, transaction previews, and payment workflows. It is suited to users who understand self-custody and want wallet operations mediated through local container tooling and a separate approval console.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be configured so an agent moves real funds without per-transaction approval and without built-in spending limits.

Mitigation: Use supervised or read-only capability settings unless autonomous payments are intentional, and keep only funds the user is prepared to risk in the wallet.

Risk: Agent-controlled shell access or exposed gateway access can undermine the intended wallet approval boundary.

Mitigation: Do not expose the gateway over a network, restrict allowed chains and tokens, and never run the approval console, seed phrase, or PIN through an agent-controlled shell.

## Reference(s):

- [Rustok MCP repository](https://github.com/rustok-org/mcp)
- [Installation guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md)
- [Wallet caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)
- [ClawHub skill page](https://clawhub.ai/rustok/skills/wallet)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet status summaries, transaction preview details, approval guidance, and container setup commands.]

## Skill Version(s):

0.10.0 (source: frontmatter, claw.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
