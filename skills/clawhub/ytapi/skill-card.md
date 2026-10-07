## Description:

Retrieves YouTube transcripts, video details, search results, channels, and playlists through the YTAPI service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can research YouTube videos and creators, retrieve captions for summaries or quotations, and explore channel uploads and playlists. This skill does not upload videos or manage YouTube accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-led registration sends your email and verification code to YTAPI.

Mitigation: Create the account and API key yourself if you prefer not to share verification details with the agent.

Risk: Persistently stored API credentials may remain accessible across sessions.

Mitigation: Store the key in a dedicated secrets manager or a session-scoped environment variable.

## Reference(s):

- [YTAPI homepage](https://ytapi.dev)
- [YTAPI documentation](https://docs.ytapi.dev)
- [API key setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown, with transcript timestamps or subtitles when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video, channel, playlist, and search data can be summarized or quoted.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
