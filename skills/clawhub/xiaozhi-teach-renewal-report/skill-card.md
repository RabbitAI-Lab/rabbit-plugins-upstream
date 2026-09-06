## Description:

Helps independent teachers create evidence-based stage reports and renewal guidance from a named student's learning records, using authorization checks before any parent-facing draft is produced.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to produce student stage reports, progress summaries, renewal suggestions, and parent-message drafts grounded in recorded lesson, homework, progress, and course-package evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads sensitive, multi-month learning records for a minor.

Mitigation: Use it only after selecting one named student; the artifact requires avoiding cross-student scans and limiting reads to fields relevant to the report.

Risk: A parent-facing report or renewal script could expose information without consent.

Mitigation: Generate parent-facing content only when recorded consent permits it, and check emotion-sharing consent before including classroom-state details.

Risk: Progress claims could mislead families if unsupported by records.

Mitigation: Use only recorded evidence for numbers and trends, omit unsupported metrics, and avoid promises about scores, ranking, or admissions outcomes.

Risk: A drafted message could be mistaken for an automated communication.

Mitigation: Keep delivery manual; the artifact states the skill drafts reports and scripts but does not send, schedule, or push messages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [Stage report templates](references/stage-report-templates.md)
- [Renewal communication scripts](references/renewal-communication-scripts.md)
- [Shared vocabulary and consent fields](shared/vocab.md)
- [Teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown reports, parent-facing draft text, structured guidance, and scoped workspace evidence updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Parent-facing content is gated by consent fields; the skill does not send messages, schedule outreach, or broadly modify student records.]

## Skill Version(s):

2.1.10 (source: evidence.release.version and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
