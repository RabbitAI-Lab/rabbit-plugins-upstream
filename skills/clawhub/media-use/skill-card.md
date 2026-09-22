## Description:

Agent Media OS for HyperFrames projects that helps agents resolve, generate, operate on, and reuse media assets including music, sound effects, images, icons, logos, voiceover, color grades, LUTs, captions, transcripts, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to find, create, transform, register, and reuse media for HyperFrames compositions while keeping outputs in project ledgers and reusable caches. It is especially useful when a project needs concrete media assets, audio production, visual polish, transcription, captions, or media treatment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local media commands and may invoke external provider tools for generation, transcription, search, or transformation.

Mitigation: Review commands before execution, run the documented doctor checks, and use local-only or offline paths when working with confidential media.

Risk: Provider workflows may read provider credentials or upload media to third-party services.

Mitigation: Use provider CLI authentication deliberately, prefer local providers where possible, and avoid provider-upload workflows for sensitive inputs unless approved.

Risk: The skill sends coarse usage telemetry unless opted out.

Mitigation: Set DO_NOT_TRACK=1 or HYPERFRAMES_NO_TELEMETRY=1 when telemetry is not appropriate.

Risk: Reusable media, preferences, recipes, and misses can be stored in project and user-level media caches.

Mitigation: Review .media and user-level media cache contents before sharing projects, and avoid loose cross-project reuse for client-specific or confidential assets.

## Reference(s):

- [Resolve guide](references/resolve.md)
- [Setup and providers](references/setup-providers.md)
- [Audio engine](references/audio.md)
- [Media operations](references/operations.md)
- [Media treatments](references/media-treatments.md)
- [Memory and recipes](references/memory.md)
- [Telemetry and privacy](references/meta.md)
- [Bundled SFX credits](audio/assets/sfx/CREDITS.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)
- [HeyGen image-to-video documentation](https://developers.heygen.com/image-to-video)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, generated file paths, and reusable configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or register local media files and ledger entries through documented commands and provider tools.]

## Skill Version(s):

1.0.51 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
