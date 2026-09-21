## Description:

Turns plain product images into photorealistic scene images with grounded shadows, matching light, and environmental reflections while preserving the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and developers use this skill to generate background-replaced product imagery from a plain product image or a product plus reference background. It guides prompt construction, provider selection, dry runs, batch generation, and quality checks for realistic commercial product photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and referenced background images may be sent to the configured image provider.

Mitigation: Use this skill only with images and prompts that are appropriate to share with the selected provider, and avoid sensitive local files or private/internal URLs.

Risk: Generation can create misleading product scenes if the requested background implies unsupported product properties or usage.

Mitigation: Keep scenarios physically plausible for the product category and avoid prompts that imply unsupported claims, such as placing non-waterproof products in water.

Risk: Incorrect save paths can place generated assets in unintended locations.

Mitigation: Use dry runs to inspect requests before execution and review save paths before running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated assets are saved as image files or returned as provider URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run request inspection, provider selection, batch generation, and local save paths.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
