## Description:

Dropbox Business API integration with managed OAuth for administering team members, groups, team folders, devices, audit logs, member file access, sharing, and file requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Dropbox Business administrators and operations teams use this skill to inspect and manage team resources through Maton-authenticated Dropbox Business API calls. It is intended for admin workflows such as member, group, team-folder, device, sharing, audit-log, and member-file-access operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Dropbox Business admin actions, including write, delete, member removal, team-folder deletion, device revocation, and admin-permission changes.

Mitigation: Use a least-privileged admin account, default to read and list calls, confirm the exact resource identifier, explain the intended effect, and require explicit approval before any change.

Risk: Member file access is privacy-sensitive and can expose individual users' Dropbox content.

Mitigation: Allow member file access only when the user explicitly requests it with a clear business justification.

Risk: Ambiguous Maton profiles or Dropbox Business connections can send a request to the wrong account.

Mitigation: Specify the intended profile and connection when more than one account or connection is available.

Risk: Long-lived API keys and provider tokens can leak through logs, shell history, files, or command-line arguments.

Mitigation: Prefer OAuth through the Maton CLI and the operating system credential store; never print, persist, or pass credentials on the command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/dropbox-business)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Dropbox Business API Documentation](https://www.dropbox.com/developers/documentation/http/teams)
- [Dropbox Team Administration Guide](https://developers.dropbox.com/dbx-team-administration-guide)
- [Dropbox Team Files Guide](https://developers.dropbox.com/dbx-team-files-guide)
- [Dropbox Authentication Types](https://www.dropbox.com/developers/reference/auth-types)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Dropbox Business endpoint paths, approval gates, and credential-handling guidance.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
