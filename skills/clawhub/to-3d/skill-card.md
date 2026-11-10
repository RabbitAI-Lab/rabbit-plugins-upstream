## Description:

平铺图转隐形模特立体图。平铺图 → 有体积感与版型的立体展示图。当用户说「转 3D」「立体图」「隐形模特」「把衣服撑起来」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product content teams use the skill to turn flat-lay clothing photos into dimensional ghost-mannequin product images. It provides image-generation prompts and commands for creating and saving those images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input garment images may be sent to an external image-generation provider for processing.

Mitigation: Use only images approved for external processing and review the selected provider's privacy terms before uploading.

Risk: The security scan reports incomplete analysis of some files, so its suspicious verdict has unresolved uncertainty.

Mitigation: Review the skill and its files before running its commands, taking the incomplete scan coverage into account.

## Reference(s):

- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [Related one-shot skill guide](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/one-shot/skill.md)
- [Related material-enhancement skill guide](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance with image-generation prompts and inline shell commands; generated product images are typically JPEG.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image aspect ratio, quality, and optional batch size can be configured.]

## Skill Version(s):

1.0.30 (source: frontmatter; release metadata agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
