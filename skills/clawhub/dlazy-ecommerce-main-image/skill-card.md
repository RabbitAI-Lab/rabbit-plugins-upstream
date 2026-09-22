## Description:

电商爆款主图生成与编辑：上传已批准的商品图，生成搜索列表里能被认出、商品事实准确、卖点有画面证据、符合渠道规则的主图候选，并按单变量原则产出 A/B 测试组。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and marketplace creative teams use this skill to produce product main-image candidates from approved product photos for white-background baselines, visual-difference images, scene images, color SKU sets, and single-variable A/B tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected product images and prompts to dLazy hosted services.

Mitigation: Use only product photos that are approved for upload and review third-party service terms before production use.

Risk: API keys are required for dLazy CLI use.

Mitigation: Keep keys scoped and revocable, prefer CLI login or managed configuration, and rotate or revoke keys when access changes.

Risk: Generated ecommerce images may alter product facts or make unsupported visual claims.

Mitigation: Review outputs against the approved SKU, platform rules, and the skill's publication checklist before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides dLazy banana-pro invocations that return hosted image output URLs; encourages dry-run cost checks and review of generated images before publication.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
