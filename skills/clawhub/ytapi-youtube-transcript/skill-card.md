## Description:

Retrieves YouTube transcripts and captions through YTAPI in text, Markdown, timestamped JSON, SRT, or VTT formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers retrieve captions from YouTube videos to read, summarize, quote, translate, search, or create timestamped subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-assisted signup involves the user's email and verification code.

Mitigation: Prefer creating the YTAPI account and API key yourself before providing the key to the agent.

Risk: Temporary signup files and a key persisted across sessions can expose reusable credentials.

Mitigation: Provide the key through a secret manager rather than chat; review where it is stored, remove temporary files, and revoke the key if exposed.

## Reference(s):

- [YTAPI documentation](https://docs.ytapi.dev)
- [YTAPI homepage](https://ytapi.dev)
- [API key setup](references/auth-setup.md)
- [ClawHub skill listing](https://clawhub.ai/ytapi/skills/ytapi-youtube-transcript)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, SRT subtitles, VTT subtitles, Configuration guidance]

**Output Format:** [Plain text, Markdown, timestamped JSON, SRT, or VTT]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language preference and optional word-level timestamps; requires a YTAPI API key and available captions.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
