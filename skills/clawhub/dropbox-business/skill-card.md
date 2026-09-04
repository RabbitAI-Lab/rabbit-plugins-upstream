## Description:

Dropbox Business API integration with managed OAuth for administering team members, groups, team folders, devices, audit logs, member file access, sharing, and file requests through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to administer Dropbox Business teams through managed OAuth, including team membership, groups, team folders, devices, audit logs, sharing, and member-file workflows. It is intended for high-privilege Dropbox Business administration where read/list calls are preferred and write, deletion, connection creation, and member-file-access operations require explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants high-privilege Dropbox Business admin access through Maton.

Mitigation: Install only when that access is intended, prefer OAuth, review Dropbox scopes, and use the least-privileged admin account available.

Risk: Write, deletion, member removal, device revocation, permission changes, and member-file access can cause significant administrative or privacy impact.

Mitigation: Require explicit user confirmation with specific resource identifiers before these operations, and require a stated business justification for member-file access.

Risk: Multiple Dropbox Business or Maton connections can make the target account ambiguous.

Mitigation: Specify the intended connection and profile before taking action.

Risk: API-key authentication exposes a long-lived credential if handled outside the credential store.

Mitigation: Prefer OAuth and avoid printing, logging, persisting, or passing API keys on command lines.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/dropbox-business)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Dropbox Business API Documentation](https://www.dropbox.com/developers/documentation/http/teams)
- [Dropbox Team Administration Guide](https://developers.dropbox.com/dbx-team-administration-guide)
- [Dropbox Team Files Guide](https://developers.dropbox.com/dbx-team-files-guide)
- [Dropbox Authentication Types](https://www.dropbox.com/developers/reference/auth-types)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, OAuth or API-key authentication, and an active Dropbox Business connection.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
