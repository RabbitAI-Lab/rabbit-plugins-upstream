## Description:

Generate high-quality images with Vidu Q2. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to create images from text prompts or edit images using Vidu Q2. Developers can provide image references and choose output dimensions and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a possible mismatch between the declared image-generation purpose and the behavior covered by the scan, with some references unresolved.

Mitigation: Confirm the intended workflow and review the complete skill and its referenced CLI behavior before installation.

Risk: Prompts and any supplied local image files are sent to dLazy-hosted services for generation.

Mitigation: Avoid submitting sensitive prompts or images unless their transfer to the service is acceptable.

## Reference(s):

- [dLazy CLI repository (listed in skill documentation)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Image assets with JSON result metadata, including output URLs and MIME types]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image; asynchronous requests may return a task ID before image outputs are ready.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
