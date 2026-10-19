## Description:

Guides mixing audio already placed in a HyperFrames composition, including fades, automation, effects, submix buses, and voiceover carving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and editors use this skill to mix existing voice, music, and effects tracks in HyperFrames compositions through track effects, automation, grouping, and voiceover carving. It does not source or generate audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The carve CLI or write commands can change composition files.

Mitigation: Use the skill only in a trusted HyperFrames project and run --dry-run before allowing changes.

Risk: Unpinned npx examples can fetch an unexpected dependency version.

Mitigation: Prefer project-local, lockfile-controlled dependencies or pin the CLI version.

## Reference(s):

- [HyperFrames Audio release](https://clawhub.ai/heygen-com/skills/hyperframes-audio)
- [Audio attributes](references/attributes.md)
- [Effects registry](references/fx-registry.md)
- [Audio presets](references/presets.md)
- [Audio diagnosis](references/diagnosis.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HTML/JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The carve CLI can update a selected composition file; --dry-run previews changes.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
