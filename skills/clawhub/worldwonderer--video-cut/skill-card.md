## Description:

Cuts agent-selected segments from one or more source videos into a frame-aligned short video, with a validated clip plan for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Video editors and agents use this skill to validate an agent-selected clip plan and assemble source footage into a short video for subsequent narration planning and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing malformed or untrusted media with ffmpeg or ffprobe may be unsafe.

Mitigation: Prefer trusted media, keep ffmpeg current, and use a dedicated work directory.

Risk: Environment settings may change boundary snapping or rendered output.

Mitigation: Review relevant settings and inspect the validated clip plan and video before use.

## Reference(s):

- [Shot review guidance](references/shot-review.md)
- [ClawHub release](https://clawhub.ai/worldwonderer/skills/video-cut)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and commands; validated JSON clip plan and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional shot-review JSON; narration is not generated.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
