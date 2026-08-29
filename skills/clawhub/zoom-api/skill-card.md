## Description:

Zoom API integration with managed OAuth for managing meetings, webinars, recordings, and user profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Zoom through Maton OAuth for meeting, webinar, recording, and user profile workflows. It supports read/list operations and user-approved write, delete, scheduling, and connection actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoom API actions are routed through Maton and require authorizing Zoom scopes.

Mitigation: Confirm the user is comfortable with Maton-mediated access and authorize only the scopes needed for the task.

Risk: Write, delete, and scheduling actions can change or remove Zoom resources and may notify participants.

Mitigation: Review the target resource, payload, and intended effect with the user before approving the action.

Risk: Long-lived API keys or provider-issued tokens can leak if printed, logged, written to files, or passed on command lines.

Mitigation: Prefer Maton OAuth, avoid exposing credential values, and use stdin-based header handling only when the CLI is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoom-api)
- [Maton Homepage](https://maton.ai)
- [Zoom API Documentation](https://developers.zoom.us/docs/api/)
- [Zoom REST API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
- [Zoom Meeting API](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Meetings)
- [Zoom OAuth Scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Zoom account; write operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
