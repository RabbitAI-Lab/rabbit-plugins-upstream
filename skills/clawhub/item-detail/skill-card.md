## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and content operators use this skill to turn product photos and concise selling points into Chinese-language product detail image modules, including banners, icon rows, material blocks, detail blocks, and parameter blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and listing details may be sent to dLazy or another configured image provider.

Mitigation: Use trusted image paths or URLs, choose only acceptable providers, and keep API keys scoped and revocable.

Risk: Generated Chinese text and product claims can be incorrect, unreadable, or non-compliant for a listing.

Mitigation: Review generated copy and images before publication, verify claimed product attributes, and avoid unsupported certifications, promotions, or comparison data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash code blocks and local image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are saved to local paths selected by the user.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
