## Description:

Rustok Wallet gives an agent a self-custody Ethereum wallet running locally in Docker or Podman for reading wallet context, balances, and DeFi positions; previewing and executing sends; and signing messages or EIP-712 typed data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[temrjan](https://clawhub.ai/user/temrjan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a local self-custody Ethereum wallet for live-chain wallet context, DeFi position checks, transaction previews and execution, and signing workflows. It is intended for users who accept real-funds risk and can manage Docker or Podman wallet setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent access can affect real funds because the wallet has broad authority and no hard-coded spending limits.

Mitigation: Use a separate low-balance wallet, restrict `RUSTOK_MCP_CAPABILITIES` to the minimum needed, and review transaction previews before execution.

Risk: Exposing the HTTP gateway over a network can broaden access to signing operations.

Mitigation: Keep the gateway loopback-only unless explicitly needed and protect any `RUSTOK_MCP_API_KEY` used for network exposure.

Risk: EIP-712 typed-data signatures can authorize approvals, permits, or off-chain orders that move funds.

Mitigation: Treat typed-data signing like transaction execution and verify the domain, intent, and spending effects before signing.

Risk: Private key recovery depends on the local wallet volume, keyring password, and one-time recovery phrase backup.

Mitigation: Back up the recovery phrase offline during onboarding and use the documented secret or password-file setup instead of placing passwords in shell history or MCP configuration.

## Reference(s):

- [Rustok MCP homepage](https://github.com/rustok-org/mcp)
- [ClawHub skill page](https://clawhub.ai/temrjan/skills/rustok-wallet)
- [ClawHub publisher profile](https://clawhub.ai/user/temrjan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with shell commands and JSON configuration examples; runtime wallet interactions return structured wallet data, transaction previews, transaction hashes, or signatures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker or Podman, a created wallet volume, an Ethereum RPC URL, and local keyring password handling.]

## Skill Version(s):

0.5.1 (source: SKILL.md frontmatter, claw.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
