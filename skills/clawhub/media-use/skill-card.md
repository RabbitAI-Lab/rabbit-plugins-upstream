## Description:

Media Use helps agents resolve, generate, operate on, and reuse media assets for HyperFrames projects, including audio, images, icons, logos, voices, color grades, LUTs, transcription, captions, background removal, and media treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-building agents use this skill in HyperFrames projects to find or generate media assets, freeze them into local project files, assemble audio and caption workflows, and apply media operations or visual treatments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default telemetry can be linked to a HeyGen account email or username.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 before use when telemetry is not desired.

Risk: Image-to-video and avatar-style workflows can involve likeness or consent-sensitive media.

Mitigation: Use these workflows only with clear likeness rights and consent for the source media.

Risk: Music generation paths may install Python packages automatically and may not be pinned by the skill evidence.

Mitigation: Use a dedicated virtual environment or preinstall reviewed, pinned dependencies before enabling music generation.

Risk: Persistent project and global media caches can retain reused assets across projects.

Mitigation: Review project and global media cache contents before sharing a workspace or reusing assets across clients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and providers](references/setup-providers.md)
- [Resolve command and reuse workflow](references/resolve.md)
- [Audio engine](references/audio.md)
- [Media operations](references/operations.md)
- [Media treatments](references/media-treatments.md)
- [Color grading](references/grading.md)
- [User memory](references/memory.md)
- [Telemetry and privacy](references/meta.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, and paste-ready configuration or treatment blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local media file paths, ledger records, usage statistics, captions, transcripts, and reusable recipe or preference records.]

## Skill Version(s):

1.0.48 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
