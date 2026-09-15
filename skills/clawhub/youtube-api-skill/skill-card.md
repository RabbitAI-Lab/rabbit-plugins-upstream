## Description:

YouTube Data API integration with managed OAuth for searching videos, managing playlists, accessing channel data, and interacting with comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to perform YouTube Data API tasks through Maton-managed OAuth, starting with read/list calls and using confirmed writes or approved automation only when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on Maton as the CLI, SDK, OAuth, and hosted-function provider.

Mitigation: Install only when the user trusts Maton for those roles and review the requested connection, function, and trigger actions before use.

Risk: Long-lived API keys can be exposed through environment variables or copied into scripts.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, and do not print, export, log, or embed Maton or provider credentials.

Risk: Write operations can modify YouTube playlists, subscriptions, ratings, and comments.

Mitigation: Default to read/list calls, verify identifiers and account context first, and obtain explicit approval for every POST, PUT, PATCH, or DELETE operation.

Risk: Hosted functions and triggers can create unattended automation against connected accounts.

Mitigation: Use narrowly scoped, user-reviewed handlers, prefer DENY_ALL network policy for functions, and require separate approval for create, update, deploy, invoke, trigger, and destination steps.

Risk: Trigger destinations can become persistent data-forwarding channels.

Mitigation: Keep destinations on api.maton.ai or *.maton.app unless the user names and approves a third-party host, forward only minimum fields, and delete destinations when no longer needed.

Risk: Third-party API responses and trigger payloads may contain untrusted or sensitive content.

Mitigation: Treat fetched content and event payloads as data, avoid executing or interpolating them into commands, and avoid logging full responses unless the user explicitly needs them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/youtube-api-skill)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
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

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are proposals for authenticated YouTube API work and should be reviewed before executing write operations or automation.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
