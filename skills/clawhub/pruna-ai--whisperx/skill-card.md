## Description:

Use when someone needs word-level timestamps from audio for lyric alignment, line boundary timing, or caption source timing before video editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media-production agents use this skill to obtain word-level audio transcripts for lyric alignment, caption timing, and video edit cut planning with WhisperX via Replicate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Replicate API token and upload the selected audio to Replicate for processing.

Mitigation: Confirm user consent before uploading audio, avoid sensitive audio unless approved, and keep tokens in environment variables rather than chat or committed files.

Risk: Optional npx skills add commands fetch current remote skill content before use.

Mitigation: Review the source and installed skill content before running or relying on fetched commands.

## Reference(s):

- [ClawHub skill page: whisperx](https://clawhub.ai/pruna-ai/skills/whisperx)
- [Replicate model: victor-upmeet/whisperx](https://replicate.com/victor-upmeet/whisperx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and Replicate request parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in transcript JSON and SRT timing files when the helper pipeline is used.]

## Skill Version(s):

1.0.11 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
