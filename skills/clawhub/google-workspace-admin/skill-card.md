## Description:

Google Workspace Admin SDK integration with managed OAuth for reading and administering users, groups, organizational units, roles, and domain settings through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Google Workspace administrators and support engineers use this skill to inspect and manage Workspace users, groups, organizational units, roles, and domain settings from an agent workflow. It is intended for tasks that require Google Workspace administration and explicit review of high-impact write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact Google Workspace write operations can delete accounts, change access, alter organizational units, or modify domain-wide settings.

Mitigation: Use read/list calls first, then require explicit user approval showing the exact method, endpoint, target resource identifier, payload, and consequences before POST, PUT, PATCH, or DELETE.

Risk: Overbroad or stale administrator credentials can expose more Workspace resources than the task requires.

Mitigation: Use a least-privileged Google admin account, prefer OAuth over API keys, restrict scopes to the needed resources, specify the intended connection, and revoke unused connections after completion.

Risk: Credentials or provider-issued tokens could leak through logs, command lines, files, or copied output.

Mitigation: Do not print, persist, inspect, or pass credentials on command lines; let the CLI or SDK credential store handle tokens and send direct API keys only to api.maton.ai when the CLI is unavailable.

Risk: External API responses may contain untrusted content that attempts to influence follow-up actions.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and do not let fetched content choose endpoints, recipients, or subsequent actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Admin SDK Overview](https://developers.google.com/admin-sdk)
- [Directory API Users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
- [Directory API Groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups)
- [Directory API Org Units](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)
- [Directory API Domains](https://developers.google.com/admin-sdk/directory/reference/rest/v1/domains)
- [Directory API Roles](https://developers.google.com/admin-sdk/directory/reference/rest/v1/roles)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide Maton CLI, SDK, or HTTPS calls; write operations require explicit user approval with method, endpoint, target, payload, and consequences.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
