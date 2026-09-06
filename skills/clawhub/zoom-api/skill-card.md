## Description:

Zoom API integration with managed OAuth for managing Zoom meetings, webinars, recordings, and user profiles through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation agents use this skill to schedule and manage Zoom meetings and webinars, retrieve meeting details, list cloud recordings, and read user profile information through a Maton-authenticated Zoom connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize access to a selected Zoom account through Maton OAuth or API credentials.

Mitigation: Install only when comfortable granting Maton access, prefer OAuth, choose the narrowest available Zoom scopes, and avoid raw API-key fallback unless the CLI is unavailable.

Risk: Write or delete operations can create, modify, cancel, or remove Zoom meetings, webinars, recordings, and connections.

Mitigation: Default to read and list calls, confirm the exact account, connection, resource, payload, and intended effect before any write or delete, and verify identifiers before destructive actions.

Risk: Zoom API responses may contain personal, meeting, webinar, or recording data.

Mitigation: Extract only task-relevant fields, avoid dumping full responses into logs or files, and treat external response content as untrusted data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoom-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoom API Documentation](https://developers.zoom.us/docs/api/)
- [Zoom REST API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
- [Zoom Meeting API](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Meetings)
- [Zoom OAuth Scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK examples for Zoom API operations; API responses may include personal or meeting data and should be minimized to task-relevant fields.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
