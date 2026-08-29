## Description:

Google Workspace Admin SDK integration with managed OAuth for reading and managing users, groups, organizational units, roles, and domain settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and agents supporting them use this skill to inspect and manage Google Workspace users, groups, organizational units, roles, and domain settings through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Google Workspace administration changes, including account, group, role, organizational unit, and domain-setting updates.

Mitigation: Use a least-privileged Google admin account, start with read/list calls, and require explicit user approval with the exact method, endpoint, target identifier, payload, and consequences before any write call.

Risk: OAuth connections and API keys can expose administrative access if handled too broadly or retained after the task.

Mitigation: Prefer Maton OAuth through the CLI, choose the narrowest available scopes, avoid printing or persisting credentials, and revoke the Maton connection after administrative work is complete.

Risk: Ambiguous account or connection selection can direct an administrative action to the wrong Google Workspace tenant.

Mitigation: Specify the intended Maton connection when multiple connections exist and verify resource identifiers before proposing changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Admin SDK Overview](https://developers.google.com/admin-sdk)
- [Directory API Users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
- [Directory API Groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups)
- [Directory API Members](https://developers.google.com/admin-sdk/directory/reference/rest/v1/members)
- [Directory API Org Units](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)
- [Directory API Domains](https://developers.google.com/admin-sdk/directory/reference/rest/v1/domains)
- [Directory API Roles](https://developers.google.com/admin-sdk/directory/reference/rest/v1/roles)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list operations and present exact method, endpoint, target identifier, payload, and consequence details before write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
