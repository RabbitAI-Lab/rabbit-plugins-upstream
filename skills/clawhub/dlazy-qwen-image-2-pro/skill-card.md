## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation for complex text rendering, multi-line layout, photorealistic detail, semantic adherence, and mixed Chinese-English image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to invoke dLazy's hosted Qwen Image 2 Pro workflow for text-to-image generation, optional reference-image inputs, asynchronous generation, and saved image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input media may be sent to dLazy's hosted service for generation.

Mitigation: Use the skill only for content that can be shared with dLazy and avoid submitting sensitive prompts or media unless that use is approved.

Risk: Login can store a dLazy API key in local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable or the pinned npx path when less local persistence is preferred, and rotate or revoke API keys when needed.

Risk: Generated image outputs are hosted by dLazy.

Mitigation: Review returned output URLs and data-handling requirements before sharing or retaining generated assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces hosted image output URLs and can save generated image assets locally when requested.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
