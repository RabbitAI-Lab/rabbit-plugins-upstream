## Description:

Zoho Mail API integration with managed OAuth for sending, reading, searching, and managing email, folders, and labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with a user's Zoho Mail account through managed OAuth, including reading, searching, sending, and organizing messages, folders, and labels. It also documents how approved Maton functions and triggers can automate Zoho Mail actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Zoho Mail data through an authorized user connection.

Mitigation: Use OAuth where possible, authorize only the Zoho Mail scopes and accounts needed for the task, and rely on provider-enforced authorization.

Risk: Write operations can send, move, label, draft, or delete email.

Mitigation: Default to read and list operations, and require explicit user confirmation before any POST, PUT, PATCH, DELETE, or connection-changing command.

Risk: Hosted functions, triggers, and destinations can run automatically or forward data until removed.

Mitigation: Review and approve each function, trigger, destination, and network policy before use; remove automation when the task is complete.

Risk: Long-lived API keys or environment variables can expose account access.

Mitigation: Prefer OAuth and OS credential storage, avoid exporting MATON_API_KEY except where the CLI cannot be installed, and keep raw responses out of logs unless requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-mail)
- [Maton homepage](https://maton.ai)
- [Zoho Mail API Overview](https://www.zoho.com/mail/help/api/overview.html)
- [Zoho Mail API Index](https://www.zoho.com/mail/help/api/)
- [Email Messages API](https://www.zoho.com/mail/help/api/email-api.html)
- [Getting Started with Zoho Mail API](https://www.zoho.com/mail/help/api/getting-started-with-api.html)
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

**Other Properties Related to Output:** [May propose authenticated Zoho Mail API calls and Maton CLI operations; writes, connection changes, functions, and triggers require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
