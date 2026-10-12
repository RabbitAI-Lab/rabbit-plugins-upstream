## Description:

将服装平铺图与模特姿势参考图合成为电商试穿图，并尽量保留服装的颜色、纹理和版型。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商商家和内容制作人员可用服装照片及姿势参考图制作模特上身展示图，也可组合上装与下装生成整套造型。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, reference, and optional model-face images may be sent to a cloud image provider.

Mitigation: Use --dry-run first; choose the provider deliberately and share only images you are comfortable uploading.

Risk: Identifiable faces in commercial imagery may be used without appropriate rights or consent.

Mitigation: Use identifiable people and model faces only when you have the right and consent to do so.

Risk: Generated images can alter garment details or introduce visible defects.

Mitigation: Check colors, fabric texture, logos, fit, and anatomy before publishing; regenerate unsuitable results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider CLI and data handling](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inspect generated images for garment fidelity and visual defects before publication.]

## Skill Version(s):

1.0.20 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
