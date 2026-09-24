## Description:

Analyzes recurring middle-school math mistakes by refining general error categories into math-specific subtypes, cross-dimension patterns, weakness reports, and consent-controlled follow-up guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-speaking K-12 learners, guardians, and education agents use this skill to identify why math mistakes recur, generate math weakness maps or monthly reports, and route follow-up practice or records through consent-controlled learning workflows.

### Deployment Geography for Use:

Mainland China Chinese-speaking K-12 deployments; localize safety channels, curriculum assumptions, consent rules, and language before use elsewhere.

## Known Risks and Mitigations:

Risk: Use outside mainland China or outside Chinese-speaking K-12 settings may provide mismatched curriculum assumptions, consent expectations, or crisis-resource guidance.

Mitigation: Localize curriculum references, emergency and support channels, language, and minor-data consent rules before deployment in other regions.

Risk: Persistent student profiles, cross-skill sharing, parent visibility, or reminders could expose minor learning records without appropriate consent.

Mitigation: Verify guardian/student consent settings, profile sharing, parent visibility, and reminder permissions before writing records or sharing summaries.

Risk: Math-history statistics or recurring-weakness conclusions may be misleading when cross-session memory or statistics are unavailable.

Mitigation: Use only current-session counts or clearly labeled preliminary trends unless the platform supplies authorized historical statistics.

Risk: Learning-pressure conversations can contain crisis signals that exceed ordinary tutoring support.

Mitigation: Route self-harm, severe distress, bullying, or family-safety signals through the crisis referral protocol before any study workflow, report, or parent-facing summary.

Risk: Generated diagnostic or practice items may be mathematically invalid or mismatched to the targeted weakness.

Mitigation: Apply the bundled item self-check guidance and review generated items before presenting them to students.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [数学错因维度表](references/math-error-dimension-table.md)
- [初中数学高频概念混淆对照表](references/concept-confusion-map.md)
- [数学读题失误训练方法手册](references/reading-habits.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown-style learner-facing reports plus structured profile, writeback, and reminder handoff fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on consent state, available memory/statistics capabilities, and crisis-safety routing.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
