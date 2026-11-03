## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation with strong text rendering, multi-line layout, photorealistic detail, and semantic adherence for mixed text and image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate images from text prompts, optionally guided by reference images, with Qwen Image 2 Pro.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's hosted service, and the external CLI and service behavior were not fully audited.

Mitigation: Avoid uploading sensitive material, use images you are authorized to share, and review the service terms before use.

Risk: The CLI stores an API key locally, and image generation may incur costs.

Mitigation: Use a revocable key, protect the local CLI configuration, and check the cost estimate before submitting a request.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits dashboard](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON generation result with image URLs and task status; optionally a saved image file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests accept a text prompt and up to three reference images; generation supports listed image sizes and asynchronous results.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
