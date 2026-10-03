## Description:

Guides the creation of styled captions for single-subject talking-head videos using local transcription, subject matting, previews, and rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to add readable subtitles or cinematic and VFX-style captions to an existing single-speaker talking-head clip while preserving the source footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local video workflow downloads models and packages and requires a heavyweight media toolchain.

Mitigation: Run in a dedicated caption project, retain the dependency lockfile, and allow for downloads and local processing of source footage.

Risk: Updating or initializing HyperFrames may affect globally installed skills.

Mitigation: Review the update or init action and confirm it before running.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption style catalog](artifact/CATALOG.md)
- [Caption grouping guide](artifact/references/caption-grouping.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and JSON caption plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local production of composited MP4 captions after preview and quality checks.]

## Skill Version(s):

1.0.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
