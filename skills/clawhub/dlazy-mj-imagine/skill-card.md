## Description:

Generates stylized images through a Midjourney-style workflow, with configurable aspect ratio, bot type, and grid or upscaled output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate artistic images from prompts, choose an aspect ratio and Midjourney or Niji Journey bot type, and request a grid or an upscaled result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted a mismatch between the advertised image-generation purpose and inspected CLI authentication instructions; some referenced details could not be fully checked.

Mitigation: Before use, confirm the dLazy CLI provides the intended image-generation command and review its package and external service flow.

Risk: Prompts and supplied local media are sent to dLazy hosted endpoints.

Mitigation: Avoid sending sensitive prompts or files unless your organization permits that service flow.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON metadata, Image URLs or saved image files]

**Output Format:** [Image assets with JSON status and result metadata]

**Output Parameters:** [Prompt with optional aspect ratio, bot type, output selection, and asynchronous wait settings]

**Other Properties Related to Output:** [Results may be returned as hosted URLs or saved locally; asynchronous mode can return a generation ID before completion.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
