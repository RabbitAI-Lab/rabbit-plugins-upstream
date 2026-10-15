## Description:

帮助中文中小学生归档具体错题、分析错误原因、追踪重复弱项并生成复习建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in a Chinese-language K-12 learning setting use this skill to review specific incorrect answers, identify recurring error patterns, and request practice sets or term reports. Guardians or teachers should supervise primary-school use.

### Deployment Geography for Use:

Global (Chinese-language K-12 learning context)

## Known Risks and Mitigations:

Risk: Long-term wrong-answer records, reminders, and cross-skill or parent-visible summaries can expose student learning information.

Mitigation: Confirm student or guardian consent before enabling retention, sharing, reminders, or parent-visible summaries; honor pause, delete, export, and sharing controls.

Risk: Broad matching may treat a general request as a specific incorrect-answer case.

Mitigation: Ask for a concrete incorrect question before recording or analyzing an error, and confirm uncertain details with the student.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](references/error-analysis-framework.md)
- [Shared terminology and counting rules](shared/vocab.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Chinese-language conversational text, Markdown study reports, and structured record handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Record updates and cross-skill sharing are subject to student or guardian consent.]

## Skill Version(s):

2.11.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
