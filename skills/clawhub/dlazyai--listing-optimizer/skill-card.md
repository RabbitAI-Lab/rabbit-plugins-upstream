## Description:

根据商品图和卖点设计主图 A/B 对照方案，生成多组图像及差异假设，并提供转化复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营者和商品内容团队可用它设计主图对照实验：每轮只改变一个变量，先记录效果假设，再生成对照图并用模板复盘投放数据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes a gap between the stated A/B purpose and additional compliance-checking and repair behavior; it also flags external API calls, broad activation phrases, and incomplete analysis of some files.

Mitigation: Before use, confirm the behavior and trigger phrases fit the intended workflow, check that product images may be sent to the selected image service, and review compliance-checking or repair results.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Platform compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Shell commands, Guidance]

**Output Format:** [Generated image files plus a Markdown experiment and review template, with shell commands for generation and listing checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user supplies platform performance data; the skill does not connect to seller dashboards or assess statistical significance.]

## Skill Version(s):

1.0.26 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
