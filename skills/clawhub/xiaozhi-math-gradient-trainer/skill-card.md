## Description:

A Chinese-language junior-high math tutoring skill that locates a student's current five-level practice tier for a known topic, then generates progressive exercises, hints, growth diary entries, and weekly checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and tutoring agents use this skill for Chinese-language junior-high math practice after a topic is basically understood. It identifies the student's current practice tier, generates stepwise exercises and hints, and prepares consent-gated learning record or reminder handoffs.

### Deployment Geography for Use:

China mainland by default; use elsewhere requires localization of crisis referral resources, curriculum assumptions, consent rules, and language support.

## Known Risks and Mitigations:

Risk: Use outside China mainland may provide mismatched crisis contacts, curriculum assumptions, consent expectations, or language support.

Mitigation: Localize referral channels, curriculum framing, consent rules, and language before deploying outside the default region.

Risk: The skill may prepare student learning records and reminder handoffs for minors.

Mitigation: Require the stated consent checks before sharing or reminders, and preserve the view, correct, delete, pause, sharing-control, and export controls.

Risk: Generated math practice items can be incorrect, ambiguous, or outside the intended grade band.

Mitigation: Apply the bundled item-check protocol: self-solve, verify uniqueness or openness, check condition sufficiency, keep values grade-appropriate, and mark teacher-facing generated items for human validation.

Risk: A student may disclose self-harm, abuse, severe despair, or other safety concerns during a tutoring session.

Mitigation: Stop tutoring flow and follow the crisis exception protocol: respond without judgment, state AI limits, direct the student to trusted adults, and provide localized emergency guidance.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [Gradient levels reference](artifact/references/gradient-levels.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration]

**Output Format:** [Chinese-language tutoring responses with optional JSON handover payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate learning-record writeback and reminder enqueue payloads only with consent; no executable code.]

## Skill Version(s):

2.1.12 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
