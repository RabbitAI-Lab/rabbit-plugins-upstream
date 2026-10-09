## Description:

Helps an agent read and manage a user's Outlook mail, calendar, contacts, and tasks using access from a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using Outlook or Microsoft 365 can ask an agent to check messages and schedules or, with their approval, update mail and calendar items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A browser extension and local helper capture and store a reusable Outlook access token.

Mitigation: Install only if comfortable with this access model; prefer a scoped OAuth integration when available and protect the stored token.

Risk: The skill can expose sensitive messages, attachments, calendar details, contacts, and tasks.

Mitigation: Share only requested information and require explicit confirmation before downloading attachments.

Risk: The skill can send or change mailbox and calendar state.

Mitigation: Require explicit confirmation before sending, moving, marking mail read, creating drafts, or changing events.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook environment helpers](references/outlook-env.sh)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain user-authorized mailbox or calendar information.]

## Skill Version(s):

0.4.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
