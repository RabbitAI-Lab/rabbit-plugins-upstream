## Description:

帮助初高中学生按六类生物错因分析错题根因，识别具体弱项并生成有针对性的学习建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初高中学生用它分析生物错题的概念、结构与功能、图表、实验、表述和计算弱项；经学生授权后，可形成弱项报告并提出练习建议。

### Deployment Geography for Use:

Chinese-language, China-aligned K12 use; other regions require localized curriculum, minor-consent practices, and crisis resources.

## Known Risks and Mitigations:

Risk: Long-term learning records or parent-facing summaries may disclose a minor's learning information without appropriate consent.

Mitigation: Review profile, cross-skill sharing, parent-summary, and reminder consent settings; use the skill's pause, correction, deletion, and sharing controls.

Risk: China-aligned crisis resources, curriculum assumptions, and minor-consent rules may not fit other regions.

Mitigation: Localize those resources and rules before deployment outside the intended context.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [生物错因维度表](references/biology-error-dimension-table.md)
- [Learning profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language analysis, weakness reports, and practice suggestions in conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term profile updates, sharing, and reminders require appropriate student consent; sparse evidence is flagged.]

## Skill Version(s):

2.6.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
