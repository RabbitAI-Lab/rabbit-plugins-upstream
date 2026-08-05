## Description:

Media-use helps agents resolve, generate, reuse, and operate on production media assets including music, sound effects, images, icons, logos, voiceover, captions, transcription, background removal, color grades, LUTs, and media treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and agents use this skill to select or create media assets, apply source-aware treatments, and produce reusable local files or paste-ready instructions for HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-linked telemetry and ambient credentials may be inappropriate in sensitive or multi-client environments.

Mitigation: Use a separate HOME or profile for isolation, run account checks before use, and set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when telemetry should be disabled.

Risk: Cross-project memory and global media reuse can expose prompts or asset metadata across project boundaries.

Mitigation: Use an isolated profile for sensitive work and review reusable candidates before adopting assets from global media storage.

Risk: Runtime downloads and external providers can send requests outside the local environment.

Mitigation: Prefer --local-only where possible and install local providers for workflows that need network isolation.

Risk: Recipe workflows can mutate project files, including replacing frame.md.

Mitigation: Review recipe effects before applying them and keep project changes under reviewable version control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and providers](artifact/references/setup-providers.md)
- [Resolve command and reuse](artifact/references/resolve.md)
- [Audio engine](artifact/references/audio.md)
- [Media treatments](artifact/references/media-treatments.md)
- [Media operations](artifact/references/operations.md)
- [Color grading and LUTs](artifact/references/grading.md)
- [User memory, telemetry, and privacy](artifact/references/meta.md)
- [SFX credits](artifact/audio/assets/sfx/CREDITS.md)
- [LUT library](artifact/luts/README.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)
- [HyperFrames media catalog](https://hyperframes.heygen.com/catalog)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown or text guidance with inline shell commands, JSON or configuration blocks, code snippets, and local file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference frozen local media assets, paste-ready blocks, and ledger records for project reuse.]

## Skill Version(s):

1.0.37 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
