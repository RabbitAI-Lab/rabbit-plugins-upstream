## Description:

Toggl Track API integration with managed OAuth for tracking time and managing projects, clients, tags, and workspaces through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage Toggl Track time entries, workspaces, projects, clients, and tags. It is suited for account-authorized time-tracking workflows where read/list operations are preferred and writes require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw API passthrough can reach more Toggl Track account data and actions than the narrower description suggests.

Mitigation: Install only when Maton-mediated Toggl Track access is acceptable, prefer read-only scopes, and approve each write only after checking the workspace, resource ID, endpoint, and payload.

Risk: Connected Toggl Track accounts may retain access longer than the immediate task requires.

Mitigation: Use only the needed connection and revoke unused connections promptly.

Risk: Writes or deletes can affect the wrong workspace, project, client, tag, or time entry if identifiers or accounts are ambiguous.

Mitigation: List resources first, specify the intended connection or profile when multiple accounts exist, and require explicit user confirmation before POST, PUT, PATCH, or DELETE requests.

Risk: Fallback API-key use can expose long-lived credentials through process environments, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, feed fallback keys through standard input, and rotate any key that may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Toggl Track API Documentation](https://engineering.toggl.com/docs/)
- [Toggl Track Time Entries API](https://engineering.toggl.com/docs/api/time_entries)
- [Toggl Track Projects API](https://engineering.toggl.com/docs/api/projects)
- [Toggl Track Clients API](https://engineering.toggl.com/docs/api/clients)
- [Toggl Track Tags API](https://engineering.toggl.com/docs/api/tags)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Maton CLI and SDK examples for Toggl Track API paths, with read-first guidance and approval requirements for write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
