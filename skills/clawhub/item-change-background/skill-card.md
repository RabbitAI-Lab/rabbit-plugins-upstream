## Description:

Helps turn product photos with plain backgrounds into realistic lifestyle scenes with matching lighting, reflections, and contact shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and marketers use this skill to place product photos into photorealistic scenes while preserving product appearance and matching scene lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and optional brand references are sent to the configured image-generation provider.

Mitigation: Use an approved provider; choose it explicitly and inspect requests in dry-run mode. Avoid private customer data and unreleased assets unless approved.

Risk: Generated scenes may change product details or imply misleading product use.

Mitigation: Review each image for product fidelity, believable lighting and shadows, and appropriate placement before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with prompt templates and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can save generated product-scene image files locally.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
