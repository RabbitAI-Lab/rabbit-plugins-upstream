## Description:

Helps storefront teams keep product imagery consistent across SKUs using a shared brand configuration for models, lighting, composition, and tone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Storefront teams and developers use a shared brand.yaml to guide consistent imagery across product listings and batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced product or model images may be sent to the selected image-generation provider.

Mitigation: Choose a trusted provider and share only images and prompts you are comfortable sending to it.

Risk: The sample brand configuration includes fixed human model attributes, and batch generation may multiply unwanted results.

Mitigation: Review or edit the sample configuration, then dry-run or select a provider explicitly and test one SKU before generating a batch.

## Reference(s):

- [Brand Kit release](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand configuration schema](artifact/references/brand-schema.md)
- [Image provider usage](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Configuration, Shell commands]

**Output Format:** [Brand YAML, generation prompts, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional image files when generation commands are run]

## Skill Version(s):

1.0.21 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
