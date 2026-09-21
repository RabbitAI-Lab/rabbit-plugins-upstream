## Description:

Reach for this when a video needs to become text: a pasted YouTube link or ID, a transcribe/summarize/translate request, mining a video for facts, or a bare URL shared with 'what does this say?'. Skip it for uploads and account chores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to fetch YouTube transcripts through TranscriptOut for transcription, summarization, translation, fact extraction, and timestamp-aware review when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can expose or persist TranscriptOut API secrets in unsafe locations.

Mitigation: Create and store the API key through a trusted secret manager or approved environment-secret mechanism, and avoid pasting keys into ordinary chat.

Risk: YouTube video identifiers are sent to TranscriptOut and transcript requests may consume account credits.

Mitigation: Use the skill only for videos you are comfortable disclosing to TranscriptOut, and request transcripts selectively to control credit usage.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API Key Setup](references/auth-setup.md)
- [ClawHub Skill Page](https://clawhub.ai/artemchuikin/skills/video-transcript)
- [Publisher Profile](https://clawhub.ai/user/artemchuikin)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples and transcript text or JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com; transcript requests consume TranscriptOut credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
