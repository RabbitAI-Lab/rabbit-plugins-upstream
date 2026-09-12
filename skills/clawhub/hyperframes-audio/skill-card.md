## Description:

Helps agents mix audio already placed in a HyperFrames composition by applying fades, crossfades, gain, automation, ducking, voiceover carve, effects chains, and audio-group bus settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-building agents use this skill to finish HyperFrames audio mixes after media has already been placed. It guides corrective effects, automation, submix buses, and voiceover-carve workflows without sourcing or generating new audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The carve workflow can update the selected HyperFrames composition HTML.

Mitigation: Run the carve command with --dry-run first and keep compositions in source control or backed up before write mode.

Risk: The carve workflow reads local composition media while analyzing audio relationships.

Mitigation: Install and run the skill only in HyperFrames projects where local media access is acceptable.

Risk: The workflow depends on project-resolved HyperFrames packages and ffmpeg for audio analysis.

Mitigation: Use pinned package versions or lockfile-managed installs for @hyperframes/core and hyperframes, and verify ffmpeg is available before relying on the CLI.

## Reference(s):

- [Attributes](references/attributes.md)
- [Diagnosing audio you cannot hear](references/diagnosis.md)
- [Effect registry](references/fx-registry.md)
- [Presets, jobs and one-knob profiles](references/presets.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or HTML attribute snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or write HyperFrames composition attributes such as data-fx-carve, data-fx-chain, and data-automation when the carve CLI is used.]

## Skill Version(s):

1.0.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
