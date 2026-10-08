## Description:

Helps an agent read and manage Outlook mail, calendars, contacts, and tasks using a token captured from the user's signed-in browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with their Outlook account can find and summarize mail, check calendars and contacts, manage tasks, and request mailbox or calendar changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured browser bearer token enables broad read and write access to the user's mailbox, calendar, contacts, and tasks.

Mitigation: Use only with informed authorization; protect the saved token and delete ~/.outlook-fpx/curlrc or revoke the session when finished.

Risk: Mail sends and mailbox or calendar changes can have lasting effects.

Mitigation: Require explicit confirmation before sending mail, moving or marking messages read, creating drafts, or creating events; re-read changed resources to confirm the result.

Risk: Reading Outlook content can inadvertently expose private messages, recipients, or attachments in an agent conversation.

Mitigation: Return only the information requested and avoid incidental disclosure of bodies, recipients, and attachments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook shell helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language answers and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain sensitive mailbox details; share only requested information.]

## Skill Version(s):

0.3.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
