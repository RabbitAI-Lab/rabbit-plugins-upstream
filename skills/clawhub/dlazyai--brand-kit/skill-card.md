## Description:

Helps ecommerce teams keep product imagery consistent across SKUs by applying a shared brand configuration to image-generation prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and developers use this skill to define shared model, lighting, composition, layout, and exclusion rules for product images across a store's SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model references, prompts, and remote image URLs may be shared with the selected cloud image-generation provider.

Mitigation: Review requests with --dry-run and use a provider whose data handling is acceptable before generating images.

Risk: The example brand configuration specifies model demographics that may not suit the store.

Mitigation: Customize brand.yaml, including model details and reference images, before use.

## Reference(s):

- [Brand Kit release](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand configuration schema](references/brand-schema.md)
- [Provider usage and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance with YAML configuration and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can preview brand constraints as text or JSON; image generation can save resulting files.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
