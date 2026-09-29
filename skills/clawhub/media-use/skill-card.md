## Description:

Helps agents find, generate, edit, and reuse media assets for HyperFrames projects, including audio, imagery, video, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to source or generate project media, create voiceovers and captions, edit footage and audio, and reuse approved assets across HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media tools can run shell commands and access network providers or credentials.

Mitigation: Review commands, use a pinned HyperFrames package, and run from a clean project without unrelated parent .env secrets.

Risk: Private media or usage telemetry may be sent to third parties.

Mitigation: Prefer --local-only for private media when practical; set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 to disable telemetry.

Risk: Generated assets and preferences can persist across projects.

Mitigation: Review reusable state under .media, ~/.media, and ~/.hyperframes before sharing or reusing it.

## Reference(s):

- [media-use release on ClawHub](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and providers](references/setup-providers.md)
- [Media resolution and reuse](references/resolve.md)
- [Audio workflows](references/audio.md)
- [Media operations](references/operations.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with commands and local asset paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can direct creation of local media files and reusable asset records.]

## Skill Version(s):

1.0.63 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
