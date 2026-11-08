## Description:

Read and act on the user's Outlook / Microsoft 365 mailbox — mail, folders, calendar, contacts, tasks — via the Outlook REST API, using a bearer token lifted from their signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to find and summarize Outlook mail, calendar events, contacts, and tasks, and to carry out requested mailbox actions such as sending mail or creating calendar items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Arbitrary curl options could expose mailbox credentials or data to an unintended destination; the security review is incomplete and does not establish that exposure occurred.

Mitigation: Review curl options and destinations before use, and avoid sending mailbox credentials or content to untrusted destinations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook REST request examples](references/api-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, API Calls, Shell commands, JSON]

**Output Format:** [Concise natural-language mailbox summaries and Outlook REST request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read mailbox content and perform requested mail or calendar actions.]

## Skill Version(s):

0.8.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
