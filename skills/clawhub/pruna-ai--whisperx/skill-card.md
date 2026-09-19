## Description:

Use when someone needs word-level timestamps from audio for lyric alignment, cut-safe line boundaries, or caption source timing before burn-in with video editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content production agents use this skill to transcribe audio with word-level timestamps for lyric alignment, caption timing, and edit-safe cut planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Related-skill install commands may pull unpinned external skill versions.

Mitigation: Review the referenced PrunaAI skills and prefer pinned or vetted versions before installation.

Risk: The workflow uses a Replicate API token and uploads audio to Replicate for transcription.

Mitigation: Confirm token handling and approval to upload the audio before making API calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/whisperx)
- [Replicate model: victor-upmeet/whisperx](https://replicate.com/victor-upmeet/whisperx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and parameter lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Replicate-backed WhisperX transcription; downstream workflows may produce transcript JSON and SRT files.]

## Skill Version(s):

1.0.13 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
