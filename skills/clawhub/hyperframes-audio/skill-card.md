## Description:

Guides agents through mixing audio already placed in a HyperFrames composition with fades, volume automation, effects chains, voiceover carve, and shared audio-group buses while leaving sourcing and timeline layout to other skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative automation authors use this skill to adjust audio that is already placed in a HyperFrames composition, including fades, gain, automation, effects, voiceover carve, and group-bus mixing. It is not for finding or generating audio, clip timing, or track layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local carve CLI can edit the selected HTML composition file during a normal run.

Mitigation: Run the command with --dry-run first, confirm the intended composition and media files, and keep the composition under version control or backed up before allowing writes.

Risk: Carve analysis depends on local media files plus ffmpeg and @hyperframes/core being available.

Mitigation: Verify those dependencies and media paths before applying generated commands to a production composition.

Risk: Audio diagnosis without listening can be under-determined when no clean original, useful pause, or internal comparison is available.

Mitigation: Use the skill's diagnostic comparison workflow and report uncertainty rather than applying a corrective chain from a single absolute spectrum.

## Reference(s):

- [The three audio attributes](references/attributes.md)
- [Diagnosing audio you cannot hear](references/diagnosis.md)
- [Effect registry](references/fx-registry.md)
- [Presets, jobs and one-knob profiles](references/presets.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON attribute examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HyperFrames data-attribute snippets, effect-chain configuration, automation examples, diagnostic commands, and local carve CLI commands.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
