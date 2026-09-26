## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation for complex text rendering, multi-line layouts, photorealistic detail, and mixed Chinese-English image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Qwen Image 2 Pro generation workflow from an agent, producing images from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external hosted dLazy CLI and sends prompts and generation parameters to dLazy services.

Mitigation: Review prompts for sensitive content before execution and confirm network use to api.dlazy.com is acceptable.

Risk: The CLI stores a dLazy API key in local configuration or accepts it through an environment variable.

Mitigation: Use a scoped API key, keep local config access restricted to the OS user, and rotate or revoke the key when access changes.

Risk: Local image paths explicitly provided by the user may be uploaded to the hosted service for model input.

Mitigation: Provide only files intended for processing by the hosted service and avoid passing private or regulated images unless approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted CLI returns JSON containing generated image output URLs; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
