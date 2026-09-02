## Description:

Use this skill when an agent needs word-level timestamps from audio for lyric alignment, line-boundary edits, or caption source timing before video burn-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use whisperx to transcribe uploaded audio and obtain word-level timing for captions, lyric alignment, and cut planning. It is suited to workflows that can use a Replicate token and send the selected audio file to the Replicate/Pruna workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files and Replicate credentials are used with a third-party workflow.

Mitigation: Use a scoped Replicate token where possible and avoid submitting confidential audio unless provider terms and account controls are acceptable.

Risk: Incorrect timestamps can affect downstream captions, lyric alignment, or edit boundaries.

Mitigation: Set language, align_output true, and an initial_prompt when helpful, then review transcript and cut outputs before final burn-in or publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/whisperx)
- [Replicate model: victor-upmeet/whisperx](https://replicate.com/victor-upmeet/whisperx)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline bash commands and expected transcript file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Replicate API token and an audio_file HTTPS URL; word-level alignment uses align_output true.]

## Skill Version(s):

1.0.10 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
