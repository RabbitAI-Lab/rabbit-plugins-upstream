## Description:

平铺图转隐形模特立体图。平铺图 -> 有体积感与版型的立体展示图。当用户说「转 3D」「立体图」「隐形模特」「把衣服撑起来」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and product-content teams use this skill to turn flat-lay garment photos into ghost-mannequin-style product images with apparent volume while preserving garment color, texture, trim, and proportions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and reference images may be sent to external image-generation providers.

Mitigation: Use the skill only with images and prompts that are approved for the selected provider, and confirm the provider route before generation.

Risk: Remote image URLs may expose private or internal resources when fetched from the local machine.

Mitigation: Prefer local image files, avoid private or internal URLs, and harden URL fetching before shared or corporate-network use.

Risk: Generated garment images can distort fit, fabric details, or proportions.

Mitigation: Review outputs against the source garment before publication and regenerate with stronger preservation prompts when details drift.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Example flat-lay input image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/to-3d/garment-flatlay.jpg)
- [Example 3D output image](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/to-3d/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces saved JPEG image files through the selected image-generation provider; supports dry-run cost estimates and batch generation.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
