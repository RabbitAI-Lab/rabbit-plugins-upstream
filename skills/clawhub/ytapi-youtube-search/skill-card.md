## Description:

Search YouTube videos, channels, playlists, and Shorts through YTAPI, filter results, and retrieve video transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

People researching YouTube content use this skill to find relevant videos, channels, playlists, or Shorts and read selected video transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional account setup shares the user's email address and verification code with YTAPI.

Mitigation: Ask for consent first; users can instead create an account themselves and provide an API key only when needed.

Risk: The setup flow may persist a long-lived API key across sessions.

Mitigation: Prefer a secrets store or session-only key when requested; never print the key, and remove temporary signup files.

## Reference(s):

- [YTAPI documentation](https://docs.ytapi.dev)
- [YTAPI authentication setup](references/auth-setup.md)
- [YTAPI website](https://ytapi.dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown search results and transcript-based answers, with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search and transcript requests use YTAPI credits.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
