## Description:

Connects an agent to personal Outlook mail, calendars, contacts, tasks, drafts, and attachments through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers use this MCP server to let agents read and manage a personal Outlook mailbox, calendar, contacts, and To Do lists. Depending on configured permissions, agents can also create or send messages, drafts, invitations, and other updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server can access sensitive mailbox data and, when enabled, make consequential changes such as sending messages or editing calendars.

Mitigation: Start with read_only enabled and limit allow_categories to the write actions the agent needs; use a separate app with read_only_consent when read-only access must be enforced by Microsoft.

Risk: Optional document parsing is unsandboxed, and parsed mail or attachment content may contain untrusted instructions.

Mitigation: Enable document tools only when needed and treat mailbox and attachment content as data, not instructions to take actions.

Risk: Remote HTTP transport exposes mailbox access to requests that reach the server, and plain HTTP does not protect the token in transit.

Mitigation: Keep remote access opt-in, require its bearer token, and place a TLS-terminating proxy in front of non-loopback access.

Risk: Inbox rule changes persist, while calendar changes can send notifications to other people.

Mitigation: Review recipients and affected rules or events before making these changes, and keep the corresponding write categories disabled unless needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mpalermiti/skills/outlook-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [MCP tool results containing text and structured Outlook data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected mailbox and configured permissions; write tools can change mailbox data or notify other people.]

## Skill Version(s):

1.31.3 (source: release evidence, artifact/server.json, artifact/pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
