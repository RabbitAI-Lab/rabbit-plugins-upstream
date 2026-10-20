## Description:

为短剧人物、造型、地点、道具和状态编写或修改可直接复制的图片提示词 Markdown，不生成图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Short-drama creators use this skill to prepare reusable character, location, prop, visual-style, and scoped-edit image prompts from established visual facts and actual project references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt text defaults to English even when the creator-facing guidance is Chinese.

Mitigation: Check short-drama.json prompt_language if another prompt language is required.

Risk: Prepared prompts may be mistaken for generated images or approved generation requests.

Mitigation: Treat the Markdown as prompts only; confirm any subsequent image-generation task separately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-image-prompts)
- [Prompt recipe](artifact/references/common-recipe.md)
- [Stage contract](artifact/references/stage-contract.md)
- [Scoped edits and revisions](artifact/references/edit-and-revision.md)
- [Review and examples](artifact/references/review-and-fixtures.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown image-prompt entries with reusable prompt text and reference-image boundaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prepares prompts only; image generation requires a separate, explicitly confirmed workflow.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
