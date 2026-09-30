## Description:

Guides agents in restoring realistic garment texture in product photos using a high-resolution photo of the same item while preserving the original composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product-image editors use this skill to guide cloud image editing that rebuilds clothing fabric detail from a matching product reference without intentionally changing the model, color, or background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to dlazy or another configured cloud image provider.

Mitigation: Use explicit image paths, avoid private URLs and sensitive files, and preview the request with --dry-run before sending.

Risk: Image editing may unintentionally alter garment color, the model, or the background, or reconstruct the wrong fabric if reference photos do not match.

Mitigation: Use a reference photo of the same product and compare the edited result against the original before publishing.

## Reference(s):

- [Material Enhancement on ClawHub](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with image-editing prompts and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the suggested commands can save edited image files; inspect the result before use.]

## Skill Version(s):

1.0.14 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
