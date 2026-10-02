## Description:

Helps storefront teams keep imagery consistent across products using a shared brand specification for models, lighting, composition, layout, and tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Storefront teams and their agents use a shared brand.yaml to maintain consistent product imagery across SKUs, preview task-specific visual guidance, and optionally generate images with the selected provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image-generation commands may send prompts and selected images to an external provider.

Mitigation: Review provider selection and preview with --dry-run; use only providers approved for any sensitive product images, URLs, or prompt content.

Risk: A missing model reference image is skipped, which can reduce visual consistency.

Mitigation: Check reference paths and preview one product before generating a batch.

## Reference(s):

- [Brand specification fields and task mapping](references/brand-schema.md)
- [Provider configuration and data flow](references/provider-cli.md)
- [ClawHub Brand Kit release](https://clawhub.ai/dlazyai/skills/brand-kit)
- [dLazy CLI source and usage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown guidance with YAML configuration and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce a reusable brand.yaml and optionally save provider-generated product images.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
