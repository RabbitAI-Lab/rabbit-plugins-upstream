## Description:

Agent Media OS for HyperFrames projects that resolves BGM, SFX, images, icons, brand logos, voices, color grades, and LUTs into frozen local files or paste-ready blocks; generates via TTS, music, or image models when catalogs miss; produces voiceover, transcription, captions, and background removal through a shared audio engine; operates on media; and reuses assets across projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media-building agents use this skill to resolve, generate, transform, caption, transcribe, and reuse project media assets in HyperFrames workflows. It is intended for media selection and production tasks such as background music, sound effects, voices, images, logos, color treatments, LUTs, and editing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider credentials may be read from local auth stores or .env files.

Mitigation: Review configured providers before use, prefer scoped credentials, and avoid running cloud-backed workflows on confidential media without consent and vendor review.

Risk: Some media, prompts, and asset metadata can be cached or reused across projects.

Mitigation: Use private project workspaces, review reuse candidates before accepting them, and clear or segregate caches for sensitive client or brand assets.

Risk: Examples can invoke mutable external tooling and cloud APIs.

Mitigation: Pin or vet the HyperFrames CLI version before running examples and use --local-only when network calls are not appropriate.

Risk: Usage telemetry may be emitted by normal workflows.

Mitigation: Opt out where required by policy, and confirm telemetry settings before using the skill in regulated or confidential environments.

Risk: Background generation jobs and local model downloads can continue after an initial command returns.

Mitigation: Run the documented status or wait commands, verify generated files before publishing, and preflight required dependencies on managed machines.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/media-use)
- [Skill overview](artifact/SKILL.md)
- [Resolve workflow](artifact/references/resolve.md)
- [Setup and providers](artifact/references/setup-providers.md)
- [Audio engine](artifact/references/audio.md)
- [Media treatments](artifact/references/media-treatments.md)
- [Media operations](artifact/references/operations.md)
- [Memory and reuse](artifact/references/memory.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)
- [HeyGen image-to-video documentation](https://developers.heygen.com/image-to-video)
- [HyperFrames catalog](https://hyperframes.heygen.com/catalog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and generated or resolved local media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ledger records, media metadata, caption/transcript data, and reusable asset references for downstream agent workflows.]

## Skill Version(s):

1.0.52 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
