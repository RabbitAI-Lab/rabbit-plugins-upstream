## Description:

Generates images with Alibaba Bailian Qwen Image 2 Pro, supporting prompts, up to three reference images, multiple aspect ratios, prompt rewriting, dry runs, and asynchronous generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate images through the dLazy-hosted Qwen Image 2 Pro service, including text-heavy or mixed Chinese and English image designs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local files passed as inputs may be uploaded to the dLazy cloud service.

Mitigation: Use the skill only when cloud processing is acceptable, avoid passing sensitive local files unless approved, and review prompt and file inputs before invocation.

Risk: The dLazy CLI can store an organization API key in a local user configuration file.

Mitigation: Prefer DLAZY_API_KEY on shared systems, review local config file permissions, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Generated files are returned as hosted URLs from the dLazy file service.

Mitigation: Treat returned URLs according to the user's data-handling policy and avoid sharing outputs that contain sensitive or restricted content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-image-2-pro)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Shell command output containing JSON with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted file URLs; asynchronous mode can return a task identifier for later polling.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
