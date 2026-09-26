## Description:

帮助独立教师分类保存、检索和改编讲义、题目、讲评话术及脱敏错因案例，并记录版权状态和复用效果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中国大陆的独立教师用它整理、检索并改编教学资源，按知识点与难度匹配材料，同时记录使用效果；学生使用前由教师审核。

### Deployment Geography for Use:

中国大陆；其他地区须先本地化课程、未成年人隐私要求和求助渠道。

## Known Risks and Mitigations:

Risk: Broad trigger wording or the listed homework-tracker dependency may cause unexpected routing or setup assumptions.

Mitigation: Review triggers and dependency behavior before deployment; keep resource-library actions teacher-initiated.

Risk: Student cases may expose identifying information when stored or shared.

Mitigation: Anonymize cases, confirm sharing consent, and retain teacher controls for confirmation, deletion, pause, and export.

Risk: Unlicensed teaching materials or unverified AI-generated questions may be reused improperly.

Mitigation: Record copyright status, store textbook and past-exam questions as citations only, and require teacher verification before using AI-generated questions with students.

Risk: Mainland China-specific curricula and safety guidance may not fit other regions.

Mitigation: Localize curricula, minor-data rules, and emergency referral information before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource categorization and retrieval](references/resource-categorization.md)
- [Resource entry examples](references/resource-entry-examples.md)
- [Copyright annotation template](references/copyright-annotation-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language resource matches, adaptation guidance, and structured library records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing only; AI-generated questions require teacher verification before student use.]

## Skill Version(s):

2.6.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
