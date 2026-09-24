## Description:

A Chinese K12 grammar-coaching skill that identifies six common sentence-error categories, guides students through corrections, and, with consent, tracks recurring grammar-error patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners and supporting educators use this skill to diagnose sentence-level grammar errors, practice corrections, and monitor recurring grammar-error patterns with consent-gated learner records.

### Deployment Geography for Use:

China Mainland by default; other regions require localization of curriculum assumptions, minor consent handling, and crisis referral channels.

## Known Risks and Mitigations:

Risk: Learner grammar-error profiles can expose minor student learning data if memory, cross-skill sharing, parent visibility, or reminders are enabled without the right consent.

Mitigation: Confirm student or guardian consent settings before enabling memory, profile writes, cross-skill sharing, parent-visible summaries, or reminders; keep sharing to the minimum necessary fields.

Risk: The artifact is written for Mainland China Chinese K12 use, including curriculum assumptions and crisis referral channels.

Mitigation: Localize curriculum references, minor consent requirements, and emergency or youth-support channels before using the skill outside Mainland China.

Risk: If platform memory or cross-session statistics are unavailable, the skill could overstate progress history.

Mitigation: Use the documented fallback: provide current-session-only checks and counts, and do not claim historical memory or monthly progress numbers.

Risk: Grammar help during an active exam or test could support academic misconduct.

Mitigation: When the student indicates an exam or test is in progress, refuse to explain that item and offer post-exam review instead.

Risk: Generated grammar exercises may contain invalid, ambiguous, or multi-error examples.

Mitigation: Apply the bundled AI item self-check before presenting generated exercises and mark teacher-facing generated items for human validation before reuse.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Grammar error library](references/grammar-error-library.md)
- [Chinese error dimension table](shared/chinese-error-dimension-table.md)
- [Learner profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Hint ladder](shared/hint-ladder.md)
- [AI item self-check protocol](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese tutoring dialogue, concise Markdown summaries, and consent-gated profile or handover JSON fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses platform memory and cross-session statistics when available; otherwise falls back to current-session-only guidance and counts.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
