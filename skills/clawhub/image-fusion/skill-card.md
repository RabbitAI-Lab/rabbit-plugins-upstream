## Description:

Creates a cohesive e-commerce outfit image from up to eight product photos on one model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams combine product photos into coordinated model-worn outfit images for listings and campaigns, with optional pose or model references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos, prompts, and optional model or reference images are sent to the configured cloud image provider.

Mitigation: Confirm permission to share each image and prompt with the selected provider before generation.

Risk: Cloud generation can incur charges and requires provider credentials.

Mitigation: Review the provider credentials and billing, and use a dry run to estimate cost before generating.

Risk: The default model description may not fit the intended brand or representation.

Mitigation: Customize the model description and review generated images before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider configuration and output guide](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Text guidance, Shell commands]

**Output Format:** [Generated image files with Markdown guidance and command examples]

**Output Parameters:** [2D images]

**Other Properties Related to Output:** [Supports up to eight product photos per outfit, with optional pose and model references; review the resulting image for product fidelity.]

## Skill Version(s):

1.0.17 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
