## Description:

Read and act on a user's Outlook and Microsoft 365 mailbox, folders, calendar, contacts, and tasks through the Outlook REST API using a bearer token captured from their signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agents use this skill for specific Outlook mailbox, calendar, contact, and task requests, including reading selected messages, checking schedules, and preparing or performing mailbox actions. It is intended for targeted Microsoft 365 work where the user has an active signed-in Outlook browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change real Outlook mailbox data using a captured browser session bearer token.

Mitigation: Use it only for specific Outlook tasks, avoid broad mailbox dumps, confirm before send, move, or calendar-write actions, and delete or revoke the stored token when finished.

Risk: The stored token can provide broad mailbox access while it remains valid.

Mitigation: Keep the token file private, rely on the helper's restricted file permissions, and remove or revoke the token after use.

## Reference(s):

- [Outlook REST v2.0 verified request shapes](references/api-recipes.md)
- [Outlook access shell helpers](references/outlook-env.sh)
- [Outlook REST API endpoint](https://outlook.office.com/api/v2.0)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Outlook REST API requests that read or change mailbox, calendar, contact, and task data.]

## Skill Version(s):

0.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
