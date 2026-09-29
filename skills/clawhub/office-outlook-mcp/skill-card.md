## Description:

Helps an agent read and manage a user's Outlook mail, calendar, contacts, and tasks through the Outlook REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with their Microsoft 365 account can ask it to find and summarize email, check schedules, and manage mailbox, calendar, contact, or task items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured Outlook bearer token grants access to sensitive mailbox, calendar, contact, and task data.

Mitigation: Review before installation, limit disclosure to requested information, and revoke or delete the stored token when finished.

Risk: Broad write access could send messages or change mailbox and calendar items without sufficient user oversight.

Mitigation: Prefer read-only use and require explicit confirmation before sending, moving, editing, drafting, or creating items; re-read changed items to confirm results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook environment helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language responses with optional Markdown and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize requested Outlook data or guide mailbox and calendar actions.]

## Skill Version(s):

0.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
