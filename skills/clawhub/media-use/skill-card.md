## Description:

Media-use helps agents resolve, generate, transform, grade, caption, transcribe, and reuse media assets for HyperFrames projects while freezing outputs and ledger records locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to manage media workflows for HyperFrames projects, including asset resolution, voice and audio generation, transcription, captions, color treatment, LUT handling, media operations, and cross-project reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-linked telemetry and coarse usage events may be sent when the user is signed in.

Mitigation: Review telemetry behavior before installation and set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when telemetry should be disabled.

Risk: Sensitive media may be uploaded or processed by external providers during generation, search, transcription, or media operations.

Mitigation: Use --local-only for sensitive media and confirm provider choices before running workflows that may call external services.

Risk: Direct URLs, npx, pip, and Git-sourced tools can introduce execution or download risk.

Mitigation: Avoid untrusted direct URLs and review required tools, commands, and provider setup before execution.

Risk: Recipe use can overwrite project frame.md and promote reusable state into ~/.media.

Mitigation: Review recipe adoption carefully and keep project changes under version control before applying reusable recipes.

## Reference(s):

- [ClawHub media-use release page](https://clawhub.ai/heygen-com/skills/media-use)
- [Resolve reference](references/resolve.md)
- [Audio engine reference](references/audio.md)
- [Color grading reference](references/grading.md)
- [Media treatments reference](references/media-treatments.md)
- [Media operations reference](references/operations.md)
- [Setup and providers reference](references/setup-providers.md)
- [Memory reference](references/memory.md)
- [Telemetry and privacy reference](references/meta.md)
- [LUT library reference](luts/README.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)
- [Pixabay sound effects library](https://pixabay.com/sound-effects/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, local file paths, and generated or resolved media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local ledger records, cached media assets, captions, transcripts, audio metadata, LUT files, and reusable project or user media state.]

## Skill Version(s):

1.0.42 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
