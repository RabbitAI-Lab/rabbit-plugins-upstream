## Description:

Google Workspace Admin SDK integration with managed OAuth for reading and managing users, groups, organizational units, roles, and domain settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, administrators, and developers use this skill when they need an agent to help administer Google Workspace accounts, groups, organizational units, roles, and domain settings through a Maton-managed OAuth connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Workspace admin actions can change tenant-wide identity and access controls.

Mitigation: Use a least-privileged admin account, prefer read-only scopes where possible, and require user review of the exact HTTP method, endpoint path, and target resource before any write.

Risk: Long-lived credentials or broad OAuth access could expose administrative authority beyond the immediate task.

Mitigation: Prefer OAuth over API keys, avoid exposing MATON_API_KEY, restrict OAuth scopes to the resources needed, and revoke or delete unused connections after the task.

Risk: Hosted functions, triggers, or destinations can keep running after the original administrative task is complete.

Mitigation: Create automation only after explicit approval, keep function network policy restrictive, avoid bulk privilege changes, and delete unused Maton functions, triggers, or destinations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Admin SDK overview](https://developers.google.com/admin-sdk)
- [Google Admin SDK Directory API guides](https://developers.google.com/admin-sdk/directory/v1/guides)
- [Google Directory API users reference](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with inline shell, Python, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, a Google Workspace admin connection, and explicit user approval before write operations.]

## Skill Version(s):

1.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
