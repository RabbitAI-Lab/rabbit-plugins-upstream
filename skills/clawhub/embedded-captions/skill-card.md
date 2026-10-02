## Description:

Adds styled captions or subtitles to an existing single-subject talking-head video while preserving the footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to add readable, timed captions or cinematic typography to single-subject talking-head clips without changing the original footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads local video and audio and installs dependencies or downloads speech and matting models.

Mitigation: Run it only in trusted caption projects and review dependency and model downloads before use.

Risk: Refreshing HyperFrames skills can change the tools used by the workflow.

Mitigation: Confirm skill update commands with the user before running them.

## Reference(s):

- [Embedded Captions on ClawHub](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption Style Catalog](artifact/CATALOG.md)
- [Caption Grouping Guidance](artifact/references/caption-grouping.md)
- [Caption Quality Checks](artifact/references/reference-bar.md)

## Skill Output:

**Output Type(s):** [Video files, JSON configuration, Guidance]

**Output Format:** [MP4 video, JSON, and text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Locally rendered captioned video; single-shot, single-subject input recommended.]

## Skill Version(s):

1.0.22 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
