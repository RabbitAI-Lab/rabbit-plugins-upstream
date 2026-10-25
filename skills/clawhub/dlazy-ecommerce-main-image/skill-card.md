## Description:

电商爆款主图生成与编辑。上传已批准的商品图，生成搜索列表里能被认出、商品事实准确、卖点有画面证据、符合渠道规则的主图候选，并按单变量原则产出 A/B 测试组。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and creative operators use this skill to prepare accurate product-image candidates for listing pages and single-variable A/B tests. It guides white-background, product-state, lifestyle, color-variant, and background-test workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference images are sent to dLazy services for image generation.

Mitigation: Submit only approved product images and prompts you are comfortable sending to dLazy; avoid including sensitive material.

Risk: The skill saves an organization API key in local CLI configuration, and generated imagery may not accurately represent a product or meet a channel's rules.

Mitigation: Protect the saved key and rotate or revoke it if exposed; verify product accuracy and platform requirements before publishing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source code (referenced by the skill)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions, CLI commands, and generated image outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image-generation commands use approved product references and can specify prompts, aspect ratio, output size, dry-run estimates, and asynchronous completion.]

## Skill Version(s):

1.0.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
