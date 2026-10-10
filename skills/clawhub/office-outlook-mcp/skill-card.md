## Description:

Helps an agent read and manage a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks using a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with authorized Outlook access can retrieve mail and scheduling information, manage messages, and prepare calendar updates through the Outlook REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured Outlook session token grants access to sensitive mailbox data and is stored locally.

Mitigation: Use a trusted machine, limit access to the token, and delete the stored token or revoke the bridge grant when finished.

Risk: Sending or modifying mail and calendar items can make unintended changes.

Mitigation: Review each send, move, patch, or event action before execution and confirm changes by re-reading the affected item.

Risk: Mailbox responses can expose unrelated sensitive content.

Mitigation: Request only the fields needed and surface only information the user asked for.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook environment helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include user-authorized mailbox and calendar information.]

## Skill Version(s):

0.4.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
