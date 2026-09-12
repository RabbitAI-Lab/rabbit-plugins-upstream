## Description:

Organizes a student's weekly learning records into an evidence-based weekly review with self-reflection prompts, a focused next step, consent-gated family sharing, and limited handoffs for memory, reminders, and monthly-report summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to turn weekly learning activity into a concise review report that identifies progress, weak points, evidence, and one priority for the next week. With student consent, it can also prepare a family-facing version and hand off approved summaries or reminder requests to companion learning skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weekly reports may use cross-session learning records and produce family-facing summaries.

Mitigation: Keep consent defaults off, confirm the speaker before family reports, and require parent-sharing and emotion-sharing consent before exposing those details.

Risk: Ambiguous activation phrases may trigger a review flow when the student intended a different learning task.

Mitigation: Confirm the weekly-review intent when phrasing is unclear and route monthly reports or single-question analysis to the appropriate companion skill.

Risk: Handoff payloads could reach an unintended recipient or include fields beyond the approved purpose.

Mitigation: Use the bundled handover schema, enforce the intended recipient for each handoff type, and include only consent-approved fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Weekly review report template](references/review-report-template.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown reports and structured handoff payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include student self-use reports, consent-gated family summaries, reminder queue requests, and approved learning-summary handoffs.]

## Skill Version(s):

2.1.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
