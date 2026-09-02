## Description:

Ava lets coding agents manage DeFi lending under human-defined mandates, using session tokens, two-phase previews, and receipts with chain proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kamalbuilds](https://clawhub.ai/user/kamalbuilds)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use Ava to let a coding agent prepare and execute DeFi lending actions within human-set capital mandates. The skill is intended for live USDC lending on Base through a two-phase preview and execution flow, while copilot commands are labeled testnet-only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live financial actions can be triggered through Ava's lending flow.

Mitigation: Review each preview yourself and execute only after explicit human confirmation of the returned previewHash.

Risk: A local bearer token authorizes financial actions.

Mitigation: Keep AVA_TOKEN private, rely on the 0600 state file behavior, and avoid printing or sharing the token.

Risk: The generic call command can invoke MCP tools directly.

Mitigation: Avoid the generic call command unless the user knows exactly which Ava MCP tool and arguments are being invoked.

Risk: Mainnet execution paths can be enabled intentionally.

Mitigation: Do not set AVA_ENABLE_LIVE=true unless mainnet execution is deliberate and approved.

## Reference(s):

- [ClawHub Ava Skill](https://clawhub.ai/kamalbuilds/skills/ava)
- [Ava Homepage](https://getava.xyz)
- [Ava MCP Endpoint](https://www.getava.xyz/mcp)
- [Artifact README](README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, MCP tool names, and receipt interpretation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live-money execution is framed as a previewHash confirmation flow; CLI and MCP responses are JSON.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact package.json reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
