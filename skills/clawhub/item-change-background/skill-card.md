## Description:

Helps turn product photos on plain backgrounds into realistic lifestyle scenes with matching lighting, reflections, and contact shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to place existing product photos into suitable lifestyle settings while aiming to preserve product details and match the scene's lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected image-generation provider.

Mitigation: Choose the provider deliberately; avoid confidential unreleased assets unless its terms and account controls are acceptable.

Risk: Image-generation requests may incur costs.

Mitigation: Use --dry-run first to inspect the request and estimated cost.

Risk: Generated scenes may change product details or imply an unsuitable use.

Mitigation: Review product fidelity, lighting, shadows, and scene suitability before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with prompt and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands can generate product scene image files; review results before publication.]

## Skill Version(s):

1.0.16 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
