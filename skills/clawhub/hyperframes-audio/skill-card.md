## Description:

Mixes audio already placed in HyperFrames compositions through voiceover carve, track effects, and automation envelopes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media-production agents use this skill to make HyperFrames audio mixes clearer by carving music beds around voiceover, applying track effects, and writing automation data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The carve CLI rewrites the selected HTML composition file's audio attributes.

Mitigation: Run with --dry-run first or keep the composition under version control before applying changes.

Risk: The audio-analysis workflow depends on ffmpeg and @hyperframes/core being available in the composition project.

Mitigation: Verify ffmpeg is on PATH and install or point the CLI to @hyperframes/core before running the carve command.

## Reference(s):

- [HyperFrames Audio Skill](https://clawhub.ai/heygen-com/skills/hyperframes-audio)
- [Audio Attributes](references/attributes.md)
- [FX Registry](references/fx-registry.md)
- [Presets](references/presets.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose HyperFrames audio attribute values and CLI commands; the carve workflow can rewrite the selected composition file.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
