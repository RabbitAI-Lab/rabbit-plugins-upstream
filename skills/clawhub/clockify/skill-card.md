## Description:

Clockify API integration with managed OAuth for tracking time and managing projects, clients, tasks, tags, workspaces, and workspace members through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Clockify account, inspect time-tracking data, and perform approved changes to workspaces, projects, clients, tasks, tags, and time entries. It also documents how approved Clockify actions can run through Maton-hosted functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clockify writes, deletes, or connection changes can affect business time-tracking data or account access.

Mitigation: Default to read and list calls, then require explicit user approval for the target account, resource, payload, and intended effect before any write, delete, or new connection.

Risk: Long-lived API keys or exposed credentials can broaden access beyond the immediate task.

Mitigation: Prefer OAuth with operating-system credential storage, avoid printing or exporting tokens, and use raw HTTP with MATON_API_KEY only where the CLI cannot be installed.

Risk: Hosted functions, triggers, and destinations can create persistent automation or data forwarding.

Mitigation: Review each function, trigger, destination host, data scope, persistence behavior, and cleanup step separately; keep destinations on api.maton.ai or *.maton.app unless the user explicitly approves another host.

Risk: Event watch with --exec runs local code against event data.

Mitigation: Use event listing or plain watch for inspection, and use --exec only with a user-authored or user-reviewed handler and separate approval.

## Reference(s):

- [Clockify Skill on ClawHub](https://clawhub.ai/byungkyu/skills/clockify)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Clockify API Documentation](https://docs.clockify.me/)
- [Clockify Time Entry API Reference](https://docs.clockify.me/#tag/Time-entry)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with inline shell, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Clockify authorization.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
