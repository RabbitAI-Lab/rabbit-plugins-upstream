## Description:

为短剧人物、造型、地点、道具和状态编写或修改可直接复制的图片提示词 Markdown；本技能产出提示词文档，不生成图片或调用供应商。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者和视觉开发团队可用此技能，根据已接受的项目视觉设定编写、修订并整理可复用的人物、造型、场景、道具及局部编辑图片提示词。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect or conflicting visual facts in a prompt can carry into production references.

Mitigation: Base prompts on accepted project settings, state each reference image's scope, and have the creator review the prompt before use.

Risk: A prompt document does not generate or verify the resulting image.

Mitigation: Handle image generation as a separate production step and confirm the exact task with the creator.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/short-drama-image-prompts)
- [通用资产图片提示词配方](references/common-recipe.md)
- [人物设定图与造型变体](references/character-and-look.md)
- [地点板配方](references/location-plate.md)
- [道具板配方](references/prop-plate.md)
- [定点修改与修订](references/edit-and-revision.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown project document with reusable, copy-ready image prompt blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creator-facing labels follow the project language; prompt prose follows the project's prompt-language setting and defaults to English when unspecified.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
