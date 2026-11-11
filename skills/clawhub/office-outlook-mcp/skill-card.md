## Description:

Read and act on the user's Outlook / Microsoft 365 mailbox — mail, folders, calendar, contacts, tasks — via the Outlook REST API, using a bearer token lifted from their signed-in browser tab. Use when asked about their Outlook email, calendar or meetings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an Outlook-connected agent can ask it to find or summarize mail, check calendars and tasks, or carry out requested mailbox actions such as sending or updating messages. The skill supports Outlook and Microsoft 365 mailbox work through the Outlook REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Outlook requests may expose credentials or local files if unrestricted curl arguments or an overridden API destination are used.

Mitigation: Review the scanner concerns before installation; constrain requests to the expected Outlook API host and avoid passing untrusted curl arguments.

## Reference(s):

- [Outlook API recipes](artifact/references/api-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls, Mailbox actions]

**Output Format:** [Text summaries and Outlook REST API operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or modify mailbox content when requested.]

## Skill Version(s):

0.11.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
