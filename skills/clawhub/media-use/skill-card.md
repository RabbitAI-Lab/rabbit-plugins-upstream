## Description:

Helps agents source, generate, edit, and reuse media assets in HyperFrames projects, including audio, images, captions, and visual treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to find or generate media, produce voice and captions, edit footage, and reuse assets in HyperFrames projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A project .env file may pass unsafe settings to tools launched by the audio workflow.

Mitigation: Review the skill before use with untrusted projects; run audio work in an isolated workspace with only intended provider credentials and no untrusted .env files.

Risk: Unpinned command-line tools can change between runs.

Mitigation: Pin or locally install trusted CLI versions rather than copying unpinned npx commands.

Risk: External transcription may disclose sensitive audio to third parties.

Mitigation: Check audio sensitivity and provider handling before using external transcription.

## Reference(s):

- [ClawHub media-use release](https://clawhub.ai/heygen-com/skills/media-use)
- [Media resolution and reuse](references/resolve.md)
- [Audio workflows](references/audio.md)
- [Media treatments](references/media-treatments.md)
- [Provider setup](references/setup-providers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance, command-line output, and local media assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolved assets can include a local file and ledger record.]

## Skill Version(s):

1.0.58 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
