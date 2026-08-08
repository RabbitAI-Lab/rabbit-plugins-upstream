## Description:

Self-custody Ethereum agent wallet that runs locally as a containerized MCP server, keeps private keys on the user's machine, reads wallet context, balances, and DeFi positions, previews transactions, executes on-chain sends only after separate console approval, and signs messages without console gating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to give an agent access to a local self-custody Ethereum wallet for reading wallet context, checking balances and DeFi positions, previewing transactions, executing human-approved on-chain sends, and signing messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose an agent-facing wallet to real funds.

Mitigation: Install only when comfortable with that risk, keep only intended funds in the wallet, and use lower-trust agents with read-only or preview-only capabilities.

Risk: Seed phrases, PINs, and keyring passwords can leak if entered through agent-controlled terminals.

Mitigation: Create the wallet and approve transactions only in a separate user-controlled terminal, and keep recovery material offline.

Risk: Message signing is not separately console-approved.

Mitigation: Treat sign_message as sensitive and connect the wallet only to agents trusted to sign ordinary plaintext messages.

Risk: On-chain transactions have no hard-coded spending limits or budgets.

Mitigation: Preview every transaction, review decoded effects and simulation results, and require separate console approval before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rustok/skills/rustok-wallet-tui)
- [Rustok MCP homepage](https://github.com/rustok-org/mcp)
- [Rustok caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)
- [Rustok install guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing wallet guidance may include transaction previews, wallet state summaries, approval instructions, and status polling guidance.]

## Skill Version(s):

0.8.5 (source: frontmatter, claw.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
