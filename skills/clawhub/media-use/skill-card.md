## Description:

Agent Media OS for HyperFrames projects that resolves BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or paste-ready block plus ledger record; generates via TTS, music, or image models when the catalog misses; produces voiceover, transcription, captions, and background removal through one shared audio engine; operates on media; and reuses assets across projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use media-use in HyperFrames projects to resolve, generate, transform, and reuse media assets such as BGM, SFX, images, logos, voiceovers, captions, transcripts, and color grades. The skill also guides media treatment choices and records resolved assets for local reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider-backed media workflows can involve account-linked provider calls and default telemetry.

Mitigation: Use the skill only when those workflows are acceptable, and set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when telemetry should be disabled.

Risk: Cross-project local caches can expose client-confidential assets or prior project context if reused carelessly.

Mitigation: Use --local-only for sensitive projects, avoid shared global caches for confidential assets, and review ~/.media and ~/.hyperframes storage regularly.

Risk: Automatic and background execution can download, generate, or process media outside an immediately visible foreground step.

Mitigation: Run doctor/preflight checks, review generated files and ledger entries before use, and prefer explicit provider or local-only choices for sensitive work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and providers](references/setup-providers.md)
- [Resolve](references/resolve.md)
- [Audio](references/audio.md)
- [Media treatments](references/media-treatments.md)
- [Operations](references/operations.md)
- [Grading](references/grading.md)
- [Memory](references/memory.md)
- [Telemetry and privacy](references/meta.md)
- [SFX credits](audio/assets/sfx/CREDITS.md)
- [LUT library](luts/README.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and generated file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May resolve or generate local media assets, write ledger/cache records, and invoke provider or local CLI tools.]

## Skill Version(s):

1.0.40 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
