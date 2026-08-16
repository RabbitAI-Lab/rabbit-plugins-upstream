## Description:

Self-custody Ethereum agent wallet that runs locally as an MCP container, keeps private keys on the user's machine, reads wallet and DeFi context, previews transactions, and gates on-chain sends through a separate approval console.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect a local Ethereum wallet, review balances and DeFi positions, preview transactions, and submit on-chain transactions that require explicit approval unless autonomous mode has been confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to a real-money self-custody Ethereum wallet, and transactions can send funds after execution is enabled or autonomous mode is confirmed.

Mitigation: Install only for wallets funded within the user's risk tolerance, prefer read-only or preview-only capabilities until execution is needed, preview every transaction, and avoid autonomous mode unless the wallet holds only funds the user is willing to risk.

Risk: Wallet secrets, seed phrases, keyring passwords, and approval PINs are sensitive local credentials that can be exposed if handled inside the agent session.

Mitigation: Keep seed phrases and PINs out of agent chats, use Podman secrets where possible, and deliver passwords through secret or file-based mechanisms rather than shell history or agent-visible configuration.

Risk: An agent with shell or docker exec access to the wallet container can bypass the intended separation between chat guidance and the wallet approval surface.

Mitigation: Do not give the agent shell or docker exec access to the wallet container, and require approval through the separate console controlled by the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rustok/skills/wallet)
- [Rustok MCP repository](https://github.com/rustok-org/mcp)
- [Rustok installation guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md)
- [Rustok caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose wallet tool calls and transaction review steps; users must keep secrets and approval flows outside the agent session.]

## Skill Version(s):

0.9.8 (source: server release metadata, SKILL.md frontmatter, claw.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
