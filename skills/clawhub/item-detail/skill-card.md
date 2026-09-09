## Description:

生成带中文排版的商品详情页模块，将商品图和卖点文案转成可上架的详情页图文模块。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agent users use this skill to turn a product image, product category, and short selling points into Chinese product-detail image modules for listing pages. It focuses on modular generation, Chinese text legibility, product fidelity, and claim review before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the configured cloud image provider.

Mitigation: Use dry-run or doctor output to confirm the selected provider, and only submit product assets approved for that provider.

Risk: Helper scripts can fetch image URLs, including untrusted or private-network URLs.

Mitigation: Prefer local image files or trusted HTTPS image hosts; avoid untrusted image URLs.

Risk: An ARK endpoint override can redirect requests and expose credentials if misconfigured.

Mitigation: Keep ARK_BASE_URL unset or confirm it points to the official provider before using ARK.

Risk: Generated Chinese text or product claims can be incorrect or misleading.

Mitigation: Review output image text against the provided copy and verify claims before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [provider-cli.md](references/provider-cli.md)
- [model-flags.md](references/model-flags.md)
- [dLazy provider documentation](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates per-module ecommerce detail images, commonly JPG outputs at 3:4, 1:1, or 9:16 with 2K resolution; batch generation is recommended for Chinese text review.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
