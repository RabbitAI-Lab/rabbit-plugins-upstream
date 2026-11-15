## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, supports text-to-image generation and image editing with reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create images from prompts or edit images using reference images, with configurable aspect ratio and quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the CLI requires a dLazy API key, and the security review of the CLI authentication flow was partial.

Mitigation: Review the CLI authentication flow before installation, protect the key, and rotate or revoke it through the dLazy dashboard if needed.

## Reference(s):

- [dLazy CLI repository (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON, Files]

**Output Format:** [JSON result with generated image URLs and metadata; image files can also be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to five reference images; supports auto and fixed aspect ratios through 21:9, quality from low to max, and asynchronous generation.]

## Skill Version(s):

1.2.30 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
