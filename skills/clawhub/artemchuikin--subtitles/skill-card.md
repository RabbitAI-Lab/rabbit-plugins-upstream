## Description:

Reach for this when subtitles are wanted from a YouTube video: following foreign-language content, reading along, translating speech, language practice, or exporting ready SRT/VTT files. Skip it for uploading subtitles or account chores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch YouTube subtitles through TranscriptOut for reading, translation, language practice, or SRT/VTT export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may involve account signup, OTP handling, API-key handling, and persistent secret storage by the agent.

Mitigation: Create the TranscriptOut account and API key yourself when possible, store the key in a scoped secret manager, and revoke any key that is pasted into chat or stored too broadly.

Risk: Using the skill requires sending YouTube video identifiers or URLs to the TranscriptOut API.

Mitigation: Review video URLs before use and avoid sending private or sensitive video identifiers unless that disclosure is acceptable.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API transcript endpoint](https://api.transcriptout.com/v1/transcript)
- [TranscriptOut authentication setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/subtitles)
- [Publisher profile](https://clawhub.ai/user/artemchuikin)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, plain text, SRT, or VTT API outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
