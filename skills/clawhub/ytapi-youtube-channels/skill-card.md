## Description:

Looks up YouTube channels, uploads, playlists, and video transcripts through the YTAPI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, researchers, and developers use this skill to inspect channel profiles, monitor new uploads, collect video lists from channels or playlists, and retrieve transcripts for summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account setup sends the user's email and verification code to YTAPI.

Mitigation: Obtain the user's consent before account creation, or use an existing API key instead.

Risk: A long-lived API key may persist across sessions without clear removal guidance.

Mitigation: Store the key through a secure secret mechanism; confirm its storage location and how to remove or revoke it.

## Reference(s):

- [YTAPI website](https://ytapi.dev)
- [YTAPI documentation](https://docs.ytapi.dev)
- [YTAPI batch requests](https://docs.ytapi.dev/batch/run)
- [API key setup](references/auth-setup.md)
- [ClawHub skill release](https://clawhub.ai/ytapi/skills/ytapi-youtube-channels)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown with channel and playlist results and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated results; YTAPI requests consume credits and may be rate-limited.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
