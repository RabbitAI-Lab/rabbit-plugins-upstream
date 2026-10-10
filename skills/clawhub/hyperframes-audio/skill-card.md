## Description:

Helps agents mix audio already placed in HyperFrames compositions using fades, track levels, effects, automation, submix buses, and voiceover carving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to diagnose and improve the mix of audio tracks in existing HyperFrames compositions, including voiceover clarity, fades, effects, and automation. It does not source audio or arrange clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The carve command can modify composition files.

Mitigation: Run it only on compositions you intend to edit, and use --dry-run to review proposed changes before writing.

Risk: Installing an unpinned HyperFrames package can introduce unreviewed dependency changes.

Mitigation: Prefer pinned package versions or a reviewed project lockfile before running setup commands.

## Reference(s):

- [HyperFrames Audio on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-audio)
- [Audio attributes](references/attributes.md)
- [Audio diagnosis](references/diagnosis.md)
- [Effects registry](references/fx-registry.md)
- [Presets and mixing recipes](references/presets.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HTML attribute examples, JSON configurations, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can propose or apply changes to composition files using the bundled carve command.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
