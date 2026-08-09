## Description: <br>
Neon Functions guides agents to define, run locally, deploy, and manage long-running Node.js HTTP functions on Neon branches with database-adjacent compute and automatic DATABASE_URL injection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build Neon Functions for APIs, long-running AI agents, WebSocket or SSE services, webhooks, bots, MCP servers, and database-backed request/response workloads. It helps produce deployable TypeScript/Node.js handlers, Neon CLI commands, neon.ts configuration, and security-aware implementation guidance. <br>

### Deployment Geography for Use: <br>
United States (Neon Functions public beta is described as available only in us-east-2). <br>

## Known Risks and Mitigations: <br>
Risk: Copyable examples can expose public Neon Function URLs backed by a database. <br>
Mitigation: Require authentication before database, MCP, WebSocket, SSE, or agent work, and scope every database action to the authenticated user or tenant. <br>
Risk: Telemetry integrations can send sensitive request, database, or agent data to third-party services. <br>
Mitigation: Sanitize telemetry before sending it to Sentry or Mastra, gate observability credentials by environment, and avoid logging secrets or user data. <br>
Risk: Broad trigger phrases can cause the skill to be applied to unrelated backend or hosting tasks. <br>
Mitigation: Use the skill only when the user specifically intends to build on Neon Functions or Neon Compute, and verify the Neon project meets the documented public beta constraints. <br>


## Reference(s): <br>
- [AI SDK agents on Neon Functions](references/ai-sdk.md) <br>
- [Hono WebSocket helper on Neon Functions](references/hono-websockets.md) <br>
- [Mastra agents with Mastra Studio observability](references/mastra-studio.md) <br>
- [MCP servers on Neon Functions](references/mcp.md) <br>
- [Sentry error monitoring on Neon Functions](references/sentry.md) <br>
- [Server-sent events (SSE) on Neon Functions](references/sse.md) <br>
- [Neon Functions overview](https://neon.com/docs/compute/functions/overview.md) <br>
- [Neon Functions get started](https://neon.com/docs/compute/functions/get-started.md) <br>
- [Neon Functions deploy](https://neon.com/docs/compute/functions/deploy.md) <br>
- [Neon Functions environment variables](https://neon.com/docs/compute/functions/environment-variables.md) <br>
- [Neon Functions neon.ts reference](https://neon.com/docs/compute/functions/reference/neon-ts.md) <br>
- [Neon Functions runtime limits](https://neon.com/docs/compute/functions/reference/runtime-limits.md) <br>
- [Neon Functions preview access](https://neon.com/docs/compute/functions/preview-access.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline TypeScript, JSON, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include deployment URLs, Neon CLI commands, neon.ts configuration, integration patterns, and security notes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
