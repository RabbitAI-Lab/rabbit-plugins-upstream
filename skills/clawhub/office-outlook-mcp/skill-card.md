## Description:

Helps an agent read and act on a user's Outlook or Microsoft 365 mail, calendar, contacts, and tasks through the Outlook REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and their assistants can use this skill to answer questions about their Outlook mailbox and schedule, and to perform requested mail, calendar, contact, or task actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access can expose private mailbox content, attachments, contacts, and schedules.

Mitigation: Use only for narrow user-requested tasks; avoid bulk body or attachment reads and share only the requested details.

Risk: Mailbox and calendar writes can change or send real user data without strong built-in confirmation controls.

Mitigation: Inspect write payloads before execution and re-read the affected resource to confirm the result.

Risk: A reusable Outlook bearer token persists locally and can grant broad access if exposed.

Mitigation: Protect the stored token, and remove or refresh it when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook environment helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language responses with optional shell commands and structured Outlook results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize mailbox and calendar data or suggest requested changes.]

## Skill Version(s):

0.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
