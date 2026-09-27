## Description:

Microsoft Outlook and OneDrive CLI and MCP for email, calendar, contacts, tasks, and files, for personal and enterprise accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rlrghb](https://clawhub.ai/user/rlrghb)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to manage Outlook mail, calendars, contacts, tasks, and OneDrive files through the olk CLI or MCP server, with personal or enterprise Microsoft accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access may expose sensitive mail, calendar, contact, task, or file data.

Mitigation: Grant only the Microsoft scopes needed and keep credentials and tokens out of logs.

Risk: Agent-initiated changes can send messages or invitations, or modify or delete account data.

Mitigation: Confirm sends and deletions with the user, preview uncertain changes with --dry-run, and use OLK_NO_WRITE=1 or OLK_NO_SEND=1 for unattended runs.

## Reference(s):

- [Outlook skill release on ClawHub](https://clawhub.ai/rlrghb/skills/olk)
- [Microsoft Graph guidance for sending mail from another user](https://learn.microsoft.com/en-us/graph/outlook-send-mail-from-other-user)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with CLI examples and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for CLI and MCP use; olk can return JSON or plain-text results.]

## Skill Version(s):

1.15.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
