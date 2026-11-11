## Description:

根据商品图片和卖点生成带中文排版的商品详情页图文模块。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce teams use this skill to turn product images and concise selling points into Chinese product detail visuals for listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and accompanying text may be sent to external image-generation services.

Mitigation: Avoid sending sensitive material; check the selected provider's data handling and confirm you are comfortable sending the inputs.

Risk: The security review reports partial scan coverage and a suspicious verdict with medium confidence.

Mitigation: Review the skill and dependency sources and verify required access and package sources before installation; the scanner findings are concerns and gaps, not proof of malicious intent.

## Reference(s):

- [Provider, authentication, and data-flow guide](references/provider-cli.md)
- [Seedream model parameters](references/model-flags.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/item-detail)

## Skill Output:

**Output Type(s):** [Image files, Prompt text, Shell commands]

**Output Format:** [Generated raster images (format depends on the selected provider) with Markdown guidance and command examples]

**Output Parameters:** [2D images; aspect ratio and resolution are configurable]

**Other Properties Related to Output:** [Review generated Chinese text and product claims before listing; combine separate modules into a full page when needed.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
