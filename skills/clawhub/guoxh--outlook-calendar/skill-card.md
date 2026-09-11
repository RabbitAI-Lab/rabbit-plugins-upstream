## Description:

Read and write the signed-in user's Microsoft 365 or Outlook.com personal calendar through Microsoft Graph using calendar-scoped device-code authentication and a dedicated token store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to inspect Microsoft 365 or Outlook.com calendar events and to create, update, fetch, or delete a single event through Microsoft Graph with explicit confirmation controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify the signed-in user's Outlook calendar after consent.

Mitigation: Use dry-run output before applying writes, require explicit apply/confirmation for changes, and avoid --yes unless non-interactive changes are intentional.

Risk: The skill stores reusable Microsoft Graph tokens locally under ~/.outlook-calendar/.

Mitigation: Keep the token directory private, clear or revoke tokens when no longer needed, and install only when local token storage is acceptable.

Risk: Calendar event details may include sensitive personal or business information.

Mitigation: The documented behavior limits requested scopes to calendar access plus User.Read, avoids printing tokens, and minimizes delete preview fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guoxh/skills/outlook-calendar)
- [Microsoft Graph calendar reference](references/graph-calendar.md)
- [Microsoft Graph documentation](https://learn.microsoft.com/graph/)
- [Microsoft Graph API endpoint](https://graph.microsoft.com)
- [Microsoft identity platform login endpoint](https://login.microsoftonline.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON or text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Microsoft Graph calendar endpoints and local token/configuration files under ~/.outlook-calendar/.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
