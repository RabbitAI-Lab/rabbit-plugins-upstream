## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。当用户说「统一风格」「同一个模特」「店铺调性」「品牌规范」「几百个 SKU 看起来像一家店」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营者和使用图像生成技能的代理，用一份可复用的 brand.yaml 统一多个 SKU 的模特、色调、构图与文案约束，并将相关约束加入图像生成提示词。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is rated suspicious, and the scan fully inspected only 6 of 10 components, with several analyzers degraded.

Mitigation: Review the broader generation and provider-authentication behavior and inspect the unreviewed components before installation or use.

Risk: Prompts and reference images may be sent to external image providers, and provider usage may incur charges.

Mitigation: Confirm the selected provider and its data handling, review the request with the documented dry-run option, and check expected costs before generating.

Risk: Saving generated files to an existing path can overwrite prior output, and recovery instructions are not pinned.

Mitigation: Choose a fresh output path, preserve originals or backups, and confirm recovery steps before batch generation.

## Reference(s):

- [品牌规范字段说明](references/brand-schema.md)
- [图像生成 CLI 与 provider 使用说明](references/provider-cli.md)
- [ClawHub 发布页](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [Configuration, Guidance, Shell commands, Image files]

**Output Format:** [YAML brand configuration, prompt text, and provider-generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation depends on the selected provider; prompts and reference images may be sent to external providers, and usage charges may apply.]

## Skill Version(s):

1.0.31 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
