## Description:

Helps e-commerce teams plan controlled product-image A/B tests by generating comparison main-image variants, recording hypotheses, checking listing compliance, and producing a retrospective template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketers, and listing teams use this skill to design single-variable product-main-image A/B tests, generate controlled image variants, and prepare a post-test review table. It also helps check objective platform listing requirements before variants are used in an experiment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the configured cloud image-generation provider.

Mitigation: Confirm the selected provider and data-sharing expectations before running generation commands, especially for confidential product imagery.

Risk: Compliance repair can create modified JPEG copies of listing assets.

Mitigation: Use repair options only when modified local outputs are intended, and review the resulting images before publishing.

Risk: Example brand and model defaults may not match the seller's market or brand requirements.

Mitigation: Replace the sample brand configuration with market-appropriate brand, model, photography, and platform settings before generating final variants.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [platform-specs.md](references/platform-specs.md)
- [provider-cli.md](references/provider-cli.md)
- [platform-compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [brand-kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands, JSON-capable CLI output, and local image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-generation prompts, controlled A/B test hypotheses, compliance-check commands, and a fillable retrospective table; generated image files are written locally by the configured provider workflow.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
