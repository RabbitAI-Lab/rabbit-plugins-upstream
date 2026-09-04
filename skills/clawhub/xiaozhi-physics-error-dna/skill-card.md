## Description:

初中物理错题的根因分析与档案系统，用五维分类定位图景、概念、公式、过程和数学工具类错因，并生成弱项报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-support agents use this skill to analyze junior-high physics mistakes, separate physics visualization issues from concept, formula, process, and math-tool errors, and produce consent-based weak-spot reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may rely on a long-term learner profile for physics mistakes, including weak spots and learning-emotion signals.

Mitigation: Enable memory, emotion tracking, reminders, and sharing only when the platform enforces the documented consent flags, deletion, export, and pause controls.

Risk: Physics mistake records could be shared across skills or shown to parents beyond the learner's intent.

Mitigation: Limit sharing to the physics branch and minimum required fields, and require parent-sharing and emotion-sharing consent before producing parent-facing summaries.

Risk: Reports can overstate patterns when there are too few observations or no cross-session statistics.

Mitigation: Mark single-session or low-sample conclusions as sample-limited and avoid historical counts unless the platform supplies them.

Risk: Student distress may exceed ordinary learning anxiety.

Mitigation: Apply the crisis-safety path before tutoring, reporting, reminders, or parent summaries; store only the referral handling fact, not sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-error-dna)
- [物理错因维度表](references/physics-error-dimension-table.md)
- [物理高频概念混淆对照表](references/physics-concept-confusion-map.md)
- [物理数学工具自检清单](references/physics-math-tools-checklist.md)
- [四类物理图景绘制追问手册](shared/physics-diagram-guide.md)
- [全库统一词表](shared/vocab.md)
- [LearningDNAProfile schema](shared/dna-profile.schema.json)
- [Multi-agent handover protocol schema](shared/handover-protocol.schema.json)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown explanations plus JSON-compatible profile and handover records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated long-term profile updates; no shell commands or API calls.]

## Skill Version(s):

2.1.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
