## Description:

Adds styled captions to an existing single-subject talking-head video, with options for readable subtitles or cinematic text placed behind the subject.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to add verbatim subtitles or stylized captions to existing single-subject talking-head clips while preserving the source footage in standard and cinematic modes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skill update commands can change installed skills and related components globally.

Mitigation: Review the update scope and obtain approval before running update commands.

Risk: Some renders load GSAP runtime code from an external CDN.

Mitigation: Use offline or locally managed dependencies when external runtime loading is unacceptable.

Risk: Processing may download large models or packages and modify local video project files.

Mitigation: Run only on intended video projects and account for downloads before starting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption identity catalog](artifact/CATALOG.md)
- [Caption composition guidance](artifact/references/composition-craft.md)
- [Subtitle rail guidance](artifact/references/rail.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON configuration]

**Output Format:** [Markdown instructions with shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the workflow can produce a captioned MP4 video.]

## Skill Version(s):

1.0.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
