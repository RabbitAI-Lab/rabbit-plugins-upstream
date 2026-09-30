## Description:

Defines a reusable brand.yaml visual guide to keep ecommerce product imagery consistent across SKUs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and creative operators use a shared brand guide to align model references, lighting, composition, and layout across product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, and optional model reference images may be sent to a third-party image provider.

Mitigation: Run --dry-run first, choose the provider deliberately, and upload confidential assets only when approved.

Risk: A missing model reference image may reduce consistency across generated images.

Mitigation: Check the reference path and image before generating a batch.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand configuration schema](references/brand-schema.md)
- [Image provider and CLI guidance](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Configuration, Text, Images]

**Output Format:** [YAML brand guide, prompt constraints, and optionally generated image files or JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Applies relevant brand sections by task; optionally includes a model reference image.]

## Skill Version(s):

1.0.13 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
