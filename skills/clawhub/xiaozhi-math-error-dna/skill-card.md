## Description:

Supports Chinese middle-school math error analysis by refining correction-notebook handoffs into math-specific root-cause subtypes, cross-dimension patterns, weakness reports, and consent-controlled follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and learning-support agents use this skill to turn repeated middle-school math mistakes into specific root-cause categories, trend summaries, and targeted next steps. It is intended to work after a correction notebook has captured the original mistake and consent settings permit any longer-term profile, sharing, reminder, or parent-summary behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile memory, cross-skill sharing, reminders, and parent-visible summaries may expose learner data if enabled outside the student's and guardian's consent settings.

Mitigation: Confirm consent settings before enabling profile memory, cross-skill sharing, reminders, or parent-visible summaries, and keep unsupported sharing disabled.

Risk: The skill may encounter student math-anxiety messages that include crisis signals beyond learning support.

Mitigation: Use the documented crisis-handling flow when crisis signals appear and avoid continuing error analysis, data display, or practice generation during that handoff.

Risk: Reports can overstate trends when cross-session statistics are unavailable or when the source notebook has not supplied counts.

Mitigation: Use only notebook-provided counts or current-session observations, label weak evidence as preliminary or insufficient, and avoid fabricating historical numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [数学错因维度表](artifact/references/math-error-dimension-table.md)
- [初中数学高频概念混淆对照表](artifact/references/concept-confusion-map.md)
- [数学读题失误训练方法手册](artifact/references/reading-habits.md)
- [Publisher profile](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text guidance with optional profile writeback payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce subtype IDs, root-cause summaries, confidence labels, weakness reports, reminder enqueue guidance, and consent-gated parent summaries.]

## Skill Version(s):

2.2.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
