## Description:

A professional product image generation skill for Amazon product listings that helps agents plan and generate compliant main images, secondary images, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, designers, and developers use this skill to plan and generate Amazon-ready product listing imagery, including main images, secondary infographics, lifestyle and detail images, and A+ Brand Content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes a third-party npm package and stores a dLazy API key locally.

Mitigation: Review the dLazy CLI package and intended version before installation, protect the local API key file, and rotate or revoke the key when access changes.

Risk: Product prompts and local media can be sent to dLazy cloud services for generation.

Mitigation: Only provide product images, media, and copy that are approved for upload to dLazy's cloud service.

Risk: Generated marketplace imagery or claims may still be inaccurate or noncompliant for a specific listing.

Mitigation: Review generated images, text, visual claims, and Amazon guideline compliance before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown status updates with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides iterative image generation through dLazy CLI commands, with user confirmation between generated assets.]

## Skill Version(s):

1.3.21 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
