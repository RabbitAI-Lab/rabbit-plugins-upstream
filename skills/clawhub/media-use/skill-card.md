## Description:

media-use helps agents resolve, generate, transform, reuse, and document project media including audio, images, icons, logos, voice, captions, video, color treatments, and LUTs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media-producing agents use this skill to choose, fetch, generate, edit, freeze, and reuse media assets for HyperFrames projects while keeping a local record of selected assets and treatments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can contact external media providers and make broad media requests.

Mitigation: Use --local-only when network calls are not acceptable, and avoid resolving or ingesting untrusted media URLs.

Risk: Some workflows run local CLIs and may install unpinned Python packages for BGM generation.

Mitigation: Use a prepared controlled environment, review provider setup before execution, or avoid the local BGM generation path.

Risk: Usage telemetry can be account-linked by default.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 before use when telemetry is not appropriate.

Risk: The skill writes reusable media state under the project and ~/.media.

Mitigation: Run it in an intended project workspace and review generated assets, cache records, and ledger entries before reuse or publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and Providers](artifact/references/setup-providers.md)
- [Resolve Workflow](artifact/references/resolve.md)
- [Audio Engine](artifact/references/audio.md)
- [Media Treatments](artifact/references/media-treatments.md)
- [Media Operations](artifact/references/operations.md)
- [Color Grading](artifact/references/grading.md)
- [Memory and Reuse](artifact/references/memory.md)
- [Telemetry and Privacy](artifact/references/meta.md)
- [HeyGen CLI Documentation](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, paste-ready configuration, and generated or resolved local file references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may direct an agent to create or reuse media files, ledger entries, cache records, transcripts, captions, treatment JSON, or LUT references.]

## Skill Version(s):

1.0.47 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
