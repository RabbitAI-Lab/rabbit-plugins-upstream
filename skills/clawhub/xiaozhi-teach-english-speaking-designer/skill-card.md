## Description:

Designs task-based English speaking lessons that turn reading or memorized dialogues into contextual speaking activities with goals, input preparation, output practice, feedback, and optional class-workspace writeback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to design English speaking classes for upper-primary and middle-school learners, including task-based activities, rubrics, feedback language, differentiated practice, and recordkeeping proposals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Class records or student speaking data could be saved without proper school privacy controls.

Mitigation: Confirm writebacks before saving, honor teacher writeback consent, and keep privacy controls for viewing, correction, deletion, pause, sharing, and export available to the teacher.

Risk: Student recordings may expose sensitive personal data.

Mitigation: Use recordings only with proper consent, minimization, and access controls; do not publicly disclose student speaking recordings.

Risk: Generated assessment entries could be used outside their intended oral-speaking scope.

Mitigation: Restrict exam blueprint writebacks to oral scoring items and require teacher review before generated items enter a class resource or exam workflow.

Risk: Pronunciation feedback could overclaim accuracy when the platform lacks speech evaluation capability.

Mitigation: Do not make phoneme-level pronunciation judgments from recordings or transcripts; rely on teacher judgment or a dedicated speech-evaluation capability when pronunciation scoring is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-speaking-designer)
- [Task-based speaking activity template](references/task-based-template.md)
- [Speaking rubric](references/speaking-rubric.md)
- [Error correction strategies](references/error-correction-strategies.md)
- [Feedback phrase bank](references/feedback-phrases.md)
- [Speaking profile template](references/speaking-profile-template.md)
- [Restaurant task design sample](references/task-design-sample-restaurant.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item check protocol](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown and structured classroom-planning text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include teacher-confirmed class-workspace writeback proposals, speaking rubrics, feedback phrases, and AI-generated item labels.]

## Skill Version(s):

2.1.12 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
