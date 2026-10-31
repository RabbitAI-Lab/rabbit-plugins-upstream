## Description:

Use to run supervised autopilot cycles under a bounded, revocable session grant: intents, policy checks, approvals, receipts. Execution stays preview-gated.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to coordinate FarmDash agent sessions, plan and review DeFi intents, and track approvals and receipts. Transaction execution requires user signing or a separately scoped grant and current domain readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DeFi trading can lose money, and a paid tier does not grant execution authority.

Mitigation: Before enabling trading, review the signed grant's assets, actions, spending limits, expiry, and revocation process; check live domain status.

Risk: Exposed session tokens or signing keys could compromise an agent's delegated operation.

Mitigation: Keep session tokens private and signing keys in the local agent runtime.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash agent integration documentation](https://www.farmdash.one/docs)
- [Live agent capability status](https://www.farmdash.one/api/v1/agent/status)
- [Security and authority boundaries](https://www.farmdash.one/security)
- [FarmDash OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP discovery manifest](https://www.farmdash.one/.well-known/mcp.json)
- [Canonical Autonomous Operator skill manual](https://www.farmdash.one/openclaw-skills/farmdash-autonomous-operator/SKILL.md)

## Skill Output:

**Output Type(s):** [Structured data, Guidance, Execution and status records]

**Output Format:** [JSON tool requests and structured responses, with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-scoped; may include intent, approval, authority, readiness, and receipt data.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
