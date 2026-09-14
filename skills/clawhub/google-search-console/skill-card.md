## Description:

Google Search Console API integration with managed OAuth for querying search analytics, managing sitemaps, and monitoring site performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access authorized Google Search Console data through Maton, inspect search performance, and manage site and sitemap workflows with approval-gated writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to Google Search Console through Maton and can access account data authorized by the user's connection.

Mitigation: Review the exact account and connection before use, prefer OAuth, select the least privilege scope available, and revoke unused connections.

Risk: Write operations, hosted functions, triggers, and persistent destinations can change data or create ongoing automation.

Mitigation: Require explicit approval for connection creation, writes, function deployment or invocation, trigger setup, destination URLs, payload fields, and persistence.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Use the CLI when available; otherwise keep the key in the runtime environment only, do not print or persist it, and send it only to api.maton.ai.

Risk: Trigger destinations can forward sensitive event data to external hosts.

Mitigation: Keep function network policy at DENY_ALL unless a host is specifically needed, prefer Maton-hosted destinations, and avoid third-party destinations for sensitive event data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-search-console)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Search Console API Reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [Search Console List Sites](https://developers.google.com/webmaster-tools/v1/sites/list)
- [Search Console Search Analytics](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [Search Console Sitemaps](https://developers.google.com/webmaster-tools/v1/sitemaps)
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

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list workflows and request explicit user approval before connection creation, writes, hosted functions, triggers, or persistent destinations.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
