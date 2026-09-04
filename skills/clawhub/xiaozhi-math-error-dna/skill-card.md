## Description:

Analyzes junior-high math mistakes by refining correction-notebook error dimensions into math-specific subtypes and cross-dimension patterns for targeted remediation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and tutoring agents use this skill to identify recurring junior-high math error roots, generate mistake-pattern summaries, and guide focused follow-up practice after the correction notebook hands off a math mistake record.

### Deployment Geography for Use:

Mainland China; localize crisis contacts and emergency instructions before use in other regions.

## Known Risks and Mitigations:

Risk: The crisis-response content uses mainland China emergency and youth-support contacts.

Mitigation: Before use outside mainland China, replace crisis contacts and emergency instructions with locale-appropriate resources.

Risk: Math mistake analysis can rely on persistent student profile data and cross-skill sharing.

Mitigation: Use only in workflows where the correction notebook and learning-profile skills enforce consent, deletion, pause, export, and sharing controls.

Risk: Direct intake could bypass the correction notebook's authority for wrong-answer capture, counting, and weak-point status.

Mitigation: Route new math wrong-answer intake through the correction notebook and use this skill only after the handoff record is available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [数学错因维度表](artifact/references/math-error-dimension-table.md)
- [初中数学高频概念混淆对照表](artifact/references/concept-confusion-map.md)
- [数学读题失误训练方法手册](artifact/references/reading-habits.md)
- [全库统一词表](artifact/shared/vocab.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [危机例外](artifact/shared/crisis-exception.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown and structured text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include consent-gated learning-profile updates and reminder requests after upstream handoff requirements are satisfied.]

## Skill Version(s):

2.1.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
