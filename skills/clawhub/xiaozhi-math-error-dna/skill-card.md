## Description:

Analyzes middle-school math mistakes by refining general notebook error dimensions into math-specific subtypes, cross-dimension patterns, weak-point reports, and consent-gated profile updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and tutoring agents use this skill to identify recurring root causes in middle-school math mistakes, generate error-pattern summaries, and guide targeted follow-up practice. It is designed to operate through consent-gated profiles and handoffs with related learning skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student math-error profiles can reveal personal learning patterns if created, retained, or shared without clear consent.

Mitigation: Keep profile creation, deletion, export, parent-sharing, emotion-sharing, and cross-skill sharing controls explicit before storing or disclosing profile data.

Risk: Cross-skill handoffs and reminder queues can disclose more information than expected if sharing boundaries are not enforced.

Mitigation: Use only the minimum handoff fields needed, respect cross-skill sharing consent, and route reminders through the designated reminder skill instead of promising direct outreach.

Risk: Math anxiety messages may include crisis signals that exceed a tutoring skill's scope.

Mitigation: Apply the bundled crisis referral protocol before normal tutoring, reporting, or parent-summary flows, and localize emergency and consent guidance for the deployment region.

Risk: Historical trend reports can be misleading when platform memory or cross-session statistics are unavailable.

Mitigation: Limit unsupported counts to the current session or clearly mark profile-derived trends as preliminary instead of fabricating precise history.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [数学错因维度表](artifact/references/math-error-dimension-table.md)
- [数学读题失误训练方法手册](artifact/references/reading-habits.md)
- [初中数学高频概念混淆对照表](artifact/references/concept-confusion-map.md)
- [全库统一词表](artifact/shared/vocab.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown-style tutoring responses, structured profile/writeback fields, handoff payload guidance, and report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should respect consent gates, avoid unsupported historical counts when cross-session statistics are unavailable, and use crisis referral behavior when safety signals appear.]

## Skill Version(s):

2.1.12 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
