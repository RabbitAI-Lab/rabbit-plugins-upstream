## Description:

Guides mixing of existing HyperFrames audio tracks with fades, automation, effects, submix groups, and voiceover carving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to mix audio already placed in HyperFrames compositions, including voiceover and music beds, with track effects, level automation, and shared submix processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying the skill can change audio settings in a local HyperFrames composition.

Mitigation: Use --dry-run first for important projects and review composition changes before rendering.

Risk: Voiceover carving runs a local script that decodes media with ffmpeg.

Mitigation: Review the command and selected media before running it.

Risk: Copying unpinned npx commands can run an unintended HyperFrames version.

Mitigation: Prefer pinned or project-local HyperFrames commands.

## Reference(s):

- [HyperFrames Audio on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-audio)
- [Audio attribute formats](artifact/references/attributes.md)
- [Audio effects and parameter ranges](artifact/references/fx-registry.md)
- [Audio diagnosis guidance](artifact/references/diagnosis.md)
- [Mixing presets](artifact/references/presets.md)

## Skill Output:

**Output Type(s):** [Configuration instructions, Code, Shell commands, Guidance]

**Output Format:** [Markdown with HTML and JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Applies changes to local composition audio attributes when instructed.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
