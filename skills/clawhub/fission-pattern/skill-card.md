## Description:

Turns a product photo and selling points into a coordinated set of e-commerce images from multiple angles and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn one product photo into a consistent set of listing and detail-page images with varied angles, settings, and close-ups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images are sent to the selected cloud image provider.

Mitigation: Use only an approved provider for confidential or customer-identifying images; otherwise avoid submitting sensitive images.

Risk: Image generation may incur charges, and results may misrepresent product details.

Mitigation: Check the destination and estimated cost with dry-run before generating, then review the images against the original product before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Image model options](artifact/references/model-flags.md)
- [Provider and CLI guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images, Text, Shell commands]

**Output Format:** [JPEG image files with prompt and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a coordinated series of product views; users can review and regenerate individual images.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
