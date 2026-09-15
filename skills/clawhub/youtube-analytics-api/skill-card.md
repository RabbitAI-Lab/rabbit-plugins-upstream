## Description:

YouTube Analytics API integration with managed OAuth for retrieving channel analytics reports and managing video, playlist, and channel groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query YouTube channel metrics, analyze performance by dimensions such as day, country, and video, and manage YouTube Analytics groups through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Maton CLI or SDK authentication and can access data allowed by the user's YouTube Analytics connection.

Mitigation: Install only if the user trusts Maton and its CLI/SDK distribution, prefer OAuth over API keys, and use only the connection needed for the current task.

Risk: Group management, connection creation, function deployment, and trigger creation can change resources or create ongoing automation.

Mitigation: Keep ordinary analytics work to read/list calls and require explicit confirmation before creating connections, modifying groups, deploying functions, or creating triggers.

Risk: Trigger destinations can create persistent forwarding of event data to a URL.

Mitigation: Avoid third-party trigger destinations unless the user intentionally wants ongoing forwarding and has reviewed the exact URL, owner, fields sent, credentials, and deletion plan.

Risk: Analytics responses and trigger payloads can include sensitive or third-party data.

Mitigation: Extract only the fields needed for the task, avoid dumping full responses into logs or files, and avoid placing credentials in destination headers or body templates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/youtube-analytics-api)
- [Maton Homepage](https://maton.ai)
- [YouTube Analytics API Overview](https://developers.google.com/youtube/analytics)
- [YouTube Analytics API Reference](https://developers.google.com/youtube/analytics/reference)
- [YouTube Analytics Channel Reports](https://developers.google.com/youtube/analytics/channel_reports)
- [YouTube Analytics Metrics](https://developers.google.com/youtube/analytics/metrics)
- [YouTube Analytics Dimensions](https://developers.google.com/youtube/analytics/dimensions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Maton CLI commands, HTTP examples, JSON payloads, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include YouTube Analytics API paths, connection and trigger configuration guidance, and explicit approval gates for writes or automation.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
