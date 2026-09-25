## Description:

面向初高中学生的遗传题辅导技能，通过判断性状与基因组成、绘制遗传图解和核对分母，引导学生逐步计算概率并分析系谱图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初高中学生用它练习教材范围内的遗传推理与概率计算，通过分步提示理解遗传图解、分离与自由组合定律及系谱图。

### Deployment Geography for Use:

Chinese Mainland (Simplified Chinese K12 curriculum); other regions require localized curriculum, crisis referrals, and minors' data controls

## Known Risks and Mitigations:

Risk: Learning profiles, reminders, or sharing could expose minors' information without appropriate consent.

Mitigation: Keep profile memory off by default; verify consent, deletion, export, parent-sharing, and cross-skill-sharing controls before enabling these features.

Risk: Chinese Mainland curriculum and crisis guidance may not fit students in other regions.

Mitigation: Review regional suitability and localize curriculum, emergency contacts, and minors' consent requirements before deployment elsewhere.

Risk: Textbook genetics examples could be mistaken for personal medical risk advice.

Mitigation: Do not assess a student's or relative's disease risk; refer personal medical questions to a physician.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-genetics-coach)
- [Genetics reasoning reference](artifact/references/genetics-reasoning.md)
- [Platform and regional conventions](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Simplified Chinese text and Markdown with stepwise hints and genetics diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Current-problem guidance by default; optional profile, error-log, and reminder actions require separate consent.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
