## Description:

Toggl Track API integration with managed OAuth for tracking time and managing projects, clients, tags, and workspaces through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to read and manage Toggl Track time entries, projects, clients, tags, and workspaces through Maton-managed authentication. It defaults to read and list operations and requires explicit confirmation before creating connections or changing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton is authorized to access the connected Toggl Track account, and raw API-key fallback can expose a long-lived credential.

Mitigation: Prefer OAuth, keep credentials in the managed store, never print or persist tokens, and use raw HTTP with MATON_API_KEY only where the CLI cannot be installed.

Risk: The API passthrough can reach endpoints beyond the documented examples if the connection permits them.

Mitigation: Use the narrowest available OAuth scopes, specify the intended connection, start with read-only calls, and confirm every POST, PUT, PATCH, or DELETE with the user.

Risk: Connection deletion and record deletion can be irreversible or disrupt existing automation.

Mitigation: List and verify exact identifiers before deletion, describe the expected effect, and proceed only after explicit user confirmation.

Risk: Toggl Track responses may include personal or sensitive account data.

Mitigation: Extract only task-relevant fields, avoid dumping full responses, and do not write raw responses to logs or files unless the user explicitly asks.

Risk: Unpinned third-party package installs can reduce supply-chain reproducibility.

Mitigation: Consider pinning Maton CLI or SDK versions and using an isolated environment for installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Toggl Track API Documentation](https://engineering.toggl.com/docs/)
- [Toggl Track API Authentication](https://engineering.toggl.com/docs/api/authentication)
- [Time Entries API](https://engineering.toggl.com/docs/api/time_entries)
- [Projects API](https://engineering.toggl.com/docs/api/projects)
- [Clients API](https://engineering.toggl.com/docs/api/clients)
- [Tags API](https://engineering.toggl.com/docs/api/tags)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API guidance and command examples; API responses may contain personal data and should be minimized to task-relevant fields.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
