## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, for text-to-image and image editing. Fast and cost-effective for high-volume everyday generation; supports reference images, aspect ratios up to 21:9 and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and developers use this skill to generate images from text prompts or edit images with optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to dLazy's hosted service, and local reference files are uploaded.

Mitigation: Use only prompts and files you are comfortable sharing with the service.

Risk: Login stores a dLazy API key in the local CLI configuration.

Mitigation: Protect access to the local account and rotate or revoke the key when it is no longer needed.

Risk: Generation uses account credits, and operation depends on the external dLazy CLI and service.

Mitigation: Review the CLI and service before use, and use the dry-run option to inspect the cost estimate before submitting a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets returned as JSON with image URLs; optionally saved as image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous results or asynchronous task IDs, with configurable aspect ratio and image quality.]

## Skill Version(s):

1.2.24 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
