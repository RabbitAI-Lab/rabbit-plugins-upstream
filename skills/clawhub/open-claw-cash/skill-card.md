## Description:

Helps agents inspect and operate OpenClawCash-managed EVM and Solana wallets, including balances, transfers, swaps, checkout escrow, and supported venue actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentwalletapi](https://clawhub.ai/user/agentwalletapi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users with OpenClawCash wallets use this skill to let an agent inspect balances and policies, prepare quotes, and perform authorized wallet, checkout, and venue actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-initiated transfers, swaps, approvals, escrow actions, and venue orders can move funds or create financial exposure.

Mitigation: Prefer approval for each write; review the recipient, amount, network, fees, and wallet policy before execution. Use delegated approval only with strict dashboard whitelists and spending limits.

Risk: Exposed API keys or wallet export passphrases can compromise wallet access.

Mitigation: Keep credentials secret, avoid exposing passphrases in command history or logs, and never commit the local credential file.

Risk: The preferred MCP integration runs a third-party package.

Mitigation: Verify the pinned package before running it.

## Reference(s):

- [OpenClawCash skill release](https://clawhub.ai/agentwalletapi/skills/open-claw-cash)
- [OpenClawCash API endpoint reference](references/api-endpoints.md)
- [OpenClawCash service](https://openclawcash.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries and authorized wallet operations; transfers and other fund-moving actions can have irreversible financial effects.]

## Skill Version(s):

1.29.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
