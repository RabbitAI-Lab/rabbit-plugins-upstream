## Description:

Brand Kit helps ecommerce teams keep generated product imagery consistent across SKUs by applying a reusable brand.yaml for model identity, lighting, composition, spacing, and copy tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and creative teams use this skill to define a store-level visual brand kit, preview the generated prompt additions, and pass the same brand constraints into image-generation workflows for consistent product visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product photos, and model reference images may be sent to the configured cloud provider or to the default dLazy CLI path during generation.

Mitigation: Use --dry-run and --doctor before generation, choose the provider deliberately, and verify the CLI and credentials before sending sensitive assets.

Risk: The example brand.yaml contains placeholder model and brand attributes that may not match approved brand requirements.

Mitigation: Replace the example values with approved brand, model, photography, layout, and compliance requirements before production use.

Risk: A missing model.reference file is skipped with a warning, which can reduce model identity consistency across generated images.

Mitigation: Check reference image paths and run one SKU comparison before batch generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/brand-kit)
- [brand.yaml field reference](artifact/references/brand-schema.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with YAML configuration examples, shell commands, prompt text additions, optional JSON reports, and generated file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses brand.yaml to append reusable visual constraints and, when configured, an extra model reference image to downstream generation commands.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
