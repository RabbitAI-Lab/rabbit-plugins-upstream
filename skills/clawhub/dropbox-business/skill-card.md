## Description:

Dropbox Business API integration with managed OAuth for administering team members, groups, team folders, devices, audit logs, member file access, sharing, and file requests for Dropbox Business teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Dropbox Business administrators use this skill to manage team accounts, groups, folders, devices, sharing, audit logs, file requests, and privacy-sensitive member file access through documented Dropbox Business operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants powerful team-level Dropbox Business administration, including access to member files and destructive operations.

Mitigation: Install only for trusted administrators, review Dropbox scopes during authorization, use the least-privileged suitable admin account, and require explicit confirmation before write, delete, member-file-access, or connection-creation actions.

Risk: Long-lived API keys or exposed credentials can leak through logs, shell history, files, or child processes.

Mitigation: Prefer OAuth, use the operating system credential store where possible, never print or persist tokens, and rotate any key that was exposed.

Risk: Administrative actions can affect the wrong Dropbox Business account or connection when multiple accounts are available.

Mitigation: Confirm the target account and resource identifiers before changes, and specify the intended connection or profile for sensitive operations.

## Reference(s):

- [Dropbox Business API Documentation](https://www.dropbox.com/developers/documentation/http/teams)
- [Team Administration Guide](https://developers.dropbox.com/dbx-team-administration-guide)
- [Team Files Guide](https://developers.dropbox.com/dbx-team-files-guide)
- [Dropbox Authentication Types](https://www.dropbox.com/developers/reference/auth-types)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, and occasional Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Dropbox Business request bodies and selected JSON response fields; avoid dumping raw personal or organizational data.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
