## Description:

Zoom API integration with managed OAuth for managing meetings, webinars, recordings, and user profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and operations teams use this skill to retrieve Zoom account information and manage meetings, webinars, recordings, registrants, and participants through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Zoom account data through Maton-managed OAuth.

Mitigation: Install only when scoped Zoom access is acceptable, prefer OAuth, choose the narrowest available scopes, and revoke unused connections after use.

Risk: Write, delete, and connection actions can create or change meetings, webinars, recordings, registrants, or account connections.

Mitigation: Confirm the target account, connection, resource identifier, payload, and intended effect before any write, delete, or new connection action.

Risk: Long-lived API keys or provider-issued tokens can be exposed if printed, logged, stored, or passed through shell commands.

Mitigation: Use the Maton CLI credential store when possible, keep credentials out of output and files, and send Maton API keys only to api.maton.ai when CLI use is unavailable.

## Reference(s):

- [Zoom API Documentation](https://developers.zoom.us/docs/api/)
- [Zoom REST API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
- [Zoom Meeting API](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Meetings)
- [Zoom OAuth Scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Bash, JSON, Python, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API request paths, command examples, response interpretation, and confirmation prompts before write or connection actions.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
