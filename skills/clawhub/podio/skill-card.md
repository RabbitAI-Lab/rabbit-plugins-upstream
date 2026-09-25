## Description:

Podio API integration with managed OAuth for managing workspaces, apps, items, tasks, comments, files, and related Podio data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access and manage Podio organizations, workspaces, apps, items, tasks, comments, and files through an authenticated Maton connection. It also guides approved automation patterns using Maton functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on Podio business data through the user's authorized Maton connection.

Mitigation: Use OAuth where possible, authorize only the Podio account and scopes needed for the task, default to read/list calls, and confirm every write or delete.

Risk: Automation setup can repeatedly run approved Podio actions or route events into hosted functions.

Mitigation: Confirm every automation setup, avoid broad trigger destinations, and deploy only user-reviewed functions with a least-privilege connection and network policy.

Risk: Long-lived API keys can expose broader access than intended when used outside the Maton CLI profile flow.

Mitigation: Prefer OAuth and OS credential storage; use raw HTTP or environment-provided API keys only when the CLI cannot be installed.

## Reference(s):

- [Podio API Documentation](https://developers.podio.com/doc)
- [Podio API Authentication](https://developers.podio.com/authentication)
- [Podio Items API](https://developers.podio.com/doc/items)
- [Podio Tasks API](https://developers.podio.com/doc/tasks)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated Maton CLI commands, raw HTTP examples, Podio endpoint guidance, and automation setup guidance.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
