## Description:

Generates high-resolution images from text prompts and reference images using the Seedream 5.0 model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate high-resolution visuals, posters, and print-oriented artwork from prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's cloud service.

Mitigation: Use only content you are authorized and comfortable sharing with the service.

Risk: The organization API key may be stored in the local CLI configuration.

Mitigation: Protect the configuration file and rotate or revoke the key when needed; the documented environment-variable option avoids saving it through CLI authentication.

Risk: Image generation can incur account costs.

Mitigation: Review the cost estimate with the documented dry-run option before submitting a generation request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON results containing generated image URLs and metadata, with optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt and reference-image inputs, 2K/3K/4K resolutions, selectable aspect ratios, and asynchronous job results.]

## Skill Version(s):

1.2.29 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
