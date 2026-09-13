## Description:

Todoist provides managed OAuth access through Maton for agents to list, create, update, complete, and organize Todoist tasks, projects, sections, labels, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to manage Todoist work items through authenticated Maton CLI or HTTP calls, with read/list defaults and confirmation before writes or automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived Maton API keys can leak through environment variables, logs, command history, or copied output when raw HTTP is used instead of the CLI.

Mitigation: Prefer OAuth through the Maton CLI; if a raw API key is unavoidable, never print or persist it, read it from the process environment, send it only to api.maton.ai, and rotate it after exposure.

Risk: Todoist writes, connection changes, function deployment, trigger setup, or deletions can alter user data or authorization state.

Mitigation: Default to read and list operations, then require explicit user confirmation before any write, connection creation or deletion, hosted function action, trigger action, or destructive command.

Risk: Hosted functions and triggers can run against the deploying account's Maton identity and may expose connected Todoist data if configured broadly.

Mitigation: Use user-authored or user-reviewed handlers, least-privilege account connections, DENY_ALL network policy by default, and trigger destinations limited to trusted Maton or user-controlled URLs.

Risk: The release pins Maton tooling versions, but package checksums or signatures are not documented in the security evidence.

Mitigation: Review pinned package versions and release notes before installation or upgrade, and avoid unpinned reinstall commands.

## Reference(s):

- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1)
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Todoist OAuth connection; writes and automation setup require explicit user confirmation.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
