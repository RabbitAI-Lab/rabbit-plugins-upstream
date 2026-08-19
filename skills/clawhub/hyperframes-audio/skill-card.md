## Description:

Helps agents mix audio already placed in a HyperFrames composition by configuring fades, crossfades, track gain, volume and effect automation, ducking, voiceover carve, and audio effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to adjust and diagnose audio mixes inside existing HyperFrames compositions, especially voiceover and music-bed conflicts, track-level effects, and automation. It is not for sourcing or generating audio or for clip timing and layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The carve command can rewrite audio effect and automation attributes in a user-specified HyperFrames composition file.

Mitigation: Review the target composition before use and run the command with --dry-run first to inspect the proposed changes without writing them.

Risk: Audio diagnosis can be under-determined when there is no clean original, usable silence, or other internal comparison point.

Mitigation: State the uncertainty and offer only readings supported by comparisons inside the same file instead of asserting a single tonal defect.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes-audio)
- [Audio Attribute Reference](references/attributes.md)
- [Audio Diagnosis Reference](references/diagnosis.md)
- [Effect Registry](references/fx-registry.md)
- [Presets, Jobs, and One-Knob Profiles](references/presets.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON attribute examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run a local carve command that edits audio effect and automation attributes in a user-specified HyperFrames HTML composition.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
