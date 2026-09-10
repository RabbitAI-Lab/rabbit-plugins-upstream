## Description:

Call third-party APIs through the Maton gateway, which injects the credential for an app the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route agent-requested actions through user-connected third-party apps, including read/list calls, writes, connection management, triggers, webhook destinations, and local event handlers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional functions and automation can grant broad account-wide authority.

Mitigation: Review handler code before deployment, prefer read/list operations, keep OAuth scopes narrow, and require explicit confirmation for writes, connections, triggers, destinations, or handlers.

Risk: Webhook destinations and local --exec handlers can forward data or run code persistently.

Mitigation: Review destinations and handlers before enabling them, specify exact connections, delete unneeded automations, and avoid running code that has not been reviewed.

Risk: Functions with broad network access can reach external hosts while using Maton account credentials.

Mitigation: Use DENY_ALL network policy unless outbound access is necessary, and document the required hosts before allowing broader network access.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill Page](https://clawhub.ai/byungkyu/skills/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API call plans, Maton CLI commands, raw HTTP examples, connection guidance, trigger setup, webhook destination configuration, and handler review guidance.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
