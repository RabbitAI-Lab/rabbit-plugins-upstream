## Description:

Guides developers in building, deploying, and operating long-running Node.js HTTP functions alongside Neon branches, including streaming endpoints and scheduled or storage-triggered work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, run, deploy, and harden Node.js APIs, streaming agents, WebSocket and SSE services, MCP servers, webhooks, and scheduled or storage-triggered jobs next to Neon databases.

### Deployment Geography for Use:

AWS regions us-east-2, us-east-1, eu-central-1, and ap-southeast-1.

## Known Risks and Mitigations:

Risk: Some examples omit per-user data limits, which can expose data across users or allow excessive usage.

Mitigation: Authenticate callers, filter database operations by verified identity, set appropriate per-user limits, and test isolation between users.

Risk: Login tokens in URLs can be exposed through request logs.

Mitigation: Use single-use connection tickets or another suitable authentication method, and redact tokens from URL logs.

## Reference(s):

- [Neon parent skill](https://neon.com/docs/ai/skills/neon/SKILL.md)
- [Neon Functions authentication](https://neon.com/docs/compute/functions/authentication.md)
- [Production hardening](references/production-hardening.md)
- [Function triggers](references/function-triggers.md)
- [MCP servers](references/mcp.md)
- [Server-sent events](references/sse.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and operational guidance for Neon Functions]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
