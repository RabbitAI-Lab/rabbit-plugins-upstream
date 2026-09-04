## Description:

电商爆款主图生成与编辑：上传已批准的商品图，生成搜索列表里能被认出、商品事实准确、卖点有画面证据、符合渠道规则的主图候选，并按单变量原则产出 A/B 测试组。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and commerce creatives use this skill to generate and iterate main-image candidates for e-commerce listings from approved product photos. It supports white-background baselines, visual-difference images, content-commerce scenes, color SKU groups, and single-variable A/B test candidates while preserving product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to dLazy's hosted API and media storage.

Mitigation: Use only approved product images, avoid confidential assets unless permitted, and confirm the workflow is acceptable for the store or client before generation.

Risk: Generated main images can misrepresent product structure, quantities, colors, logos, or unsupported product claims.

Mitigation: Review each candidate against the source SKU, approved assets, and platform rules before publishing; keep A/B tests to one changed variable at a time.

Risk: Global installation of the third-party dLazy CLI increases local footprint.

Mitigation: Use the pinned npx invocation or dry-run testing when a smaller local footprint or preflight check is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dlazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks and CLI invocation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are designed for dLazy banana-pro and may upload selected product images and prompts to dLazy hosted endpoints.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
