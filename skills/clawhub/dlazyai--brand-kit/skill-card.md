## Description:

Defines a reusable brand guide for consistent product imagery across an ecommerce store, including model references, lighting, composition, layout, and visual tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and creators use a shared brand.yaml to keep product imagery visually consistent across SKUs and image-generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation sends prompts and reference images to the selected provider.

Mitigation: Choose the provider deliberately and avoid sending confidential product images or private face references to providers you do not trust.

Risk: Brand settings may include sensitive model or demographic constraints.

Mitigation: Review brand.yaml and any model references before generating images.

## Reference(s):

- [Brand configuration schema](references/brand-schema.md)
- [Image provider usage guide](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [Configuration, Text, Shell commands]

**Output Format:** [YAML brand guide and plain-text prompt constraints; optional generation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation can save image files through a selected provider.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
