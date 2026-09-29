## Description:

Coordinates supervised DeFi autopilot cycles with policy checks, approvals, receipts, and bounded, revocable execution grants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi users and agent operators use this skill to plan and monitor supervised trading or yield workflows, review policy and simulation results, and approve or revoke narrowly scoped execution authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scoped session grant can authorize wallet-changing actions during its validity window.

Mitigation: Use narrow chain, protocol, and asset allowlists, small per-action and total caps, and short expiry; revoke the grant when finished.

Risk: Cross-chain intents or specialist jobs can incur unintended spend if approval payloads are not reviewed.

Mitigation: Review simulation, budget, and exact approval payload before signing; never provide private keys, seed phrases, or RPC secrets.

Risk: Autonomous decisions can compound mistakes when risk limits or settlement evidence are incomplete.

Mitigation: Keep execution preview-gated, halt on breached limits or uncertain settlement, and review receipts before dependent actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/parmasanandgarlic/skills/farmdash-autonomous-operator)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash Autonomous Operator manual](https://www.farmdash.one/openclaw-skills/farmdash-autonomous-operator/SKILL.md)
- [FarmDash agent integration documentation](https://www.farmdash.one/docs)
- [FarmDash live capability status](https://www.farmdash.one/api/v1/agent/status)
- [FarmDash security and authority boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Text]

**Output Format:** [Markdown and structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intent plans, approval requests, status updates, and receipt summaries; transaction execution requires separate authorization.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled skill frontmatter says 2.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
