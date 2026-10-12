## Description:

Helps agents find, generate, edit, and reuse media assets for HyperFrames projects, including audio, images, captions, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to source or generate project media, make audio and visual edits, and keep reusable assets organized across HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud media calls may transmit project content and use provider credentials.

Mitigation: Review provider settings and avoid untrusted project .env files before enabling cloud workflows.

Risk: Reusable local caches and project memory may retain sensitive media.

Mitigation: Review stored assets under .media and ~/.media and apply appropriate access and retention controls.

Risk: Coarse usage telemetry may be sent unless disabled.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 to opt out.

Risk: Unpinned CLI installation may change behavior across runs.

Mitigation: Pin CLI versions when repeatable installations are required.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](references/resolve.md)
- [Audio workflows](references/audio.md)
- [Media treatments](references/media-treatments.md)
- [Provider setup](references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Guidance]

**Output Format:** [Local media files or paste-ready text, with concise resolution details and instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolved assets may be recorded in a project ledger for reuse]

## Skill Version(s):

1.0.77 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
