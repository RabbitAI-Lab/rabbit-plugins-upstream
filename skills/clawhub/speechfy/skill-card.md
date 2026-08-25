## Description:

Generates .ogg Opus voice-message audio from text using the Speechify API with automatic Edge TTS fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rickkbarbosa](https://clawhub.ai/user/rickkbarbosa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn text or SSML into Opus .ogg voice-message files for messaging workflows, with Speechify as the primary provider and Edge TTS as a fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for synthesis may be sent to Speechify or Microsoft Edge TTS.

Mitigation: Do not synthesize secrets, regulated data, or private messages unless that provider use is approved.

Risk: A selected output path can overwrite an existing writable file.

Mitigation: Choose output paths deliberately and review file targets before running the skill.

## Reference(s):

- [Speechify API Docs](https://docs.sws.speechify.com/)
- [Speechify audio speech endpoint](https://api.speechify.ai/v1/audio/speech)
- [Edge TTS](https://github.com/rany2/edge-tts)
- [SSML W3C Specification](https://www.w3.org/TR/speech-synthesis11/)
- [Voices Reference](references/voices.md)
- [Architecture Diagram](docs/diagrama.svg)
- [ClawHub skill page](https://clawhub.ai/rickkbarbosa/skills/speechfy)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash and Python examples; runtime output is an .ogg Opus audio file path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and ffmpeg; may call Speechify or Edge TTS and can overwrite an existing writable output file.]

## Skill Version(s):

1.1.0 (source: server release evidence, SKILL.md frontmatter, manifest.json, release.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
