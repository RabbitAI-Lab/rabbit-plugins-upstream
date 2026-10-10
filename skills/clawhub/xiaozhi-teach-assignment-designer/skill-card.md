## Description:

Helps Chinese K–12 teachers design differentiated, time-bounded homework task cards with scoring rubrics and feedback templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn lesson topics and class learning needs into differentiated homework, estimated completion times, grading criteria, and feedback drafts. Teachers review generated questions and approve any use of student records or completion summaries.

### Deployment Geography for Use:

Mainland China (default Chinese K–12 setting; localize curriculum, privacy, and crisis-referral guidance elsewhere)

## Known Risks and Mitigations:

Risk: Student records or feedback may reveal sensitive information or be shared without consent.

Mitigation: Enforce consent and pause/delete/export controls, use pseudonyms and aggregate summaries, and require teacher approval before sharing or writing back.

Risk: AI-generated questions or rubrics may contain mistakes or unsuitable content.

Mitigation: Have a teacher verify generated questions and scoring criteria before assigning or storing them.

Risk: Curriculum, privacy rules, and crisis contacts may not fit users outside the default Chinese K–12 setting.

Mitigation: Localize those materials and referral channels before deployment in another region or language.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [Assignment rubrics and task-card templates](references/assignment-rubric.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI-generated item checks](shared/ai-item-check.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language homework task cards, scoring rubrics, and feedback templates in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-item time estimates and teacher-reviewed, aggregate completion summaries when class data is available.]

## Skill Version(s):

2.11.1 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
