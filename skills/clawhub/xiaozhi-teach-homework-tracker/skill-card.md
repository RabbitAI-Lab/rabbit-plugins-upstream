## Description:

帮独立教师跟进课上练习与学员带来的学校作业、考试错题：登记、追状态、归错因、导出下节课讲什么。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to record in-class practice and schoolwork brought by learners, track completion, classify errors, and prepare a next-lesson diagnostic. It keeps teachers in control of records and decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Student records could expose personal information if saved or shared without appropriate safeguards.

Mitigation: Use student aliases, obtain appropriate consent, and confirm that the platform enforces the stated privacy and deletion controls.

Risk: A preliminary weakness signal could be mistaken for a confirmed learning need.

Mitigation: Keep threshold evidence provisional and add a weakness to the learner record only after teacher confirmation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [Skill workflow and boundaries](artifact/SKILL.md)
- [Tracking vocabulary and consent controls](artifact/shared/vocab.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Off-campus training boundaries](artifact/shared/off-campus-training.md)
- [Workspace data schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Configuration]

**Output Format:** [Chinese text and Markdown summaries, plus structured workspace records conforming to a JSON schema]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-confirmed records and recommendations; does not grade work, create exercises, or send messages to learners or parents.]

## Skill Version(s):

2.12.0 (source: server release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
