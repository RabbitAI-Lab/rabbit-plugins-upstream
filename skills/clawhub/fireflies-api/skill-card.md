## Description:

Fireflies.ai GraphQL API integration with managed OAuth for retrieving meeting transcripts, summaries, users, contacts, and AI-powered meeting analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Fireflies.ai account through Maton, query meeting transcripts and metadata, analyze meeting content with AskFred, and manage meeting recordings. It supports read-first API workflows and user-approved changes or automations involving Fireflies data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived Maton API keys can leak through process environments, logs, shell history, or copied output.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is necessary, never print, persist, or pass the key on a command line and send it only to api.maton.ai.

Risk: Write, delete, connection, hosted function, and trigger destination operations can change meeting data or create ongoing forwarding.

Mitigation: Require explicit approval for each such action, confirm the exact target and payload, use least-privilege scopes, and keep hosted functions on DENY_ALL network policy unless the user approves named hosts.

Risk: Meeting transcripts, AskFred results, and trigger payloads may contain personal, confidential, or broad cross-meeting data.

Mitigation: Filter requests narrowly, extract only fields needed for the task, summarize instead of dumping raw transcripts, and avoid forwarding data to third-party hosts unless the user explicitly approves the destination and data flow.

## Reference(s):

- [Fireflies API Documentation](https://docs.fireflies.ai/)
- [Fireflies GraphQL API Reference](https://docs.fireflies.ai/graphql-api)
- [Fireflies Developer Program](https://docs.fireflies.ai/getting-started/developer-program)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell, GraphQL, HTTP, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved Fireflies connection; API responses may include meeting data and should be limited to fields needed for the task.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
