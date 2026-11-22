## Description:

Generate/edit images with Nano Banana Pro. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents can use this skill to create images from text prompts or edit images using reference images, with selectable aspect ratios and output sizes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial, and it could not establish how the CLI login step relates to image generation.

Mitigation: Review the CLI login flow and decide whether you are comfortable authorizing it before installing or using the skill.

Risk: The skill documentation says prompts and local reference images are sent to dLazy hosted services.

Mitigation: Only submit prompts and images that you are comfortable sending to the dLazy service.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Generated images with hosted URLs or saved files, plus JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image with up to 14 reference images, preset aspect ratios, and 1K, 2K, or 4K sizes.]

## Skill Version(s):

1.2.46 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
