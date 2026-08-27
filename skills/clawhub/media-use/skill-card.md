## Description:

media-use helps agents resolve, generate, transform, and reuse media assets for HyperFrames projects, including BGM, SFX, images, icons, logos, voice, captions, transcription, background removal, color grades, LUTs, and media treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use media-use to select, generate, operate on, and register media assets for HyperFrames compositions. The skill is intended for practical media production workflows that need reusable local assets, provider-aware generation, and concise agent guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media prompts or content may be sent to credentialed third-party providers.

Mitigation: For confidential client media, prefer --local-only where supported and review provider setup before processing sensitive assets.

Risk: Telemetry can link coarse usage events to an account identity.

Mitigation: Disable telemetry with HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when account-linked reporting is not appropriate.

Risk: Cross-project local reuse can persist media data in shared local caches.

Mitigation: Avoid storing sensitive assets in shared ~/.media caches and review candidate reuse before importing cached media into a project.

Risk: Recipe use can overwrite frame.md.

Mitigation: Review recipe use before allowing frame.md overwrites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and providers](artifact/references/setup-providers.md)
- [Resolve command, flags, reuse, adopt, inventory](artifact/references/resolve.md)
- [Audio engine](artifact/references/audio.md)
- [Media operations](artifact/references/operations.md)
- [Media treatments](artifact/references/media-treatments.md)
- [Telemetry, usage stats, and privacy](artifact/references/meta.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, local file paths, and generated or resolved media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write media assets, metadata ledgers, captions, transcripts, recipes, and reusable cache records depending on the requested workflow.]

## Skill Version(s):

1.0.41 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
