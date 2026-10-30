## Description:

商品精修、去褶皱。随手拍的商品图 → 可直接上架的精修图。当用户说「精修」「去褶皱」「修图」「拍得不好看」「整理一下」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce teams use this skill to refine product photos for catalog listings by improving presentation and lighting while preserving product design, colors, patterns, hardware, and structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image processing uploads selected photos and prompts to the chosen cloud provider and may incur charges.

Mitigation: Choose the provider explicitly, preview requests with --dry-run, and use only images approved for cloud processing.

Risk: Generated edits may alter product details or present a damaged item inaccurately.

Mitigation: Compare results with the originals, confirm defining product details remain accurate, and do not use retouching to conceal defects.

## Reference(s):

- [Item Repair on ClawHub](https://clawhub.ai/dlazyai/skills/item-repair)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Edited product image files (JPEG, PNG, or WebP), with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image files are saved to selected output paths; the workflow supports 1–4 images of the same product.]

## Skill Version(s):

1.0.25 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
