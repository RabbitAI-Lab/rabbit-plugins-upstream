## Description:

电商爆款主图生成与编辑：上传已批准的商品图，生成可识别、商品事实准确、卖点有画面证据、符合渠道规则的主图候选，并按单变量原则产出 A/B 测试组。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketplace sellers, and agents assisting them use this skill to create product main-image candidates for white-background baselines, visual-difference images, content-commerce scenes, color SKU sets, and single-variable A/B image tests. The workflow emphasizes approved product photos, accurate SKU representation, platform-rule checks, and measurable image variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are uploaded to dLazy hosted services for generation.

Mitigation: Use approved product photos, avoid confidential images unless policy allows cloud processing, and confirm users understand the hosted-service upload path.

Risk: A dLazy API key may be stored locally or supplied through the environment.

Mitigation: Use organization-scoped credentials, limit access to the local config, and rotate or revoke the key when access is no longer needed.

Risk: Generated marketplace images can alter SKU facts or imply unsupported claims if outputs are not reviewed.

Mitigation: Review every generated image against the approved product photos, platform rules, and the skill's checklist before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the dLazy CLI with approved product images; generated image results are returned as hosted URLs by the dLazy service.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
