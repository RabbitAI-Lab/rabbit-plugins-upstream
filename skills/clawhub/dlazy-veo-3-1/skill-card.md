## Description:

Generate cinematic videos with Google Veo 3.1 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to generate short videos from text prompts, guide generation with images, or extend an existing video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial, and it noted a possible mismatch between the video-generation description and a CLI login command.

Mitigation: Review the Chinese skill file's padded section and confirm the pinned CLI package and its login behavior before installing.

Risk: Prompts and local image, video, or audio inputs are sent to dLazy's hosted service; local media may be uploaded for generation.

Mitigation: Avoid submitting sensitive prompts or media unless their use with the hosted service is authorized.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [CLI project listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Videos, JSON, Guidance]

**Output Format:** [JSON result containing generated media URLs, task status, or errors, with video assets hosted by dLazy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts, reference images, and video extension; duration, aspect ratio, and resolution depend on generation mode.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
