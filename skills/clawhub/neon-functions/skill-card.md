## Description:

Guides developers in building and deploying long-running Node.js HTTP functions alongside their Neon database branches, including APIs, streaming agents, real-time servers, and scheduled or storage-triggered workloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to design, deploy, and secure Neon Functions for database-backed APIs, agents, WebSocket and SSE services, MCP servers, webhooks, and function triggers.

### Deployment Geography for Use:

Neon Functions is available in AWS us-east-2, us-east-1, eu-central-1, and ap-southeast-1 regions; confirm the project's region before deployment.

## Known Risks and Mitigations:

Risk: A copied agent example could expose an unauthenticated public model and database endpoint.

Mitigation: Authenticate public Functions before model, database, MCP, WebSocket, or SSE work, and review examples before deployment.

Risk: An authenticated caller could access another user's database records if queries are not scoped.

Mitigation: Scope every database query to the verified user.

Risk: Browser stream tokens or observability traces may expose sensitive user data.

Mitigation: Use very short-lived URL tokens or cookies for browser streams and explicitly assess what Sentry or Mastra telemetry receives.

## Reference(s):

- [Neon Functions on ClawHub](https://clawhub.ai/andrelandgraf/skills/neon-functions)
- [Neon Functions overview](https://neon.com/docs/compute/functions/overview.md)
- [Neon Functions deployment](https://neon.com/docs/compute/functions/deploy.md)
- [Neon Functions authentication](https://neon.com/docs/compute/functions/authentication.md)
- [Production hardening guidance](artifact/references/production-hardening.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapt examples and verify authentication before deployment.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
