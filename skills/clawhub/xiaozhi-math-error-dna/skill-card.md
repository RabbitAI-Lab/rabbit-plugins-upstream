## Description:

数学错误DNA helps agents analyze middle-school math mistakes by refining four general error dimensions into math subtypes and linking them to root-cause patterns, weak-area reports, and consent-controlled profile updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and learning-support agents use this skill after a math error has been collected by the correction notebook to classify the root cause, generate error-pattern maps or monthly weak-area reports, and guide targeted follow-up practice. The skill is intended for junior-middle-school math workflows with explicit consent controls for profile storage, cross-skill sharing, reminders, and parent-facing summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Math error records may be used for learning-profile analysis, including for minors.

Mitigation: Confirm learner and guardian consent before profile storage or ongoing analysis, and keep view, correction, deletion, pause, export, and sharing controls available.

Risk: Parent-facing summaries or cross-skill sharing may expose sensitive learning or emotion-related information.

Mitigation: Check parent-sharing, emotion-sharing, and cross-skill-sharing consent before disclosure; when consent is absent, keep outputs in the current learner-facing session.

Risk: Crisis-support guidance may be inappropriate if used outside its localized assumptions.

Mitigation: Localize crisis referral guidance before deployment and ask for region when the appropriate emergency or support channel is unclear.

Risk: Reports or practice recommendations may become misleading if the agent invents history, counts, or weakness status.

Mitigation: Use only correction-notebook statistics for counts and status, mark limited evidence as preliminary or insufficient, and keep unsupported conclusions out of long-term profiles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [数学错因维度表](references/math-error-dimension-table.md)
- [初中数学高频概念混淆对照表](references/concept-confusion-map.md)
- [数学读题失误训练方法手册](references/reading-habits.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or text reports with structured JSON-style handoff payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include math subtype labels, root-cause summaries, weak-area reports, exercise guidance, and consent-gated writeback or reminder handoff data.]

## Skill Version(s):

2.1.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
