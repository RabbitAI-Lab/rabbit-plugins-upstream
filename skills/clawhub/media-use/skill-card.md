## Description:

Helps agents find, generate, edit, and reuse media assets for HyperFrames projects, including audio, imagery, captions, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to source or generate media, prepare voiceover and captions, adjust visuals, and reuse assets across HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media-provider calls may use local credentials and send content to external services.

Mitigation: Review provider settings and permissions; use explicit providers or local-only operation when appropriate.

Risk: Telemetry may be anonymous or linked to an account.

Mitigation: Review telemetry settings and opt out if collection is unsuitable.

Risk: User-level media storage may persist and be reused across projects.

Mitigation: Review stored assets and avoid cross-project reuse of sensitive media.

Risk: Generated music may install Python dependencies and continue in detached jobs.

Mitigation: Approve dependencies before generation and check pending jobs before using their output.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](artifact/references/resolve.md)
- [Audio workflows](artifact/references/audio.md)
- [Media operations](artifact/references/operations.md)
- [Provider setup](artifact/references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance and commands; local media files and asset records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media assets can be reused across projects.]

## Skill Version(s):

1.0.84 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
