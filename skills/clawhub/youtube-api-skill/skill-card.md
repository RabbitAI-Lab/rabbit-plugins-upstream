## Description:

YouTube Data API integration with managed OAuth for searching videos, managing playlists, accessing channel data, and interacting with comments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access YouTube Data API v3 through Maton-managed OAuth for search, channel, playlist, subscription, video, and comment workflows. It is suited to account-scoped YouTube tasks where read/list operations are preferred and writes require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on the connected YouTube account through Maton.

Mitigation: Approve OAuth connections only for the intended account, specify the target connection when multiple accounts exist, and prefer read-only scopes when possible.

Risk: Comments, subscriptions, playlist edits, ratings, deletes, and other writes can modify account or public YouTube state.

Mitigation: Require explicit confirmation before write operations and verify the target resource, payload, and intended effect before execution.

Risk: Long-lived API keys or provider-issued tokens could leak if printed, persisted, or passed through commands.

Mitigation: Use Maton OAuth and the operating system credential store where possible; do not print, log, persist, or transmit credentials outside the intended Maton API flow.

## Reference(s):

- [ClawHub YouTube Skill](https://clawhub.ai/byungkyu/skills/youtube-api-skill)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [YouTube Data API Overview](https://developers.google.com/youtube/v3)
- [YouTube Data API Search](https://developers.google.com/youtube/v3/docs/search/list)
- [YouTube Data API Videos](https://developers.google.com/youtube/v3/docs/videos)
- [YouTube Data API Playlists](https://developers.google.com/youtube/v3/docs/playlists)
- [YouTube Data API Comments](https://developers.google.com/youtube/v3/docs/comments)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide Maton CLI and API usage; API responses are typically JSON.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter lists 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
