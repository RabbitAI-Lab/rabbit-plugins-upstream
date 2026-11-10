## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。当用户说「统一风格」「同一个模特」「店铺调性」「品牌规范」「几百个 SKU 看起来像一家店」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营者和制作商品素材的创作者，用一份可复用的品牌配置统一商品图的模特、色调、构图和版式约束，并将这些约束用于图像生成工作流。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags provider authentication and external image generation as capabilities beyond the stated brand-configuration purpose, and notes that parts of the artifact were only partially inspected.

Mitigation: Review the skill and its scan coverage before installation, and use it only if its provider and image-generation capabilities fit your needs.

Risk: The security guidance notes an unpinned `npx skills` reference.

Mitigation: Verify the referenced source and pin a specific version before running that install command.

## Reference(s):

- [Brand configuration schema](references/brand-schema.md)
- [Provider CLI and data-flow guide](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Brand Kit release page](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [Configuration, Text, Shell commands, Image files]

**Output Format:** [YAML brand configuration, prompt text, shell commands, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Brand settings and optional reference images guide image generation; generated files are saved to user-selected paths.]

## Skill Version(s):

1.0.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
