## Description:

Agent Media OS for HyperFrames that lets agents resolve, generate, operate on, and reuse media assets including BGM, SFX, images, icons, logos, voice, color grades, LUTs, captions, transcriptions, background removal, and source-aware media treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use media-use to resolve, generate, operate on, and remember media assets for HyperFrames projects, including audio, images, icons, logos, voice, color grades, LUTs, captions, transcription, and media treatments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call external media providers and use broad local and network media capabilities.

Mitigation: Review provider setup commands before use, prefer isolated environments, and use local-only paths when network access is not appropriate.

Risk: Usage telemetry may be linked to a HeyGen account when signed in.

Mitigation: Disable telemetry with HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when account-linked usage reporting is not acceptable.

Risk: Mutable third-party installs and untrusted direct media URLs can increase supply-chain or egress risk.

Mitigation: Install providers from verified sources, inspect commands before running them, and avoid untrusted direct media URLs until DNS-pinning or egress restrictions are in place.

## Reference(s):

- [media-use Skill Page](https://clawhub.ai/heygen-com/skills/media-use)
- [HeyGen Publisher Profile](https://clawhub.ai/user/heygen-com)
- [Resolve](references/resolve.md)
- [Audio Engine](references/audio.md)
- [Color Grading](references/grading.md)
- [Media Operations](references/operations.md)
- [Media Treatments](references/media-treatments.md)
- [Setup and Providers](references/setup-providers.md)
- [User Memory](references/memory.md)
- [Telemetry and Privacy](references/meta.md)
- [LUT Library](luts/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and local media file paths or generated metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or reference frozen local media assets, ledger records, audio metadata, captions, transcripts, color treatment JSON, LUT files, and project or user preference records.]

## Skill Version(s):

1.0.49 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
