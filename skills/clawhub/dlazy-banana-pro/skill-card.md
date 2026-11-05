## Description:

Generate/edit images with Nano Banana Pro. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to generate images from text prompts or edit images with reference images using Nano Banana Pro.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy for cloud image generation.

Mitigation: Upload only media you are authorized to share and comfortable sending to the hosted service.

Risk: The API key is stored in the local CLI configuration.

Mitigation: Protect the local configuration file and rotate or revoke the key if it may have been exposed.

Risk: The skill review does not audit the external CLI executable or hosted service.

Mitigation: Review the pinned CLI before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy website](https://dlazy.com)
- [CLI project link (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [CLI package listing](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files or hosted image URLs, returned in a JSON result.]

**Output Parameters:** [Prompt, optional reference images (up to 14), aspect ratio, and image size.]

**Other Properties Related to Output:** [Asynchronous mode returns a task ID before image outputs are ready; results can be saved locally.]

## Skill Version(s):

1.2.41 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
