## Description:

服装平铺图一键上身试穿：根据服装图和姿势参考图生成模特上身商拍图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

服装商家和电商内容创作者可用此技能将平铺服装图与姿势或场景参考图合成为模特上身商品图，并获得生成提示和调用指导。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and identifiable face photos may be sent to an external image-generation service; the security scan rated the skill suspicious and reported incomplete scan coverage.

Mitigation: Before upload, explain that images may be sent to an external service, obtain consent for identifiable faces, and review the service's data-handling terms.

## Reference(s):

- [Provider and data flow guide](references/provider-cli.md)
- [Image generation options](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Generated images, Text, Shell commands, Guidance]

**Output Format:** [Image files (typically JPEG) with Markdown guidance, image prompts, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image dimensions, format, and quality can be selected; the documented default commercial image is a vertical catalog photo.]

## Skill Version(s):

1.0.32 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
