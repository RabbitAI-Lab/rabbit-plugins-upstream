## Description:

media-use helps agents resolve, generate, edit, and reuse HyperFrames media assets, including BGM, SFX, images, icons, logos, voiceover, transcription, captions, background removal, visual treatments, color grades, and LUTs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media-building agents use this skill to resolve, generate, operate on, and reuse media assets for HyperFrames projects. It supports audio, images, icons, logos, voiceover, transcription, captions, background removal, visual treatments, cuts, reframing, color grades, and LUT workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telemetry may be linked to account identity when authenticated provider workflows are used.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 in client or sensitive workspaces.

Risk: Media prompts, assets, likenesses, scripts, or brand materials may persist and be reused across projects.

Mitigation: Use --local-only for private media and avoid global reuse for confidential material unless cross-project sharing is acceptable.

Risk: The security verdict recommends review before installation in sensitive environments.

Mitigation: Review the skill and its provider setup before deployment, especially where account-linked telemetry or shared media caches are unacceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/media-use)
- [Resolve and Reuse](references/resolve.md)
- [Setup and Providers](references/setup-providers.md)
- [Audio Engine](references/audio.md)
- [Media Treatments](references/media-treatments.md)
- [Operations](references/operations.md)
- [Telemetry and Privacy](references/meta.md)
- [HeyGen CLI Documentation](https://developers.heygen.com/cli)
- [Pixabay Sound Effects](https://pixabay.com/sound-effects/)
- [Pixabay Content License](https://pixabay.com/service/license-summary/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and CLI-oriented text with code blocks, JSON snippets, file paths, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce frozen local media files, paste-ready blocks, ledger records, treatment JSON, transcripts, captions, cut lists, and usage reports.]

## Skill Version(s):

1.0.39 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
