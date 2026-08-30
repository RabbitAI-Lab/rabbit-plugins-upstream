## Description:

YouTube Analytics API integration with managed OAuth for retrieving channel analytics reports and managing video, playlist, and channel groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query YouTube channel metrics, analyze performance by dimensions such as day, country, or video, and manage YouTube Analytics groups through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the wrong account or broader access than needed can expose YouTube Analytics data beyond the current task.

Mitigation: Use OAuth when possible, choose the narrowest available scopes, and confirm the intended account before creating a connection.

Risk: Create, update, or delete operations on groups can modify channel analytics organization.

Mitigation: Default to read and list calls, then require explicit user approval with the target resource and intended effect before any write.

Risk: Using a long-lived API key can increase credential exposure through logs, shell history, or child processes.

Mitigation: Prefer Maton OAuth; if an API key is unavoidable, do not print, persist, or pass it on the command line.

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

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and an active YouTube Analytics connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
