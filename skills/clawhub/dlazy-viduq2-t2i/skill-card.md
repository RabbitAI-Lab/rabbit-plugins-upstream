## Description:

Generate high-quality images with Vidu Q2, with support for text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from prompts or create images from prompts and reference images with Vidu Q2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment notes that the reported login flow's relationship to the image-generation purpose was not established, and that its analysis was partial.

Mitigation: Before authenticating, verify the CLI login flow through dLazy's published resources and review the CLI package details.

Risk: Prompts and local reference images are sent to dLazy services for processing.

Mitigation: Send only prompts and images you are authorized to share with the service; avoid confidential content.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Image assets, JSON result metadata]

**Output Format:** [Image files or hosted image URLs with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With --no-wait, returns a generation ID for an asynchronous task.]

## Skill Version(s):

1.3.42 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
