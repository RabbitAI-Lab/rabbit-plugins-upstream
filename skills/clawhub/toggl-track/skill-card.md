## Description:

Toggl Track API integration with managed OAuth for tracking time and managing projects, clients, tags, and workspaces through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to access a connected Toggl Track account for time entries, workspace data, projects, clients, and tags. It defaults to read and list workflows, with explicit user approval required before creating connections or changing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants API access to the connected Toggl Track account through Maton.

Mitigation: Approve only the specific Toggl Track connection needed for the task, prefer OAuth over API keys, and revoke unused connections when work is complete.

Risk: Data-changing API calls can create, update, stop, archive, restore, or delete Toggl Track records.

Mitigation: Start with read or list calls, then confirm the target resource, request payload, and intended effect with the user before every write or delete action.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or command arguments when the raw HTTP fallback is used.

Mitigation: Use OAuth and the Maton CLI when possible; if raw HTTP is required, do not print or persist the key, feed credentials through stdin, and rotate the key if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton homepage](https://maton.ai)
- [Toggl Track API Documentation](https://engineering.toggl.com/docs/)
- [Toggl Track API Reference](https://engineering.toggl.com/docs/api/authentication)
- [Toggl Track Time Entries API](https://engineering.toggl.com/docs/api/time_entries)
- [Toggl Track Projects API](https://engineering.toggl.com/docs/api/projects)
- [Toggl Track Clients API](https://engineering.toggl.com/docs/api/clients)
- [Toggl Track Tags API](https://engineering.toggl.com/docs/api/tags)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton CLI or SDK setup, and a user-approved Toggl Track connection for account access.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
