## Description:

Apify provides a managed-authentication integration for using Maton to run Apify actors and web scrapers, manage datasets, key-value stores, request queues, schedules, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to interact with Apify from an agent through Maton-managed authentication. It supports read-first API workflows, approved write operations, actor runs, storage management, schedules, webhooks, hosted functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact account actions through the user's Apify connection, including writes, actor runs, schedules, webhooks, hosted functions, and trigger destinations.

Mitigation: Require explicit user approval after checking the account, resource IDs, payload, destination host, and whether the automation persists after the chat ends.

Risk: Long-lived API keys can be exposed if raw HTTP access is used instead of the Maton CLI OAuth flow.

Mitigation: Prefer OAuth, avoid printing or persisting keys, pass secrets only through the process environment when raw HTTP is necessary, and rotate any exposed key.

Risk: Persistent schedules, webhooks, hosted functions, and triggers can keep operating after the conversation ends.

Mitigation: Create persistent automation only when the user asks for it by name, confirm the exact destination and scope, and include cleanup or deletion when the task is complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/apify-api)
- [Maton Homepage](https://maton.ai)
- [Apify API Reference](https://docs.apify.com/api/v2)
- [Apify Actors API](https://docs.apify.com/actors)
- [Apify Storage API](https://docs.apify.com/storage)
- [Apify Schedules API](https://docs.apify.com/schedules)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Format:** [Markdown guidance with inline shell commands, code blocks, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples for environments without the CLI, and least-privilege approval guidance for account actions.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence; skill frontmatter metadata is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
