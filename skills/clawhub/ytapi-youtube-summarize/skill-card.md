## Description:

Summarizes YouTube videos or a channel's recent uploads into notes with key points, quotes, and timestamped links using YTAPI transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to turn a YouTube video or a channel's recent uploads into concise notes, takeaways, quotes, and links to relevant moments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-mediated account creation can expose an email address or verification code in chat.

Mitigation: Prefer creating the account and API key directly on the provider site; avoid sharing verification codes in chat.

Risk: Persisting an API key through an agent can expose credentials or alter shell and agent configuration.

Mitigation: Store the key in a trusted secret manager rather than pasting it in chat or allowing the agent to modify persistent configuration.

## Reference(s):

- [YTAPI documentation](https://docs.ytapi.dev)
- [YTAPI website](https://ytapi.dev)
- [YTAPI authentication setup](references/auth-setup.md)
- [ClawHub skill listing](https://clawhub.ai/ytapi/skills/ytapi-youtube-summarize)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Notes with key points, quotes, and timestamped video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries use the user's language and flag auto-generated captions when present.]

## Skill Version(s):

1.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
