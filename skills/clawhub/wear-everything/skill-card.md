## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商与商品内容团队可用此技能将鞋、包及其他配饰的商品图与模特参考图合成为真人穿戴展示图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports external image-provider connections and privacy concerns, so submitted images and prompts may be sent to an external provider.

Mitigation: Before use, consider whether the images and prompts are appropriate to share with the selected provider and whether its access scope is clear.

Risk: ClawScan analysis was partial: only 5 of 9 components were fully inspected, and some script checks were degraded.

Mitigation: Review the source and referenced materials and clarify the skill's access scope before installation; the available scan does not establish that uninspected behavior is safe.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images, Prompt text, Shell commands]

**Output Format:** [JPEG image files, with prompts and command examples in Markdown]

**Output Parameters:** [2D images]

**Other Properties Related to Output:** [Image size, quality, and batch count are configurable; recommended inputs are a product image and a model or scene reference.]

## Skill Version(s):

1.0.30 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
