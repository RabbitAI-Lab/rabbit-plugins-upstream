## Description:

Full version of the Doubao image model, generating 2K/3K/4K images from prompts and reference images. Suited to key visuals, posters and anything meant for large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams can use the skill to generate high-resolution campaign visuals, posters, and print-ready images from text prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy’s hosted service, and local reference files are uploaded for processing.

Mitigation: Only submit prompts and images you are comfortable sending to dLazy.

Risk: Login stores a reusable API key in the local CLI configuration.

Mitigation: Protect the local configuration file, or use the environment-variable option; rotate or revoke a key if it is exposed.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs and image metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation supports 2K, 3K, or 4K resolution, several aspect ratios, up to 10 reference images, and optional local saving; requests may consume account credits.]

## Skill Version(s):

1.2.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
