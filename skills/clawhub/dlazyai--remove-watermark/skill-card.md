## Description:

Removes watermarks, text, logos, badges, promotional frames, and similar overlays from images, then reconstructs the covered areas with an image-editing model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and developers use this skill to clean product or marketing images before downstream image generation or publication. Outputs should be reviewed because covered regions are reconstructed rather than pixel-preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images and prompts may be sent to cloud image providers.

Mitigation: Use explicit provider selection and dry-run review, and avoid sensitive, confidential, or legally protected images.

Risk: Provider credentials or image data could be exposed through untrusted provider or endpoint configuration.

Mitigation: Keep API keys scoped and revocable, rotate them when needed, and do not set ARK_BASE_URL unless the endpoint is fully trusted.

Risk: The skill can be misused to remove copyright watermarks, brand marks, or legally required labels.

Mitigation: Use it only on images you have rights to edit, and do not remove ownership, brand, safety, certification, warning, ingredient, or other required markings.

Risk: Covered regions are reconstructed by the model and may not preserve the original pixels or exact product details.

Mitigation: Manually review generated images before use, especially when overlays cover products or important visual details.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/remove-watermark)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash commands and CLI output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, commands may save edited image files and may send prompts and input images to selected cloud providers.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
