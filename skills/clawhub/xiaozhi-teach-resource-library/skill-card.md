## Description:

Organizes independent teachers’ teaching materials into a searchable library for cataloging, finding, adapting, and reusing resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use the skill to catalog teaching resources with subject, topic, difficulty, and copyright labels, retrieve relevant materials, and record how adapted resources perform. Teachers review suggested materials before using them with learners.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Unauthorized teaching materials may be copied into the library.

Mitigation: Use authorized materials; record restricted exam and textbook questions as references only, without storing their text or scans.

Risk: Student details in teaching cases or records may identify a learner.

Mitigation: Remove identifying details from cases before saving, and check the host platform’s storage, deletion, and sharing controls.

Risk: AI-generated or adapted questions may contain errors.

Mitigation: Have a teacher solve and verify each question before it is marked ready for learner use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource categorization](artifact/references/resource-categorization.md)
- [Resource entry examples](artifact/references/resource-entry-examples.md)
- [Copyright annotation template](artifact/references/copyright-annotation-template.md)
- [AI-generated item checks](artifact/shared/ai-item-check.md)
- [Resource library workspace schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Search and reuse guidance with structured resource library records (JSON)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed resource suggestions; AI-generated questions require teacher verification before learner use.]

## Skill Version(s):

2.12.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
