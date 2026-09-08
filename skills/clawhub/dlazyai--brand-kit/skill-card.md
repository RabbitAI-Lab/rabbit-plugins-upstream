## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。当用户说「统一风格」「同一个模特」「店铺调性」「品牌规范」「几百个 SKU 看起来像一家店」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, brand operators, and developers use this skill to create and apply a reusable brand.yaml that keeps model appearance, lighting, composition, spacing, and copy tone consistent across product image generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, and model reference images may be sent to the configured image provider.

Mitigation: Use only approved providers, avoid sensitive inputs, and apply least-privilege provider keys with spending limits.

Risk: Unsafe image URLs or custom endpoints could expose private data or API keys.

Mitigation: Do not pass internal or private URLs as image references, and avoid ARK_BASE_URL unless the endpoint is trusted and controlled.

Risk: Suggested npm or GitHub installs may run third-party code.

Mitigation: Review package sources and install commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/brand-kit)
- [brand.yaml field reference](references/brand-schema.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with YAML configuration examples, shell commands, and optional JSON from CLI helpers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can append brand constraints to image-generation prompts and may add a model reference image when configured.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
