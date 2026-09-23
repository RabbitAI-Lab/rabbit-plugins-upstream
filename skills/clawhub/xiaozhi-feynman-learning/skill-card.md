## Description:

用"讲给小智听"来检验学生是否真的学会了某个概念，产出掌握度判定和卡住位置，并在同意门后支持有限的档案写回或复测提醒交接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, parents, and education agents use this skill to run a Feynman-style understanding check for Chinese K12 concepts across subjects. The skill guides explanation, examples, why-questions, transfer, and age-appropriate critical verification, then summarizes the student's mastery level and stuck point.

### Deployment Geography for Use:

China mainland by default; localize crisis referral channels before use in other regions

## Known Risks and Mitigations:

Risk: The crisis-referral content is written for a China mainland K12 context and may name support channels that are not appropriate elsewhere.

Mitigation: Localize crisis referral channels before use outside China mainland and ask the learner's country or region before providing emergency contact details.

Risk: The skill may be used by younger students and can involve consent-gated profile writeback or reminder handoffs.

Mitigation: Enable LearningDNA and IM reminder integrations only after reviewing permissions, guardian consent, and adult-supervision expectations for the deployment.

Risk: A student may mistake a fluent AI explanation or copied wording for genuine understanding.

Mitigation: Use the skill's own-language explanation, example, why-question, transfer, and critical-verification checks before accepting a mastery result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Feynman 4+1 jump state machine](artifact/references/feynman-5jump-statemachine.md)
- [Feynman dialogue patterns](artifact/references/feynman-dialogue-patterns.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Grade-band rules](artifact/shared/grade-bands.md)
- [Mastery vocabulary](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational text and Markdown-style assessment summaries, with optional structured handoff payloads for profile writeback or reminders when consent requirements are met.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces mastery labels, stuck-point summaries, next-step suggestions, and consent-gated handoff data; it does not produce executable code.]

## Skill Version(s):

2.2.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
