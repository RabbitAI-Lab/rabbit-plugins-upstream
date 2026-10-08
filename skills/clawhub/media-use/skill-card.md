## Description:

Helps HyperFrames agents find, generate, edit, and reuse media assets, including audio, images, captions, color treatments, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators using HyperFrames can source or generate media, make voiceovers and captions, edit footage, and preserve reusable local assets and treatment recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External media providers may receive requests and require local credentials.

Mitigation: Use trusted project folders, review nearby .env files, and confirm provider access before generating media.

Risk: Project-local and cross-project caches can retain media for reuse.

Mitigation: Review .media and ~/.media contents when handling sensitive or client-specific assets.

Risk: Coarse usage telemetry is sent unless opted out.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 if telemetry is not wanted.

Risk: CLI setup and freshness commands may introduce unexpected dependency changes.

Mitigation: Prefer pinned, known CLI versions and review updates before running them.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](artifact/references/resolve.md)
- [Provider setup](artifact/references/setup-providers.md)
- [Audio workflows](artifact/references/audio.md)
- [Telemetry and privacy](artifact/references/meta.md)

## Skill Output:

**Output Type(s):** [Media files, Text, Markdown, JSON, Configuration instructions]

**Output Format:** [Local media assets, paste-ready blocks, ledger records, and editing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write project-local and cross-project reuse caches.]

## Skill Version(s):

1.0.73 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
