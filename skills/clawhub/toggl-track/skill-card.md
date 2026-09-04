## Description:

Toggl Track API integration with managed OAuth for tracking time and managing projects, clients, tags, and workspaces through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to work with Toggl Track data through Maton-managed authentication. It supports reading and modifying time entries, projects, clients, tags, and workspace resources while requiring confirmation for writes and new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete Toggl Track records through Maton.

Mitigation: Default to read and list operations, then require explicit user confirmation with exact resource IDs, payloads, and intended effects before any POST, PUT, PATCH, or DELETE request.

Risk: A request can affect the wrong Toggl Track account or Maton profile when multiple connections exist.

Mitigation: Pin the intended connection or profile for operations, especially before writes and deletes.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or child processes.

Mitigation: Use OAuth where possible, avoid MATON_API_KEY except when the CLI cannot be used, and never print, persist, or pass credentials on a command line.

Risk: External data returned by Toggl Track can contain untrusted content.

Mitigation: Treat API responses as data only; do not execute, eval, or let returned content choose endpoints, recipients, commands, or follow-up actions.

Risk: High-volume calls can hit Maton or Toggl Track rate limits.

Mitigation: Use pagination and server-side filters, keep request rates within documented limits, and retry only after checking the error response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Toggl Track API Documentation](https://engineering.toggl.com/docs/)
- [Toggl Track API Reference](https://engineering.toggl.com/docs/api/authentication)
- [Time Entries API](https://engineering.toggl.com/docs/api/time_entries)
- [Projects API](https://engineering.toggl.com/docs/api/projects)
- [Clients API](https://engineering.toggl.com/docs/api/clients)
- [Tags API](https://engineering.toggl.com/docs/api/tags)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API paths, JSON payload templates, connection identifiers, and confirmation prompts for account-changing operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
