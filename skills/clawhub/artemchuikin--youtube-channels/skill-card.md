## Description:

Reach for this when a YouTube channel is the subject: a pasted @handle or channel URL, a creator's recent uploads, their full catalogue, or a search inside one channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up a YouTube creator's recent uploads, retrieve channel video catalogues, or search within a channel through TranscriptOut.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends YouTube channel handles, URLs, IDs, and search terms to TranscriptOut and may spend TranscriptOut credits.

Mitigation: Use the skill only when that data sharing and credit usage are acceptable for the task.

Risk: The skill requires a TranscriptOut API key and includes setup guidance for storing that credential.

Mitigation: Configure TRANSCRIPTOUT_API_KEY through a dedicated secret manager or trusted environment-secret mechanism, not through chat, shell profiles, or project files.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut authentication setup](references/auth-setup.md)
- [ClawHub release page](https://clawhub.ai/artemchuikin/skills/youtube-channels)
- [Publisher profile](https://clawhub.ai/user/artemchuikin)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TranscriptOut API responses and may consume TranscriptOut credits per request.]

## Skill Version(s):

1.0.0 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
