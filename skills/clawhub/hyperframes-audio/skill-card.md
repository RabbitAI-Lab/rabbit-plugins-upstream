## Description:

Helps mix audio already placed in a HyperFrames composition using fades, track levels, automation, effects, submix buses, and voiceover-aware music carving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to adjust the mix of existing audio tracks in HyperFrames compositions, including effects, automation, and carving a music bed around speech. It does not source or generate audio or arrange clip timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying a carve changes the composition and may select the wrong music or voice track.

Mitigation: Run --dry-run first, review the chosen tracks, and keep the composition under version control.

Risk: Ad hoc latest-package execution may introduce unreviewed dependency changes.

Mitigation: Prefer pinned trusted versions of hyperframes and @hyperframes/core.

## Reference(s):

- [Audio attributes and automation](references/attributes.md)
- [Audio diagnosis](references/diagnosis.md)
- [Effects and parameter registry](references/fx-registry.md)
- [Audio presets and mixing recipes](references/presets.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with HTML attributes, JSON examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update the composition's audio attributes; the carve command supports a non-writing dry run.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
