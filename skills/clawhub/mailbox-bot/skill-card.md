## Description:

Enables AI agents to send postal mail and manage an assigned mailbox through a postal mail API and MCP server, with human approval for sensitive inbound actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arbengine](https://clawhub.ai/user/arbengine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let agents prepare and send letters, certified mail, postcards and batches, and to search inbound mail or propose scans, forwarding and disposal for human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live sends and mailbox actions can incur charges.

Mitigation: Start with sandbox keys, review dry-run prices, and require human approval for sensitive actions or spending.

Risk: Mail content and credentials may contain sensitive information.

Mitigation: Keep keys out of prompts and logs, use agent-scoped keys with minimum required scopes, and require human approval for legal notices, scans, forwarding or disposal.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/arbengine/skills/mailbox-bot)
- [mailbox.bot API documentation](https://mailbox.bot/api-docs)
- [MCP installation guide](https://mailbox.bot/mcp-install)
- [OpenAPI specification](https://mailbox.bot/openapi.json)
- [Sandbox guidance](https://mailbox.bot/api-docs#sandbox)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides quoted-cost previews and approval guidance; physical forwarding requires an eligible US destination.]

## Skill Version(s):

5.3.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
