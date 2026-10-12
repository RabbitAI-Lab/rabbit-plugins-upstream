## Description:

Looks up YouTube channels and playlists through YTAPI to retrieve profiles, uploads, playlist videos, and transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, researchers, and developers use this skill to research YouTube channels, monitor new uploads, and collect playlist videos or transcripts for summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can let an agent create an account using the user's email and verification code.

Mitigation: Prefer creating the account and API key in the provider's UI; obtain explicit consent before any agent-led signup.

Risk: The setup flow can persist an API key for future sessions.

Mitigation: Provide the key only for the current session unless persistence is explicitly approved; confirm where it will be stored and how to revoke or delete it.

## Reference(s):

- [YTAPI documentation](https://docs.ytapi.dev)
- [YTAPI batch requests](https://docs.ytapi.dev/batch/run)
- [YTAPI homepage](https://ytapi.dev)
- [Authentication setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with API request examples and summaries of retrieved data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API requests require a YTAPI key; paginated requests and transcripts consume credits.]

## Skill Version(s):

1.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
