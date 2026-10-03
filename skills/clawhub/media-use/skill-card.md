## Description:

Helps agents find, generate, edit, and reuse audio and visual assets for HyperFrames projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to source and produce media for HyperFrames projects, including music, sound effects, imagery, voiceovers, captions, and video treatments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face, voice, transcript, or image-to-video media may be uploaded to external providers.

Mitigation: Confirm consent and upload suitability before using these workflows; choose a local provider when needed.

Risk: Provider credentials, project files, and cross-project media memory may expose sensitive material.

Mitigation: Review provider access and local storage before installation and reuse.

Risk: The skill sends coarse telemetry unless disabled.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 if telemetry is not wanted.

Risk: Unpinned npx commands may execute a changing package version.

Mitigation: Prefer pinned or locally installed tools for command examples.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](artifact/references/resolve.md)
- [Audio workflows](artifact/references/audio.md)
- [Provider setup](artifact/references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflows may save resolved media files and ledger records locally.]

## Skill Version(s):

1.0.66 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
