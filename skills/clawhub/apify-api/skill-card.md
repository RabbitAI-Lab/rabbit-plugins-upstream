## Description:

Access the Apify API with managed authentication to run web scrapers and actors and manage datasets, key-value stores, request queues, schedules, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to operate Apify through Maton-managed authentication, including actor runs, storage access, schedules, webhooks, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Actor runs can consume Apify compute units on the connected account.

Mitigation: Confirm the intended actor, inputs, account, and expected cost impact before starting actor runs.

Risk: Schedules, webhooks, triggers, and destinations can create persistent automation or ongoing data forwarding.

Mitigation: Require explicit user approval, show the target resource or destination host, and review existing persistent resources before creating or modifying them.

Risk: Long-lived API keys and package installs increase credential and supply-chain exposure.

Mitigation: Prefer OAuth, official Maton package channels, pinned versions, and least-privilege environments without elevated install privileges.

Risk: API responses and trigger payloads can contain personal, business, or adversarial content.

Mitigation: Treat fetched content as untrusted data, avoid logging full payloads, and extract only fields needed for the user's task.

## Reference(s):

- [ClawHub Apify Skill](https://clawhub.ai/byungkyu/skills/apify-api)
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
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API calls and automation steps that require user confirmation before writes, actor runs, schedules, webhooks, functions, triggers, or destinations.]

## Skill Version(s):

1.2.3 (source: server release metadata; frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
