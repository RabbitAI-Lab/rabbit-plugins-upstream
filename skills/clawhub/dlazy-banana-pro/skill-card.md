## Description:

Generate and edit images with Nano Banana Pro using text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to create images from text prompts or edit existing images with Nano Banana Pro.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI login flow saves a dLazy API key in the local user configuration.

Mitigation: Authenticate only with an account you control, protect the local configuration, and rotate or revoke the key if it may have been exposed.

Risk: Prompts and supplied local images are sent to dLazy services for image generation or editing.

Mitigation: Send only prompts and images you are authorized to share with the service, especially when they contain sensitive information.

Risk: The benign scan had medium confidence and partial coverage; it did not inspect the referenced CLI package and some references were unresolved.

Mitigation: Review the CLI package and unresolved references before installation; treat the scan verdict as guidance rather than a safety guarantee.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with JSON result metadata and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation or editing; supports asynchronous task identifiers when requested.]

## Skill Version(s):

1.2.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
