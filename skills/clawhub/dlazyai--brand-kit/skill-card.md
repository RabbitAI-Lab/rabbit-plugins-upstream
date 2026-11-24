## Description:

用一份 brand.yaml 统一模特、色温、构图、留白与文案语气，帮助商品图跨 SKU 保持一致的店铺视觉。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商卖家和视觉团队用它维护一份可复用的品牌视觉规范，并将模特、摄影、版式和禁用项应用到不同商品图任务中。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to an external image provider, and image-generation runs may incur API charges.

Mitigation: Choose a provider you trust, avoid sending sensitive images or prompt content, and check provider pricing or credits before batch generation.

Risk: ClawScan reports a suspicious verdict because reported authentication and image-generation capabilities exceed the stated configuration purpose; code analysis was incomplete.

Mitigation: Review the skill and its permissions before installing; the scan verdict is not a finding that the publisher acted maliciously.

## Reference(s):

- [Brand configuration fields and task mapping](references/brand-schema.md)
- [Provider setup, data flow, and generated outputs](references/provider-cli.md)
- [dLazy CLI source code](https://github.com/dlazy-ai/cli)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [Configuration, Prompt text, Shell commands, Image files]

**Output Format:** [YAML brand configuration, prompt text, and optional generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Brand settings are applied selectively by image task; image generation uses the selected provider.]

## Skill Version(s):

1.0.33 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
