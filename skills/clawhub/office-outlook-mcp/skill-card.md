## Description:

Read and act on the user's Outlook / Microsoft 365 mailbox — mail, folders, calendar, contacts, tasks — via the Outlook REST API, using a bearer token lifted from their signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using Outlook or Microsoft 365 can ask an agent to find and summarize mailbox content, check calendar events and tasks, and perform supported mailbox actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authenticated Outlook request interface is reported to accept caller-supplied curl arguments, which could send mailbox credentials to an unintended destination.

Mitigation: Avoid installation until the authenticated request interface is restricted to validated destinations and safe options, as advised by the security evidence.

## Reference(s):

- [Outlook API request recipes](references/api-recipes.md)
- [Outlook token and request helpers](references/outlook-env.sh)
- [Outlook REST API endpoint](https://outlook.office.com/api/v2.0)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural language responses based on Outlook mail, calendar, contacts, and task data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should include only mailbox information needed to answer the user's request.]

## Skill Version(s):

0.10.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
