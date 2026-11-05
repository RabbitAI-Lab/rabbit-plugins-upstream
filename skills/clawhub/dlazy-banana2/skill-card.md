## Description:

Generate and edit high-quality images with Nano Banana 2.0, including text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate images from text prompts or edit images using Nano Banana 2.0, with optional reference images and local saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images are sent to dLazy's hosted service, and image generation may incur charges.

Mitigation: Use only prompts and images you consent to share, and consider the cost before generating.

Risk: The dLazy API key is stored in the local CLI configuration.

Mitigation: Protect access to the local account and rotate or revoke the key if it is exposed.

Risk: The pinned CLI package and its claimed credential protections were not verified.

Mitigation: Review @dlazy/cli@1.2.3 before installing or authenticating.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON containing generated image URLs; images can optionally be saved as local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronously; accepts up to 14 reference images.]

## Skill Version(s):

1.3.37 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
