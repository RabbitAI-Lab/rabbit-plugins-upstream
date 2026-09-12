## Description:

Use when someone needs word-level timestamps from audio for lyric alignment, cut-safe line boundaries, or caption source timing before burn-in with video-editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media-production agents use this skill to transcribe audio through the Replicate-hosted WhisperX model and obtain word-level timing for captions, lyrics, and edit boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends installing external skills with auto-accept and references unpinned skill packages.

Mitigation: Review and pin the skills CLI and PrunaAI skill references before running install commands; avoid auto-accept where possible and perform setup in a restricted environment.

Risk: The workflow requires a Replicate API token and may send user audio to an external transcription provider.

Mitigation: Provide only tokens and audio files appropriate for external processing, and avoid submitting sensitive audio unless approved for that provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/whisperx)
- [Replicate model: victor-upmeet/whisperx](https://replicate.com/victor-upmeet/whisperx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to JSON and SRT transcript outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to upload audio, call an external transcription provider, and write transcript artifacts for downstream caption or editing workflows.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
