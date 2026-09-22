## Description:

Fetch YouTube video subtitles through TranscriptOut as timed JSON segments, plain text, or ready SRT/VTT output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve subtitles from YouTube videos for reading, translation, language practice, timestamped analysis, or SRT/VTT export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may ask an agent to handle sign-in codes and API keys.

Mitigation: Configure TRANSCRIPTOUT_API_KEY through a trusted secret manager yourself; do not paste API keys or email verification codes into chat, and rotate any exposed key.

Risk: Using the skill sends video identifiers and subtitle options to TranscriptOut.

Mitigation: Install and use the skill only when that third-party data sharing is acceptable for the videos being processed.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API key setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/subtitles)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and TranscriptOut responses that may contain JSON, plain text, SRT, or VTT transcript content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and network access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
