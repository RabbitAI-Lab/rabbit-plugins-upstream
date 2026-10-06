## Description:

Retouches product photos for catalog use by reducing incidental wrinkles, balancing lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content teams use this skill to prepare single-product photos for listings while preserving colors, construction, and visible defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to an external image provider, exposing confidential catalog material.

Mitigation: Review before installing for confidential images; choose an approved provider explicitly and avoid private or internal image URLs.

Risk: The shared generation tool can fetch supplied image URLs and supports tasks beyond item repair.

Mitigation: Use --dry-run to inspect the intended request, prefer local files or trusted HTTPS sources, and review the tool's scope before execution.

Risk: Retouching may change product structure or hide defects, making listing images misleading.

Mitigation: Ask the model to preserve construction and visible defects, then compare output against the original before publishing.

## Reference(s):

- [Item Repair on ClawHub](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save retouched product images; compare results with originals before publishing.]

## Skill Version(s):

1.0.17 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
