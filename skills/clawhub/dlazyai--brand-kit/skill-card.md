## Description:

Helps keep ecommerce product imagery visually consistent across SKUs using a shared brand configuration for models, color, composition, layout, and exclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Store owners and ecommerce creative teams use this skill to define a reusable visual style and apply it across product images for multiple SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating images through a cloud provider can send prompts and reference images outside the local environment.

Mitigation: Review the provider guide, select the provider intentionally, and avoid confidential images or internal URLs unless external processing is acceptable.

Risk: Example brand settings may impose unsuitable model demographics or visual constraints on real products.

Mitigation: Edit the example configuration for the actual brand and review a sample image before generating a full batch.

## Reference(s):

- [Brand Kit release](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand configuration schema](references/brand-schema.md)
- [Image provider guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Configuration, Text, Shell commands, Images]

**Output Format:** [YAML brand configuration, prompt guidance, and generated image files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual constraints are selected according to the image task.]

## Skill Version(s):

1.0.19 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
