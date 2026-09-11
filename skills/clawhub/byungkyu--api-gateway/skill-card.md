## Description:

Calls third-party APIs through the Maton gateway for apps the user has already connected, including read/list operations, writes, triggers, destinations, and local event handlers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to route agent actions through connected third-party services with Maton-managed credentials. It is suited for querying data, updating service records, managing event triggers, and creating reviewed automations across supported apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad authority across many connected services through Maton-managed credentials.

Mitigation: Install it only when that cross-service access is needed, connect only the minimum apps and scopes, prefer OAuth, and revoke unused connections.

Risk: Functions and local event handlers can run reviewed code with access to connected-app data or account-scoped Maton credentials.

Mitigation: Review function and --exec handler code before use, deploy from narrowly scoped accounts, use DENY_ALL networking unless outbound access is required, and require explicit approval before deployment or unattended execution.

Risk: Triggers and webhook destinations can create persistent forwarding of sensitive meeting, customer, payment, or message data.

Mitigation: Require explicit confirmation for trigger destinations, verify the destination owner and URL, forward only the minimum fields, and delete destinations when no longer needed.

Risk: Write, send, delete, billing, or bulk operations can affect external systems and users.

Mitigation: Default to read/list operations and require explicit confirmation with the target service, resource, payload, and intended effect before high-impact actions.

## Reference(s):

- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [API Gateway skill on ClawHub](https://clawhub.ai/byungkyu/skills/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, API paths, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may propose Maton CLI commands, SDK snippets, API request paths, trigger settings, function configuration, and confirmation prompts for high-impact actions.]

## Skill Version(s):

1.2.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
