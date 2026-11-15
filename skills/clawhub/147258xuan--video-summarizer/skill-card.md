## Description:

Extract keyframes and metadata from video files using ffmpeg scene detection. Use when you need to analyze, summarize, or extract scenes from a video file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[147258xuan](https://clawhub.ai/user/147258xuan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to extract scene keyframes and video metadata from local video files for review and summarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing keyframe images may be overwritten without warning; the security scan was incomplete.

Mitigation: Check for existing keyframe images before running, and set a dedicated outputDir to keep extracted frames separate.

## Reference(s):

- [Video Summarizer on ClawHub](https://clawhub.ai/147258xuan/skills/video-summarizer)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [JPEG keyframe image files and JSON metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keyframes are saved as image files; metadata includes scene timestamps, duration, dimensions, frame rate, and keyframe count.]

## Skill Version(s):

0.1.0 (source: package.json and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
