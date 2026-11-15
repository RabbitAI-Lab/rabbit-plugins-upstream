## Description:

Convert the contents of a storyboard into a video-generation pipeline that the user can add to the canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to turn storyboard details, including aspect ratio, resolution, scene names, dialogue, and prompts, into a JSON video-generation pipeline arranged for addition to a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires CLI authentication and cloud image generation, which may send prompts or media to an external service and may incur charges.

Mitigation: Review the suspicious security verdict before installing; avoid sending sensitive prompts or media, and check the service's charges before use.

Risk: The security analysis is incomplete because some referenced local paths could not be resolved.

Mitigation: Review the skill and its referenced CLI workflow before use, and treat the scan as partial.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON configuration, Guidance]

**Output Format:** [JSON pipeline configuration with canvas-drawing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pipeline dimensions are calculated from the storyboard's aspect ratio and resolution; the original audio and scene image are shared across storyboards.]

## Skill Version(s):

1.2.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
