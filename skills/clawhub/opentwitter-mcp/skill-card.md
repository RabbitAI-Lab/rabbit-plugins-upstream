## Description:

Twitter/X data via the 6551 API. Supports user profiles, tweet search, user tweets, follower events, deleted tweets, and KOL followers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[infra403](https://clawhub.ai/user/infra403)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Twitter/X user profiles, tweets, searches, follower events, deleted tweets, watch lists, and real-time monitored account events through the 6551 API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X searches, account names, tweet IDs, watchlist choices, and OPENNEWS_TOKEN are sent to the 6551 service.

Mitigation: Use a dedicated token and only submit data that is acceptable to share with the service.

Risk: Watch-list and WebSocket features can create ongoing monitoring state for selected accounts.

Mitigation: Review monitored accounts before enabling subscriptions and periodically delete entries that are no longer needed.

Risk: The documented WebSocket URL places the token in the connection URL, which can be exposed through logs, browser history, or copied transcripts.

Mitigation: Avoid sharing or logging full WebSocket URLs and rotate the token if it may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/infra403/skills/opentwitter-mcp)
- [Publisher profile](https://clawhub.ai/user/infra403)
- [6551 API base URL](https://ai.6551.io)
- [OPENNEWS_TOKEN signup](http://app.newsliquid.com/mcp)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with curl examples and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and OPENNEWS_TOKEN; API responses and rate limits are controlled by the 6551 service.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; artifact metadata lists 1.0.0 and package.json lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
