## Description:

为短剧人物、造型、地点、道具和状态编写或修改可直接复制的图片提示词 Markdown。用户提到角色设定图、三视图、参考图、场景板、道具图、风格帧、Look Development、状态变体或局部编辑提示词时使用；不生成图片，也不调用供应商。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Short-drama writers, artists, and production teams use this skill to turn accepted visual details into reusable, copy-ready prompts for character, costume, location, prop, state-variant, and targeted-edit images. It produces prompt text only; creators supply or separately generate the images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found no confirmed malicious behavior but reported possible memory manipulation; its confidence is medium and its analysis was partial.

Mitigation: Keep the skill scoped to the requested image-prompt task, and review any proposed persistent-memory or unrelated guidance changes before accepting them.

Risk: The skill defines language requirements that may not fit every project.

Mitigation: Check the project's prompt-language setting and confirm the intended language before using the generated prompt text.

Risk: The security review could not resolve one local reference.

Mitigation: Review the referenced source material before relying on guidance from that unresolved reference.

## Reference(s):

- [ClawHub release](https://clawhub.ai/worldwonderer/skills/short-drama-image-prompts)
- [阶段契约](references/stage-contract.md)
- [通用资产图片提示词配方](references/common-recipe.md)
- [人物设定图与造型状态变体](references/character-and-look.md)
- [地点板](references/location-plate.md)
- [道具板](references/prop-plate.md)
- [造型与状态变体](references/look-and-state-variant.md)
- [生产参考板配方](references/production-sheet-recipes.md)
- [Lookdev 风格帧](references/lookdev-frame.md)
- [定点修改与修订](references/edit-and-revision.md)
- [审查与示例](references/review-and-fixtures.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with structured asset entries and copy-ready image-prompt blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Copy-ready prompt text; does not generate images or call image providers.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
