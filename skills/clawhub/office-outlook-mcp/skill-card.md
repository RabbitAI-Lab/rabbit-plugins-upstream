## Description:

Read and act on the user's Outlook / Microsoft 365 mailbox — mail, folders, calendar, contacts, tasks — via the Outlook REST API, using a bearer token lifted from their signed-in browser tab. Use when asked about their Outlook email, calendar or meetings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Outlook users can use this skill to retrieve and manage their Microsoft 365 email, folders, calendar, contacts, and tasks. It provides shell-based access to the Outlook REST API and helps the agent return requested mailbox information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands do not adequately limit actions and destinations.

Mitigation: Install only if you trust the agent with your Outlook session and write access; require explicit authorization before sending or changing items, restrict authenticated URLs and curl options, and remove the cached token and revoke pairing when finished.

## Reference(s):

- [Office Outlook MCP release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Outlook REST API endpoint](https://outlook.office.com/api/v2.0)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses and concise natural-language summaries, with shell command examples in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outlook data can include sensitive mailbox content; only surface information relevant to the user's request.]

## Skill Version(s):

0.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
