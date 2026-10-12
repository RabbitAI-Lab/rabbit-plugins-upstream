## Description:

Helps an agent read and act on a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks using a browser-captured bearer token and the Outlook REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with an authorized Outlook account can retrieve and summarize mail, check meetings and contacts, and prepare or perform requested mailbox and calendar actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured browser token gives the agent broad, reusable access to the user's real Outlook mailbox, calendar, contacts, and tasks.

Mitigation: Use only in a limited environment when this access is acceptable; remove ~/.outlook-fpx/curlrc or revoke the session when finished.

Risk: Write actions can send mail or change mailbox and calendar data.

Mitigation: Review each write action before execution and re-read affected resources to confirm the result.

Risk: Responses can expose private messages, recipients, and attachments.

Mitigation: Return only information the user requested; avoid unnecessary message bodies, recipients, or attachments in the transcript.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook access helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance and Outlook API JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive mailbox data; limit responses to the user's request.]

## Skill Version(s):

0.5.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
