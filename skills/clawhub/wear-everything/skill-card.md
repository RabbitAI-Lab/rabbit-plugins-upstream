## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商卖家、商品摄影团队和开发者可用该技能把鞋、包及其他配饰商品图与模特参考图合成为真人穿戴展示图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Identifiable model photos or confidential product images may be sent to an external image service.

Mitigation: Submit only images you are authorized to use, and avoid confidential material.

Risk: Generated wear images could be mistaken for a real person's endorsement.

Mitigation: Use model images with permission and do not present generated results as real endorsements.

Risk: The security scan is partial and leaves some scripts incompletely inspected.

Mitigation: Review the remaining scripts and security findings before installing or using the skill.

## Reference(s):

- [Provider CLI setup and usage](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Related flat-lay skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG product-on-model images with prompt and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch image generation is supported.]

## Skill Version(s):

1.0.34 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
