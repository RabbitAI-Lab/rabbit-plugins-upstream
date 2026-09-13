## Description:

Klaviyo API integration with managed OAuth for accessing and managing profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, webhooks, tags, coupons, images, forms, reviews, and account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to manage Klaviyo customer data, email marketing assets, and approved automations through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Klaviyo customer and marketing data through a Maton-authenticated connection.

Mitigation: Install only when Maton access to the Klaviyo account is intended, prefer OAuth, keep authorization scopes narrow, and avoid logging or sharing full profile responses.

Risk: Write operations and persistent automations can change marketing data or trigger real customer-facing actions.

Mitigation: Review every write, connection creation, hosted function, trigger, and automation destination before approving it.

Risk: Raw HTTP fallback can expose long-lived credentials through environment variables, shell history, CI logs, or shared transcripts.

Mitigation: Use the CLI and OS credential store where possible; if raw HTTP is required, keep API keys out of logs, files, and shared command transcripts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/klaviyo)
- [Maton Homepage](https://maton.ai)
- [Klaviyo API Documentation](https://developers.klaviyo.com)
- [Klaviyo API Reference](https://developers.klaviyo.com/en/reference/api_overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, Python, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes read/list calls by default, explicit approval before writes, OAuth preference, scoped connections, and careful handling of customer data.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
