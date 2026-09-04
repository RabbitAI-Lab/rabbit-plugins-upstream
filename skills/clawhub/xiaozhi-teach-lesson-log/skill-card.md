## Description:

课后记录助手 helps independent teachers turn post-lesson recall into structured lesson records, learning trajectory notes, next-lesson handoffs, parent-summary drafts, and lesson-unit confirmation prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill after lessons to capture what was taught, mastery evidence, observed classroom response, progress, adjustments, and next-lesson focus. It is intended for Chinese-language teaching records for students from upper elementary through high school, with teacher confirmation required before records or lesson-unit ledger changes are saved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive student lesson records and parent-summary drafts.

Mitigation: Use aliases, avoid real names and family details, verify consent fields before parent-facing drafts, and keep parentSummary as an internal draft for teacher review.

Risk: Lesson-unit ledger suggestions could be mistaken for confirmed accounting changes.

Mitigation: Require explicit teacher confirmation before saving records or changing usedUnits or remainingUnits; keep unconfirmed entries in pendingConfirmations.

Risk: Crisis resources and teaching-record norms are locale-specific.

Mitigation: Use the skill only where Chinese-language teaching records and mainland-China crisis resources are appropriate, or add locale-aware crisis guidance before deployment.

Risk: Classroom observations can become unsupported labels about a student.

Mitigation: Record observable behavior only, avoid inferred traits and emotional labels, and apply the crisis referral protocol when safety signals appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Lesson log template](artifact/references/lesson-log-template.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Vocabulary and consent fields](artifact/shared/vocab.md)
- [Grade-band parameters](artifact/shared/grade-bands.md)
- [AI item self-check protocol](artifact/shared/ai-item-check.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured lesson-record field content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses student aliases, requires dates for lesson records, limits parent summaries to internal drafts, and creates pending lesson-unit confirmations rather than directly changing used or remaining units.]

## Skill Version(s):

2.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
