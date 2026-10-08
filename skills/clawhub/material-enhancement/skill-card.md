## Description:

Enhances fabric texture and fine detail in apparel photos using a high-resolution image of the same product as a reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce photographers and creative teams use this skill to restore realistic fabric detail in product photos while aiming to preserve the model, garment shape, color, and background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected image provider.

Mitigation: Avoid sensitive local images and private image URLs; confirm the selected provider before running.

Risk: Image-generation requests may incur costs or use unintended provider credentials.

Mitigation: Run a dry-run to inspect requests and estimated costs, and review active provider credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider setup and output guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Enhanced image files with Markdown instructions and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review the result against the original for texture accuracy, color fidelity, and unintended edits.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
