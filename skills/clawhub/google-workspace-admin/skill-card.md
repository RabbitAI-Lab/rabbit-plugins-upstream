## Description:

Google Workspace Admin SDK integration with managed OAuth for reading and managing users, groups, organizational units, roles, and domain settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and their delegated agents use this skill to inspect and manage Google Workspace directory resources through Maton. It is intended for user, group, organizational unit, role, and domain administration with explicit approval before write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad Google Workspace administrator actions through a raw API gateway.

Mitigation: Use a least-privileged admin account with narrow OAuth scopes and install only when Google Workspace administration through Maton is required.

Risk: Write operations can change or delete users, groups, organizational units, role assignments, and domain settings.

Mitigation: Confirm the exact HTTP method, endpoint, target resource, payload, and consequence before every POST, PUT, PATCH, or DELETE request.

Risk: Long-lived API keys and surfaced credentials can be exposed through logs, command history, files, or pasted output.

Mitigation: Prefer OAuth, never print or persist credentials, avoid broad default connections, and revoke the connection when the task is complete.

Risk: Fetched Google Workspace data may include personal data or adversarial content.

Mitigation: Treat API responses as untrusted data, avoid dumping full responses, and use only the fields required for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Maton](https://maton.ai)
- [Google Admin SDK Overview](https://developers.google.com/admin-sdk)
- [Directory API Users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
- [Directory API Groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups)
- [Directory API Members](https://developers.google.com/admin-sdk/directory/reference/rest/v1/members)
- [Directory API Org Units](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)
- [Directory API Domains](https://developers.google.com/admin-sdk/directory/reference/rest/v1/domains)
- [Directory API Roles](https://developers.google.com/admin-sdk/directory/reference/rest/v1/roles)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with shell commands, code snippets, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved Google Workspace Admin connection.]

## Skill Version(s):

1.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
