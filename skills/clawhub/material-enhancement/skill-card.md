## Description:

Enhances fabric texture in apparel photos using a high-resolution image of the same product while aiming to preserve the model, composition, silhouette, and color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and their agents use this skill to restore realistic clothing textures in product photos against a matching high-resolution reference, without intentionally changing the model or scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and related metadata are sent to the configured cloud provider.

Mitigation: Send only images and details you are comfortable sharing with that provider.

Risk: Image-generation requests can incur charges.

Mitigation: Run a dry-run first to inspect requests and estimated cost.

Risk: Provider credentials may be exposed or misused if poorly managed.

Mitigation: Use scoped, revocable API keys and keep them out of shared outputs.

Risk: An optional unpinned skill installation may retrieve a changed upstream version.

Mitigation: Verify the referenced repository and version before running that installation command.

## Reference(s):

- [ClawHub material-enhancement release](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JPEG image files and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an on-model photo and a matching high-resolution product image; outputs should be checked for texture fidelity and unintended changes.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
