## Description:

电商爆款主图生成与编辑：基于已批准的商品图生成白底基线图、可视差异图、内容电商场景图、配色 SKU 组和单变量 A/B 测试主图候选，并强调商品事实、渠道规则和可归因测试。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, designers, and developers use this skill to generate and iterate product main-image candidates for marketplace and social-commerce channels. It focuses on preserving product facts, using approved product photos, and creating single-variable image variants that can be tested with real commerce metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads approved product images and prompts to dLazy hosted services for generation.

Mitigation: Use only catalog assets approved for upload, avoid sensitive unreleased product material unless permitted, and prefer isolated execution for sensitive catalog work.

Risk: The dLazy CLI requires an API key for authenticated requests.

Mitigation: Use a revocable, minimally scoped API key where possible and rotate or revoke it from the dLazy dashboard when access is no longer needed.

Risk: Generated ecommerce images can misrepresent product facts, claims, pricing, platform logos, or bundled accessories if prompts are underspecified.

Mitigation: Review outputs against approved product photos, category restrictions, platform rules, and the skill's SKU checklist before publishing.

Risk: The skill depends on a third-party pinned npm CLI package.

Mitigation: Install only if comfortable running the pinned dLazy CLI, review npm and source provenance as part of release controls, and run in an isolated environment when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with bash command examples and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the pinned dLazy CLI and may return hosted generated-image URLs from files.dlazy.com.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
