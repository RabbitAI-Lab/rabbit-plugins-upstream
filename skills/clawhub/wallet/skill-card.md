## Description:

Rustok Agentic Wallet lets agents use a local self-custody Ethereum wallet to read wallet context, balances, and DeFi positions, preview transactions, execute approved on-chain sends, and sign messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rustok](https://clawhub.ai/user/rustok)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to connect an agent to a local Ethereum wallet for wallet reads, transaction previews, approved sends, and message signing while keeping custody on the user's machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wallet can move real funds without per-transaction approval after autonomous mode is enabled and has no built-in spending cap.

Mitigation: Use supervised or read-only capabilities for normal agent use, and enable autonomous mode only when unattended transfers are an intentional, accepted risk.

Risk: Secrets or approval authority can leak if the seed phrase, PIN, keyring password, or approval console are exposed through an agent chat or shell.

Mitigation: Enter wallet secrets and use the approval console only in a separate user-controlled terminal; prefer Podman secrets for password delivery.

Risk: Message signing is not console-gated, so a trusted session can return signatures without the separate approval flow.

Mitigation: Use message signing only with agents the user trusts for signatures, and restrict wallet capabilities when read-only or preview-only access is sufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rustok/skills/wallet)
- [Rustok MCP homepage](https://github.com/rustok-org/mcp)
- [Rustok caveats](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md)
- [Rustok install guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include wallet operation guidance, transaction preview summaries, status polling instructions, and setup commands; live wallet data depends on the connected wallet tools.]

## Skill Version(s):

0.9.4 (source: frontmatter, claw.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
