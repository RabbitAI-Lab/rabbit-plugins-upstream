## Description:

主图 A/B 组与转化复盘。商品图 + 卖点 → 多组对照主图 + 每组的差异假设 + 复盘模板。当用户说「A/B 测试」「主图优化」「提点击率」「哪版更好」「换个版本试试」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and listing teams use this skill to plan controlled main-image A/B variants, generate image groups, check platform compliance, and produce a post-campaign review template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing prompts and selected product images may be sent to the configured generation provider.

Mitigation: Use --dry-run or --doctor to confirm the provider, and avoid passing confidential files as images or prompt inputs.

Risk: Running recovery or provider commands from untrusted sources can execute code outside the skill's normal flow.

Mitigation: Use bundled scripts or trusted, pinned CLI commands; do not run npx recovery commands unless the source is trusted.

Risk: The skill does not connect to marketplace analytics or determine statistical significance.

Mitigation: Have the user supply campaign metrics after the test and avoid drawing conclusions from small samples or multi-variable prompt changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [platform-compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [brand-kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with bash commands, generated image files, and optional JSON status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks the agent to keep A/B variants single-variable, run platform checks, and provide a review table whose performance metrics are filled by the user.]

## Skill Version(s):

1.0.3 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
