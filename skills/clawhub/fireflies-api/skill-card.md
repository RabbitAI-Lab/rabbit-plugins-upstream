## Description:

Fireflies.ai GraphQL API integration with managed OAuth for accessing meeting transcripts, summaries, users, contacts, and AI-powered meeting analysis through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Fireflies.ai account through Maton, retrieve and analyze meeting data, and create narrowly approved Fireflies automations when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting transcripts, summaries, contacts, and AskFred queries can expose sensitive business or personal data.

Mitigation: Use only the intended Fireflies connection and account, prefer read-only or scoped access, extract only the fields needed for the task, and avoid dumping full raw responses.

Risk: Writes, connection changes, hosted functions, triggers, and destinations can modify data or create persistent automation.

Mitigation: Get explicit user approval for the exact target, payload, destination, and intended effect; start with read or list calls before changes.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, command lines, or persisted files.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, and use raw HTTP with MATON_API_KEY only where the CLI cannot be installed.

Risk: Trigger destinations can continuously forward event data from connected applications to another URL.

Mitigation: Confirm the destination host and transmitted fields with the user, minimize payloads with templates, and prefer Maton-controlled destinations when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/fireflies-api)
- [Maton homepage](https://maton.ai)
- [Fireflies API Documentation](https://docs.fireflies.ai/)
- [Fireflies GraphQL API Reference](https://docs.fireflies.ai/graphql-api)
- [Fireflies Developer Program](https://docs.fireflies.ai/getting-started/developer-program)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API calls, Configuration]

**Output Format:** [Markdown with bash, JSON, GraphQL, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-scoped instructions and examples for authenticated Fireflies requests; raw API responses may contain sensitive meeting data and should be minimized.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
