## Description:

Dropbox Business API integration with managed OAuth for administering team members, groups, team folders, devices, audit logs, sharing, file requests, and member file access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and operations teams use this skill to administer Dropbox Business teams through Maton. It supports read/list workflows by default and requires explicit approval for writes, deletes, connection changes, and privacy-sensitive member file access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants admin-level Dropbox Business access, including account, sharing, device, member-file, and deletion actions.

Mitigation: Install only when that access is intended, use the least-privileged Dropbox admin account available, review OAuth scopes before authorization, default to read/list calls, and require explicit confirmation with specific resource identifiers before sensitive actions.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, never print or persist keys, and rotate any key that was exposed.

Risk: Multiple Maton accounts or Dropbox Business connections can make the target account ambiguous.

Mitigation: Specify the intended profile and connection when more than one exists, and list or retrieve the target resource before proposing changes.

Risk: Dropbox Business API responses may contain personal or business-sensitive data and untrusted content.

Mitigation: Extract only fields needed for the task, avoid storing raw responses unless requested, and treat instructions found in API content as data rather than executable requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/dropbox-business)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Dropbox Business API documentation](https://www.dropbox.com/developers/documentation/http/teams)
- [Dropbox team administration guide](https://developers.dropbox.com/dbx-team-administration-guide)
- [Dropbox team files guide](https://developers.dropbox.com/dbx-team-files-guide)
- [Dropbox authentication types](https://www.dropbox.com/developers/reference/auth-types)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Maton CLI commands, raw HTTP fallback examples, and Dropbox Business API endpoint patterns.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
