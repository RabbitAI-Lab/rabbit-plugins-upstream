## Description:

Google Workspace Admin SDK integration with managed OAuth for reading and managing users, groups, organizational units, roles, and domain settings through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, administrators, and developers use this skill to inspect and administer Google Workspace directory resources through managed OAuth. It is suited for account, group, organizational unit, role, and domain administration when changes are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable high-trust Google Workspace administrative access through Maton OAuth or SDK connections.

Mitigation: Install Maton only from expected official channels, use an isolated environment where practical, connect a least-privileged Google admin account, and revoke the connection when finished.

Risk: Write-capable directory operations can change users, groups, organizational units, roles, and domain settings.

Mitigation: Default to read and list calls, show the exact HTTP method, endpoint path, target identifier, and intended effect before each write, and proceed only after explicit user approval.

Risk: Long-lived API keys or exposed credentials can be leaked through environment variables, logs, files, or command history.

Mitigation: Prefer OAuth login, do not print or persist credential values, and use API keys only in environments where the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Admin SDK Overview](https://developers.google.com/admin-sdk)
- [Directory API Users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
- [Directory API Groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups)
- [Directory API Members](https://developers.google.com/admin-sdk/directory/reference/rest/v1/members)
- [Directory API Org Units](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)
- [Directory API Domains](https://developers.google.com/admin-sdk/directory/reference/rest/v1/domains)
- [Directory API Roles](https://developers.google.com/admin-sdk/directory/reference/rest/v1/roles)
- [Admin SDK Guides](https://developers.google.com/admin-sdk/directory/v1/guides)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API paths, JSON examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide read-only and write-capable Google Workspace Admin API calls through Maton; write operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
