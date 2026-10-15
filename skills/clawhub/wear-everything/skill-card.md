## Description:

Guides agents in creating on-model ecommerce images of shoes, bags, and accessories from product and model reference photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce creators and agents use product and model photos to generate realistic on-model images of footwear, bags, and accessories while preserving product details and the surrounding scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or model images and prompt text are sent to the selected cloud image provider.

Mitigation: Use only images approved for sharing; run a dry run and check the selected provider and API key before generation.

Risk: Generated images can alter product details, model appearance, or placement despite preservation instructions.

Mitigation: Review the generated image against both references for product fidelity, realistic placement, and unintended changes before publishing.

Risk: Generation writes files to a local output path.

Mitigation: Choose and confirm a suitable output path before running the command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell command examples and image-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, saves generated on-model image files to a user-selected local path.]

## Skill Version(s):

1.0.21 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
