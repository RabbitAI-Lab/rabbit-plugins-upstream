## Description:

Turns independent teachers’ post-lesson notes into structured learner records, progress summaries, and next-lesson handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use it to turn a lesson recap into a structured, pseudonymous teaching record, review learner progress, and prepare the next lesson. It drafts parent summaries for the teacher to review; records and lesson-credit changes require teacher confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lesson records may contain sensitive learner information.

Mitigation: Use aliases, obtain required consent, review each record before saving, and manage access and retention through the host platform; consult SECURITY_BASELINE.md for complete privacy documentation.

Risk: Lesson-credit changes can affect a learner’s remaining entitlement.

Mitigation: Keep entries pending until the teacher reviews and explicitly confirms each adjustment.

Risk: An internal parent summary could be mistaken for a message that has been sent.

Mitigation: Keep summaries as drafts, check communication consent, and leave any decision to send to the teacher.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Lesson log template](references/lesson-log-template.md)
- [Shared vocabulary and consent fields](shared/vocab.md)
- [Crisis exception guidance](shared/crisis-exception.md)
- [Platform conventions and data controls](shared/platform-conventions.md)
- [Off-campus training guidance](shared/off-campus-training.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured records, Guidance]

**Output Format:** [Markdown lesson summaries and structured lesson-record fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records are shown for teacher review before saving; lesson-credit entries remain pending until confirmed; parent summaries are internal drafts.]

## Skill Version(s):

2.12.6 (source: server-resolved release, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
