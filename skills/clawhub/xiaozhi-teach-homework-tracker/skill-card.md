## Description:

Helps independent teachers track assigned homework through submission status, error dimensions, correction follow-up, and next-lesson diagnosis while leaving grading, messaging, and lesson logging to the teacher or related skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to record homework tasks, monitor seven allowed status values, classify homework errors into shared dimensions, and prepare concise next-lesson follow-up. It is designed for Chinese K12 tutoring workflows where student aliases, consent checks, and teacher confirmation are expected.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, consent requirements, and crisis referral channels before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill handles minor-student homework records, weakness evidence, consent-sensitive sharing, export, and deletion flows that the bundled artifacts cannot enforce by themselves.

Mitigation: Install only on a platform with separate identity checks, consent controls, and fail-closed permissions for profile creation, parent-facing output, cross-skill sharing, export, and deletion.

Risk: Teacher-facing homework profiles and next-lesson summaries could expose student progress information beyond the intended audience.

Mitigation: Use aliases in views, keep outputs factual, and require verified consent before any parent-facing or cross-skill sharing.

Risk: AI-generated verification or practice items may be incorrect if reused without review.

Mitigation: Apply the bundled AI item self-check protocol and require teacher validation before adding generated items to a resource library or giving them to students.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [Completion tracking views](references/completion-tracking-views.md)
- [Error reflow checklist template](references/error-reflow-checklist-template.md)
- [Persistent weakness file template](references/persistent-weakness-file-template.md)
- [Pre-diagnosis output template](references/pre-diagnosis-output-template.md)
- [Student homework profile template](references/student-homework-profile-template.md)
- [Unified vocabulary](shared/vocab.md)
- [Platform conventions](shared/platform-conventions.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured text with optional JSON-like field snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before persistent weakness updates; the skill does not grade homework, send reminders, or contact parents.]

## Skill Version(s):

2.1.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
