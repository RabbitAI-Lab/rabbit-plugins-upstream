## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use the skill to generate images from text prompts, optionally guided by reference images, through the dLazy Seedream service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local reference images are sent to dLazy hosted services, and generated assets are hosted there.

Mitigation: Avoid submitting sensitive prompts or images unless their transfer to the service is approved.

Risk: The security review was partial: the CLI package and some referenced local paths were unavailable for assessment, and the documented command only logs in despite the image-generation description.

Mitigation: Review the CLI package and any local files involved, and confirm the supported generation command before relying on the skill.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (declared in artifact metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, JSON, Guidance]

**Output Format:** [Generated image assets with a JSON result containing image URLs and metadata; Markdown guidance and shell commands for use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier; generated assets are hosted at dLazy file URLs and can optionally be saved locally.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
