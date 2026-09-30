## Description:

Helps agents administer an authorized Zoom account through Maton's managed OAuth connection, including users, meetings, webinars, recordings, and account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Zoom workspace administrators and their agents use this skill to inspect account resources and, with approval, manage users, meetings, webinars, recordings, and settings for an authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin-level access can affect users, meetings, recordings, and account settings in the connected Zoom account.

Mitigation: Confirm the intended account, favor read-only access, and approve each write against its exact target and effect.

Risk: Hosted functions and triggers can repeat approved account actions without further interaction.

Mitigation: Approve each automation separately and remove unused connections, functions, triggers, and destinations when finished.

## Reference(s):

- [Zoom Admin skill release](https://clawhub.ai/byungkyu/skills/zoom-admin-api)
- [Maton](https://maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoom API Overview](https://developers.zoom.us/docs/api/)
- [Zoom Rate Limits](https://developers.zoom.us/docs/api/rate-limits/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and explicit authorization of the intended Zoom account.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
