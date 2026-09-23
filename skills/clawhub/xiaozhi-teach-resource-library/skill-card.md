## Description:

Helps independent K12 teachers organize, search, adapt, and reuse teaching handouts, question items, lesson commentary, error cases, and lesson plans with tagging, copyright status, and reuse notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Independent K12 teachers use this skill to maintain a searchable teaching resource library, retrieve suitable materials by topic and difficulty, adapt resources for a learner's current needs, and record how reused materials performed. It is intended for teacher-facing resource management, not direct student instruction, grading, lesson delivery, or parent communication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent resource indexing could retain identifiable student details in error-case examples or reuse notes.

Mitigation: Require teacher review and the skill's de-identification checklist before storing cases; avoid real names, schools, contact details, dates, and details that can be traced back to a student.

Risk: Copyrighted questions, exam materials, scans, or unauthorized online resources could be stored as full text.

Mitigation: Use the skill's copyrightStatus workflow and store tutoring-book originals and past exam questions as index-only references rather than copying prompts or scans.

Risk: AI-generated or adapted questions may contain unsound answers, unsuitable difficulty, or invalid conditions.

Mitigation: Keep aiGenerated and verifiedByTeacher fields visible, label unverified generated items, and require teacher verification before student use.

Risk: Cross-skill sharing or deletion behavior may conflict with local privacy expectations.

Mitigation: Review platform sharing and deletion controls before installation, and remove or further de-identify resource-library entries when a related student deletion request is made.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource Categorization](artifact/references/resource-categorization.md)
- [Resource Entry Examples](artifact/references/resource-entry-examples.md)
- [Copyright Annotation Template](artifact/references/copyright-annotation-template.md)
- [AI Item Check Protocol](artifact/shared/ai-item-check.md)
- [Solo Teacher Workspace Schema](artifact/shared/solo-teacher-workspace.schema.json)
- [Shared Vocabulary](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured resource-index field recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resource entries should include copyrightStatus, aiGenerated, verifiedByTeacher, and usageNotes when applicable.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
