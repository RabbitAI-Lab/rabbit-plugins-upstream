## Description:

主图 A/B 组与转化复盘。商品图 + 卖点 → 多组对照主图 + 每组的差异假设 + 复盘模板。当用户说「A/B 测试」「主图优化」「提点击率」「哪版更好」「换个版本试试」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and agents use this skill to plan controlled main-image A/B tests, generate image variants that change one variable at a time, check listing-image compliance, and prepare a post-test review table for manually supplied performance data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and provider credentials may pass through a configured cloud provider path.

Mitigation: Use non-sensitive assets where possible, keep API keys low-privilege and revocable, and install only when the configured provider path is acceptable.

Risk: A custom ARK_BASE_URL could route requests to an untrusted endpoint.

Mitigation: Set ARK_BASE_URL only to trusted, controlled endpoints and review provider configuration before running generation.

Risk: Returned output URLs are downloaded without strong validation.

Mitigation: Run generation in a contained environment and manually review downloaded outputs before using them in production listings.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [Platform Image Specifications](references/platform-specs.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/listing-optimizer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands, prompts, compliance-check commands, and review tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated image files through a configured provider path; platform performance metrics must be supplied by the user.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
