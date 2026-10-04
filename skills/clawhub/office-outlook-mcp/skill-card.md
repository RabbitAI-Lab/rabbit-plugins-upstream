## Description:

Helps an agent read and manage a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks using access captured from a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Outlook users can ask an agent to find and summarize email, check schedules, and manage messages, events, contacts, or tasks in their Microsoft 365 account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A copied browser bearer token grants broad access to the user's real mailbox, calendar, contacts, and tasks.

Mitigation: Install only with informed consent; protect the local token file and remove it or revoke browser bridge pairing when finished.

Risk: Write actions can send mail or change messages and calendar entries without adequate safeguards.

Mitigation: Require explicit user confirmation before sending, moving, marking read, drafting, or creating items, and re-read affected resources to verify changes.

Risk: Reading or displaying more Outlook content than requested can expose private messages and recipients.

Mitigation: Retrieve and surface only the fields and content needed for the user's request; avoid incidental message bodies, recipients, and attachments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook environment helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language answers with optional Markdown and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may contain requested mailbox or calendar information.]

## Skill Version(s):

0.3.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
