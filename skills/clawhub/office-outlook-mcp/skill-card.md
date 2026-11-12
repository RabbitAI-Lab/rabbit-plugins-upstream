## Description:

Read and act on the user's Outlook / Microsoft 365 mailbox — mail, folders, calendar, contacts, tasks — via the Outlook REST API, using a bearer token lifted from their signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Outlook and Microsoft 365 users use this skill to retrieve and manage their own email, folders, calendar, contacts, and tasks. It can also make mailbox changes such as marking messages read, moving mail, creating drafts or events, and sending messages when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious because unrestricted curl options and an unvalidated API destination could expose the mailbox bearer token; scan coverage is partial.

Mitigation: Review the destination and curl options before use, account for the unresolved references, and avoid installing until comfortable with the reported mailbox credential risk.

Risk: The skill reads private mailbox data and can perform write actions, including sending messages and changing calendar or mail items.

Mitigation: Return only requested mailbox details and confirm the intended recipient or resource before making a write.

## Reference(s):

- [Outlook REST API request recipes](references/api-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [API Calls, Text, Shell commands, Guidance]

**Output Format:** [JSON API responses and concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mailbox content can include sensitive personal information; surface only what was requested.]

## Skill Version(s):

0.12.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
