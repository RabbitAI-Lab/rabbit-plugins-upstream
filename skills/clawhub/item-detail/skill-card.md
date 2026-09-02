## Description:

生成带中文排版的商品详情页模块，将商品图和卖点转化为可用于上架的详情页图文内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and content creators use this skill to turn product images and short selling points into Chinese product-detail modules such as banners, icon rows, material blocks, detail close-ups, and parameter blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send product images, prompts, and referenced image URLs to dlazy or another configured image provider.

Mitigation: Use trusted product images, avoid private-network or sensitive URLs, and confirm that the selected provider is appropriate for the data being processed.

Risk: Generated detail-page text or imagery can introduce unsupported claims, incorrect Chinese text, or product changes.

Mitigation: Keep claims grounded in supplied product information, use short exact text in prompts, and manually review generated modules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with bash commands and generated image file paths or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated image files and can emit JSON status when the helper is run with JSON output enabled.]

## Skill Version(s):

1.0.4 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
