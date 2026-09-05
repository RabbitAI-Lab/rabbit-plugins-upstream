## Description:

平铺图转隐形模特立体图。平铺图 → 有体积感与版型的立体展示图。当用户说「转 3D」「立体图」「隐形模特」「把衣服撑起来」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and developers use this skill to turn flat-lay garment photos into dimensional ghost-mannequin product images while preserving color, material, pattern placement, and garment proportions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, prompts, and related reference files may be sent to the configured cloud image-generation provider.

Mitigation: Use the skill only with images approved for the selected provider agreement, review the selected provider and API key before execution, and use --dry-run to inspect requests before upload or credit spend.

Risk: Generated product images may alter garment structure, proportions, texture, or labels despite the preservation prompt.

Mitigation: Inspect each output for body artifacts, changed proportions, incorrect collar depth, lost knit or material detail, and inconsistent shadows before using it in a product listing.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy E-commerce Skills Repository](https://github.com/dlazy-ai/ecommerce-skills)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/to-3d)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and generated JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses cloud image-generation providers and can dry-run requests before uploading images or spending credits.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
