## Description:

帮化学老师组织实验教学，包括演示与分组取舍、分组与器材安排、课堂安全组织、实验报告与实验操作考试组织，覆盖初中 8 个学生必做实验与高中必修起点的必做实验。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 chemistry teachers use this skill to plan safer lab lessons, decide whether an experiment should be demonstrated or done in groups, organize equipment and student roles, and prepare lab-report or operation-exam guidance. The skill produces teacher-reviewed drafts rather than replacing teacher judgment or school laboratory rules.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, emergency contacts, and minor-data requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill is designed for a Chinese K12 chemistry-teaching context and may not fit other curricula, emergency contact norms, or minor-data rules.

Mitigation: Localize curriculum assumptions, grade bands, crisis contacts, and privacy requirements before deploying outside that context.

Risk: Chemistry lab guidance can be unsafe if used without local laboratory controls or teacher review.

Mitigation: Require teacher confirmation, apply the documented safetyLevel rules, and defer to school laboratory and hazardous-chemical policies before classroom use.

Risk: Workspace memory or file permissions could expose or persist class data beyond the teacher's intent.

Mitigation: Review platform memory, import/export, deletion, sharing, and teacher-confirmed write controls before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chemistry-lab-guide)
- [Chemistry lab teaching reference](references/chemistry-lab-teaching.md)
- [Lab safety conventions](shared/lab-safety.md)
- [Platform conventions and localization guidance](shared/platform-conventions.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance and structured teaching-plan entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are drafts for teacher review, with teacher-confirmed workspace writes when platform memory is enabled.]

## Skill Version(s):

2.3.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
