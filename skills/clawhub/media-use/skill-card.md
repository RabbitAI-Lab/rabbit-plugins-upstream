## Description:

Helps agents find, generate, edit, and reuse audio and visual assets for HyperFrames projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to source and generate project media, make voiceovers and captions, apply visual treatments, and reuse approved assets across HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project credential files may be loaded by the skill.

Mitigation: Use only in trusted projects and avoid putting provider secrets in project .env files unless you intend this skill to use them.

Risk: Account-linked usage telemetry may expose project activity.

Mitigation: Review telemetry settings and disable it with HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when appropriate.

Risk: Unpinned npx execution may fetch a changing HyperFrames CLI version.

Mitigation: Pin or preinstall the HyperFrames CLI rather than relying on unpinned npx resolution.

Risk: Recipes and preferences stored in ~/.media may persist across client projects.

Mitigation: Review stored media memory before reusing recipes or preferences in another project.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](artifact/references/resolve.md)
- [Audio workflows](artifact/references/audio.md)
- [Media treatments](artifact/references/media-treatments.md)
- [Provider setup](artifact/references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance and shell commands; local media files and asset records when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolved assets can be saved locally with ledger records for project reuse.]

## Skill Version(s):

1.0.83 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
