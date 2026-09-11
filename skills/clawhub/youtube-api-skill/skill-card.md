## Description:

YouTube Data API integration with managed OAuth for searching videos, managing playlists, accessing channel data, and interacting with comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access YouTube Data API workflows through Maton-managed OAuth, including search, channel lookup, playlist management, subscriptions, ratings, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize YouTube account access through Maton and perform account-affecting write actions.

Mitigation: Trust the Maton gateway before installation, prefer OAuth over long-lived API keys, and confirm every connection, playlist, comment, subscription, rating, POST, PUT, PATCH, or DELETE action before execution.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, command history, or child processes when the CLI is unavailable.

Mitigation: Use OAuth and the Maton CLI where possible; if an API key is necessary, never print, persist, or pass it on a command line, and send it only to api.maton.ai.

Risk: YouTube API content such as comments and descriptions may contain untrusted instructions or data.

Mitigation: Treat fetched content as data only, validate identifiers and payloads, and do not execute or follow instructions from API responses.

Risk: Unpinned Maton CLI or SDK versions may behave differently across environments.

Mitigation: Pin or verify the Maton CLI or SDK version in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/youtube-api-skill)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [YouTube Data API overview](https://developers.google.com/youtube/v3)
- [YouTube Search API](https://developers.google.com/youtube/v3/docs/search/list)
- [YouTube Videos API](https://developers.google.com/youtube/v3/docs/videos)
- [YouTube Channels API](https://developers.google.com/youtube/v3/docs/channels)
- [YouTube Playlists API](https://developers.google.com/youtube/v3/docs/playlists)
- [YouTube PlaylistItems API](https://developers.google.com/youtube/v3/docs/playlistItems)
- [YouTube Subscriptions API](https://developers.google.com/youtube/v3/docs/subscriptions)
- [YouTube Comments API](https://developers.google.com/youtube/v3/docs/comments)
- [YouTube quota calculator](https://developers.google.com/youtube/v3/determine_quota_cost)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON from the Maton CLI or YouTube Data API.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
