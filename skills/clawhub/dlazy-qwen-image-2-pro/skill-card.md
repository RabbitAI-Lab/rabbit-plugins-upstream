## Description:

Alibaba Bailian qwen-image-2.0-pro image generation for complex text rendering, multi-line layouts, photorealistic detail, and mixed text/image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can generate images from prompts, optionally using reference images, with the Qwen Image 2 Pro model through dLazy. They can adjust image size and prompt handling, then receive or save the generated image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy, and generation incurs charges.

Mitigation: Confirm you are comfortable with the service and its charges; avoid uploading sensitive images unless you have appropriate permission.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the saved key and rotate or revoke it if needed; review the pinned CLI before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [Dlazy CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [Dlazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [Dlazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [Generated image asset (PNG) with a JSON result containing its URL and metadata; asynchronous requests can return task status.]

**Output Parameters:** [Variable; prompt, optional reference images (up to three), negative prompt, image size, and prompt extension.]

**Other Properties Related to Output:** [Generated images can optionally be saved to a local path.]

## Skill Version(s):

1.3.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
