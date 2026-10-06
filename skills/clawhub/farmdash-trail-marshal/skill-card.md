## Description:

Coordinates named DeFi workflow recipes, checks required skills, and records guarded runs without executing wallet transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi users and their agents use this skill to choose named workflow recipes, assess missing prerequisites and confirmation requirements, and track supervised runs. Wallet-changing steps require separately installed execution skills and explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A workflow may suggest financially risky DeFi actions or rely on stale market data.

Mitigation: Refresh research and review costs and risks before any handoff; require separate user confirmation for every wallet-changing action.

Risk: Sharing wallet secrets or credentials with an untrusted endpoint could compromise assets or account access.

Mitigation: Never provide private keys, seed phrases, signed transactions, or raw wallet secrets; use optional API keys and session tokens only with trusted FarmDash endpoints.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash agent integration documentation](https://www.farmdash.one/docs)
- [FarmDash OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP discovery manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash Trail Marshal skill manual](https://www.farmdash.one/openclaw-skills/farmdash-trail-marshal/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Workflow plans, Workflow status]

**Output Format:** [Text and structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Catalog entries, prerequisite and confirmation checks, and guarded run records; no wallet execution.]

## Skill Version(s):

0.1.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
