## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and content teams use this skill to turn a product image and short selling points into Chinese product-detail modules such as banners, icon rows, material blocks, detail closeups, and parameter blocks. It helps agents draft provider commands and prompts for cloud image generation while preserving product appearance and requiring manual review of rendered Chinese text and claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and product images may be sent to the selected cloud image-generation provider.

Mitigation: Use local product images or trusted public URLs, avoid private or unreleased assets, and confirm the selected provider credentials before running generation.

Risk: Generated Chinese text or product claims may be malformed, unsupported, or unsuitable for publication.

Mitigation: Keep prompt copy short and source-backed, generate detail pages in modules, then manually review the Chinese text, product fidelity, and claims before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI Reference](references/provider-cli.md)
- [seedream-5.0-pro Model Flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output; generated assets are saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces prompts and commands for image-generation providers and commonly saves JPG outputs for product-detail modules.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
