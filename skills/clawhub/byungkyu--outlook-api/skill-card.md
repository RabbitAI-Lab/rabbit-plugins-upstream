## Description:

Helps agents read and manage Outlook mail, calendars, folders, and contacts through a connected Microsoft account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to retrieve Outlook information and, with approval, send messages, update calendars or contacts, and set up related automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Outlook gives Maton access to account data within the approved authorization scope.

Mitigation: Connect only when intended, prefer read-only scopes where possible, and revoke unused connections.

Risk: Sending, deleting, or updating Outlook data can have unintended effects.

Mitigation: Get explicit approval for each send, delete, update, or automation.

Risk: Third-party automation destinations can receive ongoing data.

Mitigation: Avoid third-party trigger destinations unless the continuing data flow is understood; remove unused functions.

## Reference(s):

- [Outlook skill release](https://clawhub.ai/byungkyu/skills/outlook-api)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and an authorized Outlook connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
