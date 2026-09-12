## Description:

主图 A/B 组与转化复盘：商品图和卖点输入后，产出多组单变量对照主图、每组差异假设和可填写的复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and marketing teams use this skill to plan controlled main-image A/B tests, generate comparable image variants, check listing compliance, and prepare a post-test review table. It is suited to workflows where the user supplies product imagery, chooses one variable to test, and later fills in platform performance data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Ark or custom provider configuration can send API keys and product or model imagery to an arbitrary configured endpoint.

Mitigation: Review the skill before installing, do not set ARK_BASE_URL unless the endpoint is fully trusted, and avoid sending confidential imagery to unapproved providers.

Risk: The selected generation provider and destination may differ from user expectations.

Mitigation: Run --dry-run to confirm the selected provider, request destination, and cost before executing generation.

Risk: External CLI use can introduce supply-chain risk.

Mitigation: Prefer pinned or audited installs for any external CLI.

## Reference(s):

- [Platform Image Specifications](artifact/references/platform-specs.md)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [Platform Compliance Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand Kit Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, generated image file paths, optional JSON command output, and a Markdown review table template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image batches are saved to local paths when the generation command is run; users provide performance metrics after the test.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
