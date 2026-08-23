## Description:

Self-custody Ethereum agent wallet that runs locally, reads balances and DeFi positions, previews transactions, and can send funds through console approval or confirmed autonomous mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Rustok Agentic Wallet to let an agent inspect an Ethereum wallet, preview transactions, and request on-chain sends through a local self-custody wallet with console-gated approval or deliberately enabled autonomous mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wallet can move real funds without per-transaction approval after autonomous mode is intentionally enabled.

Mitigation: Keep the wallet in read-only or supervised mode unless autonomous spending is deliberate, and fund the agent wallet only with limited amounts.

Risk: Seed phrases, PINs, restore flows, and approval-console actions can leak if handled through an agent chat or shell.

Mitigation: Run seed, PIN, restore, and approval-console commands only in the user's own terminal, never through the agent session.

Risk: Keyring password handling can expose secrets when weaker Docker fallback paths are used.

Mitigation: Prefer Podman secrets and avoid putting passwords in MCP config, shell history, env files, or agent-visible commands.

## Reference(s):

- [Rustok Agentic Wallet on ClawHub](https://clawhub.ai/rustok/skills/wallet)
- [Rustok MCP homepage](https://github.com/rustok-org/mcp)
- [Rustok caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)
- [Rustok install guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet tool calls, transaction preview summaries, and execution status guidance; no fixed output schema.]

## Skill Version(s):

0.11.0 (source: SKILL.md frontmatter, claw.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
