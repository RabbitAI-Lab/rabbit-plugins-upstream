## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, designers, and agents use this skill to turn a product image and short selling points into Chinese product-detail page modules such as banners, icon rows, material blocks, detail blocks, and parameter blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand settings may be sent to external image-generation providers.

Mitigation: Use only providers approved for the workflow, and avoid confidential unreleased product photos or private URLs unless the provider is approved.

Risk: Generated detail-page copy or imagery may imply product functions, certifications, promotions, or comparisons that were not supplied.

Mitigation: Constrain prompts to verified selling points and review outputs for unsupported claims before publication.

Risk: Chinese text in generated images can be malformed, crowded, or misplaced.

Mitigation: Keep copy short, generate modules separately, require clear Chinese text in prompts, and proofread every generated image before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell command examples and generated image files saved to local paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product images, prompt text, optional brand settings, and image-generation provider credentials; image outputs are expected to be reviewed before publication.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
