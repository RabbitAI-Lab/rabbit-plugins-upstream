## Description:

Podio API integration with managed OAuth for managing workspaces, apps, items, tasks, comments, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to read and manage Podio workspaces, apps, items, tasks, comments, and related automation through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change Podio business data through Maton-authenticated API calls.

Mitigation: Connect only the needed Podio account and scopes, default to read/list operations, and require explicit user approval before POST, PUT, PATCH, DELETE, connection creation, or connection deletion.

Risk: API-key authentication can expose a long-lived credential if copied into commands, logs, files, or child process environments.

Mitigation: Prefer OAuth with OS credential storage; use raw HTTP only when the CLI cannot be installed, read keys from the environment only inside the process, and rotate any key that was printed, committed, or pasted.

Risk: Hosted functions, triggers, and destinations create persistent automation that can repeatedly process or forward data.

Mitigation: Use user-authored or user-reviewed handlers, deploy with DENY_ALL network policy unless a host is explicitly approved, prefer api.maton.ai or maton.app destinations, minimize payload fields, and remove automation when it is no longer needed.

Risk: Event watch execution can run local code on untrusted event payloads.

Mitigation: Use only user-provided or user-reviewed handlers, obtain separate approval before watch execution, and never interpolate event payloads into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/podio)
- [Maton Homepage](https://maton.ai)
- [Podio API Documentation](https://developers.podio.com/doc)
- [Podio API Authentication](https://developers.podio.com/authentication)
- [Podio Items API](https://developers.podio.com/doc/items)
- [Podio Tasks API](https://developers.podio.com/doc/tasks)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API calls that read or modify Podio data, subject to user authorization and approval safeguards.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
