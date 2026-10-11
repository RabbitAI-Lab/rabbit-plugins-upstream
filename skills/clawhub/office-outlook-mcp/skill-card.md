## Description:

Helps an agent read and act on a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks using access captured from a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with a signed-in Microsoft 365 account can ask an agent to find and summarize mail, check meetings, contacts, and tasks, or perform approved Outlook changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured browser access grants broad read and write access to real Microsoft 365 data.

Mitigation: Use only on an account where broad access is acceptable, and review each requested write before execution.

Risk: A locally stored bearer token can enable access until it expires or is revoked.

Mitigation: Keep the token file private; remove it or revoke access when the skill is no longer needed.

Risk: Mailbox queries may expose sensitive message bodies, recipients, or attachments unnecessarily.

Mitigation: Request only needed fields and surface only the information the user asked for.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook shell helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain requested Outlook account data; write actions require confirmation.]

## Skill Version(s):

0.5.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
