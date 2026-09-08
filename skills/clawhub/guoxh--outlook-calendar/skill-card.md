## Description:

Read and write the signed-in user's Microsoft 365 / Outlook.com personal calendar via Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

People who use Microsoft 365 or Outlook.com use this skill through an agent to list upcoming calendar events, inspect token status, and create, update, or delete individual calendar events with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores persistent Microsoft calendar tokens locally and can use them for calendar read/write access.

Mitigation: Install only when that access is acceptable, treat ~/.outlook-calendar/tokens.json as a secret, use a dedicated Azure app registration, and revoke consent when the skill is no longer needed.

Risk: The security evidence notes an event-ID path encoding issue in authenticated Graph requests.

Mitigation: Avoid using event IDs copied from untrusted text until the event-ID path encoding issue is fixed, and review update or delete targets before applying changes.

Risk: Calendar create, update, and delete operations can change a user's live calendar.

Mitigation: Use the dry-run defaults and explicit confirmation flow; require visible apply and confirmation steps before modifying events.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guoxh/skills/outlook-calendar)
- [Microsoft Graph calendar reference](references/graph-calendar.md)
- [Microsoft Graph documentation](https://learn.microsoft.com/graph/)
- [Allowed Microsoft identity endpoint](https://login.microsoftonline.com)
- [Allowed Microsoft Graph endpoint](https://graph.microsoft.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Text, Guidance]

**Output Format:** [Markdown guidance with inline shell commands plus JSON or text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bash, jq, curl, python3, Microsoft Graph network access, and a local token store under ~/.outlook-calendar/.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
