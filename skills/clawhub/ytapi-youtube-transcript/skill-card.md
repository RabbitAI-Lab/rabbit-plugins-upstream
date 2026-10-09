## Description:

Retrieves YouTube video captions through YTAPI for reading, summarizing, translating, searching, or exporting as transcripts and subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers retrieve captioned YouTube videos as readable transcripts, timestamped text, or subtitles for review, summarization, translation, and search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can create an external YTAPI account using the user's email and verification code.

Mitigation: Get the user's agreement before account creation, or ask them to create the account and provide a key themselves.

Risk: The setup asks the agent to keep an API key available across future sessions.

Mitigation: Use a secrets manager or session-scoped environment variable rather than storing the key broadly for future shells.

## Reference(s):

- [YTAPI authentication setup](references/auth-setup.md)
- [YTAPI documentation](https://docs.ytapi.dev)
- [YTAPI homepage](https://ytapi.dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Subtitle files]

**Output Format:** [Plain text, Markdown, timestamped JSON, SRT, or VTT]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Language selection and optional word-level timestamps; requires a YTAPI API key and uses credits for successful requests.]

## Skill Version(s):

1.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
