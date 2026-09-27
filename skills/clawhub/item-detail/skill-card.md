## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, designers, and agent operators use this skill to turn a product image and short selling points into Chinese item-detail page modules with readable typography, layout guidance, and generation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and ecommerce copy may be sent to the selected cloud image-generation provider.

Mitigation: Use the documented dry-run mode for visibility first, select the intended provider deliberately, and avoid sending sensitive or unapproved product material.

Risk: Generated detail-page copy or imagery may introduce unsupported claims, false promotions, or product changes.

Mitigation: Keep selling points grounded in verified product information, use the skill's prompt constraints against unsupported claims, and review each generated image before publishing.

Risk: API keys are required for cloud providers and could expose generation access if mishandled.

Mitigation: Use scoped, revocable keys, store them through the documented provider authentication flow or environment variables, and rotate them when access changes.

Risk: Generated images are written to local paths selected by the operator.

Mitigation: Use explicit save paths, review dry-run output before execution, and avoid overwriting important files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro parameter reference](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and local image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews, provider selection, reference images, batch generation, and local save paths.]

## Skill Version(s):

1.0.13 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
