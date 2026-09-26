## Description:

Dropbox Business API integration with managed OAuth for administering team members, groups, team folders, devices, audit logs, member file access, sharing, and file requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Dropbox Business administrators and operators use this skill to inspect and manage Dropbox Business team resources through authenticated API calls. It supports administrative reads and approved write or delete actions, including privacy-sensitive member file access when explicitly justified by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support admin-level Dropbox Business actions, including writes, deletes, and privacy-sensitive member file access.

Mitigation: Use the least-privileged Dropbox admin account possible, review OAuth scopes before authorizing, and require explicit user confirmation with specific resource identifiers for writes, deletes, and member file access.

Risk: Persistent triggers or hosted functions can continue moving business data after setup.

Mitigation: Avoid persistent triggers or destinations unless the user understands the data flow and duration; prefer task-scoped API calls and delete automations when the task is complete.

Risk: Long-lived API keys can expose Dropbox Business access through child processes or unattended environments.

Mitigation: Prefer OAuth login backed by the operating system credential store, and use raw API-key flows only where the CLI cannot be installed.

## Reference(s):

- [Dropbox Business API Documentation](https://www.dropbox.com/developers/documentation/http/teams)
- [Team Administration Guide](https://developers.dropbox.com/dbx-team-administration-guide)
- [Team Files Guide](https://developers.dropbox.com/dbx-team-files-guide)
- [Authentication Types](https://www.dropbox.com/developers/reference/auth-types)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-oriented instructions and API call examples for authenticated Dropbox Business administration.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
