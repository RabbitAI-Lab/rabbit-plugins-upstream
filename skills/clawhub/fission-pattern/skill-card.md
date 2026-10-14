## Description:

Turns one product photo and its selling points into a coordinated set of e-commerce images with varied angles and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content teams use this skill to create consistent product-image sets for listings and detail pages from a single product photo and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and brand assets are uploaded to the selected image provider.

Mitigation: Confirm that the assets are appropriate to share and choose the provider explicitly; use dry-run to check the planned request before submitting it.

Risk: Generated images may drift from the actual product or differ across the set.

Mitigation: Keep identifying product details consistent in every prompt and inspect all images together before publishing; rerun individual mismatches.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and shell commands; generated product images saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Multiple coordinated images with distinct angles or scenes; output location is configurable.]

## Skill Version(s):

1.0.21 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
