## Description:

YouTube Analytics API integration with managed OAuth for retrieving channel analytics reports and managing video, playlist, and channel groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to query YouTube channel performance metrics, analyze results by dimensions such as day, country, or video, and manage YouTube Analytics groups through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects a YouTube/Google account through Maton and can access channel analytics for connected accounts.

Mitigation: Install only when that connection path is acceptable, prefer OAuth over API keys, review requested Google scopes, and connect only the accounts needed for the task.

Risk: Group creation, update, deletion, and connection deletion can change or revoke resources and may be irreversible.

Mitigation: Require explicit confirmation with the exact connection, group, or item identifier before any create, update, delete, or connection deletion action.

Risk: When multiple Maton or YouTube Analytics connections exist, an ambiguous default could send a request to the wrong account.

Mitigation: Specify the intended Maton profile and YouTube Analytics connection whenever more than one account or connection is available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/youtube-analytics-api)
- [Maton Homepage](https://maton.ai)
- [YouTube Analytics API Overview](https://developers.google.com/youtube/analytics)
- [YouTube Analytics API Reference](https://developers.google.com/youtube/analytics/reference)
- [YouTube Analytics Channel Reports](https://developers.google.com/youtube/analytics/channel_reports)
- [YouTube Analytics Metrics](https://developers.google.com/youtube/analytics/metrics)
- [YouTube Analytics Dimensions](https://developers.google.com/youtube/analytics/dimensions)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user confirmation before connection creation or write actions.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
