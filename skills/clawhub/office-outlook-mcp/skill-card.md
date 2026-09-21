## Description:

The skill lets an agent read and act on a user's Outlook or Microsoft 365 mailbox, calendar, contacts, and tasks through the Outlook REST API using a bearer token captured from a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to let an agent inspect Outlook mail, folders, calendar events, contacts, tasks, and related mailbox data. It also provides command examples for creating drafts, sending mail, moving messages, marking messages read, and creating events when those actions are explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures and stores a live Outlook session token that can authorize broad mailbox, calendar, contacts, tasks, and write operations.

Mitigation: Install only when that level of Outlook access is acceptable; keep the token file private, refresh tokens deliberately, and require explicit confirmation before sending mail, moving messages, marking messages read, creating drafts, or editing calendar data.

Risk: Authorized requests can reveal sensitive mailbox contents or metadata.

Mitigation: Request only the fields needed for the task, prefer text bodies over full HTML, and avoid copying unrelated message bodies, recipients, attachments, or calendar details into the conversation.

Risk: Extra curl arguments or write payloads can change the behavior of an authorized Outlook request.

Mitigation: Use the documented helper functions and verified request shapes, review any extra curl arguments before execution, and re-read resources after writes because a 2xx response alone does not prove the intended change persisted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook REST v2.0 verified request shapes](references/api-recipes.md)
- [Outlook access helper script](references/outlook-env.sh)
- [Outlook REST API base](https://outlook.office.com/api/v2.0)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Outlook REST API request guidance and shell helper usage; does not expose the captured bearer token in normal output.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
