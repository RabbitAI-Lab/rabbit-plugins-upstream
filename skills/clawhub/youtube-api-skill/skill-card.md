## Description:

YouTube Data API integration with managed OAuth for searching videos, managing playlists, accessing channel data, and interacting with comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent perform approved YouTube Data API tasks through Maton-managed authentication, including read/list workflows, playlist management, comments, and user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A YouTube connection may expose account data beyond the immediate task if broad OAuth scopes or unnecessary accounts are authorized.

Mitigation: Prefer OAuth, choose the narrowest available YouTube scopes, connect only accounts needed for the task, and revoke unused connections.

Risk: Writes, hosted functions, triggers, and destinations can modify data or keep acting after the original request is complete.

Mitigation: Require explicit user approval for every write, new connection, hosted function, trigger, destination, and invocation; review persistent destinations and delete them when no longer needed.

Risk: API keys, raw responses, and trigger payloads can expose credentials, personal data, or business data.

Mitigation: Prefer OAuth and OS credential storage, avoid exposing MATON_API_KEY, extract only task-relevant response fields, and do not log or forward raw payloads unless the user approved the exact destination and data flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/youtube-api-skill)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [YouTube Data API Overview](https://developers.google.com/youtube/v3)
- [YouTube Search API](https://developers.google.com/youtube/v3/docs/search/list)
- [YouTube Videos API](https://developers.google.com/youtube/v3/docs/videos)
- [YouTube Channels API](https://developers.google.com/youtube/v3/docs/channels)
- [YouTube Playlists API](https://developers.google.com/youtube/v3/docs/playlists)
- [YouTube PlaylistItems API](https://developers.google.com/youtube/v3/docs/playlistItems)
- [YouTube Subscriptions API](https://developers.google.com/youtube/v3/docs/subscriptions)
- [YouTube Comments API](https://developers.google.com/youtube/v3/docs/comments)
- [YouTube Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown guidance with shell command, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for writes, new connections, hosted functions, and persistent automation.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
