## Description:

Helps an agent read and act on a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks using access from a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with their Outlook account can ask it to find and summarize mail, inspect schedules, and work with contacts and tasks. With user approval, it can also send or modify mail and create calendar events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured browser bearer token grants broad mailbox access and is stored locally for reuse.

Mitigation: Treat the token file as a password, limit access to it, and revoke or delete it when finished.

Risk: Mailbox and calendar actions can send, move, or disclose sensitive information or change user data.

Mitigation: Require explicit user confirmation before sending, moving, marking read, drafting, creating events, or changing attachments, contacts, or settings; disclose only requested content.

## Reference(s):

- [Outlook API recipes](artifact/references/api-recipes.md)
- [Outlook access helpers](artifact/references/outlook-env.sh)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/office-outlook-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, JSON]

**Output Format:** [Markdown responses and shell examples; Outlook API responses in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may contain private mailbox or calendar information; limit disclosure to what the user requests.]

## Skill Version(s):

0.3.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
