## Description:

帮助独立教师登记作业、追踪提交与批改状态、归纳错因，并生成下节课的教学重点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers working with Chinese-language K12 learners use this skill to track homework completion, review recurring error patterns, and prepare follow-up teaching plans. Teachers confirm any proposed changes to student weakness records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Homework follow-up and weakness evidence may expose information about minors.

Mitigation: Configure workspace consent, use student aliases, and do not enter real names or homework answer text.

Risk: An incorrect suggested weakness could be added to a student record.

Mitigation: Have the teacher review supporting evidence and confirm each proposed weakness before updating the student card.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [Homework completion views](artifact/references/completion-tracking-views.md)
- [Error follow-up checklist](artifact/references/error-reflow-checklist-template.md)
- [Persistent weakness record](artifact/references/persistent-weakness-file-template.md)
- [Next-lesson pre-diagnosis](artifact/references/pre-diagnosis-output-template.md)
- [Student homework profile](artifact/references/student-homework-profile-template.md)
- [Shared error categories and thresholds](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language summaries, tables, and structured homework follow-up records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Student records use aliases; suggested weaknesses require teacher confirmation.]

## Skill Version(s):

2.7.1 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
