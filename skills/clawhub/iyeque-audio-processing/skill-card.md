## Description:

An OpenClaw audio toolkit for local transcription, timestamped segments, feature extraction, speech detection, and FFmpeg transforms, with remote text-to-speech available only by explicit opt-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users can transcribe voice notes, inspect audio features and speech segments, transform workspace audio, or create speech from text with explicit network consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text supplied for remote TTS is sent to Google and may be sensitive.

Mitigation: Use TTS only with explicit network consent, and exclude secrets or confidential transcripts.

Risk: Whisper may need an initial model download before local transcription is available.

Mitigation: Download the model in an approved environment before relying on offline processing.

## Reference(s):

- [audio-processing on ClawHub](https://clawhub.ai/iyeque/skills/iyeque-audio-processing)

## Skill Output:

**Output Type(s):** [Text, Analysis, Audio files]

**Output Format:** [JSON responses with transcript text, segments, feature data, or file paths; generated audio files for TTS and transforms]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file paths are workspace-scoped; remote TTS requires explicit network consent.]

## Skill Version(s):

1.3.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
