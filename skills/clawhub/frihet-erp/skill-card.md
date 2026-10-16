## Description:

Guides agents through read-first Frihet ERP tasks using the Frihet MCP, with explicit approval before consequential changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[berthelius](https://clawhub.ai/user/berthelius)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to inspect Frihet ERP records and plan updates while keeping consequential operations subject to explicit human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting without tool restrictions could expose operations that change ERP data.

Mitigation: Apply the documented literal read-only tool allowlist before OAuth authorization; opt into writes individually only when needed.

Risk: A mutating operation may have external effects or proceed without effective host approval.

Mitigation: Check the workspace, scopes, and host approval behavior, and require explicit human confirmation before consequential operations.

Risk: Retrying a write after an uncertain response could duplicate a change.

Mitigation: Re-read the target to reconcile its state and use the operation's idempotency key before retrying.

## Reference(s):

- [Frihet ERP skill on ClawHub](https://clawhub.ai/berthelius/skills/frihet-erp)
- [Frihet agent onboarding contract](https://raw.githubusercontent.com/Frihet-io/frihet-mcp/main/docs/agent-onboarding.json)
- [Frihet MCP endpoint](https://mcp.frihet.io/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first operating guidance with explicit approval for consequential operations.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
