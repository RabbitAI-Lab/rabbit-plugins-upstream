## Description:

主图 A/B 组与转化复盘。商品图 + 卖点 → 多组对照主图 + 每组的差异假设 + 复盘模板。当用户说「A/B 测试」「主图优化」「提点击率」「哪版更好」「换个版本试试」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agents use this skill to plan controlled main-image A/B tests, generate matched product-image variants, check listing-image compliance, and prepare a Markdown recap table for post-campaign metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private product images, prompts, or provider credentials may be exposed if generation backends or custom provider base URLs are configured unsafely.

Mitigation: Review before use with private assets or valuable provider keys; use approved providers, avoid arbitrary image URLs, do not set untrusted custom provider base URLs, and rotate any Ark key used with an untrusted ARK_BASE_URL.

Risk: A/B results can be misleading if the agent changes more than one variable, uses rejected listing images, or draws conclusions from too little traffic.

Mitigation: Keep one variable per experiment, run listing compliance checks before traffic is sent, and require the user to fill real exposure, click, and conversion data before forming conclusions.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [platform-compliance supporting skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [brand-kit supporting skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, image files, guidance]

**Output Format:** [Markdown guidance with bash command blocks, generated image files, compliance-check text or JSON, and a Markdown experiment recap template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may use local or cloud provider backends; compliance checks cover measurable image properties and leave text, watermark, and collage review to a visual model or human review.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
