## Description:

Helps agents read and act on a user's Outlook and Microsoft 365 mail, calendar, contacts, and tasks using a bearer token captured from a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents with access to a signed-in Outlook account use this skill to find and manage mail, check schedules, and work with contacts and tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing and storing a live mailbox bearer token grants broad access if the token is exposed.

Mitigation: Prefer a tightly scoped OAuth integration when available; keep the local token file private and revoke access if compromised.

Risk: Broad request options or absolute URLs could send authenticated requests beyond the intended Outlook operation.

Mitigation: Use trusted, relative Outlook API paths and avoid arbitrary curl options or untrusted absolute URLs.

Risk: Mailbox contents and attachments can expose sensitive personal or organizational information.

Mitigation: Request only needed fields and surface only the information the user asked for.

Risk: Mail and calendar write operations could change or disclose account data unexpectedly.

Mitigation: Confirm intended recipients and changes before writes, then re-read affected resources to verify the result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/office-outlook-mcp)
- [Outlook API recipes](references/api-recipes.md)
- [Outlook access helpers](references/outlook-env.sh)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples for Outlook REST v2.0; returned account data may be sensitive.]

## Skill Version(s):

0.3.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
