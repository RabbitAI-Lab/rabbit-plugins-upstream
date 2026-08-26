## Description:

Use this skill to search YouTube for videos or channels on a topic or to look up a channel by name or handle through TranscriptOut.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to discover relevant YouTube videos, channels, tutorials, talks, and reviews before selecting results for deeper review or transcript retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may handle and persistently store a live TranscriptOut API credential.

Mitigation: Use a platform secret manager when available, avoid pasting live keys into chat, and confirm where TRANSCRIPTOUT_API_KEY is stored before installation.

Risk: Users may need to revoke or rotate the credential after setup or exposure.

Mitigation: Confirm the revocation path in TranscriptOut before use and rotate the API key if it was shared in an unsafe channel.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut auth setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/youtube-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples and JSON API response envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output is metadata-oriented and may include pagination fields, remaining-credit headers, and error codes from the TranscriptOut API.]

## Skill Version(s):

1.0.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
