## Description:

Helps independent teachers turn post-lesson notes into structured lesson logs with mastery observations, pending lesson-hour confirmations, and next-lesson handoff points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill after a class to capture pseudonymized K12 lesson records, mastery status, student reaction facts, progress evidence, and next-lesson focus. It also prepares pending lesson-hour confirmation entries and optional internal parent-summary drafts for teacher review.

### Deployment Geography for Use:

China mainland by default; localization is required before deployment elsewhere.

## Known Risks and Mitigations:

Risk: Lesson-hour balances could affect billing or renewals if settled without clear authority.

Mitigation: Constrain the skill to creating pending confirmation entries unless the schema and platform explicitly grant safe, idempotent ledger settlement authority.

Risk: Lesson records and parent-summary drafts may involve minors' education data.

Mitigation: Use student aliases, avoid real names and sensitive family details, check consent before parent-summary drafts, and require teacher preview before writeback.

Risk: Crisis-support guidance is region-specific by default.

Mitigation: Use China-mainland emergency resources only when that region is confirmed; otherwise ask for location and provide localized emergency guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Lesson log template](references/lesson-log-template.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Shared vocabulary](shared/vocab.md)
- [Grade bands](shared/grade-bands.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown or text with structured workspace field values for teacher review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records, parent-summary drafts, and lesson-hour entries require teacher confirmation before writeback or settlement.]

## Skill Version(s):

2.1.12 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
