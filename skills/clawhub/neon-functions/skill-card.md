## Description:

Guides developers in building, deploying, and operating long-running Node.js HTTP functions alongside Neon branches for APIs, agents, streaming, webhooks, and triggers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and deploy long-running HTTP backends near their Neon database, including APIs, streaming agents, WebSocket or SSE services, webhooks, MCP servers, and scheduled or storage-triggered functions.

### Deployment Geography for Use:

North America, Europe, and Asia Pacific (AWS us-east-1, us-east-2, eu-central-1, and ap-southeast-1)

## Known Risks and Mitigations:

Risk: The optional Mastra setup can deploy application code and the selected environment file to another cloud service.

Mitigation: Review or skip the Mastra setup before running it, and check the code and environment file being deployed.

Risk: Authentication parameters in stream URLs could be exposed through logs.

Mitigation: Use narrowly scoped stream tickets and redact authentication parameters from logs.

Risk: The todo example may expose records without checking user verification or whether a todo is open.

Mitigation: Add verified-user and open-status filters to the todo example.

Risk: Private uploads or optional telemetry and quota integrations may be configured unsafely.

Mitigation: Keep private uploads out of public buckets and review optional telemetry and quota providers before enabling them.

## Reference(s):

- [Neon Functions overview](https://neon.com/docs/compute/functions/overview.md)
- [Neon Functions authentication](https://neon.com/docs/compute/functions/authentication.md)
- [Neon Function Triggers](https://neon.com/docs/compute/functions/triggers/overview.md)
- [Mastra observability exporters](https://mastra.ai/docs/observability/tracing/exporters/cloud)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript and JavaScript snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
