## Description:

帮助化学老师设计元素符号、化合价、化学式和化学方程式的分级过关训练、间隔回看与分层跟进体系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External chemistry teachers use this skill to build class-level notation drills, short mastery cards, spaced review, and follow-up tasks for middle school chemistry and high school entry-level notation practice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Class workspace data may contain student performance or classroom records.

Mitigation: Use scoped memory and file access, keep records anonymized by alias or seat number, and require teacher confirmation before saving or using records with students.

Risk: Generated chemistry notation questions may be wrong if used without review.

Mitigation: Label AI-generated items and require teacher verification of formulas, valence, and equation balancing before classroom, homework, or resource-bank use.

Risk: Unreleased unified exam materials and personally identifying student information are sensitive.

Mitigation: Do not input pre-release exam questions, answers, scoring rubrics, real student names, contact details, or family information.

## Reference(s):

- [化学用语五级过关体系](references/notation-drill-system.md)
- [ClassTeachingWorkspace schema](shared/class-teaching-workspace.schema.json)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chemistry-notation-drill)
- [Publisher profile: qizhitang](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or plain text plans with structured class workspace record drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing drafts; AI-generated drill items require teacher verification before classroom, homework, or resource-bank use.]

## Skill Version(s):

2.3.0 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
