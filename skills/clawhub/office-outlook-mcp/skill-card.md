## Description:

Read and act on the user's Outlook / Microsoft 365 mailbox — mail, folders, calendar, contacts, tasks — via the Outlook REST API, using a bearer token lifted from their signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Outlook account holders use the agent to find and summarize mail, folders, calendar events, contacts, and tasks, and to make mailbox or calendar changes when asked. A signed-in Outlook browser session is needed to obtain access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The request helper may send a saved mailbox access token to destinations outside Microsoft.

Mitigation: Before connecting a mailbox, have the maintainer remove arbitrary curl options and validate HTTPS Microsoft destinations, including pagination URLs. Use trusted CLI and extension builds, explicitly authorize mailbox changes, and revoke pairing and remove the saved token when access is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Outlook REST request recipes](references/api-recipes.md)
- [Outlook environment helpers](references/outlook-env.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown responses, with shell command examples and JSON request payloads where relevant.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include private mailbox content; show only information requested.]

## Skill Version(s):

0.8.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
