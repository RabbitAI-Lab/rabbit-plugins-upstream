## Description:

Helps teachers design differentiated, time-bounded homework task cards with grading rubrics and feedback templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to create differentiated K–12 homework, grading criteria, and feedback templates informed by class learning data. It does not automatically grade student work or prepare examination papers.

### Deployment Geography for Use:

Mainland China; other regions require localization of curriculum, emergency contacts, and legal and privacy defaults.

## Known Risks and Mitigations:

Risk: Mainland China-specific curriculum, emergency contacts, and privacy defaults may be inappropriate elsewhere.

Mitigation: Localize these defaults and confirm the deployment region before use outside Mainland China.

Risk: Class or student tier data and homework completion summaries may expose student information without appropriate controls.

Mitigation: Confirm platform consent and writeback controls; share only permitted feedback and store aggregate, de-identified completion summaries.

Risk: AI-generated questions or grading criteria may contain errors.

Mitigation: Have a teacher verify generated questions and review rubrics before assigning homework.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [Assignment rubric](references/assignment-rubric.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Teacher-facing task cards, grading rubrics, and feedback templates in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tasks include estimated time; aggregate homework completion summaries may be written back when platform controls permit.]

## Skill Version(s):

2.7.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
