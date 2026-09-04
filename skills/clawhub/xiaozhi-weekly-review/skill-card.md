## Description:

A Chinese-language weekly learning review agent that turns student learning records into evidence-based weekly reports, self-reflection prompts, and focused next-step study guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and families use this skill to summarize a week of learning activity into a student-facing review, consent-gated family summary, and one prioritized action plan for the next week. It is designed for Chinese-language learning support across upper-primary, middle-school, and high-school contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses student learning history, cross-skill sharing, reminders, and optional parent-facing summaries.

Mitigation: Confirm profile memory, cross-skill sharing, reminder, and parent-sharing consent settings before use; honor student denial controls for family sharing.

Risk: Crisis-resource text is localized for mainland China and may be inappropriate or incomplete elsewhere.

Mitigation: Replace or supplement emergency and crisis referral resources with locally valid guidance before deployment outside mainland China.

Risk: Weekly reports can overstate certainty when memory or cross-session statistics are unavailable.

Mitigation: Use only current-session information or student-provided recollection when memory or statistics are unavailable, and avoid fabricated historical counts or completion rates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report template](artifact/references/review-report-template.md)
- [Grade band guidance](artifact/shared/grade-bands.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown reports with plain-text prompts and structured handoff payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces student self-use weekly reviews, consent-gated family summaries, focused next-week actions, reminder enqueue guidance, and profile writeback guidance.]

## Skill Version(s):

2.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
