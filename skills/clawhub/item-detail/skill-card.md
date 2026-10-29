## Description:

生成带中文排版的商品详情页图像模块，使用商品图与卖点制作可用于商品展示的图文内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers provide a product image and concise selling points to create Chinese-language product-detail banners, feature callouts, material or detail panels, and specification graphics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud provider for generation.

Mitigation: Select the provider explicitly and submit only images and prompts approved for that provider.

Risk: Documented per-image credit estimates conflict with the bundled estimator.

Mitigation: Check current provider pricing before generating and use --dry-run to review the request first.

Risk: An unpinned CLI version may change behavior between runs.

Mitigation: Prefer a pinned CLI version for repeatable use.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-detail)

## Skill Output:

**Output Type(s):** [Image files, Chinese text embedded in images]

**Output Format:** [Product-detail image modules (for example, banners, feature callouts, material and detail panels, and specification graphics)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation uses a selected cloud provider; image and prompt data are sent to that provider.]

## Skill Version(s):

1.0.25 (source: server-resolved release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
