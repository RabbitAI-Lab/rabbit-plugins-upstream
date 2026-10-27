## Description:

Generates high-quality images with Doubao Seedream 4.5 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can generate images from text prompts or reference images, choose output size and resolution, and optionally save generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted service; local input media is uploaded for processing.

Mitigation: Upload only content you are comfortable sharing with dLazy, and review the external CLI before installation.

Risk: The dLazy API key is saved in the local CLI configuration when using the login flow.

Mitigation: Protect the local API-key configuration and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Files, JSON]

**Output Format:** [Generated image files or hosted image URLs with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts and up to 10 reference images, with 2K or 4K resolution and selectable aspect ratios; asynchronous runs may return a task identifier before the image is ready.]

## Skill Version(s):

1.3.32 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
