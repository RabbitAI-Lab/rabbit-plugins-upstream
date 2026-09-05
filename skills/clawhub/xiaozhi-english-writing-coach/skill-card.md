## Description:

英语写作教练：从语法、用词、逻辑三个维度给整段或整篇反馈，用追问引导学生自己修改。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education agents use this skill to coach English writing for full paragraphs or essays. It provides grammar, vocabulary, and logic feedback, asks revision prompts, supports scenario-based writing practice, and can update a writing profile when consent allows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The active skill instructions may handle minors' self-harm, abuse, bullying, or severe distress disclosures without placing the packaged crisis exception as a top-priority override.

Mitigation: Before deployment, add the crisis exception near the top of SKILL.md and make it override writing review, profile reads and writes, reports, reminders, parent-facing output, and cross-skill handoffs.

Risk: The skill can maintain cross-session writing profiles and coordinate with other skills or parent-facing summaries.

Mitigation: Require explicit consent checks before profile writes, cross-skill sharing, reminders, and parent-visible output; honor view, correction, deletion, pause, sharing-control, and export requests.

Risk: Generated writing practice and feedback can be overbroad, misleading, or too substitutive for a student's own work.

Mitigation: Keep feedback focused on the most important two or three issues, ask the student to revise before showing stronger hints, and apply the packaged AI item self-check before generated practice items are reused.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-english-writing-coach)
- [Vocabulary upgrade reference](artifact/references/vocabulary-upgrade.md)
- [English error dimension table](artifact/shared/english-error-dimension-table.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with structured feedback, revision prompts, practice tasks, profile-update guidance, and progress reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce consent-gated profile update payloads and cross-skill handoff guidance; does not execute local code or shell commands.]

## Skill Version(s):

2.1.6 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
