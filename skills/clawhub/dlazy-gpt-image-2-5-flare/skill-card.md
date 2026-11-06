## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for text-to-image and image editing. Fast and cost-effective for high-volume everyday generation; supports reference images, aspect ratios up to 21:9 and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate or edit images from text prompts, optionally using reference images, and receive generated image URLs or save image files locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy, and local API-key configuration is required.

Mitigation: Use only prompts and images you are comfortable uploading, and keep the API key private; rotate or revoke it if needed.

Risk: Generation requests may consume account credits, and the external CLI and hosted service were not fully audited.

Mitigation: Use the documented dry-run option to review the payload and cost estimate, and review the CLI and service before use.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI project listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs and metadata; image files can also be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Synchronous results include image URLs; asynchronous runs can return a task ID for later status checks.]

## Skill Version(s):

1.2.27 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
