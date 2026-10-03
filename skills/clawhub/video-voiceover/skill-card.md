## Description:

Converts timestamped Chinese narration into time-aligned voiceover clips and placement metadata using a configured text-to-speech provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Video editors and developers use this skill to generate segment-level Chinese narration audio for a supplied timeline and metadata for later assembly. An additional dubbing path can transcribe video and synthesize a cloned speaker voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dubbing and voice-reference modes can clone a speaker's voice without their consent.

Mitigation: Use only with authorized voices and media; avoid dubbing and voice-reference modes unless consent is confirmed.

Risk: Narration, audio clips, and reference voice data may be sent to external providers.

Mitigation: Review provider data handling, set the provider explicitly, and use a dedicated work directory before processing sensitive content.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/video-voiceover)
- [IndexTTS endpoint reference](references/index-tts.md)

## Skill Output:

**Output Type(s):** [Audio files, JSON metadata]

**Output Format:** [WAV segments and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces timestamped WAV clips and tts_meta.json for downstream assembly; optional dubbing produces a dub manifest.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
