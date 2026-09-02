## Description:

主图 A/B 组与转化复盘。商品图 + 卖点 -> 多组对照主图 + 每组的差异假设 + 复盘模板。当用户说「A/B 测试」「主图优化」「提点击率」「哪版更好」「换个版本试试」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, catalog operators, and ecommerce agents use this skill to plan controlled main-image A/B tests, generate comparison image groups, check listing compliance, and prepare a post-test review table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to the configured image-generation provider.

Mitigation: Use local files or trusted public image URLs, configure only approved providers, and review credential setup before processing real catalog assets.

Risk: Sample brand demographic defaults may not match a real catalog or target market.

Mitigation: Replace the bundled brand sample values before applying the workflow across production listings.

Risk: A/B conclusions can be misleading when traffic is too low, variables are not isolated, or platform performance data is missing.

Mitigation: Change one variable at a time, document the hypothesis before launch, collect sufficient impressions, and have the user fill in platform metrics before drawing conclusions.

## Reference(s):

- [ClawHub Listing Optimizer Skill Page](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [Platform Image Specifications](artifact/references/platform-specs.md)
- [Platform Compliance Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand Kit Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and tabular review templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image-generation requests and saved image files through configured providers; review templates require users to supply platform performance data.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
