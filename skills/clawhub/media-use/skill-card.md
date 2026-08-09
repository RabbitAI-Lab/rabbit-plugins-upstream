## Description:

Agent Media OS, the single skill for every media need in a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or paste-ready block + ledger record (one verb, `resolve`); generate via TTS / music / image models when the catalog misses; produce voiceover, transcription, captions, and background removal through one shared audio engine; operate on media (cut / reframe / transform); and reuse assets across projects. Also use for vague feedback that real footage looks dark, flat, boring, should feel retro/camcorder/print/ASCII, needs privacy, or needs a media reveal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to resolve, generate, transform, caption, grade, and reuse media assets for HyperFrames projects. It supports common production tasks such as background music, sound effects, images, icons, logos, voiceover, transcription, captions, background removal, LUTs, and media treatment recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local commands, use existing HeyGen or Codex authentication, call cloud media providers, and start background jobs.

Mitigation: Review commands before execution, run `node <SKILL_DIR>/scripts/resolve.mjs --doctor` before use, and use `--local-only` for sensitive projects when network providers should be skipped.

Risk: The skill stores assets, prompts, manifests, and reusable media across projects, including the global `~/.media` cache.

Mitigation: Avoid shared global caches for client-confidential work and inspect `.media/` and cache contents before reuse or handoff.

Risk: Usage telemetry may link coarse media usage events to the shared HyperFrames install identity or signed-in HeyGen account.

Mitigation: Set `HYPERFRAMES_NO_TELEMETRY=1` or `DO_NOT_TRACK=1` before running the skill when telemetry should be disabled.

Risk: Environment and credential handling can expose auth context if `.env` files or shell profiles are shared carelessly.

Mitigation: Review `.env` placement and credential scope before running the audio engine or provider-backed resolve workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and providers](artifact/references/setup-providers.md)
- [Resolve workflow](artifact/references/resolve.md)
- [Audio engine](artifact/references/audio.md)
- [Media treatments](artifact/references/media-treatments.md)
- [Media operations](artifact/references/operations.md)
- [Grading and LUTs](artifact/references/grading.md)
- [Memory and reuse](artifact/references/memory.md)
- [Ownership, telemetry, and privacy](artifact/references/meta.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)
- [Bundled SFX credits](artifact/audio/assets/sfx/CREDITS.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, file paths, and generated or resolved local media artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or reuse project and global media files, manifests, captions, LUTs, treatment JSON, audio metadata, transcripts, and cache records.]

## Skill Version(s):

1.0.38 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
