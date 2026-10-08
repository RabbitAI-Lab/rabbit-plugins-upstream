## Description:

引导初高中学生读懂生物曲线、示意图、系谱图、数据表和材料题，先找图表依据，再联系教材概念作答。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking middle and high school students use this skill to interpret biology charts and source-based questions with stepwise hints rather than immediate answers. High school elective material is intended for students taking biology as an elective exam subject.

### Deployment Geography for Use:

Mainland China; review and localize curriculum, crisis contacts, consent practices, and language before use elsewhere.

## Known Risks and Mitigations:

Risk: Mainland-China curriculum and crisis contacts may be inappropriate in other regions.

Mitigation: Review and localize curriculum, emergency contacts, consent rules, and language before deploying elsewhere.

Risk: Optional memory, sharing, and reminders can expose student learning information without clear consent.

Mitigation: Keep these features off by default and require separate, explicit student consent for each action.

Risk: Poorly legible figures or personal medical test results could lead to misleading guidance.

Mitigation: Ask for a description when charts cannot be read; do not interpret personal test results and direct students to a parent or doctor.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-chart-reader)
- [Biology chart-reading guide](references/biology-chart-guide.md)
- [Required high school biology charts](references/biology-hs-charts-required.md)
- [Elective high school biology charts](references/biology-hs-charts-elective.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise chart interpretation and hints grounded in the supplied question; optional text export of a student learning profile with consent.]

## Skill Version(s):

2.11.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
