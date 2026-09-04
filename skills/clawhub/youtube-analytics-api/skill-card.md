## Description:

YouTube Analytics API integration with managed OAuth for retrieving channel analytics reports and managing video, playlist, and channel groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query YouTube channel performance metrics, analyze results by dimensions such as date, country, or video, and manage analytics groups through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the integration grants Maton access to the relevant YouTube Analytics account.

Mitigation: Prefer OAuth, review requested Google scopes, and connect only the account needed for the current task.

Risk: Group creation, updates, deletion, or connection changes can alter analytics organization or account access.

Mitigation: Require explicit user confirmation before any group management operation, connection creation, connection deletion, or non-read API call.

Risk: Multiple Maton or YouTube Analytics connections can route requests to the wrong account.

Mitigation: Use a specific Maton profile and connection identifier whenever more than one account or connection is available.

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

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, SDK snippets, API request paths, and summarized API responses.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
