## Description:

Convert the contents of a storyboard into a video-generation pipeline that the user can add to the canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video editors use the skill to turn storyboard details, dialogue, and scene prompts into a video-generation pipeline they can add to a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud rendering can send prompts and local media to dLazy services, creating data-sharing and potential cost concerns.

Mitigation: Keep rendering optional and get explicit agreement on submitted content, uploaded files, and possible charges; use canvas setup alone when preferred.

Risk: The release evidence identifies version 1.2.33, while the skill's CLI installation instructions specify @dlazy/cli 1.2.3.

Mitigation: Confirm the intended CLI package version before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, Configuration]

**Output Format:** [JSON video-generation pipeline configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canvas-ready pipeline assembled from storyboard dimensions, dialogue, and video prompts.]

## Skill Version(s):

1.2.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
