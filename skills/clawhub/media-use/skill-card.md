## Description:

Helps agents find, generate, edit, and reuse media for HyperFrames projects, including images, audio, captions, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to source or generate media, prepare voiceovers and captions, adjust footage, and reuse approved assets across HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default telemetry may associate usage with a HeyGen email or username.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 before use if telemetry is not wanted.

Risk: Cloud providers, local credentials, and project .env values may expose sensitive data.

Mitigation: Review provider access and avoid running in workspaces with unrelated secrets in .env files.

Risk: Unpinned npx commands and persistent cross-project media memory expand execution and data-retention scope.

Mitigation: Review commands and persisted assets before use, and restrict access to projects and data the skill needs.

## Reference(s):

- [media-use release on ClawHub](https://clawhub.ai/heygen-com/skills/media-use)
- [Provider setup](references/setup-providers.md)
- [Audio workflows](references/audio.md)
- [Media operations](references/operations.md)
- [Privacy and telemetry](references/meta.md)
- [Pixabay Content License for bundled sound effects](https://pixabay.com/service/license-summary/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce local media files, captions, and asset ledger records.]

## Skill Version(s):

1.0.75 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
