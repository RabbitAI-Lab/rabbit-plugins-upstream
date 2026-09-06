## Description:

把一周零散的学习记录整理成有结论、有证据、有下一步的周报，并带学生做一次自我复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

External students and learning-support agents use this skill to turn weekly study activity into a concise self-review, next-week priority, and optional family-facing report. It is designed for Chinese K12 learning contexts and uses consent-gated handoffs for reminders and learning-profile updates.

### Deployment Geography for Use:

China Mainland by default; localize crisis resources, school-system assumptions, and minor-data consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Student-data handoffs can validate transfers that should be blocked when consent snapshots are stale, false, or mismatched to the recipient.

Mitigation: Deploy only where the platform separately enforces current consent, rejects stale consent snapshots, and binds each handover type to its allowed recipient.

Risk: Family-facing reports may expose student information or emotion-related content without proper authorization.

Mitigation: Confirm the speaker, require current student or guardian authorization as appropriate, honor student refusal for family sharing, and omit emotion content unless emotion-sharing consent is present.

Risk: Crisis-support instructions are written for China Mainland by default and may be unsafe if emergency contacts are reused in other regions.

Mitigation: Localize crisis-referral guidance for the deployment region and ask for the user location before giving region-specific emergency numbers when location is unknown.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report template](references/review-report-template.md)
- [Platform conventions](shared/platform-conventions.md)
- [Grade bands](shared/grade-bands.md)
- [Vocabulary and consent fields](shared/vocab.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Published handover schema URL](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration]

**Output Format:** [Markdown-style weekly review reports with optional structured handover JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Student-facing and family-facing variants depend on verified identity, consent status, available weekly data, grade band, and crisis-safety checks.]

## Skill Version(s):

2.1.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
