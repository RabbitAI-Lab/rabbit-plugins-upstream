## Description:

Generates images with the Kling o1 model from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create images from text prompts or use reference images for image-to-image generation with Kling o1.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial, and it reported login behavior whose connection to image generation is unclear; the scan did not establish credential theft.

Mitigation: Review the CLI and its login flow before setup, and proceed only if that behavior is expected.

Risk: Prompts and local reference images are sent to dLazy's hosted service for generation.

Mitigation: Avoid sending sensitive prompts or images unless they are appropriate to share with the service.

Risk: The dLazy API key is stored in the local CLI configuration when using the login flow.

Mitigation: Keep the key private and rotate or revoke it through the dLazy dashboard if it is exposed.

## Reference(s):

- [dLazy CLI repository linked in the skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [PNG images and JSON response metadata containing hosted output URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to 10 reference images; supports multiple aspect ratios and asynchronous generation.]

## Skill Version(s):

1.3.42 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
