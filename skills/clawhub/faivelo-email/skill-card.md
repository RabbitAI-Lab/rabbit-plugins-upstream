## Description:

Helps agents configure custom-domain email with Faivelo and integrate sending, inbound webhooks, and mailbox access through its SDKs, REST API, and hosted MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ethannschwartz](https://clawhub.ai/user/ethannschwartz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to set up mailboxes on their own domains, send transactional email, handle inbound messages, and connect an agent to an inbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP connection may expose non-email drive files if drive:read is granted.

Mitigation: Grant only the mailbox access and API key scopes needed; omit drive:read unless explicitly required.

Risk: Email, deletion, and DNS actions can affect messages and live mail delivery.

Mitigation: Confirm sending, deletion, and DNS changes with the user before execution, especially changes to existing MX records.

Risk: Running an unpinned CLI may execute a newly published package version.

Mitigation: Prefer a pinned or preinstalled Faivelo CLI version over unpinned npx commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ethannschwartz/skills/faivelo-email)
- [Faivelo documentation for coding agents](https://faivelo.com/docs/developers/coding-agents/)
- [Faivelo API reference](https://faivelo.com/docs/api)
- [REST API guide](references/rest-api.md)
- [MCP server guide](references/mcp.md)
- [Webhook guide](references/webhooks.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize completed email setup when the MCP server is connected.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
