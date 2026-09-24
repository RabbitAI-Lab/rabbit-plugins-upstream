## Description:

YouTube Analytics API integration with managed OAuth for retrieving channel analytics reports and managing video, playlist, and channel groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to authenticate YouTube Analytics through Maton, query channel performance metrics by dimensions such as day, country, or video, and manage analytics groups with user-approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the integration gives Maton access to the selected YouTube Analytics account within the approved connection scopes.

Mitigation: Confirm the user intends to authorize the account, select only the scopes needed for the task when scope selection is offered, and use read-only reporting calls by default.

Risk: Write operations can create, update, or delete analytics groups, group items, connections, functions, triggers, or destinations.

Mitigation: Require explicit user approval before any write, connection creation, deletion, function deployment, trigger change, or destination change; list current resources first to verify identifiers and account context.

Risk: Raw API keys, hosted functions, triggers, and outbound destinations can increase credential exposure or unattended automation risk.

Mitigation: Prefer OAuth and the Maton credential store, avoid embedding credentials in destination headers or bodies, deploy functions with DENY_ALL unless the user approves specific hosts, and remove automation that is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/youtube-analytics-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [YouTube Analytics API Overview](https://developers.google.com/youtube/analytics)
- [YouTube Analytics API Reference](https://developers.google.com/youtube/analytics/reference)
- [YouTube Analytics Channel Reports](https://developers.google.com/youtube/analytics/channel_reports)
- [YouTube Analytics Metrics](https://developers.google.com/youtube/analytics/metrics)
- [YouTube Analytics Dimensions](https://developers.google.com/youtube/analytics/dimensions)
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

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with command examples, configuration guidance, code snippets, and API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved YouTube Analytics connection.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
