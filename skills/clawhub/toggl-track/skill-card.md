## Description:

Integrates Toggl Track with Maton-managed OAuth so agents can read and modify time entries, projects, clients, tags, and workspaces through approved API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Toggl Track time tracking data through Maton-authenticated API calls. The skill is intended for account, workspace, time entry, project, client, and tag workflows where reads are preferred by default and write actions require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Toggl Track data through Maton, including account, workspace, time entry, project, client, and tag records.

Mitigation: Install only when that access is intended, prefer OAuth, choose the narrowest available scopes, and revoke unused connections.

Risk: Write operations can create, update, archive, or delete Toggl records, and connection deletion is irreversible.

Mitigation: Default to read and list calls, verify identifiers and target connection first, and require explicit user confirmation for every POST, PUT, PATCH, DELETE, archive, restore, or connection deletion.

Risk: Using a Maton API key instead of OAuth can expose a long-lived credential through environment variables, logs, command history, or copied output.

Mitigation: Prefer OAuth and the OS credential store; when raw HTTP is unavoidable, read the key only from the process environment, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Toggl Track API responses may contain personal or business data and should not be treated as trusted instructions.

Mitigation: Extract only the fields needed for the task, avoid dumping full responses into logs or files, and treat response content as untrusted data rather than executable instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Toggl Track API documentation](https://engineering.toggl.com/docs/)
- [Toggl Track authentication reference](https://engineering.toggl.com/docs/api/authentication)
- [Toggl Track time entries API](https://engineering.toggl.com/docs/api/time_entries)
- [Toggl Track projects API](https://engineering.toggl.com/docs/api/projects)
- [Toggl Track clients API](https://engineering.toggl.com/docs/api/clients)
- [Toggl Track tags API](https://engineering.toggl.com/docs/api/tags)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Toggl Track API request paths, request bodies, response-field guidance, and Maton CLI or SDK usage examples.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
