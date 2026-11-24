## Description:

Generate MiniMax Hailuo video clips with native stereo audio from text prompts, frame pairs, or multiple reference assets, with durations of 5–15 seconds and resolutions up to 2K.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to generate short MiniMax Hailuo videos from prompts, first and last frames, or reference images, videos, and audio. They can configure clip duration, resolution, and aspect ratio, then receive a media URL or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI package was unavailable for inspection, so the scan could not verify that all advertised options work as described.

Mitigation: Review the third-party CLI and its options before installing or relying on a generation workflow.

Risk: Local image, video, or audio files supplied as references are uploaded to dLazy media storage, and prompts are sent to its hosted API.

Mitigation: Only submit prompts and media that you are permitted to share with the service.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON result with generated media URLs; optionally a saved video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated clips are 5–15 seconds; resolution and aspect ratio are configurable.]

## Skill Version(s):

1.2.40 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
