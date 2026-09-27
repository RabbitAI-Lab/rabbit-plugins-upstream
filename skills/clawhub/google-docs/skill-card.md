## Description:

Google Docs API integration with managed OAuth for creating documents, inserting text, applying formatting, managing document content, and configuring approved Maton-based automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with a user's authorized Google Docs account through Maton, including document reads, document creation, content updates, formatting, and user-approved automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access the selected Google Docs account through the user's authorized Maton connection.

Mitigation: Prefer OAuth, review requested scopes and the connection ID, and install only when that account access is acceptable.

Risk: Write operations and automation setup can change documents or continue moving data after initial configuration.

Mitigation: Confirm every write, function, trigger, destination, and automation setup with the user, and remove automation when it is no longer needed.

Risk: Raw API keys are long-lived credentials and can be exposed through environment variables, logs, or copied commands.

Mitigation: Use OAuth where possible, avoid raw API keys unless the CLI cannot be installed, and rotate any key that was printed, committed, or pasted into an unsafe location.

## Reference(s):

- [ClawHub Google Docs Skill](https://clawhub.ai/byungkyu/skills/google-docs)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Docs API Overview](https://developers.google.com/docs/api/how-tos/overview)
- [Google Docs Get Document](https://developers.google.com/docs/api/reference/rest/v1/documents/get)
- [Google Docs Create Document](https://developers.google.com/docs/api/reference/rest/v1/documents/create)
- [Google Docs Batch Update](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate)
- [Google Docs Request Types](https://developers.google.com/docs/api/reference/rest/v1/documents/request)
- [Google Docs Document Structure](https://developers.google.com/docs/api/concepts/structure)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, user-authorized Google Docs connection, and user confirmation for writes or automation setup.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
