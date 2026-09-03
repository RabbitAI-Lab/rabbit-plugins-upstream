## Description:

商品换背景：将白底商品图转换为逼真场景图，并让光影、投影和环境反光匹配新环境。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, creators, and developers use this skill to place product images into photorealistic lifestyle scenes while preserving the product's shape, color, material, and logo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and optional brand or reference images may be sent to dLazy or another configured image provider.

Mitigation: Review the selected provider and API keys before running generation, use trusted image URLs, and use dry-run mode to inspect the request before sending data.

Risk: Generated scenes can misrepresent product capabilities or alter important product details.

Mitigation: Keep prompts constrained to preserve the product's shape, color, material, and logo, avoid misleading scenes, and review outputs for grounded shadows, light direction, edges, and product fidelity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI Repository](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with bash command examples, JSON status envelopes, and saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use dry-run mode to inspect provider, cost, and payload before generation.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
