## Description:

Twitter/X data via the 6551 API. Supports user profiles, tweet search, user tweets, follower events, deleted tweets, and KOL followers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[infra403](https://clawhub.ai/user/infra403)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use opentwitter to query Twitter/X profile, tweet, follower, deleted tweet, watchlist, and real-time event data through the 6551 API using an OPENNEWS_TOKEN.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a reusable OPENNEWS_TOKEN credential and documents a WebSocket URL that can carry the token.

Mitigation: Use a narrowly scoped, revocable token; prefer HTTPS for token provisioning; and avoid sharing logs, prompts, or WebSocket URLs that contain credentials.

Risk: Watchlist add/delete and subscription operations can create or change server-side monitoring.

Mitigation: Run monitoring operations only when the user explicitly intends to create, change, or remove monitoring, and review the target username and event flags before execution.

Risk: The security verdict is suspicious because the skill documents credentialed Twitter/X data access and persistent monitoring behavior.

Mitigation: Review the skill before installing or deploying it, and keep token scope, retention, and operational access limited to the intended use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/infra403/skills/opentwitter-mcp)
- [6551 API base URL](https://ai.6551.io)
- [OPENNEWS_TOKEN provisioning](http://app.newsliquid.com/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with curl commands and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and OPENNEWS_TOKEN; API responses depend on the 6551 service and Twitter/X data availability.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
