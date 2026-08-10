## Description:

Self-custody Ethereum agent wallet that runs locally over MCP, keeps private keys in a local container volume, reads wallet balances and DeFi positions, previews transactions, signs messages, and can submit on-chain transactions with human console gating or user-confirmed autonomous mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to give an agent a local self-custody Ethereum wallet for wallet context, balances, DeFi positions, transaction previews, gated on-chain sends, execution status checks, and message signing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent operate a real self-custody Ethereum wallet with funds at risk and no hard-coded spending limits.

Mitigation: Use it only for funds you can afford to risk, prefer supervised mode, and restrict capabilities and allowed chains where possible.

Risk: Autonomous mode can send transactions without per-transaction approval after the user confirms that mode in the separate console.

Mitigation: Use supervised mode unless autonomous sending is intentional, and review transaction previews before execution.

Risk: Message signing is not console-gated and can return signatures without the separate approval window.

Mitigation: Connect the wallet only to agents trusted to sign messages, and treat sign-in or off-chain order messages as sensitive.

Risk: Wallet initialization, approval PIN entry, or keyring password handling through an agent shell can expose secrets to the agent context or shell history.

Mitigation: Run wallet initialization and the approval console only in the user's own terminal, never paste seed phrases or PINs into chat, and prefer Podman secrets for password delivery.

Risk: An agent with shell or container exec access can reach sensitive wallet surfaces outside the intended approval flow.

Mitigation: Do not give the agent shell or docker exec access to the wallet container, and keep approval operations in a separate user-controlled terminal.

## Reference(s):

- [Rustok ClawHub skill page](https://clawhub.ai/rustok/skills/wallet)
- [Rustok MCP homepage](https://github.com/rustok-org/mcp)
- [Rustok caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)
- [Rustok install guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transaction preview summaries, approval instructions, execution status guidance, and MCP configuration snippets.]

## Skill Version(s):

0.9.3 (source: server release, SKILL.md frontmatter, claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
