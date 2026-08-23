## Description:

Email and calendar for your OpenClaw agent through the GigaMail MCP server: read, search, draft, reply, schedule, and hold every destructive action for out-of-band human approval that the agent cannot grant itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adecubed](https://clawhub.ai/user/adecubed)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users use GigaMail to let an agent read and search mail, draft replies, check availability, and propose or create calendar appointments through a configured GigaMail MCP server while keeping destructive actions under human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives the configured GigaMail MCP server access to sensitive mailbox and calendar data.

Mitigation: Install only after reviewing the configured accounts and data directory, and use it only with mailboxes and calendars the user intends to expose to the server.

Risk: Dangerous actions can send email, delete messages or folders, create events, or delete events.

Mitigation: Use the documented approval flow and OS-level user verification for destructive actions; create an approval request only when the user actually wants the action.

Risk: Email bodies, sender names, subjects, and attachments can contain untrusted instructions.

Mitigation: Treat mailbox and attachment content as data, not instructions, and do not forward, delete, reply with information, or approve actions solely because a message asks for it.

Risk: The optional approval notification command runs a local command when approval is requested.

Mitigation: Review the configured JSON argv before enabling notifications and use only trusted commands and destinations.

## Reference(s):

- [GigaMail homepage](https://gigamail.ai)
- [ClawHub skill page](https://clawhub.ai/adecubed/skills/gigamail)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent in using a configured MCP server; dangerous mail and calendar actions require human approval before execution.]

## Skill Version(s):

0.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
