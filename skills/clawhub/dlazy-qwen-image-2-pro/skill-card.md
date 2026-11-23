## Description:

Generates images with Alibaba Bailian's Qwen Image 2 Pro, including detailed compositions, rendered text, and Chinese and English layouts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to generate images from text prompts, with optional reference images and controls for image size, prompt expansion, and saving results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference images are sent to dLazy's hosted API and media storage, and use requires a dLazy API key.

Mitigation: Avoid sending sensitive content, and use an account and service you trust.

Risk: The security scan was partial with medium confidence and flagged login behavior whose connection to image generation was unclear.

Mitigation: Review the CLI installation and credential requirements and assess whether you trust the dLazy login and service before use.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with JSON result metadata and image URLs]

**Output Parameters:** [Prompt with optional reference images]

**Other Properties Related to Output:** [Supports asynchronous generation and saving image results to a local path.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
