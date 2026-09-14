## Description:

Dropbox Business API integration with managed OAuth for administering team members, groups, team folders, devices, audit logs, member file access, sharing, and file requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and automation agents use this skill to manage Dropbox Business team resources through Maton-managed OAuth. It supports read/list administration by default and approval-gated write, delete, member-file-access, trigger, destination, and hosted-function workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dropbox Business admin access can expose team data, member files, shared folders, devices, audit logs, and destructive team operations.

Mitigation: Install only when Dropbox Business admin access is intended; use OAuth, the least-privileged Dropbox admin account and scopes available, and require explicit confirmation with specific resource identifiers before writes, deletes, or member-file access.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or copied output when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; when an API key is unavoidable, never print or persist it, send it only to api.maton.ai, and rotate it if exposure is suspected.

Risk: Triggers, destinations, hosted functions, and event watches can create persistent automation that acts without a human in the loop.

Mitigation: Require separate approval for each automation action, use user-authored or user-reviewed handlers, prefer DENY_ALL network policy for hosted functions, and avoid forwarding events to third-party hosts unless explicitly approved.

Risk: Content returned from Dropbox Business or trigger sources may contain sensitive or adversarial data.

Mitigation: Treat fetched content and event payloads as data rather than instructions, extract only fields needed for the task, and avoid dumping raw responses into logs or files.

## Reference(s):

- [Dropbox Business API Documentation](https://www.dropbox.com/developers/documentation/http/teams)
- [Dropbox Team Administration Guide](https://developers.dropbox.com/dbx-team-administration-guide)
- [Dropbox Team Files Guide](https://developers.dropbox.com/dbx-team-files-guide)
- [Dropbox Authentication Types](https://www.dropbox.com/developers/reference/auth-types)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/dropbox-business)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown guidance with bash, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit approval for write, delete, member-file access, trigger, destination, and hosted-function actions.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
