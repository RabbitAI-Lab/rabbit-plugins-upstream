## Description:

Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, drafts, and approved Gmail automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent interact with a connected Gmail account through Maton-managed OAuth, including read/list workflows, user-approved message sends, label and draft management, and narrowly scoped hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Gmail content through a connected account.

Mitigation: Install only when the publisher and Maton account are trusted, prefer OAuth, select the narrowest Gmail scopes available, and avoid exposing raw responses unless needed for the task.

Risk: Write operations such as send, delete, label, draft, connection, function, and trigger changes can affect user data or create ongoing automation.

Mitigation: Confirm each write or new connection with the user, list or read current state first, and verify exact identifiers before destructive or persistent changes.

Risk: Triggers and destinations can forward future email events continuously.

Mitigation: Scope triggers narrowly, prefer Maton-hosted destinations, disclose the destination host and transmitted fields, and forward only the minimum fields required.

Risk: API keys are long-lived credentials and may be exposed through environment variables or logs.

Mitigation: Prefer OAuth and the operating system credential store; use raw HTTP and MATON_API_KEY only where the CLI cannot be installed, and never print, search, or persist credential values.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/gmail)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Gmail API Overview](https://developers.google.com/gmail/api/reference/rest)
- [Gmail List Messages](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list)
- [Gmail Get Message](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get)
- [Gmail Send Message](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)
- [Gmail List Threads](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/list)
- [Gmail List Labels](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list)
- [Gmail Create Draft](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, HTTP examples, JSON examples, and short code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may describe authenticated Gmail API calls, Maton CLI workflows, hosted function snippets, trigger configuration, and security checks for OAuth scopes and user approvals.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
