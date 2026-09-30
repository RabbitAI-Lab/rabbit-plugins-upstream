## Description:

Provides AI agents with tools to read and manage personal Outlook mail, calendars, contacts, and tasks through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users connect an agent to a personal Outlook account to find and organize mail, manage events, contacts, and tasks, and optionally send or update items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with account access may expose personal Outlook data or send, change, or delete content.

Mitigation: Start with read_only enabled; for Microsoft-enforced read-only access, use a separate Azure app with read-only permissions.

Risk: Attachment tools can email files from their permitted attachment directory.

Mitigation: Keep attachments_dir narrowly scoped and review files before sending.

## Reference(s):

- [ClawHub outlook-mcp release](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [Installation repository listed in skill metadata](https://github.com/mpalermiti/outlook-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Structured MCP tool responses and text prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain personal Outlook data; enabled write tools can change account content.]

## Skill Version(s):

1.22.1 (source: ClawHub release, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
