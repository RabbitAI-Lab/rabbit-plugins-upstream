## Description:

Generate Seedance 2.5 videos up to 30 seconds long, with up to 4K resolution, multimodal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts, optional image, video, or audio references, and first or last frame controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to the skill are sent to dLazy's hosted API and media storage.

Mitigation: Only submit prompts and media that are appropriate to share with the service.

Risk: The security scan advised checking the CLI and authentication steps, which it found were not clearly connected to the video-generation purpose.

Mitigation: Review the CLI and authentication instructions before installing or entering an API key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON generation results, Generated media, Media URLs]

**Output Format:** [JSON with generated media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completed media can optionally be saved to a local path; asynchronous runs can return a task ID.]

## Skill Version(s):

1.2.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
