## Description:

Ava is an OpenClaw and HTTP MCP finance runtime that lets coding agents work under human-defined capital mandates with testnet default behavior, fail-closed live execution, and receipts for provable outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kamalbuilds](https://clawhub.ai/user/kamalbuilds)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use Ava to create sessions, wallets, mandates, quotes, approvals, portfolio checks, and automation workflows for agent-managed capital under explicit human limits. It is intended for finance workflows where the agent must request confirmation before capital-moving execution and return receipts for what it can prove.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ava can support capital-moving finance workflows when live execution is deliberately enabled.

Mitigation: Keep testnet defaults unless live behavior is intentional, review every quote or mandate, and require explicit human approval before execution.

Risk: Session tokens, local state, agent credentials, and signing keys can authorize sensitive finance actions if exposed.

Mitigation: Keep AVA_TOKEN, the Ava state file, agent credentials, and signing keys private; use key files or environment variables rather than passing raw keys as command arguments.

Risk: A model or operator could overstate execution status or mistake testnet behavior for a live fill.

Mitigation: Rely on Ava receipts and returned venue order IDs or transaction signatures, and treat missing live confirmation as a failed or testnet-only outcome.

## Reference(s):

- [Ava homepage](https://getava.xyz)
- [ClawHub Ava skill](https://clawhub.ai/kamalbuilds/skills/ava)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown instructions with shell commands, JSON configuration, and MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce finance workflow guidance, API/MCP call examples, local CLI commands, and receipt-oriented execution summaries.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact package.json reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
