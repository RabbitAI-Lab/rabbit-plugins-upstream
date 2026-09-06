## Description:

测评设计师 helps teachers design standards-aligned assessment blueprints, two-way specification tables, item revisions, difficulty mixes, scoring rubrics, and review-item lists for Chinese K12 classrooms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to plan diagnostic, formative, and summative assessments from a blueprint before selecting or generating items. It supports exam design, rubric drafting, item revision from post-exam statistics, and teacher-facing review lists while leaving post-exam statistical calculation to the student-analysis skill.

### Deployment Geography for Use:

China mainland Chinese K12 context; localize curriculum, consent, privacy, and crisis-response guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill may use class-level teaching records and cross-skill teaching context involving minors.

Mitigation: Confirm workspace sharing, parent-sharing, and cross-skill consent settings before deployment or use with real class data.

Risk: AI-generated or skill-generated assessment items can be wrong, ambiguous, unsolved, over-level, or misaligned with the blueprint.

Mitigation: Require teacher self-solution and verification before setting verifiedByTeacher=true or including an item in a formal exam.

Risk: Assessment artifacts can expose student identity or sensitive performance information.

Mitigation: Use aliases, seat numbers, or student IDs in outputs and avoid real names, individual rankings, or public low-score callouts.

Risk: Copied textbook, workbook, or prior-exam items can create copyright risk.

Mitigation: Record copyrightStatus for every item, keep restricted sources as indexes only, and document adaptation provenance when using adapted items.

Risk: The bundled safety and curriculum guidance is written for mainland China and may be incorrect elsewhere.

Mitigation: Localize emergency contacts, curriculum standards, consent requirements, and student-data practices before serving users outside that context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [Exam blueprint and two-way specification templates](artifact/references/exam-blueprint.md)
- [AI item self-check protocol](artifact/shared/ai-item-check.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Platform conventions and localization boundaries](artifact/shared/platform-conventions.md)
- [Crisis exception and referral protocol](artifact/shared/crisis-exception.md)
- [Shared vocabulary and consent fields](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured classWorkspace-compatible fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces examBlueprints entries, scoring rubrics, item-revision lists, review-item lists, and teacher-facing verification warnings.]

## Skill Version(s):

2.1.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
