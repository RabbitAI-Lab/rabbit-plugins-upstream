## Description:

ManyChat API integration with managed authentication for managing subscribers, tags, custom fields, Facebook Messenger messages, and bot automation through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to connect an agent to ManyChat through Maton, inspect account and subscriber data, manage tags and custom fields, send approved messages, and build approved hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ManyChat account access and stored Maton credentials can expose subscriber, messaging, tag, and automation data.

Mitigation: Use OAuth when possible, create or select the exact connection with user approval, choose only needed scopes, and remove stale or unused connections.

Risk: Write operations and message sends can modify ManyChat state or contact users.

Mitigation: Default to read and list calls, then obtain explicit confirmation before POST, PUT, PATCH, DELETE, imports, tag changes, custom-field updates, flow sends, or message sends.

Risk: Hosted functions and triggers can turn a one-time ManyChat action into ongoing automation.

Mitigation: Deploy only user-authored or user-reviewed handlers, use DENY_ALL network policy unless specific hosts are approved, minimize forwarded fields, and delete functions or triggers when no longer needed.

Risk: Raw HTTP mode requires handling a long-lived Maton API key in the process environment.

Mitigation: Use raw HTTP only where the CLI cannot be installed, never print or persist the key, send it only to api.maton.ai, and rotate it if it is exposed.

## Reference(s):

- [ManyChat API Documentation](https://api.manychat.com/swagger)
- [ManyChat API Key Generation Guide](https://help.manychat.com/hc/en-us/articles/14959510331420)
- [ManyChat Dev Program](https://help.manychat.com/hc/en-us/articles/14281269835548)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, Python snippets, and API endpoint descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTPS request examples, hosted function handlers, trigger configuration guidance, and least-privilege approval prompts.]

## Skill Version(s):

1.2.6 (source: server release metadata; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
