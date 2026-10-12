## Description:

审查中文短剧的原著分析、剧本、资产连续性、分镜、提示词和已有媒体，提供有证据的结论与修订要求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

中文短剧的创作者和审稿人使用本技能检查项目文件中的故事、剧本、资产与镜头连续性，并获得定位清晰的审查结论和修订要求；技能本身不替创作者改写来源文件。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 审查可能接触项目私有内容或凭据。

Mitigation: 仅读取用户指定的文件，审查记录仅保留修订所需的最少证据，避免复制完整私有输入。

Risk: 在缺少可读取媒体或关键输入时可能作出无法验证的制作判断。

Mitigation: 明确证据限制，对依赖缺失输入的判断暂缓，不从文字推断媒体中的实际表现。

## Reference(s):

- [ClawHub release](https://clawhub.ai/worldwonderer/skills/short-drama-review)
- [审查方法](artifact/references/review-method.md)
- [原著分析审查表](artifact/references/rubric-source-analysis.md)
- [故事剧本审查表](artifact/references/rubric-story-script.md)
- [资产提示词审查表](artifact/references/rubric-assets-prompts.md)
- [视觉运动审查表](artifact/references/rubric-visual-motion.md)
- [生产质量门](artifact/references/production-quality-gates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [中文审查结论与问题清单；需要落盘时为 Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [标明审查范围、问题位置、证据、影响、严重程度及修订要求；不生成媒体或修改来源文件。]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
