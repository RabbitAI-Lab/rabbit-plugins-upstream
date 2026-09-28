## Description:

Guides agents through planning and generating Amazon product listing images and A+ content using dLazy's CLI and hosted image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and creative teams use this skill to plan and generate Amazon listing main images, secondary images, and A+ brand content, reviewing each image before continuing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the third-party CLI and hosted service requires an API key.

Mitigation: Review the CLI package before installation; protect the key and rotate or revoke it if needed.

Risk: Generation prompts and selected local media may be sent to dLazy's cloud service.

Mitigation: Confirm each generation command and share only prompts and files appropriate for upload.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with image URLs and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are generated individually after user confirmation and hosted by dLazy.]

## Skill Version(s):

1.3.23 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
