## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。当用户说「统一风格」「同一个模特」「店铺调性」「品牌规范」「几百个 SKU 看起来像一家店」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和图像生成工作流维护者可用一份可复用的品牌规范统一不同 SKU 的模特、色调、构图与文案风格，并将其应用到支持的生图任务。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud image generation may upload product or face images to a provider and incur charges.

Mitigation: Choose the provider explicitly, review charges with --dry-run, and upload only images you are authorized to share.

Risk: Bulk generation or exposed credentials can lead to unintended usage or charges.

Mitigation: Use a reviewed CLI version, protect stored keys, and confirm the sample style and batch size before bulk work.

## Reference(s):

- [Brand configuration schema](artifact/references/brand-schema.md)
- [Provider CLI guidance](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Configuration, Guidance, Prompt text, Shell commands]

**Output Format:** [YAML brand configuration, prompt text, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reusable brand settings are selected by task type and appended to generation prompts.]

## Skill Version(s):

1.0.23 (source: SKILL.md frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
