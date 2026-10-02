## Description:

Search YouTube videos, channels, playlists, and Shorts through YTAPI and retrieve transcripts for selected videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can find relevant YouTube content using search filters and read transcripts to research talks, tutorials, reviews, or creators' views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and transcript requests are sent to the third-party YTAPI service.

Mitigation: Use the skill only when sharing those queries and video identifiers with YTAPI is acceptable.

Risk: Optional account setup handles an email address, verification code, signup token, and API key.

Mitigation: Prefer creating the account and key yourself; provide the key through a secure secrets mechanism rather than chat.

Risk: Persistent API-key storage may expose credentials if saved in an unsuitable location.

Mitigation: Review where the key is stored and how to remove it; avoid shell-wide storage unless necessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ytapi/skills/ytapi-youtube-search)
- [YTAPI homepage](https://ytapi.dev)
- [YTAPI documentation](https://docs.ytapi.dev)
- [API key setup](artifact/references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with search results and transcript excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches can be filtered by date, duration, and sort order.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
