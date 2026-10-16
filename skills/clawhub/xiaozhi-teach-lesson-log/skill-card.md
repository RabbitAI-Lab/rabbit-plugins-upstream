## Description:

Helps independent teachers turn post-lesson observations into structured learning records, progress notes, and next-lesson suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to draft and, after review, maintain lesson logs for students identified by aliases. It tracks topic-level mastery, prepares course-unit entries for confirmation, and suggests follow-up teaching steps; parent-facing summaries remain teacher-reviewed internal drafts.

### Deployment Geography for Use:

Mainland China; localize emergency contacts, curriculum assumptions, and legal and privacy requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: Persistent lesson records about minors could expose sensitive information.

Mitigation: Use student aliases, avoid real names and speculative traits, and have the teacher review each record before saving.

Risk: Unreviewed course-unit changes or parent summaries could misstate attendance or disclose observations.

Mitigation: Require teacher confirmation for records and course-unit changes; keep parent summaries as internal drafts subject to authorization and teacher review.

Risk: Emergency and legal guidance may be unsuitable outside Mainland China.

Mitigation: Localize emergency contacts, curriculum assumptions, and legal and privacy requirements before deployment elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Lesson log template](references/lesson-log-template.md)
- [Workspace data schema](shared/solo-teacher-workspace.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data, Guidance]

**Output Format:** [Teacher-reviewed lesson-log drafts, structured workspace records, and written follow-up guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records and course-unit changes require teacher confirmation; parent summaries are internal drafts only.]

## Skill Version(s):

2.11.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
