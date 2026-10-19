## Description:

Helps agents source, generate, edit, and reuse media for HyperFrames projects, including audio, imagery, color treatments, captions, and transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find or generate assets, prepare voiceovers and captions, edit footage, and reuse approved media across HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and local provider credentials may be used with external services, including credentials loaded from nearby .env files.

Mitigation: Review provider choice, media sensitivity, and nearby .env files before running cloud workflows.

Risk: Reusable assets and preferences may persist across projects under ~/.media.

Mitigation: Review cached assets and preferences before reuse, especially for client or brand material.

Risk: Coarse usage telemetry is sent unless opted out.

Mitigation: Set DO_NOT_TRACK=1 or HYPERFRAMES_NO_TELEMETRY=1 when telemetry is not appropriate.

Risk: External CLI installation can introduce supply-chain variability.

Mitigation: Pin or preinstall approved CLI versions when reproducibility matters.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](references/resolve.md)
- [Audio workflows](references/audio.md)
- [Media treatments](references/media-treatments.md)
- [Provider setup](references/setup-providers.md)
- [Privacy and telemetry](references/meta.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Media files]

**Output Format:** [Markdown guidance and commands; local media assets and ledger records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolved assets are stored locally for project use and reuse.]

## Skill Version(s):

1.0.85 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
